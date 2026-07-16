from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class PendingApproval:
    id: str
    name: str
    reason: str


def pending_approval_interruptions(result: Any) -> tuple[PendingApproval, ...]:
    interruptions = getattr(result, "interruptions", ()) or ()
    pending: list[PendingApproval] = []
    for item in interruptions:
        pending.append(
            PendingApproval(
                id=str(getattr(item, "id", getattr(item, "call_id", ""))),
                name=str(getattr(item, "name", getattr(item, "tool_name", "approval"))),
                reason=str(getattr(item, "reason", "Host approval required.")),
            )
        )
    return tuple(pending)


def serialize_run_state(result: Any) -> str:
    state = result.to_state()
    if hasattr(state, "to_string"):
        return str(state.to_string())
    if hasattr(state, "to_json"):
        return str(state.to_json())
    raise TypeError("Run state does not expose an SDK serialization method.")


def approve_pending_item(state: Any, interruption_id: str, reason: str) -> Any:
    return state.approve(interruption_id, {"reason": reason})


def reject_pending_item(state: Any, interruption_id: str, reason: str) -> Any:
    return state.reject(interruption_id, {"reason": reason})


async def resume_approved_run(agent: Any, state: Any, *, max_turns: int = 12) -> Any:
    try:
        from agents import Runner
    except ImportError as exc:
        raise RuntimeError("Install openai-agents to resume SDK runs.") from exc

    return await Runner.run(agent, state, max_turns=max_turns)
