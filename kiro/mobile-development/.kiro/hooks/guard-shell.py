#!/usr/bin/env python3
"""PreToolUse guard for Kiro mobile shell execution."""

import base64
import json
import re
import shlex
import sys
from typing import Any


SHELL_TOOL_NAMES = {"execute_bash", "shell", "execute_cmd"}

BLOCK_PATTERNS = [
    (r"(^|[\s;&|])git\s+(commit|push|pull|merge|rebase|reset|clean|checkout|restore|switch|branch|tag)\b", "git state-changing command"),
    (r"(^|[\s;&|])rm\s+(-|/|~|\*|\.)", "destructive remove command"),
    (r"(^|[\s;&|])(mv|cp|chmod|chown)\s+.*(/etc|/var|/private|/usr|/bin|/sbin|/Library|~/.ssh)\b", "sensitive filesystem mutation"),
    (r"(^|[\s;&|])(sudo|su)\b", "privilege escalation"),
    (r"\b(npm|pnpm|yarn)\s+(install|add|update|upgrade|publish)\b", "dependency installation or publication"),
    (r"\b(pip|pip3|gem|brew|cargo)\s+install\b", "dependency installation"),
    (r"\b(dart|flutter)\s+pub\s+(add|upgrade|publish)\b", "dependency installation or publication"),
    (r"\b(bundle)\s+(install|update|exec\s+fastlane)\b", "dependency installation or release automation"),
    (r"\b(publish|upload|deploy|submit|distribute|release)\b", "publication or deployment action"),
    (r"\b(sign|codesign|notarytool|altool|fastlane\s+(deliver|supply|pilot|match))\b", "signing or store action"),
    (r"\b(keystore|provisioning\s+profile|certificate|p12|mobileprovision|service-account)\b", "signing or credential material"),
    (r"\b(firebase|appcenter|sentry-cli|play\s+store|app\s+store|eas\s+(build|submit))\b", "external release or telemetry service"),
    (r"(;|&&|\|\||\|)", "command chaining"),
    (r"(^|[^\\])([<>])", "redirection"),
    (r"\$\(|`", "command substitution"),
    (r"\b(base64|openssl\s+enc|xxd\s+-r|python\s+-c|python3\s+-c|perl\s+-e|ruby\s+-e|node\s+-e)\b", "encoded or inline executable payload"),
    (r"(^|[\s\"'])\.\.(/|\\)", "path traversal"),
    (r"(^|[\s\"'])(/etc|/var|/private|/usr|/bin|/sbin|/Library|~/.ssh)\b", "sensitive POSIX path"),
    (r"\b[A-Za-z]:\\", "Windows absolute path"),
]


def block(message: str) -> None:
    print(message, file=sys.stderr)
    sys.exit(2)


def load_event() -> dict[str, Any]:
    raw = sys.stdin.read()
    if "\x00" in raw:
        block("Blocked malformed shell hook input containing a null byte.")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        block("Blocked malformed shell hook input.")
    if not isinstance(data, dict):
        block("Blocked malformed shell hook input: expected an object.")
    return data


def command_from_event(event: dict[str, Any]) -> str:
    if event.get("hook_event_name") != "preToolUse":
        block("Blocked shell hook event with unsupported hook_event_name.")
    if event.get("tool_name") not in SHELL_TOOL_NAMES:
        block("Blocked shell hook event for unsupported tool_name.")
    for key in ("cwd", "session_id", "tool_input"):
        if key not in event:
            block(f"Blocked malformed shell hook input: missing {key}.")

    tool_input = event["tool_input"]
    if not isinstance(tool_input, dict):
        block("Blocked malformed shell hook input: tool_input must be an object.")
    command = tool_input.get("command")
    if not isinstance(command, str) or not command.strip():
        block("Blocked malformed shell hook input: missing command.")
    if "\x00" in command:
        block("Blocked shell command containing a null byte.")
    return command.strip()


def check_encoded_tokens(tokens: list[str]) -> None:
    for token in tokens:
        if len(token) < 80:
            continue
        padded = token + ("=" * (-len(token) % 4))
        try:
            decoded = base64.b64decode(padded, validate=False)
        except Exception:
            continue
        lowered = decoded.lower()
        if any(marker in lowered for marker in (b"sh", b"rm ", b"curl ", b"bash", b"python")):
            block("Blocked suspicious encoded shell payload.")


def main() -> int:
    command = command_from_event(load_event())
    lowered = command.lower()

    for pattern, reason in BLOCK_PATTERNS:
        if re.search(pattern, lowered):
            block(f"Blocked mobile shell command: {reason}. Request human approval and keep work scoped to kiro/mobile-development.")

    try:
        tokens = shlex.split(command)
    except ValueError as exc:
        block(f"Blocked malformed shell command: {exc}")
    if not tokens:
        block("Blocked empty shell command.")
    if any(token.strip() in {"", ".", ".."} for token in tokens):
        block("Blocked malformed shell command containing empty or traversal token.")

    check_encoded_tokens(tokens)
    return 0


if __name__ == "__main__":
    sys.exit(main())
