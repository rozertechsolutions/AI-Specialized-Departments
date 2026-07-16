#!/usr/bin/env python3
import json
import re
import sys


SECRET_FILE_RE = re.compile(
    r"(^|/)(\.env(\.|$)|.*\.(keystore|jks|p12|pfx|pem|key|mobileprovision|cer|crt)$|"
    r"service-account.*\.json$)",
    re.IGNORECASE,
)
SECRET_VALUE_RE = re.compile(
    r"(?i)(api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|private[_-]?key|"
    r"password|passwd|secret|signing[_-]?key|keystore[_-]?password)\s*[:=]\s*['\"][^'\"<>{}\s]{8,}['\"]"
)
PRIVATE_KEY_RE = re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")
ALLOWLIST_RE = re.compile(r"(?i)(example|sample|placeholder|<[^>]+>|\$\{[^}]+}|your[_-]?(key|token|secret|password))")


def block(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def edit_text(data):
    for edit in data.get("tool_info", {}).get("edits", []) or []:
        value = edit.get("new_string")
        if isinstance(value, str):
            yield value


def main():
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError as exc:
        block(f"secret_guard: malformed hook JSON: {exc}")

    if data.get("agent_action_name") != "pre_write_code":
        return

    info = data.get("tool_info", {})
    file_path = str(info.get("file_path") or "")
    if SECRET_FILE_RE.search(file_path.replace("\\", "/")):
        block(f"secret_guard: blocked write to secret or signing material path: {file_path}")

    for text in edit_text(data):
        if PRIVATE_KEY_RE.search(text):
            block("secret_guard: blocked private key material")
        for match in SECRET_VALUE_RE.finditer(text):
            snippet = match.group(0)
            if not ALLOWLIST_RE.search(snippet):
                block("secret_guard: blocked likely hardcoded secret")


if __name__ == "__main__":
    main()
