from __future__ import annotations

from agents import GuardrailFunctionOutput, RunContextWrapper, input_guardrail, output_guardrail

from .policies import appears_to_contain_secret, claims_unsupported_completion, requires_human_approval


def _input_to_text(input_data: str | list[object]) -> str:
    return input_data if isinstance(input_data, str) else repr(input_data)


@input_guardrail
async def data_ai_input_guardrail(
    context: RunContextWrapper[object], agent: object, input_data: str | list[object]
) -> GuardrailFunctionOutput:
    text = _input_to_text(input_data)
    triggered = appears_to_contain_secret(text) or requires_human_approval(text)
    return GuardrailFunctionOutput(
        output_info={
            "secret_like_input": appears_to_contain_secret(text),
            "requires_human_approval": requires_human_approval(text),
        },
        tripwire_triggered=triggered,
    )


@output_guardrail
async def data_ai_output_guardrail(
    context: RunContextWrapper[object], agent: object, output_data: object
) -> GuardrailFunctionOutput:
    text = repr(output_data)
    triggered = appears_to_contain_secret(text) or claims_unsupported_completion(text)
    return GuardrailFunctionOutput(
        output_info={
            "secret_like_output": appears_to_contain_secret(text),
            "unsupported_completion_claim": claims_unsupported_completion(text),
        },
        tripwire_triggered=triggered,
    )
