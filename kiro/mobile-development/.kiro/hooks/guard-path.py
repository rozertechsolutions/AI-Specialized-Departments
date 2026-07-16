#!/usr/bin/env python3
"""Non-mutating Kiro hook guard for file write/delete scope."""

import json
import re
import sys
from pathlib import PurePosixPath, PureWindowsPath


raw = sys.stdin.read()
try:
    data = json.loads(raw) if raw else {}
except json.JSONDecodeError:
    print("Blocked malformed path hook input.", file=sys.stderr)
    sys.exit(2)

strings = []
stack = [data]
while stack:
    item = stack.pop()
    if isinstance(item, dict):
        stack.extend(item.values())
    elif isinstance(item, list):
        stack.extend(item)
    elif isinstance(item, str):
        strings.append(item)

candidate_pattern = re.compile(
    r"([A-Za-z]:\\[^\s\"']+|/[^\s\"']+|(?:^|[\s\"'])(?:\.?\.?/)?[A-Za-z0-9_.-][A-Za-z0-9_./\\ -]*)"
)
paths = []
for value in strings:
    paths.extend(match.group(1).strip().strip("\"'") for match in candidate_pattern.finditer(value))

secret_markers = re.compile(
    r"(?i)(\.env|id_rsa|id_dsa|id_ecdsa|id_ed25519|keystore|\.jks|\.p12|\.pem|\.key|mobileprovision|provisioning|certificate|service-account)"
)

for path in paths:
    normalized = path.replace("\\", "/")
    if ".." in PurePosixPath(normalized).parts or ".." in PureWindowsPath(path).parts:
        print(f"Blocked path traversal in write/delete path: {path}", file=sys.stderr)
        sys.exit(2)
    if secret_markers.search(path):
        print(f"Blocked write/delete touching secret or signing material path: {path}", file=sys.stderr)
        sys.exit(2)
    if normalized.startswith("/") and "/kiro/mobile-development/" not in normalized:
        print(f"Blocked absolute write/delete outside kiro/mobile-development: {path}", file=sys.stderr)
        sys.exit(2)
    if not normalized.startswith(("./", "kiro/mobile-development/", ".kiro/")) and "kiro/mobile-development/" not in normalized:
        if "/" in normalized:
            print(f"Blocked relative write/delete outside specialization scope: {path}", file=sys.stderr)
            sys.exit(2)

sys.exit(0)
