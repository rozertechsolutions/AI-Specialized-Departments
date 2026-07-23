from marketing_engineering_agents.models import WorkOutput, WorkState


def test_external_action_defaults_to_false() -> None:
    output = WorkOutput(
        state=list(WorkState)[0],
        owner="review-owner",
        scope="synthetic validation scope",
        summary="synthetic validation result",
        next_human_decision="Review the decision package.",
    )
    assert output.external_action_performed is False
