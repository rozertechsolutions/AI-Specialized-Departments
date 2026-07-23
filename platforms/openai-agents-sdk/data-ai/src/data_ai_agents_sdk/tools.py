from __future__ import annotations

from agents import function_tool

from .models import ApprovalRequest
from .policies import requires_human_approval


async def sensitive_tool_needs_approval(_context: object, params: dict[str, object], _call_id: str) -> bool:
    return requires_human_approval(" ".join(str(value) for value in params.values()))


@function_tool(needs_approval=sensitive_tool_needs_approval)
async def request_human_data_ai_approval(
    action: str,
    reason: str,
    risk_owner: str,
    evidence_reference: str,
) -> ApprovalRequest:
    """Create a human approval request without performing the sensitive action."""
    return ApprovalRequest(
        action=action,
        reason=reason,
        risk_owner=risk_owner,
        evidence_reference=evidence_reference,
    )
