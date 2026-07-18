"""Structured contracts for the OpenAI Agents SDK web department."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Literal


class Verdict(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    BLOCKED = "BLOCKED"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NOT_EXECUTED = "NOT_EXECUTED"


class FindingSeverity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class ApprovalDecisionValue(str, Enum):
    APPROVE = "approve"
    REJECT = "reject"


@dataclass(frozen=True)
class RepositoryFile:
    path: str
    content: str
    language: str | None = None


@dataclass(frozen=True)
class RepositorySnapshot:
    files: list[RepositoryFile]
    root_hint: str | None = None
    observed_commands: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class TaskScope:
    goal: str
    acceptance_criteria: list[str]
    affected_paths: list[str] = field(default_factory=list)
    prohibited_changes: list[str] = field(default_factory=list)
    requires_human_review: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class EvidenceItem:
    kind: str
    description: str
    source: str
    status: Verdict = Verdict.NOT_EXECUTED


@dataclass(frozen=True)
class ArchitectureDecision:
    decision: str
    alternatives: list[str]
    rationale: str
    risks: list[str]
    rollback: str
    evidence: list[EvidenceItem] = field(default_factory=list)


@dataclass(frozen=True)
class ImplementationProposal:
    summary: str
    affected_files: list[str]
    behavior: str
    validation_plan: list[str]
    requires_approval: list[str] = field(default_factory=list)
    evidence: list[EvidenceItem] = field(default_factory=list)


@dataclass(frozen=True)
class ReviewerFinding:
    severity: FindingSeverity
    title: str
    evidence: list[EvidenceItem]
    impact: str
    remediation: str
    blocking: bool = False


@dataclass(frozen=True)
class ApprovalRequest:
    action: str
    rationale: str
    affected_paths: list[str]
    risk_level: FindingSeverity


@dataclass(frozen=True)
class ApprovalDecision:
    interruption_index: int
    decision: ApprovalDecisionValue
    rejection_message: str | None = None
    remember: bool = False


@dataclass(frozen=True)
class UnresolvedRisk:
    severity: FindingSeverity
    description: str
    owner: str
    blocking: bool = False


@dataclass(frozen=True)
class FinalVerdict:
    verdict: Verdict
    summary: str
    evidence: list[EvidenceItem]
    findings: list[ReviewerFinding] = field(default_factory=list)
    unresolved_risks: list[UnresolvedRisk] = field(default_factory=list)
    required_human_approvals: list[ApprovalRequest] = field(default_factory=list)


@dataclass(frozen=True)
class WorkflowInput:
    scope: TaskScope
    snapshot: RepositorySnapshot

    def to_prompt_payload(self) -> dict[str, Any]:
        return {
            "scope": self.scope,
            "snapshot": self.snapshot,
            "required_result": "Return FinalVerdict only.",
        }


RunStatus = Literal["completed", "interrupted"]
