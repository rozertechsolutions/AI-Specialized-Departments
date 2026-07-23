#!/usr/bin/env python3
"""Deny Copilot tool calls that expose secrets or touch protected mobile files."""

from __future__ import annotations

import json
import os
import re
import sys
from collections.abc import Iterator
from typing import Any


PATH_KEYS = {
    "path",
    "file",
    "filepath",
    "file_path",
    "filename",
    "file_name",
    "target",
    "destination",
}
PATCH_KEYS = {"diff", "patch"}
PROTECTED_NAMES = {
    ".envrc",
    ".npmrc",
    ".netrc",
    ".pypirc",
    "credentials",
    "credentials.json",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
    "id_rsa",
    "key.properties",
    "keystore.properties",
    "local.properties",
    "secrets.properties",
    "service-account.json",
}
PROTECTED_DIRECTORIES = {".aws", ".azure", ".docker", ".gem", ".gnupg", ".kube", ".ssh"}
PUBLIC_MOBILE_CONFIGS = {"firebase_options.dart", "google-services.json", "googleservice-info.plist"}
PROTECTED_SUFFIXES = {
    ".cer",
    ".crt",
    ".der",
    ".jks",
    ".key",
    ".keystore",
    ".mobileprovision",
    ".p12",
    ".p7b",
    ".p7c",
    ".p8",
    ".pem",
    ".pfx",
    ".provisionprofile",
}
SAFE_ENV_SUFFIXES = (".example", ".sample", ".template")
HIGH_CONFIDENCE_PATTERNS = (
    re.compile(r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{20,}\b"),
)
GOOGLE_API_KEY_PATTERN = re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")
ASSIGNMENT_PATTERN = re.compile(
    r"(?i)\b(?:api[_-]?key|client[_-]?secret|password|passwd|private[_-]?key|secret|token)"
    r"\b[\"']?\s*[:=]\s*(?:\"(?P<double>[^\"\r\n]{8,})\"|"
    r"'(?P<single>[^'\r\n]{8,})'|(?P<bare>[^\s\"',;}{]{12,}))"
)
ENVIRONMENT_REFERENCE = re.compile(
    r"(?i)^(?:\$\{[A-Z_][A-Z0-9_]*\}|\$[A-Z_][A-Z0-9_]*|"
    r"%[A-Z_][A-Z0-9_]*%|process\.env\.[A-Z_][A-Z0-9_]*|"
    r"\{\{\s*[A-Z_][A-Z0-9_]*\s*\}\})$"
)


def _deny(reason: str) -> dict[str, str]:
    return {"permissionDecision": "deny", "permissionDecisionReason": reason}


def _strings(value: Any) -> Iterator[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from _strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from _strings(item)


def _paths(value: Any, parent_key: str = "") -> Iterator[str]:
    if isinstance(value, dict):
        for key, item in value.items():
            normalized_key = str(key).casefold()
            if isinstance(item, str) and normalized_key in PATH_KEYS:
                yield item
            elif isinstance(item, str) and normalized_key in PATCH_KEYS:
                yield from _patch_paths(item)
            else:
                yield from _paths(item, normalized_key)
    elif isinstance(value, list):
        for item in value:
            yield from _paths(item, parent_key)


def _patch_paths(value: str) -> Iterator[str]:
    for line in value.splitlines():
        match = re.match(r"^\*\*\* (?:Add|Delete|Update) File:\s*(.+?)\s*$", line)
        if match:
            yield match.group(1)
            continue
        match = re.match(r"^(?:---|\+\+\+)\s+(?:a/|b/)?(.+?)\s*$", line)
        if match and match.group(1) != "/dev/null":
            yield match.group(1)


def _clean_path(value: str) -> str:
    return value.strip().strip("\"'").replace("\\", "/")


def _is_env_file(name: str) -> bool:
    lowered = name.casefold()
    if lowered == ".env":
        return True
    return lowered.startswith(".env.") and not lowered.endswith(SAFE_ENV_SUFFIXES)


def _is_protected_path(value: str) -> bool:
    normalized = _clean_path(value).rstrip("/.,:)")
    name = normalized.rsplit("/", 1)[-1].casefold()
    if name in PUBLIC_MOBILE_CONFIGS:
        return False
    if _is_env_file(name) or name in PROTECTED_NAMES:
        return True
    if any(part.casefold() in PROTECTED_DIRECTORIES for part in normalized.split("/")):
        return True
    if any(name.endswith(suffix) for suffix in PROTECTED_SUFFIXES):
        return True
    return name.startswith("service-account-") and name.endswith(".json")


def _is_public_mobile_config(value: str) -> bool:
    normalized = _clean_path(value).rstrip("/.,:)")
    return normalized.rsplit("/", 1)[-1].casefold() in PUBLIC_MOBILE_CONFIGS


def _path_escape_reason(value: str, cwd: str) -> str | None:
    normalized = _clean_path(value)
    parts = [part for part in normalized.split("/") if part not in {"", "."}]
    if ".." in parts:
        return "Write paths containing parent traversal require explicit review."

    drive_match = re.match(r"^([A-Za-z]:)/(.*)$", normalized)
    cwd_drive_match = re.match(r"^([A-Za-z]:)/(.*)$", _clean_path(cwd))
    if drive_match:
        if not cwd_drive_match:
            return "An absolute Windows write path cannot be verified inside the repository."
        path_value = normalized.casefold().rstrip("/")
        cwd_value = _clean_path(cwd).casefold().rstrip("/")
        if path_value != cwd_value and not path_value.startswith(cwd_value + "/"):
            return "Writes outside the repository are blocked."
        return None

    if os.path.isabs(normalized):
        if not cwd or not os.path.isabs(cwd):
            return "An absolute write path cannot be verified inside the repository."
        try:
            if os.path.commonpath((os.path.abspath(normalized), os.path.abspath(cwd))) != os.path.abspath(cwd):
                return "Writes outside the repository are blocked."
        except ValueError:
            return "The write path is on an unverified filesystem root."
    return None


def _command_tokens(command: str) -> Iterator[str]:
    normalized = command.replace("\\", "/")
    for token in re.split(r"[\s;&|<>()]+", normalized):
        cleaned = token.strip().strip("\"'`[]{}")
        if cleaned:
            yield cleaned


def _looks_like_placeholder(value: str) -> bool:
    stripped_value = value.strip()
    lowered = stripped_value.casefold()
    if ENVIRONMENT_REFERENCE.fullmatch(stripped_value):
        return True
    if stripped_value.startswith("<") and stripped_value.endswith(">"):
        return True
    normalized = re.sub(r"[^a-z0-9]+", "_", lowered).strip("_")
    markers = {"changeme", "dummy", "example", "fake", "placeholder", "redacted", "replace_me", "test_only"}
    if any(normalized == marker or normalized.startswith(marker + "_") for marker in markers):
        return True
    if normalized.startswith("your_"):
        return True
    stripped = re.sub(r"[^a-z0-9]", "", lowered)
    return bool(stripped) and len(set(stripped)) <= 2


def _looks_like_unquoted_identifier(value: str) -> bool:
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.]*", value):
        return False
    classes = sum(
        (
            any(char.islower() for char in value),
            any(char.isupper() for char in value),
            any(char.isdigit() for char in value),
        )
    )
    return classes < 3


def _contains_secret(value: str, allow_public_firebase_key: bool = False) -> bool:
    if any(pattern.search(value) for pattern in HIGH_CONFIDENCE_PATTERNS):
        return True
    if not allow_public_firebase_key and GOOGLE_API_KEY_PATTERN.search(value):
        return True
    for line in value.splitlines():
        for match in ASSIGNMENT_PATTERN.finditer(line):
            candidate = match.group("double") or match.group("single") or match.group("bare")
            if _looks_like_placeholder(candidate):
                continue
            if match.group("bare") and _looks_like_unquoted_identifier(candidate):
                continue
            return True
    return False


def evaluate(payload: Any) -> dict[str, str]:
    if not isinstance(payload, dict):
        return _deny("Malformed hook input: expected a JSON object.")

    tool_name = payload.get("toolName", payload.get("tool_name"))
    tool_args = payload.get("toolArgs", payload.get("tool_input"))
    cwd = payload.get("cwd", "")
    if not isinstance(tool_name, str) or not tool_name:
        return _deny("Malformed hook input: missing tool name.")
    if not isinstance(tool_args, (dict, list, str)):
        return _deny("Malformed hook input: missing or invalid tool arguments.")
    if not isinstance(cwd, str):
        return _deny("Malformed hook input: invalid working directory.")

    write_tools = {"apply_patch", "create", "edit", "str_replace_editor", "write"}
    write_paths = list(_paths(tool_args)) if tool_name.casefold() in write_tools else []
    if write_paths:
        for path in write_paths:
            escape_reason = _path_escape_reason(path, cwd)
            if escape_reason:
                return _deny(escape_reason)
            if _is_protected_path(path):
                return _deny("Writes to secret, credential, or mobile signing files are blocked.")

    if tool_name.casefold() in {"bash", "powershell", "execute", "shell"}:
        for value in _strings(tool_args):
            if any(_is_protected_path(token) for token in _command_tokens(value)):
                return _deny("Shell access to secret, credential, or mobile signing files is blocked.")

    allow_public_firebase_key = bool(write_paths) and all(_is_public_mobile_config(path) for path in write_paths)
    if any(_contains_secret(value, allow_public_firebase_key) for value in _strings(tool_args)):
        return _deny("The tool arguments contain a high-confidence secret or credential value.")

    return {}


def main() -> int:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        result = _deny("Malformed hook input: invalid JSON.")
    else:
        result = evaluate(payload)
    sys.stdout.write(json.dumps(result, separators=(",", ":"), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
