from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Protocol


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


class FinalState(str, Enum):
    COMPLETED = "COMPLETED"
    PAUSED = "PAUSED"
    STOPPED = "STOPPED"
    BLOCKED = "BLOCKED"


class ApprovalDecisionValue(str, Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
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
class TaskScope:
    authorized_paths: tuple[str, ...]
    exclusions: tuple[str, ...] = ()
    prohibited_actions: tuple[ToolActionType, ...] = (
        ToolActionType.GIT,
        ToolActionType.DEPLOY,
        ToolActionType.PUBLISH,
        ToolActionType.RELEASE,
        ToolActionType.SIGN,
        ToolActionType.EXTERNAL_COMMUNICATION,
        ToolActionType.CREDENTIAL,
    )


@dataclass(frozen=True)
class TaskRequest:
    objective: str
    scope: TaskScope
    acceptance_criteria: tuple[str, ...]
    risk_level: RiskLevel = RiskLevel.MEDIUM


@dataclass(frozen=True)
class DepartmentTask:
    objective: str
    authorized_scope: tuple[str, ...]
    acceptance_criteria: tuple[str, ...]
    exclusions: tuple[str, ...] = ()
    risk_level: RiskLevel = RiskLevel.MEDIUM
    workspace_root: Path | None = None

    def to_request(self) -> TaskRequest:
        return TaskRequest(
            objective=self.objective,
            scope=TaskScope(self.authorized_scope, self.exclusions),
            acceptance_criteria=self.acceptance_criteria,
            risk_level=self.risk_level,
        )


@dataclass(frozen=True)
class SpecialistInput:
    task: TaskRequest
    requested_focus: str
    available_evidence: tuple[str, ...] = ()
    approved_paths: tuple[str, ...] = ()


@dataclass(frozen=True)
class EvidenceItem:
    claim: str
    source: str
    observed: bool
    limitation: str | None = None


@dataclass(frozen=True)
class RequirementsAcceptanceCriteria:
    requirements: tuple[str, ...]
    acceptance_criteria: tuple[str, ...]
    unresolved_questions: tuple[str, ...] = ()


@dataclass(frozen=True)
class ImplementationPlan:
    steps: tuple[str, ...]
    validation_steps: tuple[str, ...]
    required_specialists: tuple[RoleSlug, ...]
    approval_checkpoints: tuple[str, ...] = ()


@dataclass(frozen=True)
class ArchitectureDecision:
    decisions: tuple[str, ...]
    contracts: tuple[str, ...]
    migration_implications: tuple[str, ...]
    compatibility_notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class ImplementationChangeProposal:
    changed_paths: tuple[str, ...]
    change_summary: str
    approved_scope_reference: str
    validation_notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class ValidationEvidence:
    role: RoleSlug
    summary: str
    evidence: tuple[EvidenceItem, ...]
    passed_checks: tuple[str, ...] = ()
    failed_checks: tuple[str, ...] = ()
    untested_areas: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = ()
    limitations: tuple[str, ...] = ()
    checks_not_run: tuple[str, ...] = ()


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
    requirements_result: RequirementsAcceptanceCriteria = field(
        default_factory=lambda: RequirementsAcceptanceCriteria((), ())
    )
    plan: ImplementationPlan = field(default_factory=lambda: ImplementationPlan((), (), ()))


@dataclass(frozen=True)
class ArchitectureOutput(SpecialistResult):
    architecture: ArchitectureDecision = field(default_factory=lambda: ArchitectureDecision((), (), ()))


@dataclass(frozen=True)
class ImplementationEvidence(SpecialistResult):
    proposal: ImplementationChangeProposal | None = None


@dataclass(frozen=True)
class CodeQualityReview:
    approved: bool
    findings: tuple[str, ...] = ()
    blocking_findings: tuple[str, ...] = ()


@dataclass(frozen=True)
class CodeReviewOutput(SpecialistResult):
    review: CodeQualityReview = field(default_factory=lambda: CodeQualityReview(False))


@dataclass(frozen=True)
class EngineeringRiskReview:
    approved: bool
    risks: tuple[str, ...] = ()
    required_mitigations: tuple[str, ...] = ()


@dataclass(frozen=True)
class RiskReviewOutput(SpecialistResult):
    review: EngineeringRiskReview = field(default_factory=lambda: EngineeringRiskReview(False))


@dataclass(frozen=True)
class DocumentationReleaseReadinessResult:
    documentation_updates: tuple[str, ...]
    release_readiness: str
    stop_before_release: bool = True


@dataclass(frozen=True)
<<<<<<< HEAD
class DocumentationReadinessOutput(SpecialistResult):
    readiness: DocumentationReleaseReadinessResult = field(
        default_factory=lambda: DocumentationReleaseReadinessResult((), "not_assessed", True)
    )


@dataclass(frozen=True)
class ApprovalDecisionRecord:
=======
class HumanDecision:
>>>>>>> feature/software-development
    subject: str
    decision: ApprovalDecisionValue
    evidence: str


@dataclass(frozen=True)
class InterruptionState:
    pending_count: int
    pending_subjects: tuple[str, ...]
    resume_available: bool


@dataclass(frozen=True)
class ProposedToolAction:
    action_type: ToolActionType
    target: str
    reason: str
    role: RoleSlug | None = None


@dataclass(frozen=True)
class ToolApprovalResult:
    action: ProposedToolAction
    decision: ApprovalDecisionValue
    message: str


@dataclass(frozen=True)
class ReadToolResult:
    path: str
    content: str
    observed: bool = True


@dataclass(frozen=True)
class WriteToolResult:
    path: str
    applied: bool
    message: str


@dataclass(frozen=True)
class ApprovalDecision:
    approved: bool
    reason: str


@dataclass(frozen=True)
class LeadFinalRecord:
    objective: str
    requirements_result: RequirementsOutput | None
    implementation_plan: ImplementationPlan | None
    architecture_result: ArchitectureOutput | None
    required_specialist_roles: tuple[RoleSlug, ...]
    specialist_completion_order: tuple[RoleSlug, ...]
    completed_requirements: tuple[str, ...]
    unmet_requirements: tuple[str, ...]
    implementation_evidence: ImplementationEvidence | None
    validation_evidence: ValidationEvidence | None
    code_quality_review_result: CodeReviewOutput | None
    engineering_risk_review_result: RiskReviewOutput | None
    documentation_release_readiness_result: DocumentationReadinessOutput | None
    approvals_and_rejections: tuple[ApprovalDecisionRecord, ...]
    remaining_risks: tuple[str, ...]
    limitations: tuple[str, ...]
    checks_not_executed: tuple[str, ...]
    final_state: FinalState

    def has_independent_review(self) -> bool:
        if self.implementation_evidence is None:
            return True
        return (
            self.code_quality_review_result is not None
            and self.code_quality_review_result.role is RoleSlug.CODE_REVIEW
            and self.engineering_risk_review_result is not None
            and self.engineering_risk_review_result.role is RoleSlug.RISK_REVIEW
        )


class RepositoryReader(Protocol):
    async def read_text(self, path: str) -> str: ...


class RepositoryWriter(Protocol):
    async def write_text(self, path: str, content: str) -> None: ...


class HumanApprovalProvider(Protocol):
    async def pending_decisions(self, interruptions: tuple[Any, ...]) -> tuple[ApprovalDecision, ...]: ...
