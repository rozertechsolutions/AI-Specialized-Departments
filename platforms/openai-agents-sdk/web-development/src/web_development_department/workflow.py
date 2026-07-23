"""Workflow entry points for preflighted, approval-aware SDK runs."""

from __future__ import annotations

import json
from typing import Any

from agents import RunConfig, RunState, Runner, ToolExecutionConfig

from .department import web_development_lead
from .models import (
    ApprovalDecision,
    POLICY_VERSION,
    RepositorySnapshot,
    RunStatus,
    SafeRunConfigState,
    TaskScope,
    WebDepartmentError,
    WebDevelopmentRunContext,
    WorkflowInput,
    enum_to_value,
)
from .policy import apply_human_approval, bind_context, create_run_context, digest_value, preflight


SAFE_RUN_CONFIG = RunConfig(
    tracing_disabled=True,
    trace_include_sensitive_data=False,
    tool_execution=ToolExecutionConfig(pre_approval_tool_input_guardrails=True),
)


def safe_run_config_state(run_config: RunConfig) -> SafeRunConfigState:
    tool_execution = run_config.tool_execution
    return SafeRunConfigState(
        tracing_disabled=bool(run_config.tracing_disabled),
        trace_include_sensitive_data=bool(run_config.trace_include_sensitive_data),
        pre_approval_tool_input_guardrails=bool(
            getattr(tool_execution, "pre_approval_tool_input_guardrails", False)
        ),
    )


def normalize_run_config(run_config: RunConfig | None = None) -> RunConfig:
    """Return a safe config; unsafe caller tracing settings cannot reach Runner."""
    if run_config is None:
        return SAFE_RUN_CONFIG
    return RunConfig(
        model=run_config.model,
        model_provider=run_config.model_provider,
        model_settings=run_config.model_settings,
        handoff_input_filter=run_config.handoff_input_filter,
        nest_handoff_history=run_config.nest_handoff_history,
        handoff_history_mapper=run_config.handoff_history_mapper,
        input_guardrails=run_config.input_guardrails,
        output_guardrails=run_config.output_guardrails,
        tracing_disabled=True,
        tracing=run_config.tracing,
        trace_include_sensitive_data=False,
        workflow_name=run_config.workflow_name,
        trace_id=run_config.trace_id,
        group_id=run_config.group_id,
        trace_metadata=run_config.trace_metadata,
        session_input_callback=run_config.session_input_callback,
        call_model_input_filter=run_config.call_model_input_filter,
        tool_error_formatter=run_config.tool_error_formatter,
        session_settings=run_config.session_settings,
        reasoning_item_id_policy=run_config.reasoning_item_id_policy,
        sandbox=run_config.sandbox,
        tool_execution=ToolExecutionConfig(pre_approval_tool_input_guardrails=True),
        tool_not_found_behavior=run_config.tool_not_found_behavior,
    )


def build_trusted_context(
    scope: TaskScope,
    snapshot: RepositorySnapshot,
    *,
    run_config: RunConfig | None = None,
) -> WebDevelopmentRunContext:
    effective = normalize_run_config(run_config)
    context = create_run_context(scope, snapshot, safe_run_config_state(effective))
    bind_context(context, context.scope, context.snapshot)
    return context


def build_workflow_input(scope: TaskScope, snapshot: RepositorySnapshot) -> str:
    scope, snapshot, result = preflight(scope, snapshot)
    if result.blocked:
        raise WebDepartmentError("; ".join(result.reasons))
    payload = WorkflowInput(
        scope_digest=digest_value(scope),
        snapshot_digest=digest_value(snapshot),
        policy_version=POLICY_VERSION,
    )
    return json.dumps(enum_to_value(payload), sort_keys=True)


async def run_web_development_request(
    scope: TaskScope,
    snapshot: RepositorySnapshot,
    *,
    run_config: RunConfig | None = None,
):
    """Run the manager workflow only after deterministic application preflight passes."""
    effective = normalize_run_config(run_config)
    context = create_run_context(scope, snapshot, safe_run_config_state(effective))
    prompt = build_workflow_input(context.scope, context.snapshot)
    bind_context(context, context.scope, context.snapshot)
    return await Runner.run(web_development_lead, prompt, context=context, run_config=effective)


def classify_run_result(result: Any) -> RunStatus:
    return "interrupted" if getattr(result, "interruptions", None) else "completed"


def serialize_context(context: WebDevelopmentRunContext) -> dict[str, Any]:
    if context.policy_version != POLICY_VERSION:
        raise WebDepartmentError("stale context policy version")
    return enum_to_value(context)


def deserialize_context(data: dict[str, Any]) -> WebDevelopmentRunContext:
    from .serialization import context_from_json

    context = context_from_json(data)
    bind_context(context, context.scope, context.snapshot)
    return context


def serialize_interrupted_run(result: Any) -> dict[str, Any]:
    if not getattr(result, "interruptions", None):
        raise ValueError("result has no approval interruptions to serialize")
    return result.to_state().to_json(context_serializer=serialize_context, strict_context=True)


def state_from_json(serialized_state: dict[str, Any]):
    return RunState.from_json(
        initial_agent=web_development_lead,
        state_json=serialized_state,
        context_deserializer=deserialize_context,
        strict_context=True,
    )


def apply_approval_decisions(
    serialized_state: dict[str, Any],
    decisions: list[ApprovalDecision],
):
    state = state_from_json(serialized_state)
    context = state.context
    if not isinstance(context, WebDevelopmentRunContext):
        raise WebDepartmentError("trusted context missing from RunState")
    interruptions = list(state.get_interruptions())
    interruption_by_action = {}
    for interruption in interruptions:
        raw = getattr(interruption, "raw_item", None) or getattr(interruption, "item", None) or interruption
        tool_call_id = getattr(raw, "call_id", None) or getattr(raw, "id", None)
        name = getattr(raw, "name", None)
        for action in context.sensitive_action_ledger:
            if action.tool_name == name or action.tool_call_id == tool_call_id or action.interruption_id == getattr(interruption, "id", None):
                interruption_by_action[action.action_id] = interruption
    for decision in decisions:
        apply_human_approval(context, decision)
        interruption = interruption_by_action.get(decision.action_id)
        if interruption is None and interruptions:
            raise WebDepartmentError("approval decision references an unknown interruption")
        if interruption is not None:
            if decision.decision.value == "approve":
                state.approve(interruption, always_approve=decision.reuse_policy == "session")
            else:
                state.reject(
                    interruption,
                    always_reject=decision.reuse_policy == "session",
                    rejection_message=decision.rejection_reason or "Rejected by required human review.",
                )
    return state


async def resume_web_development_request(
    serialized_state: dict[str, Any],
    decisions: list[ApprovalDecision],
    *,
    run_config: RunConfig | None = None,
):
    state = apply_approval_decisions(serialized_state, decisions)
    return await Runner.run(web_development_lead, state, run_config=normalize_run_config(run_config))
