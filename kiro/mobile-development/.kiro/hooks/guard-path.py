#!/usr/bin/env python3
"""PreToolUse guard for Kiro mobile file writes."""

import json
import re
import sys
from pathlib import PurePosixPath, PureWindowsPath
from typing import Any


WRITE_TOOL_NAMES = {"fs_write", "write", "fsWrite"}
PUBLIC_CLIENT_FILES = {"google-services.json", "GoogleService-Info.plist"}
PROTECTED_PATH_PATTERN = re.compile(
    r"(?i)(^|[/\\])("
    r"local\.properties|"
    r"id_rsa|id_dsa|id_ecdsa|id_ed25519|"
    r".*\.(?:jks|keystore|p12|pem|key|mobileprovision)|"
    r".*(?:service[-_]?account|provisioning|certificate|private[-_]?key).*"
    r")($|[/\\])"
)
ENV_FILE_PATTERN = re.compile(r"(?i)(^|[/\\])\.env(?:$|[.](?!(?:example|sample|template)$)[^/\\]+$)")


def block(message: str) -> None:
    print(message, file=sys.stderr)
    sys.exit(2)


def load_event() -> dict[str, Any]:
    raw = sys.stdin.read()
    if "\x00" in raw:
        block("Blocked malformed path hook input containing a null byte.")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        block("Blocked malformed path hook input.")
    if not isinstance(data, dict):
        block("Blocked malformed path hook input: expected an object.")
    return data


def paths_from_event(event: dict[str, Any]) -> tuple[str, list[str]]:
    if event.get("hook_event_name") != "preToolUse":
        block("Blocked path hook event with unsupported hook_event_name.")
    if event.get("tool_name") not in WRITE_TOOL_NAMES:
        block("Blocked path hook event for unsupported tool_name.")
    for key in ("cwd", "session_id", "tool_input"):
        if key not in event:
            block(f"Blocked malformed path hook input: missing {key}.")

    cwd = event["cwd"]
    tool_input = event["tool_input"]
    if not isinstance(cwd, str) or not cwd.strip():
        block("Blocked malformed path hook input: cwd must be a non-empty string.")
    if not isinstance(tool_input, dict):
        block("Blocked malformed path hook input: tool_input must be an object.")

    operations = tool_input.get("operations")
    if not isinstance(operations, list) or not operations:
        block("Blocked malformed path hook input: missing write operations.")

    paths: list[str] = []
    for operation in operations:
        if not isinstance(operation, dict):
            block("Blocked malformed path hook input: operation must be an object.")
        path = operation.get("path")
        if not isinstance(path, str) or not path.strip():
            block("Blocked malformed path hook input: operation path must be a non-empty string.")
        paths.append(path.strip())
    return cwd.strip(), paths


def is_windows_absolute(path: str) -> bool:
    return bool(re.match(r"^[A-Za-z]:[\\/]", path) or path.startswith("\\\\"))


def is_posix_absolute(path: str) -> bool:
    return path.startswith("/")


def contains_traversal(path: str) -> bool:
    normalized = path.replace("\\", "/")
    return ".." in PurePosixPath(normalized).parts or ".." in PureWindowsPath(path).parts


def check_path(cwd: str, path: str) -> None:
    if "\x00" in path:
        block("Blocked write path containing a null byte.")
    if path != path.strip("\"'"):
        block(f"Blocked quoted write path: {path}")
    if any(char.isspace() for char in path):
        block(f"Blocked write path containing whitespace: {path}")
    if contains_traversal(path):
        block(f"Blocked path traversal in write path: {path}")

    normalized = path.replace("\\", "/")
    name = PurePosixPath(normalized).name
    if name not in PUBLIC_CLIENT_FILES and (ENV_FILE_PATTERN.search(path) or PROTECTED_PATH_PATTERN.search(path)):
        block(f"Blocked write touching secret or signing material path: {path}")

    cwd_normalized = cwd.replace("\\", "/").rstrip("/")
    if is_windows_absolute(path):
        block(f"Blocked Windows absolute write path: {path}")
    if is_posix_absolute(path):
        if not normalized.startswith(cwd_normalized + "/") and normalized != cwd_normalized:
            block(f"Blocked absolute write outside current Kiro workspace: {path}")
        if "/kiro/mobile-development/" not in normalized and not normalized.endswith("/kiro/mobile-development"):
            block(f"Blocked absolute write outside kiro/mobile-development: {path}")


def main() -> int:
    cwd, paths = paths_from_event(load_event())
    for path in paths:
        check_path(cwd, path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
