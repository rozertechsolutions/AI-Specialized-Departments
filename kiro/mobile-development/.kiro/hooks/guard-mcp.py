#!/usr/bin/env python3
"""Non-mutating Kiro hook guard for MCP and connector activation."""

import json
import re
import sys


raw = sys.stdin.read()
try:
    payload = json.dumps(json.loads(raw), sort_keys=True) if raw else ""
except json.JSONDecodeError:
    payload = raw

blocked = re.search(
    r"(?i)(mcpservers|mcp\.json|oauth|clientid|redirecturi|connect|authenticate|authorize|token|scope|connector|server\s+url|external\s+write)",
    payload,
)

if blocked:
    print(
        "Blocked MCP/connector activation. MCP must remain inactive until a human explicitly approves exposed data, scopes, external writes, and approval behavior.",
        file=sys.stderr,
    )
    sys.exit(2)

sys.exit(0)
