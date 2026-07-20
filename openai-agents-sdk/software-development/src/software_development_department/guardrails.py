from __future__ import annotations

from agents import GuardrailFunctionOutput, RunContextWrapper, input_guardrail, output_guardrail

from .models import LeadFinalRecord, ProposedToolAction
from .policies import action_requires_human_approval, final_record_is_supported, keyword_mentions_are_allowed


@input_guardrail
async def legitimate_task_guardrail(
    context: RunContextWrapper[object], agent: object, input_data: str | list[object]
) -> GuardrailFunctionOutput:
    text = input_data if isinstance(input_data, str) else repr(input_data)
    return GuardrailFunctionOutput(
        output_info={"safe_analysis_allowed": keyword_mentions_are_allowed(text)},
        tripwire_triggered=not keyword_mentions_are_allowed(text),
    )


def proposed_action_guardrail(action: ProposedToolAction) -> GuardrailFunctionOutput:
    needs_approval = action_requires_human_approval(action)
    return GuardrailFunctionOutput(
        output_info={"requires_human_approval": needs_approval, "action_type": action.action_type.value},
        tripwire_triggered=False,
    )


@output_guardrail
async def evidence_and_self_review_guardrail(
    context: RunContextWrapper[object], agent: object, output_data: object
) -> GuardrailFunctionOutput:
    supported = isinstance(output_data, LeadFinalRecord) and final_record_is_supported(output_data, context.context)
    return GuardrailFunctionOutput(
        output_info={"typed_final_record": isinstance(output_data, LeadFinalRecord), "evidence_supported": supported},
        tripwire_triggered=not supported,
    )
