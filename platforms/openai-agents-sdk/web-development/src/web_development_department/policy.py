"""Application-owned policy, preflight, ledgers, and final reconciliation."""

from __future__ import annotations

import base64
import hashlib
import json
import posixpath
import re
import uuid
from dataclasses import replace
from typing import Iterable

from .models import (
    ActionIntent,
    ApprovalDecision,
    ApprovalDecisionValue,
    ApprovalLedgerRecord,
    ApprovalRequest,
    ClassifiedAction,
    EvidenceRecord,
    EvidenceType,
    FinalReconciliationState,
    FinalVerdict,
    FindingSeverity,
    POLICY_VERSION,
    PreflightResult,
    RepositoryFile,
    RepositorySnapshot,
    ReviewPlanItem,
    ReviewType,
    RiskAcceptanceDecision,
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
    enum_to_value,
)


MAX_SNAPSHOT_FILES = 200
MAX_FILE_BYTES = 256_000
MAX_TOTAL_BYTES = 2_000_000
MAX_TOOL_READ_BYTES = 24_000

SENSITIVE_ACTIONS = frozenset(
    {
        "authentication",
        "authorization",
        "secret_access",
        "sensitive_data",
        "database_migration",
        "dependency_change",
        "third_party_script",
        "tracking",
        "production_change",
        "deployment",
        "publication",
        "billing",
        "signing",
        "submission",
        "git_mutation",
        "destructive_action",
    }
)

PROHIBITED_AUTOMATIC_ACTIONS = frozenset(
    {
        "execute_command",
        "install_dependency",
        "git_mutation",
        "deploy",
        "publish",
        "authenticate",
        "expose_secret",
        "spend",
        "sign",
        "submit",
        "destructive_action",
    }
)

SECRET_PATTERNS = (
    re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"\b(?:api[_-]?key|token|secret|password)\s*[:=]\s*['\"]?[^'\"\s,;]{8,}", re.I),
    re.compile(r"https?://[^/\s]+:[^@\s]+@"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)

ACTION_PATTERNS: tuple[tuple[str, str], ...] = (
    ("destructive_action", r"rm\s+-rf|\bdrop\s+database\b|\bdelete\s+everything\b"),
    ("git_mutation", r"\bgit\s+push\b|\bpush\s+main\b|\bmerge\s+(?:pull request|pr|to main)\b"),
    ("install_dependency", r"\b(?:npm|pnpm|yarn|pip|uv|poetry|bundle|composer|go)\s+install\b"),
    ("deploy", r"\bdeploy(?:ment)?\b"),
    ("publish", r"\bpublish(?:ing|ed|es)?\b|\bpublication\b"),
    ("authenticate", r"\blog\s*in\b|\bauthenticate\b|\boauth consent\b"),
    ("spend", r"\bspend\b|\bpurchase\b|\bcharge\b|\bbilling\b"),
    ("sign", r"\bsign\b|\bnotarize\b"),
    ("submit", r"\bsubmit\b"),
)

ACTION_SPLIT_RE = re.compile(r"\b(?:and then|after that|then|and)\b|[.;]")
NEGATION_RE = re.compile(r"\b(?:do not|don't|without|no|not)\b", re.I)
DOCUMENT_RE = re.compile(r"\b(?:document|write|explain|checklist|readme|guide|instructions?)\b", re.I)
ANALYZE_RE = re.compile(r"\b(?:review|analy[sz]e|audit|assess|inspect|evaluate)\b", re.I)
PROPOSE_RE = re.compile(r"\b(?:plan|prepare|proposal|design)\b", re.I)
CONTENT_RE = re.compile(r"\b(?:contains|mentions|says|includes the text)\b", re.I)

WEB_ALLOWED = {
    ScopeCategory.WEB_FRONTEND,
    ScopeCategory.WEB_BACKEND_API,
    ScopeCategory.WEB_ARCHITECTURE,
    ScopeCategory.WEB_SECURITY_PRIVACY,
    ScopeCategory.WEB_ACCESSIBILITY_PERFORMANCE_SEO,
    ScopeCategory.WEB_TESTING_RELEASE,
}


