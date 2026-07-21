import asyncio
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from software_development_department.agents import build_department_agents
from software_development_department.models import (
    ApprovalDecision,
    ApprovalDecisionRecord,
    CodeReviewOutput,
    DepartmentTask,
    EvidenceItem,
    FinalState,
    ImplementationEvidence,
    LeadFinalRecord,
    RequirementsOutput,
    RiskLevel,
    RiskReviewOutput,
    RoleSlug,
    ToolActionType,
)
from software_development_department.orchestrator import DepartmentContext, DepartmentRuntime, RunLimits
from software_development_department.policies import (
    action_requires_human_approval,
    final_record_is_supported,
    keyword_mentions_are_allowed,
    normalize_relative_path,
    validate_scope,
)
from software_development_department.tools import DeterministicApprovalProvider, MemoryRepository


class DepartmentRuntimeTests(unittest.TestCase):
    def test_department_construction_has_lead_seven_tools_and_no_handoffs(self) -> None:
        agents = build_department_agents()
        self.assertEqual(len(agents), 8)
        lead = agents["software-development-lead"]
        self.assertEqual(len(lead.tools), 7)
        self.assertEqual(getattr(lead, "handoffs", []), [])
        for slug, agent in agents.items():
            if slug != "software-development-lead":
                self.assertEqual(getattr(agent, "handoffs", []), [])

    def test_models_include_current_approval_and_final_state_records(self) -> None:
        record = ApprovalDecisionRecord("src/a.py", "write", ApprovalDecision.APPROVED, "approved scoped edit")
        self.assertEqual(record.decision, ApprovalDecision.APPROVED)
        self.assertEqual(FinalState.PAUSED.value, "paused")
        self.assertEqual(RiskLevel.MEDIUM.value, "medium")

    def test_scope_validation_normalizes_and_blocks_escape(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.assertTrue(validate_scope(("src/a.py",), ("src",), root))
            self.assertFalse(validate_scope(("../outside",), ("src",), root))
            with self.assertRaisesRegex(ValueError, "absolute"):
                normalize_relative_path(root, "/absolute/path")

    def test_scope_validation_rejects_symlink_escape(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp) / "workspace"
            outside = Path(tmp) / "outside"
            root.mkdir()
            outside.mkdir()
            (root / "link").symlink_to(outside)
            with self.assertRaisesRegex(ValueError, "escapes"):
                normalize_relative_path(root, "link/secret.txt")

    def test_context_uses_injected_reader_writer_and_approval_provider(self) -> None:
        async def scenario() -> None:
            repo = MemoryRepository({"src/a.py": "old"})
            approval = DeterministicApprovalProvider(ApprovalDecision.APPROVED)
            context = DepartmentContext(Path("."), ("src",), repo, repo, approval)
            self.assertEqual(await context.read_text("src/a.py"), "old")
            result = await context.write_text("src/a.py", "new", "approved scoped change")
            self.assertEqual(result.decision, ApprovalDecision.APPROVED)
            self.assertEqual(repo.files["src/a.py"], "new")
            self.assertEqual(len(approval.requested), 1)

        asyncio.run(scenario())

    def test_rejection_prevents_write(self) -> None:
        async def scenario() -> None:
            repo = MemoryRepository({"src/a.py": "old"})
            approval = DeterministicApprovalProvider(ApprovalDecision.REJECTED)
            context = DepartmentContext(Path("."), ("src",), repo, repo, approval)
            result = await context.write_text("src/a.py", "new", "rejected scoped change")
            self.assertEqual(result.decision, ApprovalDecision.REJECTED)
            self.assertEqual(repo.files["src/a.py"], "old")

        asyncio.run(scenario())

    def test_run_limits_are_bounded(self) -> None:
        self.assertEqual(RunLimits(max_turns=2, max_specialist_calls=2, max_approval_cycles=1).max_turns, 2)
        with self.assertRaises(ValueError):
            RunLimits(max_turns=0)
        with self.assertRaises(ValueError):
            RunLimits(max_specialist_calls=25)

    def test_final_record_requires_validation_and_independent_reviews(self) -> None:
        evidence = EvidenceItem("implemented", "diff", True)
        implementation = ImplementationEvidence(
            RoleSlug.IMPLEMENTATION,
            "done",
            (evidence,),
            changed_paths=("src/a.py",),
            validation_notes=("security-sensitive path changed",),
        )
        review = CodeReviewOutput(RoleSlug.CODE_REVIEW, "reviewed", (EvidenceItem("review", "review notes", True),), approved=True)
        risk = RiskReviewOutput(RoleSlug.RISK_REVIEW, "risk reviewed", (EvidenceItem("risk", "risk notes", True),), approved=True)
        validation = RequirementsOutput(RoleSlug.REQUIREMENTS, "requirements", (EvidenceItem("req", "prompt", True),))
        record = LeadFinalRecord(
            objective="Add capability",
            requirements=validation,
            plan=("step",),
            implementation_evidence=implementation,
            validation_evidence=None,
            code_review=review,
            risk_review=risk,
            documentation_release_readiness=None,
            limitations=(),
            approval_decisions=(),
            final_state=FinalState.COMPLETED,
        )
        self.assertFalse(final_record_is_supported(record))
        complete = LeadFinalRecord(
            objective="Add capability",
            requirements=validation,
            plan=("step",),
            implementation_evidence=implementation,
            validation_evidence=None,
            code_review=None,
            risk_review=risk,
            documentation_release_readiness=None,
            limitations=(),
            approval_decisions=(),
            final_state=FinalState.COMPLETED,
        )
        self.assertFalse(complete.has_independent_review())

    def test_policy_blocks_sensitive_actions_but_allows_analysis_text(self) -> None:
        self.assertTrue(action_requires_human_approval(type("Action", (), {"action_type": ToolActionType.PUBLISH})()))
        self.assertTrue(keyword_mentions_are_allowed("Analyze credential handling and deployment risk without taking action"))

    def test_runtime_build_accepts_host_injected_models(self) -> None:
        repo = MemoryRepository({"src/a.py": "old"})
        context = DepartmentContext(Path("."), ("src",), repo, repo, DeterministicApprovalProvider())
        runtime = DepartmentRuntime.build(context=context, limits=RunLimits(max_turns=2), models={})
        self.assertEqual(runtime.lead.name, "software-development-lead")
        self.assertEqual(len(runtime.specialists), 7)

    def test_empty_task_is_blocked_without_sdk_call(self) -> None:
        async def scenario() -> None:
            repo = MemoryRepository({"src/a.py": "old"})
            context = DepartmentContext(Path("."), ("src",), repo, repo, DeterministicApprovalProvider())
            runtime = DepartmentRuntime.build(context=context)
            result = await runtime.run(DepartmentTask("", ("src",), ("done",)))
            self.assertEqual(result.state, FinalState.BLOCKED)

        asyncio.run(scenario())


if __name__ == "__main__":
    unittest.main()
