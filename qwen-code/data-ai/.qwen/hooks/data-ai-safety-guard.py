#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from typing import Any


DENIED_TOOLS = {
    "bash",
    "shell",
    "run_shell_command",
    "webfetch",
    "websearch",
    "web_fetch",
    "web_search",
}
PROTECTED_PATHS = ("/.git/", "/.env", ".pem", ".key")
SENSITIVE_TERMS = (
    "deploy",
    "publish",
    "release",
    "submit",
    "sign",
    "production",
    "credential",
    "private endpoint",
    "sensitive dataset",
    "personal data",
)
SECRET_PATTERNS = (
    re.compile("api" + r"[_-]?key", re.IGNORECASE),
    re.compile("pass" + "word", re.IGNORECASE),
    re.compile(r"BEGIN (RSA|OPENSSH|PRIVATE)", re.IGNORECASE),
)


def decision(kind: str, reason: str) -> dict[str, Any]:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": kind,
            "permissionDecisionReason": reason,
        }
    }


def deny(reason: str) -> None:
    print(json.dumps(decision("deny", reason)))
    sys.exit(0)


payload = json.load(sys.stdin)
tool_name = str(payload.get("tool_name", "")).strip().lower()
tool_input = payload.get("tool_input", {})
tool_text = json.dumps(tool_input, sort_keys=True)
normalized = tool_text.casefold()

if tool_name in DENIED_TOOLS or tool_name.startswith("mcp__"):
    deny("Data and AI policy denies shell, web, and MCP tools by default.")

if any(path in normalized for path in PROTECTED_PATHS):
    deny("Data and AI policy blocks protected paths and secret-like files.")

if any(term in normalized for term in SENSITIVE_TERMS):
    deny("Data and AI policy requires human review for sensitive, external, release, or production actions.")

if any(pattern.search(tool_text) for pattern in SECRET_PATTERNS):
    deny("Data and AI policy blocks secret-like tool input.")

print(json.dumps(decision("allow", "Data and AI safety guard passed.")))
