#!/usr/bin/env python3
import json
import sys


def main():
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError as exc:
        print(f"mcp_guard: malformed hook JSON: {exc}", file=sys.stderr)
        sys.exit(2)

    if data.get("agent_action_name") == "pre_mcp_tool_use":
        info = data.get("tool_info", {})
        server = info.get("mcp_server_name", "unknown")
        tool = info.get("mcp_tool_name", "unknown")
        print(f"mcp_guard: MCP use requires explicit human approval: {server}.{tool}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
