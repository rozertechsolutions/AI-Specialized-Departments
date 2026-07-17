from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Callable, Mapping

from mobile_development_agents.context import SDKWorkflowContext, serialize_sdk_context


@dataclass(frozen=True, slots=True)
class PendingApproval:
    id: str
    name: str
    reason: str
    arguments: str | None = None
    item: Any = field(repr=False, compare=False, default=None)


def _approval_item_id(item: Any, index: int) -> str:
    for attribute in ("id", "call_id", "tool_call_id"):
        value = getattr(item, attribute, None)
        if isinstance(value, str) and value.strip():
            return value
    name = getattr(item, "name", getattr(item, "tool_name", "approval"))
    return f"{name}:{index}"


def _approval_item_name(item: Any) -> str:
    agent = getattr(item, "agent", None)
    agent_name = getattr(agent, "name", None)
    tool_name = getattr(item, "tool_name", getattr(item, "name", None))
    if agent_name and tool_name:
        return f"{agent_name}.{tool_name}"
    return str(tool_name or "approval")


def pending_approval_interruptions(result_or_state: Any) -> tuple[PendingApproval, ...]:
    interruptions = getattr(result_or_state, "interruptions", None)
    if interruptions is None and hasattr(result_or_state, "get_interruptions"):
        interruptions = result_or_state.get_interruptions()
    pending: list[PendingApproval] = []
    for index, item in enumerate(interruptions or ()):
        pending.append(
            PendingApproval(
                id=_approval_item_id(item, index),
                name=_approval_item_name(item),
                reason=str(getattr(item, "reason", "Human approval required.")),
                arguments=_safe_arguments(item),
                item=item,
            )
        )
    return tuple(pending)


def _safe_arguments(item: Any) -> str | None:
    arguments = getattr(item, "arguments", None)
    if arguments is None:
        return None
    text = str(arguments)
    if len(text) > 1000:
        return text[:1000] + "...[truncated]"
    return text


def _resolve_pending_item(state: Any, interruption_id: str) -> Any:
    if not isinstance(interruption_id, str) or not interruption_id.strip():
        raise ValueError("approval identifier is required")
    if not hasattr(state, "get_interruptions"):
        raise TypeError("state does not expose get_interruptions()")
    pending = pending_approval_interruptions(state)
    if not pending:
        raise ValueError("no pending approval interruptions remain")

    ids: dict[str, int] = {}
    for item in pending:
        ids[item.id] = ids.get(item.id, 0) + 1
    duplicated = sorted(identifier for identifier, count in ids.items() if count > 1)
    if duplicated:
        raise ValueError(f"duplicate pending approval identifiers: {', '.join(duplicated)}")

    matches = [item for item in pending if item.id == interruption_id]
    if not matches:
        raise ValueError(f"unknown or resolved approval identifier: {interruption_id}")
    return matches[0].item


def _record_decision(
    context: SDKWorkflowContext | None,
    item: Any,
    decision: str,
    reason: str | None = None,
) -> None:
    if context is None:
        return
    name = _approval_item_name(item)
    entry = f"{decision}:{name}"
    if reason:
        entry = f"{entry}:{reason[:200]}"
    context.approval_audit.append(entry)


def serialize_run_state(result_or_state: Any) -> str:
    state = result_or_state.to_state() if hasattr(result_or_state, "to_state") else result_or_state
    if hasattr(state, "to_string"):
        return state.to_string(
            context_serializer=serialize_sdk_context,
            strict_context=True,
            include_tracing_api_key=False,
        )
    if hasattr(state, "to_json"):
        return json.dumps(
            state.to_json(
                context_serializer=serialize_sdk_context,
                strict_context=True,
                include_tracing_api_key=False,
            ),
            indent=2,
        )
    raise TypeError("Run state does not expose an SDK serialization method.")


def approve_pending_item(
    state: Any,
    interruption_id: str,
    *,
    always_approve: bool = False,
    workflow_context: SDKWorkflowContext | None = None,
) -> Any:
    item = _resolve_pending_item(state, interruption_id)
    result = state.approve(item, always_approve=always_approve)
    _record_decision(workflow_context, item, "approved")
    return result


def reject_pending_item(
    state: Any,
    interruption_id: str,
    reason: str,
    *,
    always_reject: bool = False,
    workflow_context: SDKWorkflowContext | None = None,
) -> Any:
    item = _resolve_pending_item(state, interruption_id)
    result = state.reject(item, always_reject=always_reject, rejection_message=reason)
    _record_decision(workflow_context, item, "rejected", reason)
    return result


async def load_run_state_from_string(
    initial_agent: Any,
    state_string: str,
    *,
    tool_host: object | None = None,
) -> Any:
    try:
        from agents import RunState
    except ImportError as exc:
        raise RuntimeError("Install openai-agents to deserialize SDK run state.") from exc

    return await RunState.from_string(
        initial_agent,
        state_string,
        context_deserializer=_context_deserializer(tool_host),
        strict_context=True,
    )


async def load_run_state_from_json(
    initial_agent: Any,
    state_json: Mapping[str, Any],
    *,
    tool_host: object | None = None,
) -> Any:
    try:
        from agents import RunState
    except ImportError as exc:
        raise RuntimeError("Install openai-agents to deserialize SDK run state.") from exc

    return await RunState.from_json(
        initial_agent,
        dict(state_json),
        context_deserializer=_context_deserializer(tool_host),
        strict_context=True,
    )


def _context_deserializer(tool_host: object | None) -> Callable[[object], SDKWorkflowContext]:
    def deserialize(data: object) -> SDKWorkflowContext:
        if not isinstance(data, Mapping):
            raise TypeError("Serialized SDK workflow context must be an object")
        return SDKWorkflowContext.from_json_dict(data, tool_host=tool_host)

    return deserialize


async def resume_approved_run(
    coordinator: Any,
    state: Any,
    *,
    run_config: Any | None = None,
    max_turns: int = 12,
) -> Any:
    try:
        from agents import Runner
    except ImportError as exc:
        raise RuntimeError("Install openai-agents to resume SDK runs.") from exc

    kwargs: dict[str, Any] = {"max_turns": max_turns}
    if run_config is not None:
        kwargs["run_config"] = run_config
    return await Runner.run(coordinator, state, **kwargs)
