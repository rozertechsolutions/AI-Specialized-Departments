from __future__ import annotations

from dataclasses import replace

import pytest
from agents import RunConfig

from web_development_department.department import SPECIALIST_AGENTS, web_development_lead
from web_development_department.guardrails import final_pass_is_allowed
from web_development_department.models import (
    ActionIntent,
    ApprovalDecision,
    ApprovalDecisionValue,
    EvidenceItem,
    EvidenceRecord,
    EvidenceType,
    FinalVerdict,
    FindingSeverity,
    RepositoryFile,
    RepositorySnapshot,
    ReviewerFinding,
    ReviewType,
    RiskAcceptanceDecision,
    RiskRecord,
    SpecialistReviewResult,
    TaskScope,
    Verdict,
    WebDepartmentError,
)
from web_development_department.policy import (
    MAX_FILE_BYTES,
    MAX_SNAPSHOT_FILES,
    MAX_TOTAL_BYTES,
    add_evidence,
    apply_human_approval,
    apply_risk_decision,
    bind_context,
    canonical_snapshot,
    classify_actions,
    create_run_context,
    preflight,
    record_specialist_execution,
    stable_id,
    validate_final_verdict,
)
from web_development_department.serialization import context_from_json
from web_development_department.workflow import (
    SAFE_RUN_CONFIG,
    build_trusted_context,
    build_workflow_input,
    normalize_run_config,
    safe_run_config_state,
    serialize_context,
)


def scope(text: str = "Review a React form and web API authentication flow") -> TaskScope:
    return TaskScope(goal=text, acceptance_criteria=["Find web risks and release evidence"], affected_paths=["src/app.tsx"])


def snapshot(files: list[RepositoryFile] | None = None) -> RepositorySnapshot:
    return RepositorySnapshot(files=files or [RepositoryFile("src/app.tsx", "export const ok = true", "tsx")])


def context():
    return build_trusted_context(scope(), snapshot())


def passing_result(review_type: ReviewType) -> SpecialistReviewResult:
    return SpecialistReviewResult(review_type=review_type, status=Verdict.PASS, summary=f"{review_type.value} reviewed")


def run_all_required_reviews(ctx):
    for item in ctx.authoritative_review_plan:
        if item.applicable and item.review_type is not ReviewType.INDEPENDENT_FINAL_QUALITY:
            record_specialist_execution(ctx, item.review_type, item.specialist_identity, passing_result(item.review_type))
    final_item = [item for item in ctx.authoritative_review_plan if item.review_type is ReviewType.INDEPENDENT_FINAL_QUALITY][0]
    record_specialist_execution(ctx, final_item.review_type, final_item.specialist_identity, passing_result(final_item.review_type))


def final_verdict(ctx, evidence_ids: list[str] | None = None, status: Verdict = Verdict.PASS) -> FinalVerdict:
    ids = [item.evidence_id for item in ctx.trusted_evidence_ledger] if evidence_ids is None else evidence_ids
    return FinalVerdict(
        verdict=status,
        summary="Ready based on trusted evidence.",
        evidence=[EvidenceItem("trusted", evidence_id, "ledger", Verdict.PASS, evidence_id) for evidence_id in ids],
    )


def test_all_agents_construct_and_use_manager_tools_not_handoffs() -> None:
    assert web_development_lead.handoffs == []
    names = {getattr(tool, "name", "") for tool in web_development_lead.tools}
    assert "analyze_web_architecture" in names
    assert "review_security_privacy" in names
    assert "review_independent_final_quality" in names
    assert len(SPECIALIST_AGENTS) == 7


def test_specialists_construct_and_reviewers_are_read_only() -> None:
    for agent in SPECIALIST_AGENTS:
        assert agent.output_type is SpecialistReviewResult
        names = {getattr(tool, "name", "") for tool in agent.tools}
        assert "list_snapshot_files" in names
        assert "read_snapshot_file" in names
    for agent in SPECIALIST_AGENTS[3:]:
        names = {getattr(tool, "name", "") for tool in agent.tools}
        assert "draft_scoped_proposal" not in names
        assert "request_sensitive_transition" not in names


