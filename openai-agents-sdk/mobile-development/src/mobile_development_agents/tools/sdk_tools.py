from __future__ import annotations

from mobile_development_agents.tools.contracts import GuardedToolHost, ToolResult


def _host_from_context(ctx: object) -> GuardedToolHost:
    workflow_context = getattr(ctx, "context", None)
    host = getattr(workflow_context, "tool_host", None)
    if not isinstance(host, GuardedToolHost):
        raise PermissionError("No host-injected project tool host is available.")
    return host


def build_project_function_tools() -> list[object]:
    try:
        from agents import RunContextWrapper, function_tool
    except ImportError as exc:
        raise RuntimeError("Install openai-agents to build SDK function tools.") from exc

    from mobile_development_agents.guardrails.tools import build_sdk_tool_guardrails

    tool_input_guardrail, tool_output_guardrail = build_sdk_tool_guardrails()
    common = {
        "tool_input_guardrails": [tool_input_guardrail],
        "tool_output_guardrails": [tool_output_guardrail],
    }

    @function_tool(**common)
    def read_project_file(ctx: RunContextWrapper[object], path: str) -> ToolResult:
        """Read a project-relative file through the host-injected read tool."""
        return _host_from_context(ctx).read_project_file(path)

    @function_tool(needs_approval=True, **common)
    def edit_project_file(ctx: RunContextWrapper[object], path: str, content: str) -> ToolResult:
        """Write scoped project content through the host-injected edit tool after approval."""
        return _host_from_context(ctx).edit_project_file(path, content)

    @function_tool(needs_approval=True, **common)
    def run_validation_command(ctx: RunContextWrapper[object], command: str) -> ToolResult:
        """Run a discovered non-destructive validation command through the host."""
        return _host_from_context(ctx).run_validation_command(command)

    return [read_project_file, edit_project_file, run_validation_command]
