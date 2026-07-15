#!/usr/bin/env python3
"""Shared, standard-library-only helpers for project Claude Code hooks."""

from __future__ import annotations

import json
import ntpath
import os
import posixpath
import re
import sys
from dataclasses import dataclass
from typing import Any, Dict, Iterable, Optional


MAX_INPUT_BYTES = 1_000_000


class HookInputError(ValueError):
    """Raised when Claude Code hook input is missing or malformed."""


@dataclass(frozen=True)
class NormalizedPath:
    absolute: str
    relative: str
    within_root: bool
    traversal: bool
    windows_style: bool


def read_event() -> Dict[str, Any]:
    raw = sys.stdin.buffer.read(MAX_INPUT_BYTES + 1)
    if not raw:
        raise HookInputError("hook input is empty")
    if len(raw) > MAX_INPUT_BYTES:
        raise HookInputError("hook input exceeds the 1 MB safety limit")
    try:
        decoded = raw.decode("utf-8", errors="strict")
        event = json.loads(decoded)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise HookInputError("hook input is not valid UTF-8 JSON") from exc
    if not isinstance(event, dict):
        raise HookInputError("hook input must be a JSON object")
    return event


def tool_input(event: Dict[str, Any]) -> Dict[str, Any]:
    value = event.get("tool_input")
    if not isinstance(value, dict):
        raise HookInputError("tool_input must be an object")
    return value


def project_root(event: Dict[str, Any]) -> str:
    value = os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd")
    if not isinstance(value, str) or not value.strip():
        raise HookInputError("CLAUDE_PROJECT_DIR or cwd is required")
    if "\x00" in value:
        raise HookInputError("project path contains a NUL byte")
    return value


def _is_windows_path(path: str) -> bool:
    return bool(re.match(r"^[A-Za-z]:[\\/]", path)) or path.startswith("\\\\")


def _has_traversal(path: str) -> bool:
    return any(part == ".." for part in re.split(r"[\\/]", path))


def normalize_target(
    raw_path: str, root: str, *, cwd: Optional[str] = None
) -> NormalizedPath:
    if not isinstance(raw_path, str) or not raw_path.strip():
        raise HookInputError("target path is required")
    if "\x00" in raw_path:
        raise HookInputError("target path contains a NUL byte")
    if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", raw_path):
        raise HookInputError("a URL is not a filesystem path")

    traversal = _has_traversal(raw_path)
    windows_style = _is_windows_path(root) or _is_windows_path(raw_path)
    base = cwd or root

    if windows_style:
        if not _is_windows_path(root):
            return NormalizedPath(raw_path, raw_path, False, traversal, True)
        root_abs = ntpath.normcase(ntpath.abspath(root))
        if not _is_windows_path(base):
            base = root_abs
        base_abs = ntpath.normcase(ntpath.abspath(base))
        target_abs = ntpath.normcase(
            ntpath.normpath(raw_path if ntpath.isabs(raw_path) else ntpath.join(base_abs, raw_path))
        )
        try:
            within = ntpath.commonpath([root_abs, target_abs]) == root_abs
        except ValueError:
            within = False
        relative = ntpath.relpath(target_abs, root_abs) if within else target_abs
    else:
        root_abs = os.path.realpath(os.path.abspath(root))
        base_abs = os.path.realpath(os.path.abspath(base))
        target_abs = os.path.realpath(
            os.path.abspath(raw_path if posixpath.isabs(raw_path) else os.path.join(base_abs, raw_path))
        )
        try:
            within = os.path.commonpath([root_abs, target_abs]) == root_abs
        except ValueError:
            within = False
        relative = os.path.relpath(target_abs, root_abs) if within else target_abs

    return NormalizedPath(target_abs, relative, within, traversal, windows_style)


def protected_path_reason(path: str) -> Optional[str]:
    normalized = path.replace("\\", "/").strip("\"'")
    segments = [segment.lower() for segment in normalized.split("/") if segment]
    basename = segments[-1] if segments else normalized.lower()

    public_mobile_config = {
        "google-services.json",
        "googleservice-info.plist",
    }
    if basename in public_mobile_config:
        return None

    public_env_suffixes = (".example", ".sample", ".template", ".dist", ".defaults")
    if basename == ".env":
        return "environment secret file"
    if basename.startswith(".env.") and not basename.endswith(public_env_suffixes):
        return "environment-specific secret file"

    if any(character in basename for character in "*?[") and (
        basename.startswith(".env")
        or re.search(
            r"secret|credential|service[-_]?account|firebase-adminsdk|authkey_",
            basename,
        )
    ):
        return "wildcard that may resolve to protected credential material"
    if any(segment in {".*", ".??*"} for segment in segments):
        return "wildcard that may resolve to hidden credential material"

    protected_names = {
        ".envrc": "environment secret file",
        ".netrc": "network credential file",
        ".npmrc": "package-registry credential file",
        ".pypirc": "package-registry credential file",
        "credentials.json": "credential file",
        "credentials.yml": "credential file",
        "credentials.yaml": "credential file",
        "secret.json": "secret file",
        "secret.yml": "secret file",
        "secret.yaml": "secret file",
        "secrets.json": "secret file",
        "secrets.yml": "secret file",
        "secrets.yaml": "secret file",
        "secrets.properties": "secret property file",
        "key.properties": "Android signing-property file",
        "keystore.properties": "Android signing-property file",
        "local.properties": "user-specific local configuration",
        "serviceaccountkey.json": "service-account credential",
        "api_key.json": "API-key file",
    }
    if basename in protected_names:
        return protected_names[basename]

    if re.search(r"(?:^|[-_])service[-_]?account(?:[-_].*)?\.json$", basename):
        return "service-account credential"
    if re.match(r"firebase-adminsdk-.*\.json$", basename):
        return "Firebase Admin service-account credential"
    if re.match(r"authkey_.*\.p8$", basename):
        return "Apple API private key"

    protected_extensions = {
        ".pem": "private key or certificate bundle",
        ".key": "private key",
        ".p8": "private key",
        ".p12": "signing identity bundle",
        ".pfx": "signing identity bundle",
        ".jks": "Java signing keystore",
        ".keystore": "signing keystore",
        ".mobileprovision": "Apple provisioning profile",
    }
    for suffix, reason in protected_extensions.items():
        if basename.endswith(suffix):
            return reason

    protected_directories = {
        ".ssh",
        ".gnupg",
        ".aws",
        ".azure",
        ".docker",
        ".kube",
        ".secrets",
        "private-keys",
        "signing-keys",
    }
    if any(segment in protected_directories for segment in segments):
        return "protected credential directory"
    if any(
        segments[index : index + 2] == [".config", "gcloud"]
        for index in range(max(0, len(segments) - 1))
    ):
        return "protected credential directory"
    return None


def emit_pretool_decision(decision: str, reason: str) -> int:
    if decision not in {"deny", "ask", "defer"}:
        raise ValueError("guard hooks must not auto-allow operations")
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
            "permissionDecisionReason": reason,
        }
    }
    sys.stdout.write(json.dumps(output, separators=(",", ":")))
    return 0


def emit_context(message: str, *, event_name: str = "PostToolUse") -> int:
    output = {
        "hookSpecificOutput": {
            "hookEventName": event_name,
            "additionalContext": message,
        }
    }
    sys.stdout.write(json.dumps(output, separators=(",", ":")))
    return 0


def first_string(mapping: Dict[str, Any], keys: Iterable[str]) -> Optional[str]:
    for key in keys:
        value = mapping.get(key)
        if isinstance(value, str) and value:
            return value
    return None