def test_guardrails_and_safe_run_config_are_attached() -> None:
    assert web_development_lead.input_guardrails
    assert web_development_lead.output_guardrails
    state = safe_run_config_state(SAFE_RUN_CONFIG)
    assert state.tracing_disabled is True
    assert state.trace_include_sensitive_data is False
    assert state.pre_approval_tool_input_guardrails is True


def test_unsafe_run_config_override_is_normalized() -> None:
    unsafe = RunConfig(tracing_disabled=False, trace_include_sensitive_data=True)
    normalized = normalize_run_config(unsafe)
    assert normalized.tracing_disabled is True
    assert normalized.trace_include_sensitive_data is False
    assert safe_run_config_state(normalized).pre_approval_tool_input_guardrails is True


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Review deployment readiness without deploying.", ActionIntent.NEGATED),
        ("Document npm install instructions but do not run them.", ActionIntent.DOCUMENT),
        ("Prepare a publication checklist; do not publish.", ActionIntent.PROPOSE),
        ("The README contains npm install.", ActionIntent.CONTENT_REFERENCE),
        ("Review the web API used by a mobile app.", None),
    ],
)
def test_intent_allows_non_executing_sensitive_references(text, expected) -> None:
    actions = classify_actions(text)
    if expected is None:
        assert actions == []
    else:
        assert actions[0].intent is expected
        assert not actions[0].prohibited


@pytest.mark.parametrize(
    "text",
    [
        "Deploy the application to production.",
        "Run npm install.",
        "Git push main.",
        "Publish the package.",
        "Run rm -rf /tmp/example.",
    ],
)
def test_intent_blocks_execution(text) -> None:
    actions = classify_actions(text)
    assert actions
    assert any(action.intent is ActionIntent.EXECUTE and action.prohibited for action in actions)


@pytest.mark.parametrize(
    "text, blocked_reasons",
    [
        ("Review the README, then deploy the application.", {"deploy"}),
        ("Do not publish the documentation. Deploy the application.", {"deploy"}),
        ("The README contains npm install and deploy the application.", {"deploy"}),
        ("Analyze authentication, then run rm -rf /tmp/example.", {"destructive_action"}),
        ("Do not edit docs and git push main.", {"git_mutation"}),
    ],
)
def test_mixed_action_intent_is_action_local(text, blocked_reasons) -> None:
    reasons = {action.reason for action in classify_actions(text) if action.prohibited}
    assert blocked_reasons <= reasons


@pytest.mark.parametrize(
    "goal, allowed, rejected",
    [
        ("Review frontend responsive React behavior", {ReviewType.FRONTEND}, set()),
        ("Review REST API authorization for a mobile client", {ReviewType.BACKEND_API}, set()),
        ("Implement native iOS app screen", set(), {"out of Web Development scope"}),
        ("Build a desktop app updater", set(), {"out of Web Development scope"}),
        ("Provision Kubernetes cluster", set(), {"out of Web Development scope"}),
        ("Write Terraform cloud provisioning", set(), {"out of Web Development scope"}),
        ("Execute a marketing campaign", set(), {"out of Web Development scope"}),
        ("Review SEO metadata for a web product", {ReviewType.ACCESSIBILITY_PERFORMANCE_SEO}, set()),
    ],
)
def test_scope_assessment(goal, allowed, rejected) -> None:
    task = TaskScope(goal=goal, acceptance_criteria=["Assess scope"])
    try:
        _, _, result = preflight(task, snapshot())
    except WebDepartmentError as exc:
        assert str(exc) in rejected
        return
    if rejected:
        assert result.blocked
        assert any(reason in rejected for reason in result.reasons)
        return
    assert not result.blocked
    planned = set(result.required_reviews)
    assert allowed <= planned


def test_mixed_scope_is_blocked() -> None:
    with pytest.raises(WebDepartmentError, match="mixed-scope"):
        create_run_context(scope("Review web API auth and implement native Android app"), snapshot(), safe_run_config_state(SAFE_RUN_CONFIG))


