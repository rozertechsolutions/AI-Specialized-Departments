from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class RoleSlug(str, Enum):
    REQUIREMENTS = "requirements-and-planning-specialist"
    ARCHITECTURE = "software-architect"
    IMPLEMENTATION = "implementation-and-maintenance-engineer"
    TESTING = "test-and-quality-engineer"
    CODE_REVIEW = "code-quality-reviewer"
    RISK_REVIEW = "engineering-risk-reviewer"
    DOCUMENTATION = "documentation-and-release-readiness-specialist"


class OrchestrationState(str, Enum):
    READY = "ready"
    RUNNING = "running"
    PAUSED_FOR_HUMAN_APPROVAL = "paused_for_human_approval"
    STOPPED = "stopped"
    COMPLETED = "completed"


class ApprovalDecision(str, Enum):
    APPROVED = "approved"
    DENIED = "denied"
    PENDING = "pending"


class ToolActionType(str, Enum):
    READ = "read"
    SEARCH = "search"
    WRITE = "write"
    DELETE = "delete"
    DEPENDENCY = "dependency"
    GIT = "git"
    DEPLOY = "deploy"
    PUBLISH = "publish"
    RELEASE = "release"
    SIGN = "sign"
    EXTERNAL_COMMUNICATION = "external_communication"
    PERMISSION = "permission"
    CREDENTIAL = "credential"


@dataclass(frozen=True)
class DepartmentTask:
    objective: str
    authorized_scope: tuple[str, ...]
    acceptance_criteria: tuple[str, ...]
    exclusions: tuple[str, ...] = ()
    risk_level: RiskLevel = RiskLevel.MEDIUM
    workspace_root: Path | None = None


@dataclass(frozen=True)
class EvidenceItem:
    claim: str
    source: str
    observed: bool
    limitation: str | None = None


@dataclass(frozen=True)
class SpecialistResult:
    role: RoleSlug
    summary: str
    evidence: tuple[EvidenceItem, ...]
    assumptions: tuple[str, ...] = ()
    limitations: tuple[str, ...] = ()
    checks_not_run: tuple[str, ...] = ()


@dataclass(frozen=True)
class RequirementsOutput(SpecialistResult):
    requirements: tuple[str, ...] = ()
    acceptance_criteria: tuple[str, ...] = ()
    plan: tuple[str, ...] = ()


@dataclass(frozen=True)
class ArchitectureOutput(SpecialistResult):
    decisions: tuple[str, ...] = ()
    contracts: tuple[str, ...] = ()
    migration_notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class ImplementationEvidence(SpecialistResult):
    changed_paths: tuple[str, ...] = ()
    validation_notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class ValidationEvidence(SpecialistResult):
    passed_checks: tuple[str, ...] = ()
    failed_checks: tuple[str, ...] = ()
    untested_areas: tuple[str, ...] = ()


@dataclass(frozen=True)
class CodeReviewOutput(SpecialistResult):
    approved: bool = False
    findings: tuple[str, ...] = ()
    blocking_findings: tuple[str, ...] = ()


@dataclass(frozen=True)
class RiskReviewOutput(SpecialistResult):
    approved: bool = False
    risks: tuple[str, ...] = ()
    required_mitigations: tuple[str, ...] = ()


@dataclass(frozen=True)
class DocumentationReadinessOutput(SpecialistResult):
    documentation_updates: tuple[str, ...] = ()
    release_readiness: str = "not_assessed"
    stop_before_release: bool = True



@dataclass(frozen=True)
class ReviewResult:
    reviewer: str
    approved: bool
    findings: tuple[str, ...] = ()
    blocking_findings: tuple[str, ...] = ()

@dataclass(frozen=True)
class HumanDecision:
    subject: str
    decision: ApprovalDecision
    evidence: str


@dataclass(frozen=True)
class ProposedToolAction:
    action_type: ToolActionType
    target: str
    reason: str
    role: RoleSlug | None = None


@dataclass(frozen=True)
class ToolApprovalResult:
    action: ProposedToolAction
    decision: ApprovalDecision
    message: str


@dataclass(frozen=True)
class LeadFinalRecord:
    objective: str
    requirements: RequirementsOutput | None
    plan: tuple[str, ...]
    implementation_evidence: ImplementationEvidence | None
    validation_evidence: ValidationEvidence | None
    code_review: CodeReviewOutput | None
    risk_review: RiskReviewOutput | None
    documentation_release_readiness: DocumentationReadinessOutput | None
    limitations: tuple[str, ...]
    human_decisions: tuple[HumanDecision, ...]
    stop_state: OrchestrationState = OrchestrationState.STOPPED
    checks_not_run: tuple[str, ...] = field(default_factory=tuple)

    def has_independent_review(self) -> bool:
        if self.implementation_evidence is None:
            return True
        return self.code_review is not None and self.code_review.role is RoleSlug.CODE_REVIEW
