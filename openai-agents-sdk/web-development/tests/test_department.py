from dataclasses import asdict

import pytest

from web_development_department.department import SPECIALIST_AGENTS, web_development_lead
from web_development_department.guardrails import final_pass_is_allowed
from web_development_department.models import (
    ApprovalDecision,
    ApprovalDecisionValue,
    EvidenceItem,
    FinalVerdict,
    FindingSeverity,
    RepositoryFile,
    RepositorySnapshot,
    ReviewerFinding,
    TaskScope,
    UnresolvedRisk,
    Verdict,
)
from web_development_department.policy import contains_secret, final_verdict_is_valid, requires_human_approval
from web_development_department.tools import request_sensitive_action
from web_development_department.workflow import build_workflow_input, classify_run_result, serialize_interrupted_run


def _tool_names(agent):
    return {getattr(tool, "name", "") for tool in agent.tools}


def test_lead_uses_manager_tools_not_handoffs() -> None:
    assert web_development_lead.handoffs == []
    names = _tool_names(web_development_lead)
    assert "analyze_web_architecture" in names
    assert "review_security_privacy" in names
    assert "review_quality_release" in names


def test_specialists_have_bounded_context_tools() -> None:
    for agent in SPECIALIST_AGENTS:
        names = _tool_names(agent)
        assert "inspect_repository_context" in names
        assert names


def test_reviewers_are_read_only() -> None:
    for agent in SPECIALIST_AGENTS[3:]:
        names = _tool_names(agent)
        assert "draft_implementation_proposal" not in names
        assert "request_sensitive_action" not in names


def test_sensitive_tool_requires_sdk_approval() -> None:
    assert getattr(request_sensitive_action, "needs_approval") is True


def test_guardrails_are_attached_to_lead() -> None:
    assert web_development_lead.input_guardrails
    assert web_development_lead.output_guardrails


def test_policy_flags_secrets_and_sensitive_actions() -> None:
    assert contains_secret("api_key=sk-example000000000000")
    assert requires_human_approval("deployment")
    assert requires_human_approval("git mutation")
    assert not requires_human_approval("read_workspace")


def test_final_pass_rejects_blocking_findings_and_missing_evidence() -> None:
    finding = ReviewerFinding(
        severity=FindingSeverity.CRITICAL,
        title="Auth bypass",
        evidence=[EvidenceItem(kind="file", description="route lacks auth", source="app.py")],
        impact="unauthorized access",
        remediation="enforce authorization",
        blocking=True,
    )
    verdict = FinalVerdict(
        verdict=Verdict.PASS,
        summary="ready",
        evidence=[],
        findings=[finding],
    )
    assert final_verdict_is_valid(verdict)
    assert not final_pass_is_allowed(verdict)


def test_final_pass_rejects_unresolved_blocking_risk() -> None:
    verdict = FinalVerdict(
        verdict=Verdict.PASS,
        summary="ready",
        evidence=[EvidenceItem(kind="test", description="unit tests", source="pytest", status=Verdict.PASS)],
        unresolved_risks=[
            UnresolvedRisk(
                severity=FindingSeverity.HIGH,
                description="missing security review",
                owner="security reviewer",
                blocking=True,
            )
        ],
    )
    assert final_verdict_is_valid(verdict)


def test_workflow_input_is_in_memory_json() -> None:
    scope = TaskScope(goal="Add form validation", acceptance_criteria=["invalid input is rejected"])
    snapshot = RepositorySnapshot(files=[RepositoryFile(path="src/form.ts", content="export {}", language="ts")])
    payload = build_workflow_input(scope, snapshot)
    assert "src/form.ts" in payload
    assert "Return FinalVerdict only" in payload


def test_result_classification_and_serialization_guards() -> None:
    class Completed:
        interruptions = []

    assert classify_run_result(Completed()) == "completed"
    with pytest.raises(ValueError):
        serialize_interrupted_run(Completed())


def test_approval_decision_contract_supports_rejection() -> None:
    decision = ApprovalDecision(
        interruption_index=0,
        decision=ApprovalDecisionValue.REJECT,
        rejection_message="Rejected by human reviewer.",
        remember=True,
    )
    assert asdict(decision)["decision"] == ApprovalDecisionValue.REJECT
