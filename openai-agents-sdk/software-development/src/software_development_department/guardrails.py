from __future__ import annotations

from agents import GuardrailFunctionOutput, RunContextWrapper, input_guardrail, output_guardrail

from .policies import requires_human_approval


@input_guardrail
async def sensitive_action_guardrail(
    context: RunContextWrapper[object], agent: object, input_data: str | list[object]
) -> GuardrailFunctionOutput:
    text = input_data if isinstance(input_data, str) else repr(input_data)
    triggered = requires_human_approval(text)
    return GuardrailFunctionOutput(
        output_info={"requires_human_approval": triggered},
        tripwire_triggered=triggered,
    )


@output_guardrail
async def unsupported_completion_claim_guardrail(
    context: RunContextWrapper[object], agent: object, output_data: object
) -> GuardrailFunctionOutput:
    text = repr(output_data).casefold()
    suspicious = any(phrase in text for phrase in (
        "tests passed" , "build succeeded", "deployed successfully", "released successfully"
    )) and "evidence" not in text
    return GuardrailFunctionOutput(
        output_info={"unsupported_completion_claim": suspicious},
        tripwire_triggered=suspicious,
    )
