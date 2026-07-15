from __future__ import annotations

from mobile_development_agents.policies.security import validate_shell_command


def validate_tool_arguments(arguments: str) -> tuple[str, ...]:
    return tuple(finding.message for finding in validate_shell_command(arguments) if finding.blocked)


def build_sdk_tool_guardrails() -> tuple[object, object]:
    try:
        from agents import ToolGuardrailFunctionOutput, tool_input_guardrail, tool_output_guardrail
    except ImportError as exc:
        raise RuntimeError("Install openai-agents to build SDK tool guardrails.") from exc

    @tool_input_guardrail
    def block_unsafe_tool_input(data: object) -> object:
        context = getattr(data, "context", None)
        tool_arguments = getattr(context, "tool_arguments", "") if context is not None else ""
        issues = validate_tool_arguments(str(tool_arguments or ""))
        if issues:
            return ToolGuardrailFunctionOutput.reject_content("; ".join(issues))
        return ToolGuardrailFunctionOutput.allow()

    @tool_output_guardrail
    def block_secret_tool_output(data: object) -> object:
        from mobile_development_agents.policies.security import contains_secret

        if contains_secret(str(getattr(data, "output", "") or "")):
            return ToolGuardrailFunctionOutput.reject_content("Tool output contained sensitive data.")
        return ToolGuardrailFunctionOutput.allow()

    return block_unsafe_tool_input, block_secret_tool_output
