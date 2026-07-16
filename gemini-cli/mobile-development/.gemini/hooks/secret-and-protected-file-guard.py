#!/usr/bin/env python3
"""Gemini CLI BeforeTool hook that blocks real secrets and signing material."""

from __future__ import annotations

import json
import os
import re
import shlex
import sys
import unittest
from pathlib import Path
from typing import Any

MAX_INPUT_BYTES = 1_048_576

PROTECTED_SUFFIXES = {
    ".cer",
    ".der",
    ".jks",
    ".keystore",
    ".key",
    ".mobileprovision",
    ".p12",
    ".p8",
    ".pem",
    ".pfx",
}

PROTECTED_BASENAMES = {
    ".env",
    ".envrc",
    ".netrc",
    ".npmrc",
    ".pypirc",
    "credentials",
    "id_dsa",
    "id_ed25519",
    "id_ecdsa",
    "id_rsa",
    "key.properties",
    "keystore.properties",
}

PROTECTED_DIRECTORY_NAMES = {
    ".aws",
    ".azure",
    ".docker",
    ".gem",
    ".gnupg",
    ".kube",
    ".ssh",
}

PUBLIC_MOBILE_CONFIGS = {
    "firebase_options.dart",
    "google-services.json",
    "googleservice-info.plist",
}

HIGH_CONFIDENCE_SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:ENCRYPTED |RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    re.compile(r"\bsk_live_[A-Za-z0-9]{16,}\b"),
)

SENSITIVE_ASSIGNMENT = re.compile(
    r"(?i)\b(client_secret|password|passwd|access_token|refresh_token|private_key|"
    r"_auth_token|_authtoken|npm_auth_token|npmauthtoken)"
    r"\b\s*[:=]\s*[\"']?([^\s\"',;}{]{8,})"
)

SERVICE_ACCOUNT = re.compile(
    r"(?is)[\"']type[\"']\s*:\s*[\"']service_account[\"'].{0,8192}"
    r"[\"']private_key[\"']\s*:"
)

PLACEHOLDER_MARKERS = (
    "***",
    "dummy",
    "example",
    "placeholder",
    "process.env",
    "redacted",
    "replace_me",
    "test-only",
    "your_",
)

ENVIRONMENT_REFERENCE = re.compile(
    r"(?i)^(?:\$\{[A-Z_][A-Z0-9_]*\}|\$[A-Z_][A-Z0-9_]*|"
    r"%[A-Z_][A-Z0-9_]*%|process\.env\.[A-Z_][A-Z0-9_]*)$"
)


class PayloadError(ValueError):
    """Raised when a hook payload is invalid."""


def deny(reason: str) -> dict[str, Any]:
    return {"decision": "deny", "reason": reason, "continue": True}