def stable_id(prefix: str, *parts: object) -> str:
    digest = hashlib.sha256(json.dumps(enum_to_value(parts), sort_keys=True).encode()).hexdigest()[:16]
    return f"{prefix}_{digest}"


def contains_secret(text: str) -> bool:
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def normalize_path(path: str) -> str:
    raw = path.strip().replace("\\", "/")
    if not raw:
        raise WebDepartmentError("invalid path: empty")
    if raw.startswith("/") or re.match(r"^[A-Za-z]:/", raw):
        raise WebDepartmentError("invalid path: absolute paths are not allowed")
    normalized = posixpath.normpath(raw)
    if normalized == "." or normalized.startswith("../") or normalized == "..":
        raise WebDepartmentError("invalid path: traversal is not allowed")
    return normalized


def canonical_snapshot(snapshot: RepositorySnapshot) -> RepositorySnapshot:
    if len(snapshot.files) > MAX_SNAPSHOT_FILES:
        raise WebDepartmentError("snapshot too large: too many files")
    seen: set[str] = set()
    files: list[RepositoryFile] = []
    total = 0
    for file in snapshot.files:
        normalized = normalize_path(file.path)
        if normalized in seen:
            raise WebDepartmentError("duplicate normalized snapshot path")
        seen.add(normalized)
        data = file.content.encode("utf-8", "surrogatepass")
        if b"\x00" in data:
            raise WebDepartmentError(f"binary-like snapshot content denied: {normalized}")
        if len(data) > MAX_FILE_BYTES:
            raise WebDepartmentError(f"snapshot file too large: {normalized}")
        total += len(data)
        if total > MAX_TOTAL_BYTES:
            raise WebDepartmentError("snapshot too large: total content limit exceeded")
        if contains_secret(file.content):
            raise WebDepartmentError(f"secret-like snapshot content denied: {normalized}")
        files.append(RepositoryFile(path=normalized, content=file.content, language=file.language))
    return RepositorySnapshot(files=files, root_hint=snapshot.root_hint, observed_commands=list(snapshot.observed_commands))


def canonical_scope(scope: TaskScope) -> TaskScope:
    goal = scope.goal.strip()
    if not goal:
        raise WebDepartmentError("empty task")
    criteria = [item.strip() for item in scope.acceptance_criteria if item and item.strip()]
    if not criteria:
        raise WebDepartmentError("invalid acceptance criteria")
    affected = [normalize_path(path) for path in scope.affected_paths]
    if len(set(affected)) != len(affected):
        raise WebDepartmentError("duplicate normalized affected path")
    return TaskScope(
        goal=goal,
        acceptance_criteria=criteria,
        affected_paths=affected,
        prohibited_changes=list(scope.prohibited_changes),
        requires_human_review=list(scope.requires_human_review),
    )


