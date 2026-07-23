import json
import re
import sys


DENIED_TOOLS = re.compile(r"^(bash|write_file|edit|mcp_.*|connector_.*)$", re.IGNORECASE)
SECRET_PATTERNS = [
    re.compile("api" + r"[_-]?key", re.IGNORECASE),
    re.compile("pass" + "word", re.IGNORECASE),
    re.compile(r"BEGIN (RSA|OPENSSH|PRIVATE)", re.IGNORECASE),
]


def deny(reason):
    print(json.dumps({"decision": "deny", "reason": reason}))
    sys.exit(0)


payload = json.load(sys.stdin)
tool_name = str(payload.get("tool_name", ""))
tool_input = json.dumps(payload.get("tool_input", {}), sort_keys=True)

if DENIED_TOOLS.match(tool_name):
    deny("Data and AI Vibe policy denies write-capable, shell, MCP, and connector tools by default.")

if any(pattern.search(tool_input) for pattern in SECRET_PATTERNS):
    deny("Data and AI Vibe policy blocks tool input that appears to reference secrets or private key material.")

sys.exit(0)
