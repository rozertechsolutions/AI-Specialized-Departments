#!/usr/bin/env python3
import json
import re
import shlex
import sys


BLOCK_PATTERNS = [
    r"(?i)\brm\s+-[^\n]*[rf]",
    r"(?i)\bsudo\b",
    r"(?i)\bchmod\s+(-R\s+)?777\b",
    r"(?i)\b(chown|mkfs|diskutil|dd)\b",
    r"(?i)\bgit\s+(reset|clean|checkout|restore|push|pull|merge|rebase|branch|switch|commit|tag)\b",
    r"(?i)\b(fastlane|gradle|./gradlew|xcodebuild|flutter|eas|appcenter|firebase|gcloud|aws)\b.*\b(upload|publish|deploy|submit|release|sign|archive|distribute)\b",
    r"(?i)\bsecurity\s+(import|unlock-keychain|set-key-partition-list)\b",
    r"(?i)\b(npm|pnpm|yarn|bun|pip|gem|bundle|brew)\b.*\b(install|add|update|upgrade)\b",
]
SHELL_OPERATOR_RE = re.compile(r"(\|\||&&|;|\||`|\$\(|<\(|>|>>|<<)")
ENCODED_RE = re.compile(r"(?i)(base64\s+-d|frombase64string|certutil\s+-decode|powershell.+-enc)")


def block(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def main():
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError as exc:
        block(f"command_guard: malformed hook JSON: {exc}")

    if data.get("agent_action_name") != "pre_run_command":
        return

    command = str(data.get("tool_info", {}).get("command_line") or "")
    if not command.strip():
        return

    if "\x00" in command:
        block("command_guard: blocked command with null byte")
    if SHELL_OPERATOR_RE.search(command):
        block("command_guard: blocked shell chaining, redirection, pipe, or substitution")
    if ENCODED_RE.search(command):
        block("command_guard: blocked encoded or decoded command execution")

    try:
        shlex.split(command, posix=True)
    except ValueError as exc:
        block(f"command_guard: malformed command quoting: {exc}")

    for pattern in BLOCK_PATTERNS:
        if re.search(pattern, command):
            block("command_guard: blocked command requiring explicit human approval")


if __name__ == "__main__":
    main()
