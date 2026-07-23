from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from mobile_development_agents.context import ActionRisk
from mobile_development_agents.policies.permissions import PermissionDecision, decision_for_risk


@dataclass(frozen=True, slots=True)
class ApprovalRequest:
    action: str
    risk: ActionRisk
    reason: str


@dataclass(frozen=True, slots=True)
class ApprovalResult:
    approved: bool
    reason: str


class ApprovalProvider(Protocol):
    def request_approval(self, request: ApprovalRequest) -> ApprovalResult:
        """Return a host-controlled approval decision."""


class DenyByDefaultApprovalProvider:
    def request_approval(self, request: ApprovalRequest) -> ApprovalResult:
        rule = decision_for_risk(request.risk)
        if rule.decision is PermissionDecision.ALLOW:
            return ApprovalResult(True, rule.reason)
        return ApprovalResult(False, f"{rule.decision.value}: {rule.reason}")


def require_approval(provider: ApprovalProvider, request: ApprovalRequest) -> None:
    result = provider.request_approval(request)
    if not result.approved:
        raise PermissionError(result.reason)
