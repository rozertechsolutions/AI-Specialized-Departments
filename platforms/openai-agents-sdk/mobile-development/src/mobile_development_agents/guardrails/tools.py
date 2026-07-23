from __future__ import annotations

import json
from typing import Any, Mapping

from mobile_development_agents.policies.security import (
    contains_secret,
    validate_relative_project_path,
    validate_shell_command,
)


def _blocked_messages(findings: object) -> tuple[str, ...]:
    return tuple(finding.message for finding in findings if getattr(finding, "blocked", False))


def _tool_context(data: object) -> object | None:
    return getattr(data, "context", None)


def _tool_name(data: object) -> str:
    context = _tool_context(data)
    return str(getattr(context, "tool_name", "") or "")


def _tool_arguments(data: object) -> Mapping[str, Any] | None:
    context = _tool_context(data)
    structured = getattr(context, "tool_input", None)
    if isinstance(structured, Mapping):
        return structured
    raw = getattr(context, "tool_arguments", None)
    if not isinstance(raw, str) or not raw.strip():
        return None
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, Mapping) else None


def validate_tool_arguments(tool_name: str, arguments: Mapping[str, Any] | None) -> tuple[str, ...]:
    if arguments is None:
        return ("Tool arguments must be structured JSON.",)

    issues: list[str] = []
    if tool_name in {"read_project_file", "edit_project_file"}:
        path = arguments.get("path")
        if not isinstance(path, str):
            issues.append("Tool path must be a string.")
        else:
            issues.extend(_blocked_messages(validate_relative_project_path(path)))

    if tool_name == "edit_project_file":
        content = arguments.get("content")
        if not isinstance(content, str):
            issues.append("Edit content must be a string.")
        elif contains_secret(content):
            issues.append("Edit content appears to contain a secret.")

    if tool_name == "run_validation_command":
        command = arguments.get("command")
        if not isinstance(command, str):
            issues.append("Validation command must be a string.")
        else:
            issues.extend(_blocked_messages(validate_shell_command(command)))

    if tool_name not in {"read_project_file", "edit_project_file", "run_validation_command"}:
        issues.append(f"Unsupported guarded function tool: {tool_name or 'unknown'}.")
    return tuple(issues)


def build_sdk_tool_guardrails() -> tuple[object, object]:
    try:
        from agents import ToolGuardrailFunctionOutput, tool_input_guardrail, tool_output_guardrail
    except ImportError as exc:
        raise RuntimeError("Install openai-agents to build SDK tool guardrails.") from exc

    @tool_input_guardrail
    def block_unsafe_tool_input(data: object) -> object:
        issues = validate_tool_arguments(_tool_name(data), _tool_arguments(data))
        if issues:
            return ToolGuardrailFunctionOutput.reject_content("; ".join(issues))
        return ToolGuardrailFunctionOutput.allow()

    @tool_output_guardrail
    def block_secret_tool_output(data: object) -> object:
        output = getattr(data, "output", "")
        if contains_secret(str(output or "")):
            return ToolGuardrailFunctionOutput.reject_content(
                "Tool output contained sensitive data."
            )
        return ToolGuardrailFunctionOutput.allow()

    return block_unsafe_tool_input, block_secret_tool_output
