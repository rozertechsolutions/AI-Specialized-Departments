import unittest
from pathlib import Path

from software_development_department.agents import build_department_agents
from software_development_department.orchestrator import DepartmentRuntime, OrchestrationLimits
from software_development_department.models import OrchestrationState


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "software_development_department"


def read(name: str) -> str:
    return (SRC / name).read_text()


class AgentsStaticTests(unittest.TestCase):
    def test_lead_uses_agents_as_tools_and_no_handoffs_remain(self) -> None:
        agents = read("agents.py")
        orchestrator = read("orchestrator.py")
        self.assertIn(".as_tool(", agents)
        self.assertNotIn("handoff", agents)
        self.assertNotIn("handoffs", agents)
        self.assertNotIn("handoff", orchestrator)

    def test_typed_outputs_are_required_for_lead_and_specialists(self) -> None:
        agents = read("agents.py")
        for output_name in (
            "RequirementsOutput",
            "ArchitectureOutput",
            "ImplementationEvidence",
            "ValidationEvidence",
            "CodeReviewOutput",
            "RiskReviewOutput",
            "DocumentationReadinessOutput",
            "LeadFinalRecord",
        ):
            self.assertIn(output_name, agents)
        self.assertIn("output_type=LeadFinalRecord", agents)

    def test_lead_retains_control_after_specialist_calls(self) -> None:
        orchestrator = read("orchestrator.py")
        self.assertIn("Lead remains the active top-level agent", orchestrator)
        self.assertIn("Runner.run(self.lead", orchestrator)
        self.assertIn("PAUSED_FOR_HUMAN_APPROVAL", orchestrator)

    def test_department_construction_has_lead_and_seven_tools(self) -> None:
        agents = build_department_agents()
        self.assertEqual(len(agents), 8)
        lead = agents["software-development-lead"]
        self.assertEqual(len(lead.tools), 7)
        self.assertEqual(lead.handoffs, [])

    def test_orchestration_limits_cover_turn_specialist_total_and_approval_counts(self) -> None:
        runtime = DepartmentRuntime.build(OrchestrationLimits(max_turns=2, max_specialist_calls=2, max_total_tool_calls=3, max_approval_cycles=1))
        self.assertEqual(runtime.validate_specialist_call_sequence(("software-architect",)), OrchestrationState.RUNNING)
        self.assertEqual(runtime.validate_specialist_call_sequence(("software-architect", "software-architect")), OrchestrationState.STOPPED)
        self.assertEqual(runtime.validate_total_tool_calls(3), OrchestrationState.RUNNING)
        self.assertEqual(runtime.validate_total_tool_calls(4), OrchestrationState.STOPPED)
        self.assertEqual(runtime.validate_approval_cycles(1), OrchestrationState.RUNNING)
        self.assertEqual(runtime.validate_approval_cycles(2), OrchestrationState.STOPPED)

    def test_no_real_external_or_operational_tools_are_implemented(self) -> None:
        tools = read("tools.py")
        forbidden_defs = ("subprocess", "requests", "urllib", "git ", "def deploy", "def publish", "def sign")
        self.assertIn("Protocol", tools)
        self.assertIn("InertWorkspaceTools", tools)
        self.assertTrue(all(term not in tools for term in forbidden_defs))

    def test_workflows_are_differentiated_and_complete(self) -> None:
        workflows = read("workflows.py")
        self.assertEqual(workflows.count('"purpose":'), 11)
        self.assertEqual(workflows.count('"exclusive_focus":'), 11)
        self.assertIn("symptom-not-suppressed confirmation", workflows)
        self.assertIn("stop before publication/deployment/signing/release", workflows)

    def test_fourteen_capabilities_are_preserved(self) -> None:
        skills = read("skills.py")
        self.assertEqual(skills.count("'title':"), 14)


if __name__ == "__main__":
    unittest.main()
