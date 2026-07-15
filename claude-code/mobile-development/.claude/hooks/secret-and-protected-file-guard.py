#!/usr/bin/env python3
"""Deny direct access to protected mobile-development files and paths."""

from __future__ import annotations

import re
import shlex
from typing import Optional

from hook_common import (
    HookInputError,
    emit_pretool_decision,
    first_string,
    normalize_target,
    project_root,
    protected_path_reason,
    read_event,
    tool_input,
)


FILE_PATH_KEYS = {
    "Read": ("file_path", "path"),
    "Edit": ("file_path",),
    "Write": ("file_path",),
    "NotebookEdit": ("notebook_path", "file_path"),
}


def command_protected_reason(command: str, *, posix: bool) -> Optional[str]:
    if "\x00" in command:
        return "command contains a NUL byte"
    if "-----BEGIN PRIVATE KEY-----" in command:
        return "command contains private-key material"
    try:
        tokens = shlex.split(command, posix=posix)
    except ValueError:
        return "command quoting is malformed and cannot be inspected safely"

    for token in tokens:
        candidate = token.strip("\"'(),;|&<>")
        if "=" in candidate and not candidate.startswith(("http://", "https://")):
            _, candidate = candidate.split("=", 1)
        reason = protected_path_reason(candidate)
        if reason:
            return f"command references {reason}: {candidate}"

    lower = command.lower().replace("\\", "/")
    if re.search(r"(?:^|[\s'\"])(?:~/)?\.(?:ssh|gnupg|aws)(?:/|[\s'\"]|$)", lower):
        return "command references a protected credential directory"
    return None


def main() -> int:
    try:
        event = read_event()
        if event.get("hook_event_name") != "PreToolUse":
            raise HookInputError("expected a PreToolUse event")
        name = event.get("tool_name")
        if not isinstance(name, str):
            raise HookInputError("tool_name is required")
        payload = tool_input(event)

        if name in {"Bash", "PowerShell"}:
            command = payload.get("command")
            if not isinstance(command, str) or not command.strip():
                raise HookInputError("Bash command is required")
            reason = command_protected_reason(command, posix=name == "Bash")
            if reason:
                return emit_pretool_decision("deny", f"Protected-file guard blocked the operation: {reason}.")
            return 0

        keys = FILE_PATH_KEYS.get(name)
        if keys is None:
            raise HookInputError(f"unsupported matched tool: {name}")
        raw_path = first_string(payload, keys)
        if raw_path is None:
            raise HookInputError(f"{name} target path is required")

        root = project_root(event)
        cwd = event.get("cwd") if isinstance(event.get("cwd"), str) else root
        target = normalize_target(raw_path, root, cwd=cwd)
        if target.traversal:
            return emit_pretool_decision("deny", "Protected-file guard blocked a path containing '..' traversal.")
        if not target.within_root:
            return emit_pretool_decision("deny", "Protected-file guard blocked access outside CLAUDE_PROJECT_DIR.")
        reason = protected_path_reason(target.relative)
        if reason:
            return emit_pretool_decision(
                "deny", f"Protected-file guard blocked {name} access to {reason}: {target.relative}."
            )
        return 0
    except HookInputError as exc:
        return emit_pretool_decision("deny", f"Protected-file guard failed closed: {exc}.")
    except Exception:
        return emit_pretool_decision("deny", "Protected-file guard failed closed because validation could not complete.")


if __name__ == "__main__":
    raise SystemExit(main())
