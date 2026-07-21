"""Static reference package for the Software Development department."""

from .models import (
    DepartmentTask,
    EvidenceItem,
    LeadFinalRecord,
    ProposedToolAction,
    RiskLevel,
    ToolActionType,
)


def build_department_agents():
    """Import SDK-backed agent construction only when the host requests it."""
    from .agents import build_department_agents as _build_department_agents

    return _build_department_agents()


__all__ = [
    "build_department_agents",
    "DepartmentTask",
    "EvidenceItem",
    "LeadFinalRecord",
    "ProposedToolAction",
    "RiskLevel",
    "ToolActionType",
]
