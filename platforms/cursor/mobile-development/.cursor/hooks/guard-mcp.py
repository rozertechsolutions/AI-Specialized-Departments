#!/usr/bin/env python3
import json
import re
import sys


DENY_PATTERNS = [
    r"\b(auth|oauth|login|connect|token|secret|credential|key|certificate)\b",
    r"\b(write|create|update|delete|remove|publish|upload|submit|deploy|release)\b",
    r"\b(payment|billing|charge|spend)\b",
]


def emit(permission, message):
    print(json.dumps({"continue": True, "permission": permission, "user_message": message}))


def main():
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        emit("deny", "MCP action blocked: malformed hook input.")
        return

    command = str(payload.get("command") or payload.get("tool_name") or "")
    lowered = command.lower()

    if any(re.search(pattern, lowered) for pattern in DENY_PATTERNS):
        emit("deny", "MCP action blocked: authentication, credentials, external writes, publishing, deployment, or spending are not allowed by default.")
        return

    emit("ask", "MCP action requires human review because MCP integrations are inactive by default in this specialization.")


if __name__ == "__main__":
    main()
