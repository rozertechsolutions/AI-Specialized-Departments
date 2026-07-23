from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from mobile_development_agents.context import ActionRisk


class PermissionDecision(str, Enum):
    ALLOW = "allow"
    REQUIRE_APPROVAL = "require-approval"
    DENY = "deny"


@dataclass(frozen=True, slots=True)
class PermissionRule:
    risk: ActionRisk
    decision: PermissionDecision
    reason: str


PERMISSION_RULES: dict[ActionRisk, PermissionRule] = {
    ActionRisk.ROUTINE_READ: PermissionRule(ActionRisk.ROUTINE_READ, PermissionDecision.ALLOW, "Routine reads are allowed."),
    ActionRisk.PROJECT_EDIT: PermissionRule(ActionRisk.PROJECT_EDIT, PermissionDecision.REQUIRE_APPROVAL, "Project edits require scoped authorization."),
    ActionRisk.SECURITY_SENSITIVE: PermissionRule(ActionRisk.SECURITY_SENSITIVE, PermissionDecision.REQUIRE_APPROVAL, "Security-sensitive changes require human control."),
    ActionRisk.RELEASE_SENSITIVE: PermissionRule(ActionRisk.RELEASE_SENSITIVE, PermissionDecision.REQUIRE_APPROVAL, "Release-sensitive work must be manually initiated."),
    ActionRisk.EXTERNAL_WRITE: PermissionRule(ActionRisk.EXTERNAL_WRITE, PermissionDecision.DENY, "External writes are not enabled by default."),
    ActionRisk.DESTRUCTIVE: PermissionRule(ActionRisk.DESTRUCTIVE, PermissionDecision.DENY, "Destructive actions are outside this package."),
}


def decision_for_risk(risk: ActionRisk) -> PermissionRule:
    return PERMISSION_RULES[risk]
