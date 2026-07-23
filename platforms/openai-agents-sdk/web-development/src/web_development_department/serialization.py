"""JSON-safe context serialization for strict RunState persistence."""

from __future__ import annotations

from typing import Any, TypeVar

from .models import (
    ActionIntent,
    ApprovalDecisionValue,
    ApprovalLedgerRecord,
    ApprovalRequest,
    ClassifiedAction,
    EvidenceRecord,
    EvidenceType,
    FindingSeverity,
    FinalReconciliationState,
    POLICY_VERSION,
    PreflightResult,
    RepositoryFile,
    RepositorySnapshot,
    ReviewPlanItem,
    ReviewType,
    RiskRecord,
    SafeRunConfigState,
    ScopeAssessment,
    ScopeCategory,
    SpecialistExecutionRecord,
    SpecialistReviewResult,
    TaskScope,
    Verdict,
    WebDepartmentError,
    WebDevelopmentRunContext,
    ReviewerFinding,
    EvidenceItem,
)
from .policy import bind_context

TEnum = TypeVar("TEnum")


def _enum(enum_type: type[TEnum], value: str) -> TEnum:
    return enum_type(value)  # type: ignore[call-arg]


def _evidence_item(data: dict[str, Any]) -> EvidenceItem:
    return EvidenceItem(
        kind=str(data["kind"]),
        description=str(data["description"]),
        source=str(data["source"]),
        status=_enum(Verdict, data.get("status", Verdict.NOT_EXECUTED.value)),
        evidence_id=data.get("evidence_id"),
    )


def _finding(data: dict[str, Any]) -> ReviewerFinding:
    return ReviewerFinding(
        severity=_enum(FindingSeverity, data["severity"]),
        title=str(data["title"]),
        evidence=[_evidence_item(item) for item in data.get("evidence", [])],
        impact=str(data["impact"]),
        remediation=str(data["remediation"]),
        blocking=bool(data.get("blocking", False)),
    )


def _specialist_result(data: dict[str, Any] | None) -> SpecialistReviewResult | None:
    if data is None:
        return None
    return SpecialistReviewResult(
        review_type=_enum(ReviewType, data["review_type"]),
        status=_enum(Verdict, data["status"]),
        summary=str(data["summary"]),
        findings=[_finding(item) for item in data.get("findings", [])],
        limitations=[str(item) for item in data.get("limitations", [])],
        recommendations=[str(item) for item in data.get("recommendations", [])],
        evidence_claims=[str(item) for item in data.get("evidence_claims", [])],
    )


def _reject_duplicates(values: list[str], label: str) -> None:
    if len(values) != len(set(values)):
        raise WebDepartmentError(f"malformed state: duplicate {label}")


