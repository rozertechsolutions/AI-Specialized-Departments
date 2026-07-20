from __future__ import annotations

from pathlib import Path

from .models import (
    ApprovalDecisionValue,
    EvidenceItem,
    FinalState,
    LeadFinalRecord,
    ProposedToolAction,
    RoleSlug,
    ToolActionType,
)

SENSITIVE_ACTION_TYPES = frozenset({
    ToolActionType.WRITE,
    ToolActionType.DELETE,
    ToolActionType.DEPENDENCY,
    ToolActionType.GIT,
    ToolActionType.DEPLOY,
    ToolActionType.PUBLISH,
    ToolActionType.RELEASE,
    ToolActionType.SIGN,
    ToolActionType.EXTERNAL_COMMUNICATION,
    ToolActionType.PERMISSION,
    ToolActionType.CREDENTIAL,
})

PROHIBITED_ACTION_TYPES = frozenset({
    ToolActionType.DELETE,
    ToolActionType.GIT,
    ToolActionType.DEPLOY,
    ToolActionType.PUBLISH,
    ToolActionType.RELEASE,
    ToolActionType.SIGN,
    ToolActionType.EXTERNAL_COMMUNICATION,
    ToolActionType.CREDENTIAL,
})


def action_requires_human_approval(action: ProposedToolAction) -> bool:
    return action.action_type in SENSITIVE_ACTION_TYPES


def concrete_action_is_prohibited(action: ProposedToolAction) -> bool:
    return action.action_type in PROHIBITED_ACTION_TYPES


def keyword_mentions_are_allowed(text: str) -> bool:
    return bool(text.strip())


def normalize_relative_path(workspace_root: Path, candidate: str) -> Path:
    root = workspace_root.expanduser().resolve(strict=False)
    requested = Path(candidate)
    if not candidate.strip():
        raise ValueError("path must not be empty")
    if requested.is_absolute():
        raise ValueError("absolute paths are outside the injected workspace scope")
    if any(part in {"", ".", ".."} for part in requested.parts):
        raise ValueError("path traversal or ambiguous path components are not allowed")
    resolved = (root / requested).resolve(strict=False)
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError("path escapes the injected workspace scope") from exc
    return resolved


def validate_scope(
    requested_paths: tuple[str, ...],
    authorized_paths: tuple[str, ...],
    workspace_root: Path | str = ".",
) -> bool:
    root = Path(workspace_root)
    try:
        authorized = tuple(normalize_relative_path(root, path) for path in authorized_paths)
        requested = tuple(normalize_relative_path(root, path) for path in requested_paths)
    except ValueError:
        return False
    for path in requested:
        if not any(path == allowed or allowed in path.parents for allowed in authorized):
            return False
    return True


def can_claim_observed(evidence: EvidenceItem) -> bool:
    return evidence.observed and bool(evidence.source.strip())


def derive_final_state(record: LeadFinalRecord) -> FinalState:
    if record.final_state in {FinalState.PAUSED, FinalState.BLOCKED, FinalState.STOPPED}:
        return record.final_state
    if record.unmet_requirements:
        return FinalState.BLOCKED
    if record.implementation_evidence and not record.has_independent_review():
        return FinalState.BLOCKED
    if record.code_quality_review_result and not record.code_quality_review_result.review.approved:
        return FinalState.BLOCKED
    if record.engineering_risk_review_result and not record.engineering_risk_review_result.review.approved:
        return FinalState.BLOCKED
    if record.remaining_risks:
        return FinalState.BLOCKED
    return FinalState.COMPLETED


def final_record_is_supported(record: LeadFinalRecord, context: object | None = None) -> bool:
    evidence_groups = (
        record.implementation_evidence.evidence if record.implementation_evidence else (),
        record.validation_evidence.evidence if record.validation_evidence else (),
        record.code_quality_review_result.evidence if record.code_quality_review_result else (),
        record.engineering_risk_review_result.evidence if record.engineering_risk_review_result else (),
        record.documentation_release_readiness_result.evidence
        if record.documentation_release_readiness_result
        else (),
    )
    evidence = tuple(item for group in evidence_groups for item in group)
    if not record.objective.strip():
        return False
    if record.final_state is not derive_final_state(record):
        return False
    if record.final_state is FinalState.COMPLETED and not record.documentation_release_readiness_result:
        return False
    if record.documentation_release_readiness_result and not record.documentation_release_readiness_result.readiness.stop_before_release:
        return False
    if not record.has_independent_review():
        return False
    if record.implementation_evidence and record.validation_evidence is None:
        return False
    if record.implementation_evidence and record.code_quality_review_result is None:
        return False
    if record.implementation_evidence and record.engineering_risk_review_result is None:
        return False
    if context is not None:
        observed = getattr(context, "specialist_outputs", {})
        for role in record.required_specialist_roles:
            if role not in observed or not observed[role]:
                return False
        if tuple(getattr(context, "specialist_completion_order", ())) != record.specialist_completion_order:
            return False
        linked = {
            RoleSlug.REQUIREMENTS: record.requirements_result,
            RoleSlug.ARCHITECTURE: record.architecture_result,
            RoleSlug.IMPLEMENTATION: record.implementation_evidence,
            RoleSlug.TESTING: record.validation_evidence,
            RoleSlug.CODE_REVIEW: record.code_quality_review_result,
            RoleSlug.RISK_REVIEW: record.engineering_risk_review_result,
            RoleSlug.DOCUMENTATION: record.documentation_release_readiness_result,
        }
        for role, output in linked.items():
            if output is not None and (role not in observed or output not in observed[role]):
                return False
        if record.implementation_evidence and record.implementation_evidence.proposal:
            claimed = set(record.implementation_evidence.proposal.changed_paths)
            actual = {path for path, _content in getattr(context, "write_events", ())}
            if not claimed or not claimed <= actual:
                return False
    elif record.final_state is FinalState.COMPLETED:
        return False
    return all(can_claim_observed(item) or item.limitation for item in evidence)


def approval_result_allows_action(decision: ApprovalDecisionValue) -> bool:
    return decision is ApprovalDecisionValue.APPROVED
