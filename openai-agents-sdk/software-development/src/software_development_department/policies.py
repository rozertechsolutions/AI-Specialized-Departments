from __future__ import annotations

from pathlib import Path

from .models import ApprovalDecision, EvidenceItem, LeadFinalRecord, ProposedToolAction, ToolActionType

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


def action_requires_human_approval(action: ProposedToolAction) -> bool:
    return action.action_type in SENSITIVE_ACTION_TYPES


def keyword_mentions_are_allowed(text: str) -> bool:
    return bool(text.strip())


def normalize_relative_path(workspace_root: Path, candidate: str) -> Path:
    root = workspace_root.expanduser().resolve(strict=False)
    requested = Path(candidate)
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


def validate_scope(requested_paths: tuple[str, ...], authorized_paths: tuple[str, ...], workspace_root: Path | str = ".") -> bool:
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


def final_record_is_supported(record: LeadFinalRecord) -> bool:
    evidence_groups = (
        record.requirements.evidence if record.requirements else (),
        record.implementation_evidence.evidence if record.implementation_evidence else (),
        record.validation_evidence.evidence if record.validation_evidence else (),
        record.code_review.evidence if record.code_review else (),
        record.risk_review.evidence if record.risk_review else (),
        record.documentation_release_readiness.evidence if record.documentation_release_readiness else (),
    )
    evidence = tuple(item for group in evidence_groups for item in group)
    if not record.objective.strip():
        return False
    if not record.has_independent_review():
        return False
    if record.implementation_evidence and record.validation_evidence is None:
        return False
    return all(can_claim_observed(item) or item.limitation for item in evidence)


def approval_result_allows_action(decision: ApprovalDecision) -> bool:
    return decision is ApprovalDecision.APPROVED
