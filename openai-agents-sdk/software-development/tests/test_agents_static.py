from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "software_development_department"


def read(name: str) -> str:
    return (SRC / name).read_text()


def test_lead_uses_agents_as_tools_and_no_handoffs_remain() -> None:
    agents = read("agents.py")
    orchestrator = read("orchestrator.py")
    assert ".as_tool(" in agents
    assert "handoff" not in agents
    assert "handoffs" not in agents
    assert "handoff" not in orchestrator


def test_typed_outputs_are_required_for_lead_and_specialists() -> None:
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
        assert output_name in agents
    assert "output_type=LeadFinalRecord" in agents


def test_lead_retains_control_after_specialist_calls() -> None:
    orchestrator = read("orchestrator.py")
    assert "Lead remains the active top-level agent" in orchestrator
    assert "Runner.run(self.lead" in orchestrator
    assert "PAUSED_FOR_HUMAN_APPROVAL" in orchestrator


def test_no_real_external_or_operational_tools_are_implemented() -> None:
    tools = read("tools.py")
    forbidden_defs = ("subprocess", "requests", "urllib", "git ", "def deploy", "def publish", "def sign")
    assert "Protocol" in tools
    assert "InertWorkspaceTools" in tools
    assert all(term not in tools for term in forbidden_defs)


def test_workflows_are_differentiated_and_complete() -> None:
    workflows = read("workflows.py")
    assert workflows.count('"purpose":') == 11
    assert workflows.count('"exclusive_focus":') == 11
    assert "symptom-not-suppressed confirmation" in workflows
    assert "stop before publication/deployment/signing/release" in workflows


def test_fourteen_capabilities_are_preserved() -> None:
    skills = read("skills.py")
    assert skills.count("'title':") == 14
