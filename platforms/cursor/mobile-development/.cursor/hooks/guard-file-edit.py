#!/usr/bin/env python3
import json
import os
import re
import sys


SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (RSA |EC |OPENSSH |DSA |)PRIVATE KEY-----"),
    re.compile(r"(?i)\b(api[_-]?key|secret|token|password|passwd|keystore|provisioning|certificate)\b\s*[:=]\s*['\"]?[^'\"\s]{12,}"),
    re.compile(r"(?i)\b(client_secret|private_key|refresh_token|access_token)\b"),
]

BLOCKED_EXTENSIONS = {".p12", ".p8", ".pem", ".key", ".keystore", ".jks", ".mobileprovision"}


def emit(permission, message):
    print(json.dumps({"continue": True, "permission": permission, "user_message": message}))


def candidate_paths(payload):
    values = []
    for key in ("file_path", "path", "modified_file", "modified_files", "files"):
        value = payload.get(key)
        if isinstance(value, str):
            values.append(value)
        elif isinstance(value, list):
            values.extend(str(item) for item in value)
    return values


def specialization_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def in_scope(path):
    workspace = specialization_root()
    normalized = os.path.abspath(path if os.path.isabs(path) else os.path.join(workspace, path))
    return normalized.startswith(workspace)


def inspect_file(path):
    _, ext = os.path.splitext(path.lower())
    if ext in BLOCKED_EXTENSIONS:
        return f"blocked signing or credential file type `{ext}`"
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as handle:
            content = handle.read(200000)
    except OSError:
        return None
    for pattern in SECRET_PATTERNS:
        if pattern.search(content):
            return "possible secret, token, credential, signing material, or private key"
    return None


def main():
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        emit("deny", "File edit blocked: malformed hook input.")
        return

    paths = candidate_paths(payload)
    if not paths:
        emit("allow", "File edit allowed: no path provided for post-edit scan.")
        return

    for path in paths:
        if ".." in path.replace("\\", "/").split("/"):
            emit("deny", f"File edit blocked: path traversal detected in `{path}`.")
            return
        if not in_scope(path):
            emit("deny", f"File edit blocked: `{path}` is outside cursor/mobile-development.")
            return
        issue = inspect_file(path)
        if issue:
            emit("deny", f"File edit blocked: {issue} detected in `{path}`.")
            return

    emit("allow", "File edit allowed by mobile-development guard.")


if __name__ == "__main__":
    main()
