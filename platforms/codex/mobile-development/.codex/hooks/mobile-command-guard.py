#!/usr/bin/env python3
"""Block destructive commands targeting mobile devices and virtual devices."""

from __future__ import annotations

import json
import re
import sys
from typing import Any


BLOCKED_COMMANDS = (
    ("firmware or partition mutation", re.compile(r"\bfastboot\b[^\n]*(?:\bflash\b|\berase\b|\bformat\b|\boem\s+unlock\b|\bflashing\s+unlock\b)", re.I)),
    ("bootloader or recovery reboot", re.compile(r"\badb\b[^\n]*\breboot\s+(?:bootloader|recovery|fastboot)\b", re.I)),
    ("destructive privileged device shell", re.compile(r"\badb\b[^\n]*\bshell\b[^\n]*(?:\bsu\b|\bmkfs\b|\bdd\s+if=|\brm\s+-[a-zA-Z]*r[a-zA-Z]*f\s+/)", re.I)),
    ("application data deletion", re.compile(r"\badb\b[^\n]*\bshell\s+pm\s+clear\b", re.I)),
    ("Android emulator data wipe", re.compile(r"\bemulator\b[^\n]*\s-wipe-data\b", re.I)),
    ("Android virtual-device deletion", re.compile(r"\bavdmanager\b[^\n]*\bdelete\s+avd\b", re.I)),
    ("Apple simulator erase or deletion", re.compile(r"\bxcrun\s+simctl\s+(?:erase|delete)\b", re.I)),
    ("physical Apple device erase", re.compile(r"\bideviceerase\b", re.I)),
)


def deny(reason: str) -> None:
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )
    sys.stdout.write("\n")
    raise SystemExit(0)


def command_from_stdin() -> str:
    try:
        payload: Any = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, TypeError):
        deny("Mobile command guard received invalid hook input.")
    if not isinstance(payload, dict):
        deny("Mobile command guard received invalid hook input.")
    if payload.get("hook_event_name") != "PreToolUse" or payload.get("tool_name") != "Bash":
        return ""
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict) or not isinstance(tool_input.get("command"), str):
        deny("Mobile command guard could not inspect the pending shell command.")
    return tool_input["command"]


def normalize_command(command: str) -> str:
    """Join shell line continuations so split command tokens remain inspectable."""
    return re.sub(r"\\\r?\n", " ", command)


def main() -> None:
    command = normalize_command(command_from_stdin())
    for label, pattern in BLOCKED_COMMANDS:
        if pattern.search(command):
            deny(f"Blocked {label}. Destructive device and simulator operations are prohibited.")


if __name__ == "__main__":
    main()