def validate_payload(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise PayloadError("payload must be an object")
    for key in (
        "session_id",
        "transcript_path",
        "cwd",
        "hook_event_name",
        "timestamp",
        "tool_name",
    ):
        if not isinstance(payload.get(key), str) or not payload[key]:
            raise PayloadError(f"{key} must be a non-empty string")
    if payload["hook_event_name"] != "BeforeTool":
        raise PayloadError("unexpected hook event")
    if not isinstance(payload.get("tool_input"), dict):
        raise PayloadError("tool_input must be an object")
    cwd = Path(payload["cwd"])
    if not cwd.is_absolute():
        raise PayloadError("cwd must be absolute")
    return payload


def resolve_in_workspace(raw_path: str, cwd: Path) -> Path:
    if not raw_path or "\x00" in raw_path:
        raise PayloadError("invalid path")
    candidate = Path(raw_path).expanduser()
    if not candidate.is_absolute():
        candidate = cwd / candidate
    resolved_cwd = cwd.resolve(strict=False)
    resolved = candidate.resolve(strict=False)
    try:
        resolved.relative_to(resolved_cwd)
    except ValueError as exc:
        raise PayloadError("path escapes the workspace") from exc
    return resolved


def is_env_template(name: str) -> bool:
    lowered = name.lower()
    return lowered.startswith(".env.") and lowered.endswith(
        (".example", ".sample", ".template")
    )


def is_protected_path(path: Path) -> bool:
    lowered_name = path.name.lower()
    if lowered_name in PUBLIC_MOBILE_CONFIGS:
        return False
    if is_env_template(lowered_name):
        return False
    if lowered_name in PROTECTED_BASENAMES:
        return True
    if lowered_name.startswith(".env."):
        return True
    if path.suffix.lower() in PROTECTED_SUFFIXES:
        return True
    if any(part.lower() in PROTECTED_DIRECTORY_NAMES for part in path.parts):
        return True
    if re.search(r"(?i)(?:service[-_]?account|appstoreconnect|authkey_).*(?:\.json|\.p8)$", lowered_name):
        return True
    return False


def is_placeholder(value: str) -> bool:
    stripped = value.strip()
    lowered = stripped.lower()
    if ENVIRONMENT_REFERENCE.fullmatch(stripped):
        return True
    if stripped.startswith("<") and stripped.endswith(">"):
        return True
    return any(marker in lowered for marker in PLACEHOLDER_MARKERS)


def contains_real_secret(text: str) -> bool:
    if not text:
        return False
    if any(pattern.search(text) for pattern in HIGH_CONFIDENCE_SECRET_PATTERNS):
        return True
    if SERVICE_ACCOUNT.search(text):
        return True
    return any(not is_placeholder(match.group(2)) for match in SENSITIVE_ASSIGNMENT.finditer(text))


def command_references_protected_path(command: str, cwd: Path) -> bool:
    try:
        tokens = shlex.split(command, posix=os.name != "nt")
    except ValueError:
        return True
    for token in tokens:
        if token.startswith("-") or not any(char in token for char in ("/", "\\", ".")):
            continue
        cleaned = token.strip("\"'")
        try:
            candidate = resolve_in_workspace(cleaned, cwd)
        except PayloadError:
            continue
        if is_protected_path(candidate):
            return True
    return False


def evaluate(payload: Any) -> dict[str, Any]:
    try:
        data = validate_payload(payload)
        cwd = Path(data["cwd"])
        tool_name = data["tool_name"]
        tool_input = data["tool_input"]

        if tool_name == "read_file":
            raw_path = tool_input.get("file_path")
            if not isinstance(raw_path, str):
                raise PayloadError("file_path must be a string")
            target = resolve_in_workspace(raw_path, cwd)
            if is_protected_path(target):
                return deny("Reading credential, secret, private-key, or signing-material paths is blocked.")

        elif tool_name in {"write_file", "replace"}:
            raw_path = tool_input.get("file_path")
            if not isinstance(raw_path, str):
                raise PayloadError("file_path must be a string")
            target = resolve_in_workspace(raw_path, cwd)
            if is_protected_path(target):
                return deny("Writing credential, secret, private-key, or signing-material paths is blocked.")
            new_text = tool_input.get("content") if tool_name == "write_file" else tool_input.get("new_string")
            if not isinstance(new_text, str):
                raise PayloadError("new file content must be a string")
            if contains_real_secret(new_text):
                return deny("High-confidence credential or private-key material was detected in proposed content.")

        elif tool_name == "run_shell_command":
            command = tool_input.get("command")
            if not isinstance(command, str) or not command.strip():
                raise PayloadError("command must be a non-empty string")
            if contains_real_secret(command) or command_references_protected_path(command, cwd):
                return deny("Shell access to credential, secret, private-key, or signing material is blocked.")

        return {"decision": "allow"}
    except (PayloadError, OSError, RuntimeError) as exc:
        return deny(f"Secret guard rejected invalid input: {exc}")


def read_stdin_payload() -> Any:
    raw = sys.stdin.buffer.read(MAX_INPUT_BYTES + 1)
    if len(raw) > MAX_INPUT_BYTES:
        raise PayloadError("payload exceeds size limit")
    try:
        return json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PayloadError("payload is not valid UTF-8 JSON") from exc


def base_payload(tool_name: str, tool_input: dict[str, Any]) -> dict[str, Any]:
    return {
        "session_id": "test-session",
        "transcript_path": "/tmp/transcript.json",
        "cwd": "/tmp/mobile-project",
        "hook_event_name": "BeforeTool",
        "timestamp": "2026-01-01T00:00:00Z",
        "tool_name": tool_name,
        "tool_input": tool_input,
    }


class SecretGuardTests(unittest.TestCase):
    def test_allows_public_firebase_client_config(self) -> None:
        payload = base_payload(
            "write_file",
            {
                "file_path": "android/app/google-services.json",
                "content": '{"project_info":{"project_id":"public-id"},"api_key":[{"current_key":"AIzaPublicClientIdentifier"}]}',
            },
        )
        self.assertEqual(evaluate(payload)["decision"], "allow")

    def test_blocks_private_key_content(self) -> None:
        payload = base_payload(
            "write_file",
            {"file_path": "src/config.txt", "content": "-----BEGIN PRIVATE KEY-----\nabc"},
        )
        self.assertEqual(evaluate(payload)["decision"], "deny")

    def test_blocks_protected_key_read(self) -> None:
        payload = base_payload("read_file", {"file_path": "signing/distribution.pem"})
        self.assertEqual(evaluate(payload)["decision"], "deny")

    def test_blocks_protected_env_path(self) -> None:
        payload = base_payload("write_file", {"file_path": ".env", "content": "SAFE=value"})
        self.assertEqual(evaluate(payload)["decision"], "deny")

    def test_allows_env_template_placeholders(self) -> None:
        payload = base_payload(
            "write_file",
            {"file_path": ".env.example", "content": "CLIENT_SECRET=${CLIENT_SECRET}"},
        )
        self.assertEqual(evaluate(payload)["decision"], "allow")

    def test_blocks_real_secret_containing_dollar_characters(self) -> None:
        payload = base_payload(
            "write_file",
            {"file_path": "src/config.txt", "content": "password=P@$$w0rd-actual"},
        )
        self.assertEqual(evaluate(payload)["decision"], "deny")

    def test_blocks_package_registry_credential_files(self) -> None:
        payload = base_payload(
            "write_file",
            {
                "file_path": ".npmrc",
                "content": "//registry.npmjs.org/:_authToken=actualvalue123456",
            },
        )
        self.assertEqual(evaluate(payload)["decision"], "deny")

    def test_blocks_workspace_escape(self) -> None:
        payload = base_payload("replace", {"file_path": "../outside.txt", "new_string": "safe"})
        self.assertEqual(evaluate(payload)["decision"], "deny")

    def test_invalid_payload_fails_closed(self) -> None:
        self.assertEqual(evaluate({})["decision"], "deny")


def main() -> int:
    if sys.argv[1:] == ["--self-test"]:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(SecretGuardTests)
        result = unittest.TextTestRunner(stream=sys.stderr, verbosity=2).run(suite)
        return 0 if result.wasSuccessful() else 1
    try:
        payload = read_stdin_payload()
        result = evaluate(payload)
    except PayloadError as exc:
        result = deny(f"Secret guard rejected invalid input: {exc}")
    sys.stdout.write(json.dumps(result, separators=(",", ":")))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
