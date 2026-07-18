from pathlib import Path

from software_development_department.models import (
    ApprovalDecision,
    CodeReviewOutput,
    DepartmentTask,
    EvidenceItem,
    ImplementationEvidence,
    LeadFinalRecord,
    OrchestrationState,
    RequirementsOutput,
    RiskLevel,
    RoleSlug,
)


def test_task_is_immutable_and_explicit() -> None:
    task = DepartmentTask("Add capability", ("src",), ("criterion",), risk_level=RiskLevel.MEDIUM, workspace_root=Path("."))
    assert task.authorized_scope == ("src",)


def test_typed_final_record_requires_independent_review_role() -> None:
    evidence = EvidenceItem("implemented", "diff", True)
    implementation = ImplementationEvidence(RoleSlug.IMPLEMENTATION, "done", (evidence,), changed_paths=("src/a.py",))
    review = CodeReviewOutput(RoleSlug.CODE_REVIEW, "reviewed", (EvidenceItem("review", "review notes", True),), approved=True)
    record = LeadFinalRecord(
        objective="Add capability",
        requirements=RequirementsOutput(RoleSlug.REQUIREMENTS, "requirements", (EvidenceItem("req", "prompt", True),)),
        plan=("step",),
        implementation_evidence=implementation,
        validation_evidence=None,
        code_review=review,
        risk_review=None,
        documentation_release_readiness=None,
        limitations=(),
        human_decisions=(),
        stop_state=OrchestrationState.STOPPED,
    )
    assert record.has_independent_review()


def test_human_decision_enum_is_explicit() -> None:
    assert ApprovalDecision.DENIED.value == "denied"
