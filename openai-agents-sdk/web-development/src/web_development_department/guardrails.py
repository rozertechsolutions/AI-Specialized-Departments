"""Guardrails attached to agents and function tools."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, is_dataclass
from typing import Any

from agents import (
    Agent,
    GuardrailFunctionOutput,
    RunContextWrapper,
    ToolGuardrailFunctionOutput,
    TResponseInputItem,
    input_guardrail,
    output_guardrail,
    tool_input_guardrail,
    tool_output_guardrail,
)

from .models import FinalVerdict, FindingSeverity, Verdict
from .policy import (
    contains_secret,
    describes_out_of_scope_request,
    describes_prohibited_action,
    final_verdict_is_valid,
)


def _stringify(value: Any) -> str:
    if isinstance(value, str):
        return value
    if is_dataclass(value):
        return json.dumps(asdict(value), sort_keys=True)
    try:
        return json.dumps(value, sort_keys=True)
    except TypeError:
        return str(value)


@input_guardrail
async def safe_web_request_guardrail(
    ctx: RunContextWrapper[Any],
    agent: Agent[Any],
    input: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    del ctx, agent
    text = _stringify(input).strip()
    reasons: list[str] = []
    if not text:
        reasons.append("empty request")
    if contains_secret(text):
        reasons.append("secret-bearing request")
    if describes_out_of_scope_request(text):
        reasons.append("out-of-scope request")
    if describes_prohibited_action(text):
        reasons.append("prohibited automatic action")
    return GuardrailFunctionOutput(
        output_info={"reasons": reasons},
        tripwire_triggered=bool(reasons),
    )


@output_guardrail
async def final_verdict_guardrail(
    ctx: RunContextWrapper[Any],
    agent: Agent[Any],
    output: FinalVerdict,
) -> GuardrailFunctionOutput:
    del ctx, agent
    errors = final_verdict_is_valid(output)
    return GuardrailFunctionOutput(
        output_info={"errors": errors},
        tripwire_triggered=bool(errors),
    )


@tool_input_guardrail
def no_secret_tool_arguments(data: Any) -> ToolGuardrailFunctionOutput:
    text = str(getattr(data.context, "tool_arguments", "") or "")
    if contains_secret(text):
        return ToolGuardrailFunctionOutput.reject_content(
            "Remove secrets, credentials, tokens, and private endpoints before calling this tool."
        )
    return ToolGuardrailFunctionOutput.allow()


@tool_input_guardrail
def no_prohibited_tool_arguments(data: Any) -> ToolGuardrailFunctionOutput:
    text = str(getattr(data.context, "tool_arguments", "") or "")
    if describes_prohibited_action(text):
        return ToolGuardrailFunctionOutput.reject_content(
            "This package cannot execute commands, deploy, publish, mutate Git, install dependencies, or perform destructive actions."
        )
    return ToolGuardrailFunctionOutput.allow()


@tool_output_guardrail
def no_unsupported_success_claims(data: Any) -> ToolGuardrailFunctionOutput:
    text = str(getattr(data, "output", "") or "")
    success_claim = re.search(r"\b(tests?|build|deploy|browser|integration).{0,40}\b(pass(?:ed)?|succeed(?:ed)?)\b", text, re.I)
    if success_claim and "NOT_EXECUTED" not in text and "direct evidence" not in text.lower():
        return ToolGuardrailFunctionOutput.reject_content(
            "Output claimed execution success without direct evidence."
        )
    return ToolGuardrailFunctionOutput.allow()


def has_blocking_critical_findings(verdict: FinalVerdict) -> bool:
    return any(
        finding.blocking and finding.severity in {FindingSeverity.CRITICAL, FindingSeverity.HIGH}
        for finding in verdict.findings
    )


def final_pass_is_allowed(verdict: FinalVerdict) -> bool:
    return verdict.verdict is not Verdict.PASS or (
        not has_blocking_critical_findings(verdict)
        and not any(risk.blocking for risk in verdict.unresolved_risks)
        and all(item.status is not Verdict.NOT_EXECUTED for item in verdict.evidence)
    )
