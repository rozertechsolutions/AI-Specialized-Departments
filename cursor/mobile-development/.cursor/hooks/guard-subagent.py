#!/usr/bin/env python3
import json
import sys


READ_ONLY_REVIEWERS = {
    "mobile-architect",
    "mobile-security-reviewer",
    "mobile-ui-accessibility-reviewer",
    "mobile-performance-reviewer",
    "mobile-code-reviewer",
}

KNOWN_AGENTS = READ_ONLY_REVIEWERS | {
    "android-engineer",
    "ios-engineer",
    "kmp-engineer",
    "flutter-engineer",
    "react-native-engineer",
    "mobile-test-engineer",
    "mobile-release-engineer",
}


def emit(permission, message):
    print(json.dumps({"continue": True, "permission": permission, "user_message": message}))


def main():
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        emit("deny", "Subagent blocked: malformed hook input.")
        return

    name = str(payload.get("name") or payload.get("subagent_name") or payload.get("agent_name") or "").strip()
    prompt = str(payload.get("prompt") or payload.get("description") or "").lower()

    if name and name not in KNOWN_AGENTS:
        emit("ask", f"Subagent `{name}` is not part of the mobile-development responsibility matrix.")
        return

    if name in READ_ONLY_REVIEWERS:
        write_terms = ("edit", "modify", "write", "implement", "fix", "create file", "delete", "apply patch")
        if any(term in prompt for term in write_terms):
            emit("deny", f"Subagent `{name}` is read-only and cannot perform implementation or source edits.")
            return

    if "review own" in prompt or "self-review" in prompt:
        emit("deny", "Subagent blocked: implementation roles may not perform independent final self-review.")
        return

    if "spawn" in prompt and "subagent" in prompt:
        emit("ask", "Subagent nesting requires human review to avoid delegation cycles.")
        return

    emit("allow", "Subagent allowed by mobile-development responsibility guard.")


if __name__ == "__main__":
    main()
