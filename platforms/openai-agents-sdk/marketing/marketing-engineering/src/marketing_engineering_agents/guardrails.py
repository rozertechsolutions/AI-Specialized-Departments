from __future__ import annotations

import re
from typing import Any

from agents import Agent, GuardrailFunctionOutput, RunContextWrapper, input_guardrail, output_guardrail

from .context import MarketingContext
from .models import WorkOutput


_SECRET_PATTERNS = (
    re.compile(r"(?i)\b(api[_ -]?key|secret|password|access[_ -]?token)\s*[:=]\s*\S+"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{12,}\b"),
)
_EXTERNAL_ACTIONS = (
    "publish", "send", "spend", "activate campaign", "upload audience",
    "deploy to production", "delete production", "launch campaign",
)


def _input_text(value: str | list[Any]) -> str:
    if isinstance(value, str):
        return value
    return repr(value)


@input_guardrail(name="marketing_request_guardrail", run_in_parallel=False)
async def marketing_request_guardrail(
    context: RunContextWrapper[MarketingContext],
    agent: Agent[Any],
    input: str | list[Any],
) -> GuardrailFunctionOutput:
    text = _input_text(input)
    secret_detected = any(pattern.search(text) for pattern in _SECRET_PATTERNS)
    requested_actions = [action for action in _EXTERNAL_ACTIONS if action in text.lower()]
    unauthorized_actions = [
        action for action in requested_actions
        if action not in context.context.authorized_external_actions
    ]
    blocked = secret_detected or bool(unauthorized_actions)
    return GuardrailFunctionOutput(
        output_info={
            "secret_detected": secret_detected,
            "unauthorized_external_actions": unauthorized_actions,
        },
        tripwire_triggered=blocked,
    )


@output_guardrail(name="marketing_output_guardrail")
async def marketing_output_guardrail(
    context: RunContextWrapper[MarketingContext],
    agent: Agent[Any],
    output: WorkOutput,
) -> GuardrailFunctionOutput:
    blocked = output.external_action_performed or not output.next_human_decision.strip()
    return GuardrailFunctionOutput(
        output_info={
            "external_action_performed": output.external_action_performed,
            "next_human_decision_present": bool(output.next_human_decision.strip()),
        },
        tripwire_triggered=blocked,
    )
