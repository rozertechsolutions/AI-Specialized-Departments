"""Workflow entry points for normal, interrupted, approval, and resumed runs."""

from __future__ import annotations

import json
from dataclasses import asdict
from typing import Any

from agents import RunConfig, RunState, Runner, ToolExecutionConfig

from .department import web_development_lead
from .models import ApprovalDecision, ApprovalDecisionValue, RepositorySnapshot, RunStatus, TaskScope, WorkflowInput

SAFE_RUN_CONFIG = RunConfig(
    tool_execution=ToolExecutionConfig(pre_approval_tool_input_guardrails=True),
)


def build_workflow_input(scope: TaskScope, snapshot: RepositorySnapshot) -> str:
    payload = asdict(WorkflowInput(scope=scope, snapshot=snapshot))
    payload["required_result"] = "Return FinalVerdict only."
    return json.dumps(payload, sort_keys=True)


async def run_web_development_request(
    scope: TaskScope,
    snapshot: RepositorySnapshot,
    *,
    context: Any | None = None,
):
    """Run the manager workflow. This makes model calls only when a caller explicitly invokes it."""
    prompt = build_workflow_input(scope, snapshot)
    return await Runner.run(
        web_development_lead,
        prompt,
        context=context,
        run_config=SAFE_RUN_CONFIG,
    )


def classify_run_result(result: Any) -> RunStatus:
    return "interrupted" if getattr(result, "interruptions", None) else "completed"


def serialize_interrupted_run(result: Any) -> dict[str, Any]:
    if not getattr(result, "interruptions", None):
        raise ValueError("result has no approval interruptions to serialize")
    return result.to_state().to_json(strict_context=True)


async def apply_approval_decisions(
    serialized_state: dict[str, Any],
    decisions: list[ApprovalDecision],
    *,
    context_override: dict[str, Any] | None = None,
):
    state = await RunState.from_json(
        initial_agent=web_development_lead,
        state_json=serialized_state,
        context_override=context_override,
        strict_context=True,
    )
    interruptions = list(state.get_interruptions())
    for decision in decisions:
        if decision.interruption_index < 0 or decision.interruption_index >= len(interruptions):
            raise IndexError("approval decision references a missing interruption")
        interruption = interruptions[decision.interruption_index]
        if decision.decision is ApprovalDecisionValue.APPROVE:
            state.approve(interruption, always_approve=decision.remember)
        else:
            state.reject(
                interruption,
                always_reject=decision.remember,
                rejection_message=decision.rejection_message or "Rejected by required human review.",
            )
    return state


async def resume_web_development_request(
    serialized_state: dict[str, Any],
    decisions: list[ApprovalDecision],
    *,
    context_override: dict[str, Any] | None = None,
):
    state = await apply_approval_decisions(
        serialized_state,
        decisions,
        context_override=context_override,
    )
    return await Runner.run(web_development_lead, state, run_config=SAFE_RUN_CONFIG)
