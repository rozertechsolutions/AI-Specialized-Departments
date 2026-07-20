"""SDK-backed source package for the Software Development department."""

from .models import (
    ApprovalDecision,
    ApprovalDecisionRecord,
    DepartmentTask,
    EvidenceItem,
    FinalState,
    LeadFinalRecord,
    ProposedToolAction,
    RiskLevel,
    TaskRequest,
    TaskScope,
    ToolActionType,
)
from .orchestrator import DepartmentRuntime
from .tools import RunLimits


def build_department_agents(context):
    """Import SDK-backed agent construction only when the host provides context."""
    from .agents import build_department_agents as _build_department_agents

    return _build_department_agents(context)


__all__ = [
    "ApprovalDecision",
    "ApprovalDecisionRecord",
    "build_department_agents",
    "DepartmentTask",
    "DepartmentRuntime",
    "EvidenceItem",
    "FinalState",
    "LeadFinalRecord",
    "ProposedToolAction",
    "RiskLevel",
    "RunLimits",
    "TaskRequest",
    "TaskScope",
    "ToolActionType",
]