@pytest.mark.parametrize(
    "files, message",
    [
        ([RepositoryFile("../x", "ok")], "traversal"),
        ([RepositoryFile("/x", "ok")], "absolute"),
        ([RepositoryFile("a/../b.txt", "1"), RepositoryFile("b.txt", "2")], "duplicate"),
        ([RepositoryFile("bin.dat", "abc\x00def")], "binary-like"),
        ([RepositoryFile("secret.txt", "api_key=supersecretvalue")], "secret-like"),
        ([RepositoryFile("big.txt", "x" * (MAX_FILE_BYTES + 1))], "file too large"),
    ],
)
def test_snapshot_validation_rejects_bad_content(files, message) -> None:
    with pytest.raises(WebDepartmentError, match=message):
        canonical_snapshot(snapshot(files))


def test_snapshot_file_count_and_total_limits() -> None:
    with pytest.raises(WebDepartmentError, match="too many files"):
        canonical_snapshot(snapshot([RepositoryFile(f"f{i}.txt", "x") for i in range(MAX_SNAPSHOT_FILES + 1)]))
    with pytest.raises(WebDepartmentError, match="total content"):
        canonical_snapshot(snapshot([RepositoryFile(f"f{i}.txt", "x" * (MAX_TOTAL_BYTES // 10)) for i in range(11)]))


def test_context_binding_rejects_changed_scope_snapshot_policy_or_plan() -> None:
    ctx = context()
    bind_context(ctx, ctx.scope, ctx.snapshot)
    with pytest.raises(WebDepartmentError, match="scope digest"):
        bind_context(ctx, replace(ctx.scope, goal="Different web goal"), ctx.snapshot)
    with pytest.raises(WebDepartmentError, match="snapshot digest"):
        bind_context(ctx, ctx.scope, snapshot([RepositoryFile("src/app.tsx", "changed")]))
    ctx.policy_version = "old"
    with pytest.raises(WebDepartmentError, match="stale policy"):
        bind_context(ctx, scope(), snapshot())


def test_tools_do_not_accept_model_supplied_snapshot_or_scope_json() -> None:
    tool_names = {getattr(tool, "name", "") for tool in web_development_lead.tools}
    assert "inspect_repository_context" not in tool_names
    assert "draft_implementation_proposal" not in tool_names
    assert "list_snapshot_files" in tool_names
    assert "read_snapshot_file" in tool_names


def test_authoritative_review_plan_security_and_final_are_mandatory() -> None:
    ctx = context()
    plan = {item.review_type: item for item in ctx.authoritative_review_plan}
    assert plan[ReviewType.SECURITY_PRIVACY].mandatory
    assert plan[ReviewType.INDEPENDENT_FINAL_QUALITY].mandatory
    assert plan[ReviewType.FRONTEND].applicable
    assert plan[ReviewType.BACKEND_API].applicable


def test_missing_reduced_fabricated_wrong_duplicate_review_cases() -> None:
    ctx = context()
    item = ctx.authoritative_review_plan[0]
    record_specialist_execution(ctx, item.review_type, item.specialist_identity, passing_result(item.review_type))
    with pytest.raises(WebDepartmentError, match="duplicate review"):
        record_specialist_execution(ctx, item.review_type, item.specialist_identity, passing_result(item.review_type))
    with pytest.raises(WebDepartmentError, match="wrong reviewer"):
        record_specialist_execution(context(), item.review_type, "Web Development Lead", passing_result(item.review_type))
    verdict = final_verdict(context())
    assert "required review missing" in " ".join(validate_final_verdict(context(), verdict))


def test_specialist_fail_blocked_and_blocking_findings_propagate() -> None:
    ctx = context()
    item = [plan for plan in ctx.authoritative_review_plan if plan.review_type is ReviewType.SECURITY_PRIVACY][0]
    finding = EvidenceItem("snapshot", "auth route", "ledger", Verdict.PASS)
    result = SpecialistReviewResult(
        review_type=item.review_type,
        status=Verdict.FAIL,
        summary="Auth bypass",
        findings=[
            ReviewerFinding(
                FindingSeverity.HIGH,
                "Auth bypass",
                [finding],
                "Unauthorized access",
                "Enforce authorization",
                True,
            )
        ],
    )
    record_specialist_execution(ctx, item.review_type, item.specialist_identity, result)
    assert ctx.blocking_conditions
    errors = validate_final_verdict(ctx, final_verdict(ctx))
    assert any("blocking findings remain" in error for error in errors)
    assert any("model omitted trusted blocking finding" in error for error in errors)


def test_premature_final_review_and_lead_impersonation_rejected() -> None:
    ctx = context()
    final = [item for item in ctx.authoritative_review_plan if item.review_type is ReviewType.INDEPENDENT_FINAL_QUALITY][0]
    with pytest.raises(WebDepartmentError, match="premature independent final review"):
        record_specialist_execution(ctx, final.review_type, final.specialist_identity, passing_result(final.review_type))
    run_all_required_reviews(ctx)
    with pytest.raises(WebDepartmentError, match="wrong reviewer"):
        record_specialist_execution(ctx, final.review_type, "Web Development Lead", passing_result(final.review_type))


def test_valid_trusted_evidence_required_for_pass() -> None:
    ctx = context()
    run_all_required_reviews(ctx)
    assert not validate_final_verdict(ctx, final_verdict(ctx))
    assert final_pass_is_allowed(final_verdict(ctx), ctx)
    assert "PASS requires non-empty trusted evidence" in validate_final_verdict(ctx, final_verdict(ctx, []))[0]
    fake = FinalVerdict(Verdict.PASS, "fake", [EvidenceItem("fake", "fake", "model", Verdict.PASS, "unknown")])
    assert any("unknown evidence ID" in error for error in validate_final_verdict(ctx, fake))


def test_duplicate_wrong_model_authored_and_not_executed_evidence_rejected() -> None:
    ctx = context()
    run_all_required_reviews(ctx)
    duplicate = ctx.trusted_evidence_ledger[0]
    ctx.trusted_evidence_ledger.append(duplicate)
    with pytest.raises(WebDepartmentError, match="duplicate trusted evidence"):
        validate_final_verdict(ctx, final_verdict(ctx))
    ctx.trusted_evidence_ledger.pop()
    model_evidence = EvidenceRecord(
        "model_evidence",
        "model",
        EvidenceType.TEST_EXECUTION,
        None,
        "claimed tests",
        status=Verdict.PASS,
        model_authored=True,
    )
    ctx.trusted_evidence_ledger.append(model_evidence)
    assert any("model-authored" in error for error in validate_final_verdict(ctx, final_verdict(ctx, ["model_evidence"])))
    not_executed = EvidenceRecord(
        "not_executed",
        "test",
        EvidenceType.NOT_EXECUTED,
        None,
        "browser",
        status=Verdict.NOT_EXECUTED,
    )
    ctx.trusted_evidence_ledger.append(not_executed)
    assert any("NOT_EXECUTED" in error for error in validate_final_verdict(ctx, final_verdict(ctx, ["not_executed"])))


def test_approval_contract_requires_human_identity_stable_id_and_rejection_reason() -> None:
    ctx = build_trusted_context(
            TaskScope(
                    goal="Prepare a deployment readiness proposal",
                    acceptance_criteria=["Require human approval for sensitive deployment analysis"],
                ),
        snapshot(),
    )
    action_id = ctx.sensitive_action_ledger[0].action_id
    with pytest.raises(WebDepartmentError, match="anonymous"):
        apply_human_approval(ctx, ApprovalDecision(action_id, "d1", "", ApprovalDecisionValue.APPROVE))
    with pytest.raises(WebDepartmentError, match="missing decision"):
        apply_human_approval(ctx, ApprovalDecision(action_id, "", "alice", ApprovalDecisionValue.APPROVE))
    with pytest.raises(WebDepartmentError, match="rejection requires reason"):
        apply_human_approval(ctx, ApprovalDecision(action_id, "d2", "alice", ApprovalDecisionValue.REJECT))
    with pytest.raises(WebDepartmentError, match="unknown action"):
        apply_human_approval(ctx, ApprovalDecision("unknown", "d3", "alice", ApprovalDecisionValue.APPROVE))


def test_approval_ledger_update_replay_and_non_execution_semantics() -> None:
    ctx = build_trusted_context(
        TaskScope(goal="Document npm install instructions", acceptance_criteria=["Do not run them"]),
        snapshot(),
    )
    action_id = ctx.sensitive_action_ledger[0].action_id
    record = apply_human_approval(ctx, ApprovalDecision(action_id, "decision-1", "alice@example.com", ApprovalDecisionValue.APPROVE, "Allow documentation"))
    assert record.human_identity == "alice@example.com"
    assert record.requested_transition.startswith("non_executing")
    assert ctx.trusted_evidence_ledger[-1].evidence_type is EvidenceType.HUMAN_APPROVAL
    with pytest.raises(WebDepartmentError, match="duplicate approval decision"):
        apply_human_approval(ctx, ApprovalDecision(action_id, "decision-1", "alice@example.com", ApprovalDecisionValue.APPROVE))


def test_risk_acceptance_requires_human_owned_state() -> None:
    ctx = context()
    ctx.risk_ledger.append(RiskRecord("risk-1", FindingSeverity.HIGH, "Residual auth risk", "security", True))
    with pytest.raises(WebDepartmentError, match="anonymous"):
        apply_risk_decision(ctx, RiskAcceptanceDecision("risk-1", "risk-d1", "", "accept", True))
    with pytest.raises(WebDepartmentError, match="rationale"):
        apply_risk_decision(ctx, RiskAcceptanceDecision("risk-1", "risk-d2", "alice", "", True))
    with pytest.raises(WebDepartmentError, match="unknown risk"):
        apply_risk_decision(ctx, RiskAcceptanceDecision("unknown", "risk-d3", "alice", "accept", True))
    updated = apply_risk_decision(ctx, RiskAcceptanceDecision("risk-1", "risk-d4", "alice", "Business owner accepts", True))
    assert updated.accepted_by_human
    assert updated.evidence_id


def test_independent_final_review_must_be_last() -> None:
    ctx = context()
    run_all_required_reviews(ctx)
    first = ctx.authoritative_review_plan[0]
    ctx.specialist_execution_ledger.append(
        replace(ctx.specialist_execution_ledger[0], invocation_id=stable_id("late", "x"))
    )
    errors = validate_final_verdict(ctx, final_verdict(ctx))
    assert any("independent final review was not last" in error for error in errors)


def test_context_serializer_round_trip_and_malformed_state_rejection() -> None:
    ctx = context()
    run_all_required_reviews(ctx)
    data = serialize_context(ctx)
    restored = context_from_json(data)
    assert restored.scope_digest == ctx.scope_digest
    assert restored.snapshot_digest == ctx.snapshot_digest
    assert len(restored.trusted_evidence_ledger) == len(ctx.trusted_evidence_ledger)
    bad = dict(data)
    bad["policy_version"] = "old"
    with pytest.raises(WebDepartmentError, match="stale policy"):
        context_from_json(bad)
    duplicate = serialize_context(ctx)
    duplicate["trusted_evidence_ledger"].append(duplicate["trusted_evidence_ledger"][0])
    with pytest.raises(WebDepartmentError, match="duplicate evidence ID"):
        context_from_json(duplicate)


def test_build_workflow_input_exposes_only_digests_not_snapshot_text() -> None:
    payload = build_workflow_input(scope(), snapshot([RepositoryFile("src/app.tsx", "secret-free source")]))
    assert "secret-free source" not in payload
    assert "scope_digest" in payload
    assert "snapshot_digest" in payload


def test_no_network_or_external_execution_is_used(monkeypatch) -> None:
    def denied(*args, **kwargs):
        raise AssertionError("network or shell access is forbidden in offline tests")

    monkeypatch.setattr("socket.socket", denied)
    ctx = context()
    add_evidence(ctx, "test", EvidenceType.STATIC_VALIDATION, None, "offline", [], Verdict.PASS, False)
    assert ctx.trusted_evidence_ledger[-1].status is Verdict.PASS