def digest_value(value: object) -> str:
    payload = json.dumps(enum_to_value(value), sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def _intent_for_clause(clause: str, action_key: str) -> ActionIntent:
    before_action = clause[: max(clause.lower().find(action_key.split("_")[0]), 0) or len(clause)]
    if CONTENT_RE.search(clause):
        return ActionIntent.CONTENT_REFERENCE
    if "without" in clause.lower():
        return ActionIntent.NEGATED
    if NEGATION_RE.search(before_action) or re.search(r"\bdo not\b.{0,80}\b" + re.escape(action_key.split("_")[0]), clause, re.I):
        return ActionIntent.NEGATED
    if ANALYZE_RE.search(clause):
        return ActionIntent.ANALYZE
    if PROPOSE_RE.search(clause):
        return ActionIntent.PROPOSE
    if DOCUMENT_RE.search(clause):
        return ActionIntent.DOCUMENT
    return ActionIntent.EXECUTE


def classify_actions(task_text: str) -> list[ClassifiedAction]:
    actions: list[ClassifiedAction] = []
    for clause_index, clause in enumerate(part.strip() for part in ACTION_SPLIT_RE.split(task_text) if part.strip()):
        for action_key, pattern in ACTION_PATTERNS:
            if re.search(pattern, clause, re.I):
                intent = _intent_for_clause(clause, action_key)
                prohibited = intent is ActionIntent.EXECUTE
                sensitive = action_key in SENSITIVE_ACTIONS or action_key in PROHIBITED_AUTOMATIC_ACTIONS
                actions.append(
                    ClassifiedAction(
                        action_id=stable_id("action", clause_index, action_key, clause),
                        text=clause,
                        intent=intent,
                        sensitive=sensitive,
                        prohibited=prohibited,
                        requires_approval=sensitive and intent in {ActionIntent.ANALYZE, ActionIntent.PROPOSE, ActionIntent.DOCUMENT},
                        reason=action_key,
                    )
                )
    return actions


def assess_scope(scope: TaskScope) -> ScopeAssessment:
    text = " ".join([scope.goal, *scope.acceptance_criteria]).lower()
    allowed: set[ScopeCategory] = set()
    rejected: set[ScopeCategory] = set()
    if re.search(r"\b(frontend|react|vue|svelte|html|css|browser|responsive|form|component)\b", text):
        allowed.add(ScopeCategory.WEB_FRONTEND)
    if re.search(r"\b(api|rest|graphql|websocket|webhook|backend|server|auth|cookie|session)\b", text):
        allowed.add(ScopeCategory.WEB_BACKEND_API)
    if re.search(r"\b(architecture|migration|contract|rollback)\b", text):
        allowed.add(ScopeCategory.WEB_ARCHITECTURE)
    if re.search(r"\b(security|privacy|csrf|cors|csp|xss|authorization|authentication)\b", text):
        allowed.add(ScopeCategory.WEB_SECURITY_PRIVACY)
    if re.search(r"\b(accessibility|wcag|performance|core web vitals|seo|crawl|metadata)\b", text):
        allowed.add(ScopeCategory.WEB_ACCESSIBILITY_PERFORMANCE_SEO)
    if re.search(r"\b(test|release|readiness|browser compatibility|ci)\b", text):
        allowed.add(ScopeCategory.WEB_TESTING_RELEASE)
    if re.search(r"\b(native ios|native android|android app|ios app|mobile app implementation)\b", text):
        rejected.add(ScopeCategory.NATIVE_MOBILE)
    if re.search(r"\b(desktop app|electron desktop|macos app|windows app)\b", text):
        rejected.add(ScopeCategory.DESKTOP)
    if re.search(r"\b(kubernetes|terraform|pulumi|cloud provisioning|vpc|cluster)\b", text):
        rejected.add(ScopeCategory.CLOUD_PROVISIONING)
    if re.search(r"\b(marketing campaign|ad campaign|newsletter send)\b", text):
        rejected.add(ScopeCategory.MARKETING)
    if re.search(r"\b(model training|fine[- ]tune|data pipeline)\b", text):
        rejected.add(ScopeCategory.DATA_AI)
    if "mobile client" in text and ScopeCategory.WEB_BACKEND_API in allowed:
        rejected.discard(ScopeCategory.NATIVE_MOBILE)
    if not allowed and not rejected:
        allowed.add(ScopeCategory.WEB_ARCHITECTURE)
    return ScopeAssessment(
        allowed=sorted(allowed, key=lambda item: item.value),
        rejected=sorted(rejected, key=lambda item: item.value),
        mixed=bool(allowed and rejected),
        unresolved=not allowed,
        reason="mixed web and non-web scope" if allowed and rejected else "",
    )


def build_authoritative_review_plan(assessment: ScopeAssessment) -> list[ReviewPlanItem]:
    mapping = {
        ReviewType.ARCHITECTURE: "Web Architecture Specialist",
        ReviewType.FRONTEND: "Frontend Specialist",
        ReviewType.BACKEND_API: "Backend and API Specialist",
        ReviewType.SECURITY_PRIVACY: "Security and Privacy Reviewer",
        ReviewType.ACCESSIBILITY_PERFORMANCE_SEO: "Accessibility, Performance and SEO Reviewer",
        ReviewType.TESTING_RELEASE_READINESS: "Testing and Release Readiness Reviewer",
        ReviewType.INDEPENDENT_FINAL_QUALITY: "Independent Final Quality Reviewer",
    }
    plan: list[ReviewPlanItem] = []
    for review_type, specialist in mapping.items():
        applicable = True
        reason = None
        if review_type is ReviewType.FRONTEND and ScopeCategory.WEB_FRONTEND not in assessment.allowed:
            applicable, reason = False, "No frontend surface detected."
        if review_type is ReviewType.BACKEND_API and ScopeCategory.WEB_BACKEND_API not in assessment.allowed:
            applicable, reason = False, "No backend/API surface detected."
        plan.append(
            ReviewPlanItem(
                review_id=stable_id("review", review_type.value, specialist),
                review_type=review_type,
                specialist_identity=specialist,
                mandatory=True,
                applicable=applicable,
                not_applicable_reason=reason,
            )
        )
    return plan


def preflight(scope: TaskScope, snapshot: RepositorySnapshot) -> tuple[TaskScope, RepositorySnapshot, PreflightResult]:
    reasons: list[str] = []
    try:
        scope = canonical_scope(scope)
        snapshot = canonical_snapshot(snapshot)
    except WebDepartmentError as exc:
        empty_assessment = ScopeAssessment(allowed=[], rejected=[], unresolved=True, reason=str(exc))
        result = PreflightResult(Verdict.BLOCKED, [str(exc)], [], empty_assessment, [])
        raise WebDepartmentError(str(exc)) from exc
    task_intent_text = " ".join([scope.goal, *scope.acceptance_criteria, *scope.prohibited_changes])
    if contains_secret(task_intent_text):
        reasons.append("secret-like task content denied")
    actions = classify_actions(task_intent_text)
    prohibited = [action.reason for action in actions if action.prohibited]
    if prohibited:
        reasons.append("prohibited execution action requested: " + ", ".join(sorted(set(prohibited))))
    assessment = assess_scope(scope)
    if assessment.unresolved:
        reasons.append("scope unresolved")
    if assessment.rejected and not assessment.allowed:
        reasons.append("out of Web Development scope")
    elif assessment.mixed:
        reasons.append("mixed-scope request must be separated")
    plan = build_authoritative_review_plan(assessment)
    result = PreflightResult(
        Verdict.BLOCKED if reasons else Verdict.PASS,
        reasons,
        actions,
        assessment,
        [item.review_type for item in plan if item.mandatory],
    )
    return scope, snapshot, result


def create_run_context(scope: TaskScope, snapshot: RepositorySnapshot, config_state: SafeRunConfigState) -> WebDevelopmentRunContext:
    scope, snapshot, preflight_result = preflight(scope, snapshot)
    if preflight_result.blocked:
        raise WebDepartmentError("; ".join(preflight_result.reasons))
    plan = build_authoritative_review_plan(preflight_result.scope_assessment)
    context = WebDevelopmentRunContext(
        scope=scope,
        snapshot=snapshot,
        policy_version=POLICY_VERSION,
        scope_digest=digest_value(scope),
        snapshot_digest=digest_value(snapshot),
        preflight_result=preflight_result,
        authoritative_review_plan=plan,
        effective_safe_run_config=config_state,
    )
    for action in preflight_result.actions:
        if action.requires_approval:
            context.sensitive_action_ledger.append(
                ApprovalRequest(
                    action_id=action.action_id,
                    tool_name="request_sensitive_transition",
                    requested_transition="non_executing_sensitive_analysis",
                    rationale=action.text,
                    affected_paths=scope.affected_paths,
                    risk_level=FindingSeverity.HIGH,
                )
            )
    add_evidence(context, "application", EvidenceType.STATIC_VALIDATION, None, "preflight", [], Verdict.PASS, False)
    return context


def bind_context(context: WebDevelopmentRunContext, scope: TaskScope, snapshot: RepositorySnapshot) -> None:
    scope, snapshot, result = preflight(scope, snapshot)
    if result.blocked:
        raise WebDepartmentError("context binding failed: preflight changed")
    if context.policy_version != POLICY_VERSION:
        raise WebDepartmentError("context binding failed: stale policy version")
    if context.scope_digest != digest_value(scope):
        raise WebDepartmentError("context binding failed: scope digest mismatch")
    if context.snapshot_digest != digest_value(snapshot):
        raise WebDepartmentError("context binding failed: snapshot digest mismatch")
    current_plan = build_authoritative_review_plan(result.scope_assessment)
    if [item.review_id for item in context.authoritative_review_plan] != [item.review_id for item in current_plan]:
        raise WebDepartmentError("context binding failed: review plan mismatch")


def next_sequence(context: WebDevelopmentRunContext) -> int:
    context.sequence += 1
    return context.sequence


def _reject_duplicate(ids: Iterable[str], label: str) -> None:
    seen: set[str] = set()
    for item in ids:
        if item in seen:
            raise WebDepartmentError(f"duplicate {label}: {item}")
        seen.add(item)


def add_evidence(
    context: WebDevelopmentRunContext,
    producer: str,
    evidence_type: EvidenceType,
    review_type: ReviewType | None,
    source_operation: str,
    paths_inspected: list[str],
    status: Verdict,
    model_authored: bool,
    invocation_id: str | None = None,
    tool_call_id: str | None = None,
) -> EvidenceRecord:
    evidence = EvidenceRecord(
        evidence_id=stable_id("evidence", producer, evidence_type.value, source_operation, paths_inspected, next_sequence(context)),
        producer=producer,
        evidence_type=evidence_type,
        review_type=review_type,
        source_operation=source_operation,
        invocation_id=invocation_id,
        tool_call_id=tool_call_id,
        paths_inspected=paths_inspected,
        status=status,
        digest=base64.urlsafe_b64encode(digest_value([producer, source_operation, paths_inspected]).encode()[:24]).decode(),
        model_authored=model_authored,
        sequence=context.sequence,
    )
    if evidence.evidence_id in {item.evidence_id for item in context.trusted_evidence_ledger}:
        raise WebDepartmentError("duplicate evidence")
    context.trusted_evidence_ledger.append(evidence)
    return evidence


def record_specialist_execution(
    context: WebDevelopmentRunContext,
    review_type: ReviewType,
    specialist_identity: str,
    result: SpecialistReviewResult,
    *,
    invocation_id: str | None = None,
    tool_call_id: str | None = None,
) -> SpecialistExecutionRecord:
    matches = [item for item in context.authoritative_review_plan if item.review_type is review_type]
    if not matches:
        raise WebDepartmentError("unknown review")
    plan_item = matches[0]
    if not plan_item.applicable:
        raise WebDepartmentError("review is not applicable")
    if specialist_identity != plan_item.specialist_identity:
        raise WebDepartmentError("wrong reviewer")
    if any(item.review_id == plan_item.review_id for item in context.specialist_execution_ledger):
        raise WebDepartmentError("duplicate review")
    if review_type is ReviewType.INDEPENDENT_FINAL_QUALITY:
        prior = [item for item in context.authoritative_review_plan if item.applicable and item.review_type is not ReviewType.INDEPENDENT_FINAL_QUALITY]
        executed = {item.review_type for item in context.specialist_execution_ledger if item.status in {Verdict.PASS, Verdict.FAIL, Verdict.BLOCKED}}
        missing = [item.review_type.value for item in prior if item.review_type not in executed]
        if missing:
            raise WebDepartmentError("premature independent final review: " + ", ".join(missing))
        if "Lead" in specialist_identity:
            raise WebDepartmentError("lead cannot perform independent final review")
    start = next_sequence(context)
    evidence = add_evidence(
        context,
        specialist_identity,
        EvidenceType.SPECIALIST_RESULT,
        review_type,
        "specialist_review",
        [],
        result.status,
        False,
        invocation_id or stable_id("invocation", plan_item.review_id, start),
        tool_call_id,
    )
    end = next_sequence(context)
    record = SpecialistExecutionRecord(
        review_id=plan_item.review_id,
        review_type=review_type,
        specialist_identity=specialist_identity,
        invocation_id=invocation_id or stable_id("invocation", plan_item.review_id, start),
        tool_call_id=tool_call_id,
        start_sequence=start,
        end_sequence=end,
        status=result.status,
        structured_output=result,
        trusted_findings=list(result.findings),
        limitations=list(result.limitations),
        errors=[] if result.status in {Verdict.PASS, Verdict.NOT_APPLICABLE} else [result.summary],
        evidence_ids=[evidence.evidence_id],
    )
    context.specialist_execution_ledger.append(record)
    context.review_ordering_state.append(review_type)
    for finding in result.findings:
        if finding.blocking and finding.severity in {FindingSeverity.CRITICAL, FindingSeverity.HIGH}:
            context.blocking_conditions.append(f"{review_type.value}: {finding.title}")
    return record


def apply_human_approval(context: WebDevelopmentRunContext, decision: ApprovalDecision) -> ApprovalLedgerRecord:
    if not decision.human_identity.strip():
        raise WebDepartmentError("anonymous approval denied")
    if not decision.decision_id.strip():
        raise WebDepartmentError("missing decision ID")
    if decision.decision is ApprovalDecisionValue.REJECT and not (decision.rejection_reason or "").strip():
        raise WebDepartmentError("rejection requires reason")
    if any(item.decision_id == decision.decision_id for item in context.approval_ledger):
        raise WebDepartmentError("duplicate approval decision")
    actions = [item for item in context.sensitive_action_ledger if item.action_id == decision.action_id]
    if not actions:
        raise WebDepartmentError("unknown action")
    action = actions[0]
    evidence = add_evidence(
        context,
        decision.human_identity,
        EvidenceType.HUMAN_APPROVAL,
        None,
        "non_executing_approval_decision",
        action.affected_paths,
        Verdict.PASS if decision.decision is ApprovalDecisionValue.APPROVE else Verdict.FAIL,
        False,
        action.interruption_id,
        action.tool_call_id,
    )
    record = ApprovalLedgerRecord(
        action_id=action.action_id,
        tool_name=action.tool_name,
        tool_call_id=action.tool_call_id,
        interruption_id=action.interruption_id,
        requested_transition=action.requested_transition,
        affected_paths=action.affected_paths,
        risk_level=action.risk_level,
        human_identity=decision.human_identity,
        decision_id=decision.decision_id,
        decision=decision.decision,
        rationale=decision.rationale,
        rejection_reason=decision.rejection_reason,
        reuse_policy=decision.reuse_policy,
        evidence_id=evidence.evidence_id,
        sequence=context.sequence,
    )
    context.approval_ledger.append(record)
    return record


def apply_risk_decision(context: WebDevelopmentRunContext, decision: RiskAcceptanceDecision) -> RiskRecord:
    if not decision.human_identity.strip():
        raise WebDepartmentError("anonymous risk acceptance denied")
    if not decision.rationale.strip():
        raise WebDepartmentError("risk acceptance requires rationale")
    if any(item.evidence_id == decision.decision_id for item in context.trusted_evidence_ledger):
        raise WebDepartmentError("duplicate risk decision")
    risks = [item for item in context.risk_ledger if item.risk_id == decision.risk_id]
    if not risks:
        raise WebDepartmentError("unknown risk")
    risk = risks[0]
    evidence = add_evidence(
        context,
        decision.human_identity,
        EvidenceType.HUMAN_APPROVAL,
        None,
        "risk_acceptance" if decision.accept else "risk_rejection",
        [],
        Verdict.PASS if decision.accept else Verdict.FAIL,
        False,
    )
    updated = replace(risk, accepted_by_human=decision.accept, evidence_id=evidence.evidence_id)
    context.risk_ledger[context.risk_ledger.index(risk)] = updated
    return updated


def validate_final_verdict(context: WebDevelopmentRunContext, verdict: FinalVerdict) -> list[str]:
    errors: list[str] = []
    if context.preflight_result.blocked:
        errors.append("preflight blocked")
    if context.effective_safe_run_config != SafeRunConfigState(True, False, True):
        errors.append("effective tracing is unsafe")
    evidence_ids = [item.evidence_id for item in verdict.evidence if item.evidence_id]
    if verdict.verdict is Verdict.PASS and not evidence_ids:
        errors.append("PASS requires non-empty trusted evidence")
    _reject_duplicate([item.evidence_id for item in context.trusted_evidence_ledger], "trusted evidence")
    trusted_by_id = {item.evidence_id: item for item in context.trusted_evidence_ledger}
    for evidence_id in evidence_ids:
        if evidence_id not in trusted_by_id:
            errors.append(f"unknown evidence ID: {evidence_id}")
        elif trusted_by_id[evidence_id].model_authored:
            errors.append(f"model-authored evidence is not trusted: {evidence_id}")
        elif trusted_by_id[evidence_id].status is Verdict.NOT_EXECUTED:
            errors.append(f"required evidence is NOT_EXECUTED: {evidence_id}")
    for item in context.authoritative_review_plan:
        if not item.mandatory or not item.applicable:
            continue
        records = [record for record in context.specialist_execution_ledger if record.review_id == item.review_id]
        if not records:
            errors.append(f"required review missing: {item.review_type.value}")
            continue
        record = records[0]
        if record.specialist_identity != item.specialist_identity:
            errors.append(f"wrong reviewer: {item.review_type.value}")
        if record.status in {Verdict.FAIL, Verdict.BLOCKED, Verdict.NOT_EXECUTED}:
            errors.append(f"required review not passing: {item.review_type.value}")
        if not record.evidence_ids:
            errors.append(f"required review lacks trusted evidence: {item.review_type.value}")
        for evidence_id in record.evidence_ids:
            if evidence_id not in trusted_by_id:
                errors.append(f"review evidence missing from ledger: {evidence_id}")
    final_records = [record for record in context.specialist_execution_ledger if record.review_type is ReviewType.INDEPENDENT_FINAL_QUALITY]
    if verdict.verdict is Verdict.PASS and not final_records:
        errors.append("independent final review missing")
    elif final_records and context.specialist_execution_ledger[-1].review_type is not ReviewType.INDEPENDENT_FINAL_QUALITY:
        errors.append("independent final review was not last")
    if context.blocking_conditions:
        errors.append("blocking findings remain: " + "; ".join(context.blocking_conditions))
        model_titles = {finding.title for finding in verdict.findings}
        omitted = [condition for condition in context.blocking_conditions if condition.split(": ", 1)[-1] not in model_titles]
        if omitted:
            errors.append("model omitted trusted blocking finding")
    for action in context.sensitive_action_ledger:
        approvals = [item for item in context.approval_ledger if item.action_id == action.action_id]
        if not approvals:
            errors.append(f"required approval missing: {action.action_id}")
        elif approvals[-1].decision is ApprovalDecisionValue.REJECT:
            errors.append(f"approval rejected: {action.action_id}")
        elif not approvals[-1].human_identity:
            errors.append(f"approval lacks human identity: {action.action_id}")
    for risk in context.risk_ledger:
        if risk.blocking and not risk.remediated and not risk.accepted_by_human:
            errors.append(f"blocking risk unresolved: {risk.risk_id}")
        if risk.accepted_by_human and not risk.evidence_id:
            errors.append(f"risk acceptance lacks trusted evidence: {risk.risk_id}")
    if verdict.verdict is Verdict.PASS and any(item.status is Verdict.NOT_EXECUTED for item in verdict.evidence):
        errors.append("PASS cannot rely on NOT_EXECUTED evidence")
    context.final_reconciliation_state = FinalReconciliationState(verdict.verdict, evidence_ids, errors=errors)
    return errors


def final_verdict_is_valid(verdict: FinalVerdict, context: WebDevelopmentRunContext | None = None) -> list[str]:
    if context is None:
        if verdict.verdict is Verdict.PASS and not verdict.evidence:
            return ["PASS is invalid without evidence"]
        return []
    return validate_final_verdict(context, verdict)
