from data_ai_agents_sdk import EvidenceItem, ReviewOutput, deserialize_review_output, serialize_review_output
from data_ai_agents_sdk.workflows import WORKFLOWS, workflow_names


def test_review_output_serialization_round_trips():
    output = ReviewOutput(
        owner="data-ai-assurance-reviewer",
        status="BLOCKED",
        summary="Missing provenance evidence.",
        evidence=(EvidenceItem(claim="dataset provenance reviewed", source="provided card", observed=False),),
        human_review_required=True,
        unresolved_risks=("dataset provenance unavailable",),
    )

    assert deserialize_review_output(serialize_review_output(output)) == output


def test_workflows_cover_required_lifecycle():
    names = workflow_names()

    assert "use-case-intake-risk-triage" in names
    assert "source-dataset-component-onboarding" in names
    assert "pipeline-data-product-quality" in names
    assert "analytics-metric-experiment-lifecycle" in names
    assert "ml-candidate-evaluation" in names
    assert "genai-rag-agent-release-review" in names
    assert "ai-operations-risk-readiness" in names
    assert "final-independent-assurance" in names


def test_workflow_status_values_are_canonical():
    for workflow in WORKFLOWS:
        assert workflow.final_status_values == ("PASS", "FAIL", "BLOCKED")
        assert workflow.steps
        assert workflow.gates