def context_from_json(data: dict[str, Any]) -> WebDevelopmentRunContext:
    if data.get("policy_version") != POLICY_VERSION:
        raise WebDepartmentError("malformed state: stale policy version")
    scope_data = data["scope"]
    snapshot_data = data["snapshot"]
    scope = TaskScope(
        goal=str(scope_data["goal"]),
        acceptance_criteria=[str(item) for item in scope_data.get("acceptance_criteria", [])],
        affected_paths=[str(item) for item in scope_data.get("affected_paths", [])],
        prohibited_changes=[str(item) for item in scope_data.get("prohibited_changes", [])],
        requires_human_review=[str(item) for item in scope_data.get("requires_human_review", [])],
    )
    snapshot = RepositorySnapshot(
        files=[
            RepositoryFile(path=str(item["path"]), content=str(item["content"]), language=item.get("language"))
            for item in snapshot_data.get("files", [])
        ],
        root_hint=snapshot_data.get("root_hint"),
        observed_commands=[str(item) for item in snapshot_data.get("observed_commands", [])],
    )
    preflight_data = data["preflight_result"]
    assessment_data = preflight_data["scope_assessment"]
    preflight = PreflightResult(
        status=_enum(Verdict, preflight_data["status"]),
        reasons=[str(item) for item in preflight_data.get("reasons", [])],
        actions=[
            ClassifiedAction(
                action_id=str(item["action_id"]),
                text=str(item["text"]),
                intent=_enum(ActionIntent, item["intent"]),
                sensitive=bool(item.get("sensitive", False)),
                prohibited=bool(item.get("prohibited", False)),
                requires_approval=bool(item.get("requires_approval", False)),
                reason=str(item.get("reason", "")),
            )
            for item in preflight_data.get("actions", [])
        ],
        scope_assessment=ScopeAssessment(
            allowed=[_enum(ScopeCategory, item) for item in assessment_data.get("allowed", [])],
            rejected=[_enum(ScopeCategory, item) for item in assessment_data.get("rejected", [])],
            mixed=bool(assessment_data.get("mixed", False)),
            unresolved=bool(assessment_data.get("unresolved", False)),
            reason=str(assessment_data.get("reason", "")),
        ),
        required_reviews=[_enum(ReviewType, item) for item in preflight_data.get("required_reviews", [])],
    )
    context = WebDevelopmentRunContext(
        scope=scope,
        snapshot=snapshot,
        policy_version=str(data["policy_version"]),
        scope_digest=str(data["scope_digest"]),
        snapshot_digest=str(data["snapshot_digest"]),
        preflight_result=preflight,
        authoritative_review_plan=[
            ReviewPlanItem(
                review_id=str(item["review_id"]),
                review_type=_enum(ReviewType, item["review_type"]),
                specialist_identity=str(item["specialist_identity"]),
                mandatory=bool(item.get("mandatory", True)),
                applicable=bool(item.get("applicable", True)),
                not_applicable_reason=item.get("not_applicable_reason"),
            )
            for item in data.get("authoritative_review_plan", [])
        ],
        specialist_execution_ledger=[
            SpecialistExecutionRecord(
                review_id=str(item["review_id"]),
                review_type=_enum(ReviewType, item["review_type"]),
                specialist_identity=str(item["specialist_identity"]),
                invocation_id=str(item["invocation_id"]),
                tool_call_id=item.get("tool_call_id"),
                start_sequence=int(item["start_sequence"]),
                end_sequence=item.get("end_sequence"),
                status=_enum(Verdict, item["status"]),
                structured_output=_specialist_result(item.get("structured_output")),
                trusted_findings=[_finding(finding) for finding in item.get("trusted_findings", [])],
                limitations=[str(value) for value in item.get("limitations", [])],
                errors=[str(value) for value in item.get("errors", [])],
                evidence_ids=[str(value) for value in item.get("evidence_ids", [])],
            )
            for item in data.get("specialist_execution_ledger", [])
        ],
        trusted_evidence_ledger=[
            EvidenceRecord(
                evidence_id=str(item["evidence_id"]),
                producer=str(item["producer"]),
                evidence_type=_enum(EvidenceType, item["evidence_type"]),
                review_type=_enum(ReviewType, item["review_type"]) if item.get("review_type") else None,
                source_operation=str(item["source_operation"]),
                invocation_id=item.get("invocation_id"),
                tool_call_id=item.get("tool_call_id"),
                paths_inspected=[str(value) for value in item.get("paths_inspected", [])],
                status=_enum(Verdict, item["status"]),
                digest=item.get("digest"),
                model_authored=bool(item.get("model_authored", False)),
                sequence=int(item.get("sequence", 0)),
            )
            for item in data.get("trusted_evidence_ledger", [])
        ],
        sensitive_action_ledger=[
            ApprovalRequest(
                action_id=str(item["action_id"]),
                tool_name=str(item["tool_name"]),
                requested_transition=str(item["requested_transition"]),
                rationale=str(item["rationale"]),
                affected_paths=[str(value) for value in item.get("affected_paths", [])],
                risk_level=_enum(FindingSeverity, item["risk_level"]),
                tool_call_id=item.get("tool_call_id"),
                interruption_id=item.get("interruption_id"),
            )
            for item in data.get("sensitive_action_ledger", [])
        ],
        approval_ledger=[
            ApprovalLedgerRecord(
                action_id=str(item["action_id"]),
                tool_name=str(item["tool_name"]),
                tool_call_id=item.get("tool_call_id"),
                interruption_id=item.get("interruption_id"),
                requested_transition=str(item["requested_transition"]),
                affected_paths=[str(value) for value in item.get("affected_paths", [])],
                risk_level=_enum(FindingSeverity, item["risk_level"]),
                human_identity=str(item["human_identity"]),
                decision_id=str(item["decision_id"]),
                decision=_enum(ApprovalDecisionValue, item["decision"]),
                rationale=item.get("rationale"),
                rejection_reason=item.get("rejection_reason"),
                reuse_policy=str(item["reuse_policy"]),
                evidence_id=str(item["evidence_id"]),
                sequence=int(item.get("sequence", 0)),
            )
            for item in data.get("approval_ledger", [])
        ],
        risk_ledger=[
            RiskRecord(
                risk_id=str(item["risk_id"]),
                severity=_enum(FindingSeverity, item["severity"]),
                description=str(item["description"]),
                owner=str(item["owner"]),
                blocking=bool(item.get("blocking", False)),
                accepted_by_human=bool(item.get("accepted_by_human", False)),
                remediated=bool(item.get("remediated", False)),
                evidence_id=item.get("evidence_id"),
            )
            for item in data.get("risk_ledger", [])
        ],
        review_ordering_state=[_enum(ReviewType, item) for item in data.get("review_ordering_state", [])],
        blocking_conditions=[str(item) for item in data.get("blocking_conditions", [])],
        effective_safe_run_config=SafeRunConfigState(
            tracing_disabled=bool(data["effective_safe_run_config"]["tracing_disabled"]),
            trace_include_sensitive_data=bool(data["effective_safe_run_config"]["trace_include_sensitive_data"]),
            pre_approval_tool_input_guardrails=bool(
                data["effective_safe_run_config"]["pre_approval_tool_input_guardrails"]
            ),
        )
        if data.get("effective_safe_run_config")
        else None,
        final_reconciliation_state=FinalReconciliationState(
            verdict=_enum(Verdict, data["final_reconciliation_state"]["verdict"]),
            evidence_ids=[str(item) for item in data["final_reconciliation_state"].get("evidence_ids", [])],
            omitted_blocking_findings=[
                str(item) for item in data["final_reconciliation_state"].get("omitted_blocking_findings", [])
            ],
            errors=[str(item) for item in data["final_reconciliation_state"].get("errors", [])],
        )
        if data.get("final_reconciliation_state")
        else None,
        sequence=int(data.get("sequence", 0)),
    )
    _reject_duplicates([item.review_id for item in context.authoritative_review_plan], "review ID")
    _reject_duplicates([item.evidence_id for item in context.trusted_evidence_ledger], "evidence ID")
    _reject_duplicates([item.action_id for item in context.sensitive_action_ledger], "action ID")
    _reject_duplicates([item.decision_id for item in context.approval_ledger], "approval decision ID")
    bind_context(context, context.scope, context.snapshot)
    return context
