#!/usr/bin/env python3
"""Non-mutating Kiro hook guard for mobile shell commands."""

import base64
import json
import re
import shlex
import sys


def load_payload() -> str:
    raw = sys.stdin.read()
    if not raw:
        return ""
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        print("Blocked malformed shell hook input.", file=sys.stderr)
        sys.exit(2)
    values = []
    stack = [data]
    while stack:
        item = stack.pop()
        if isinstance(item, dict):
            stack.extend(item.values())
        elif isinstance(item, list):
            stack.extend(item)
        elif isinstance(item, str):
            values.append(item)
    return "\n".join(values)


COMMAND = load_payload()
LOWER = COMMAND.lower()

BLOCK_PATTERNS = [
    (r"(^|[\s;&|])git\s+(commit|push|pull|merge|rebase|reset|clean|checkout|restore|switch|branch|tag)\b", "git state-changing command"),
    (r"(^|[\s;&|])rm\s+(-|/|~|\*)", "destructive remove command"),
    (r"(^|[\s;&|])(sudo|su)\b", "privilege escalation"),
    (r"\b(publish|upload|deploy|submit|distribute|release)\b", "publication or deployment action"),
    (r"\b(sign|codesign|notarytool|altool|fastlane\s+(deliver|supply|pilot|match))\b", "signing or store action"),
    (r"\b(keystore|provisioning profile|certificate|p12|mobileprovision|service-account)\b", "signing or credential material"),
    (r"\b(firebase|appcenter|sentry-cli|play\s+store|app\s+store)\b", "external release or telemetry service"),
    (r"(;|&&|\|\||\|)", "command chaining"),
    (r"(^|[^\\])([<>])", "redirection"),
    (r"\$\(|`", "command substitution"),
    (r"\b(base64|openssl enc|xxd -r|python -c|python3 -c|perl -e|ruby -e|node -e)\b", "encoded or inline executable payload"),
    (r"(^|[\s\"'])\.\.(/|\\)", "path traversal"),
    (r"(^|[\s\"'])(/etc|/var|/private|/usr|/bin|/sbin|/Library|~/\.ssh)\b", "sensitive POSIX path"),
    (r"\b[A-Za-z]:\\", "Windows absolute path"),
]

for pattern, reason in BLOCK_PATTERNS:
    if re.search(pattern, LOWER):
        print(f"Blocked mobile shell command: {reason}. Request human approval and keep work scoped to kiro/mobile-development.", file=sys.stderr)
        sys.exit(2)

try:
    tokens = shlex.split(COMMAND)
except ValueError as exc:
    print(f"Blocked malformed shell command: {exc}", file=sys.stderr)
    sys.exit(2)

if any(token.strip() in {"", ".", ".."} for token in tokens):
    print("Blocked malformed shell command containing empty or traversal token.", file=sys.stderr)
    sys.exit(2)

for token in tokens:
    if len(token) > 80:
        try:
            decoded = base64.b64decode(token + "==", validate=False)
        except Exception:
            continue
        if b"sh" in decoded or b"rm " in decoded or b"curl " in decoded:
            print("Blocked suspicious encoded shell payload.", file=sys.stderr)
            sys.exit(2)

sys.exit(0)
