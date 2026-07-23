"""Typed contracts for the OpenAI Agents SDK Web Development department."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, is_dataclass
from enum import Enum
from typing import Any, Literal


POLICY_VERSION = "web-development-policy-v2"


class WebDepartmentError(ValueError):
    """Predictable validation failure that does not expose sensitive values."""


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


class ActionIntent(str, Enum):
    ANALYZE = "ANALYZE"
    DOCUMENT = "DOCUMENT"
    PROPOSE = "PROPOSE"
    EXECUTE = "EXECUTE"
    NEGATED = "NEGATED"
    CONTENT_REFERENCE = "CONTENT_REFERENCE"
    AMBIGUOUS = "AMBIGUOUS"


class ScopeCategory(str, Enum):
    WEB_FRONTEND = "WEB_FRONTEND"
    WEB_BACKEND_API = "WEB_BACKEND_API"
    WEB_ARCHITECTURE = "WEB_ARCHITECTURE"
    WEB_SECURITY_PRIVACY = "WEB_SECURITY_PRIVACY"
    WEB_ACCESSIBILITY_PERFORMANCE_SEO = "WEB_ACCESSIBILITY_PERFORMANCE_SEO"
    WEB_TESTING_RELEASE = "WEB_TESTING_RELEASE"
    NATIVE_MOBILE = "NATIVE_MOBILE"
    DESKTOP = "DESKTOP"
    INFRASTRUCTURE = "INFRASTRUCTURE"
    CLOUD_PROVISIONING = "CLOUD_PROVISIONING"
    MARKETING = "MARKETING"
    DATA_AI = "DATA_AI"
    OTHER = "OTHER"


class ReviewType(str, Enum):
    ARCHITECTURE = "ARCHITECTURE"
    FRONTEND = "FRONTEND"
    BACKEND_API = "BACKEND_API"
    SECURITY_PRIVACY = "SECURITY_PRIVACY"
    ACCESSIBILITY_PERFORMANCE_SEO = "ACCESSIBILITY_PERFORMANCE_SEO"
    TESTING_RELEASE_READINESS = "TESTING_RELEASE_READINESS"
    INDEPENDENT_FINAL_QUALITY = "INDEPENDENT_FINAL_QUALITY"


class EvidenceType(str, Enum):
    AGENT_EXECUTION = "AGENT_EXECUTION"
    SNAPSHOT_LIST = "SNAPSHOT_LIST"
    SNAPSHOT_READ = "SNAPSHOT_READ"
    STATIC_VALIDATION = "STATIC_VALIDATION"
    SPECIALIST_RESULT = "SPECIALIST_RESULT"
    HUMAN_APPROVAL = "HUMAN_APPROVAL"
    TEST_EXECUTION = "TEST_EXECUTION"
    EXTERNAL_EVIDENCE = "EXTERNAL_EVIDENCE"
    NOT_EXECUTED = "NOT_EXECUTED"


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
class ClassifiedAction:
    action_id: str
    text: str
    intent: ActionIntent
    sensitive: bool = False
    prohibited: bool = False
    requires_approval: bool = False
    reason: str = ""


@dataclass(frozen=True)
class ScopeAssessment:
    allowed: list[ScopeCategory]
    rejected: list[ScopeCategory]
    mixed: bool = False
    unresolved: bool = False
    reason: str = ""


@dataclass(frozen=True)
class PreflightResult:
    status: Verdict
    reasons: list[str]
    actions: list[ClassifiedAction]
    scope_assessment: ScopeAssessment
    required_reviews: list[ReviewType]

    @property
    def blocked(self) -> bool:
        return self.status is Verdict.BLOCKED


@dataclass(frozen=True)
class ReviewPlanItem:
    review_id: str
    review_type: ReviewType
    specialist_identity: str
    mandatory: bool = True
    applicable: bool = True
    not_applicable_reason: str | None = None


@dataclass(frozen=True)
class EvidenceRecord:
    evidence_id: str
    producer: str
    evidence_type: EvidenceType
    review_type: ReviewType | None
    source_operation: str
    invocation_id: str | None = None
    tool_call_id: str | None = None
    paths_inspected: list[str] = field(default_factory=list)
    status: Verdict = Verdict.NOT_EXECUTED
    digest: str | None = None
    model_authored: bool = False
    sequence: int = 0


@dataclass(frozen=True)
class EvidenceItem:
    kind: str
    description: str
    source: str
    status: Verdict = Verdict.NOT_EXECUTED
    evidence_id: str | None = None


@dataclass(frozen=True)
class ReviewerFinding:
    severity: FindingSeverity
    title: str
    evidence: list[EvidenceItem]
    impact: str
    remediation: str
    blocking: bool = False


@dataclass(frozen=True)
class SpecialistReviewResult:
    review_type: ReviewType
    status: Verdict
    summary: str
    findings: list[ReviewerFinding] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)
    evidence_claims: list[str] = field(default_factory=list)


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
class SpecialistExecutionRecord:
    review_id: str
    review_type: ReviewType
    specialist_identity: str
    invocation_id: str
    tool_call_id: str | None
    start_sequence: int
    end_sequence: int | None
    status: Verdict
    structured_output: SpecialistReviewResult | None = None
    trusted_findings: list[ReviewerFinding] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    evidence_ids: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ApprovalRequest:
    action_id: str
    tool_name: str
    requested_transition: str
    rationale: str
    affected_paths: list[str]
    risk_level: FindingSeverity
    tool_call_id: str | None = None
    interruption_id: str | None = None


@dataclass(frozen=True)
class ApprovalDecision:
    action_id: str
    decision_id: str
    human_identity: str
    decision: ApprovalDecisionValue
    rationale: str | None = None
    rejection_reason: str | None = None
    reuse_policy: Literal["single_use", "session"] = "single_use"


@dataclass(frozen=True)
class ApprovalLedgerRecord:
    action_id: str
    tool_name: str
    tool_call_id: str | None
    interruption_id: str | None
    requested_transition: str
    affected_paths: list[str]
    risk_level: FindingSeverity
    human_identity: str
    decision_id: str
    decision: ApprovalDecisionValue
    rationale: str | None
    rejection_reason: str | None
    reuse_policy: str
    evidence_id: str
    sequence: int


@dataclass(frozen=True)
class RiskRecord:
    risk_id: str
    severity: FindingSeverity
    description: str
    owner: str
    blocking: bool = False
    accepted_by_human: bool = False
    remediated: bool = False
    evidence_id: str | None = None


@dataclass(frozen=True)
class UnresolvedRisk:
    severity: FindingSeverity
    description: str
    owner: str
    blocking: bool = False


@dataclass(frozen=True)
class RiskAcceptanceDecision:
    risk_id: str
    decision_id: str
    human_identity: str
    rationale: str
    accept: bool


@dataclass(frozen=True)
class SafeRunConfigState:
    tracing_disabled: bool
    trace_include_sensitive_data: bool
    pre_approval_tool_input_guardrails: bool


@dataclass(frozen=True)
class FinalReconciliationState:
    verdict: Verdict
    evidence_ids: list[str]
    omitted_blocking_findings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


@dataclass
class WebDevelopmentRunContext:
    scope: TaskScope
    snapshot: RepositorySnapshot
    policy_version: str
    scope_digest: str
    snapshot_digest: str
    preflight_result: PreflightResult
    authoritative_review_plan: list[ReviewPlanItem]
    specialist_execution_ledger: list[SpecialistExecutionRecord] = field(default_factory=list)
    trusted_evidence_ledger: list[EvidenceRecord] = field(default_factory=list)
    sensitive_action_ledger: list[ApprovalRequest] = field(default_factory=list)
    approval_ledger: list[ApprovalLedgerRecord] = field(default_factory=list)
    risk_ledger: list[RiskRecord] = field(default_factory=list)
    review_ordering_state: list[ReviewType] = field(default_factory=list)
    blocking_conditions: list[str] = field(default_factory=list)
    effective_safe_run_config: SafeRunConfigState | None = None
    final_reconciliation_state: FinalReconciliationState | None = None
    sequence: int = 0


@dataclass(frozen=True)
class FinalVerdict:
    verdict: Verdict
    summary: str
    evidence: list[EvidenceItem]
    findings: list[ReviewerFinding] = field(default_factory=list)
    unresolved_risks: list[RiskRecord] = field(default_factory=list)
    required_human_approvals: list[ApprovalRequest] = field(default_factory=list)


@dataclass(frozen=True)
class WorkflowInput:
    scope_digest: str
    snapshot_digest: str
    policy_version: str
    required_result: str = "Return FinalVerdict only."


RunStatus = Literal["completed", "interrupted"]


def enum_to_value(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if is_dataclass(value):
        return {key: enum_to_value(item) for key, item in asdict(value).items()}
    if isinstance(value, list):
        return [enum_to_value(item) for item in value]
    if isinstance(value, dict):
        return {str(key): enum_to_value(item) for key, item in value.items()}
    return value
