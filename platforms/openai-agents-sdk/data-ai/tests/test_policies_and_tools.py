import asyncio

from data_ai_agents_sdk.agents import build_data_ai_agents
from data_ai_agents_sdk.policies import (
    appears_to_contain_secret,
    claims_unsupported_completion,
    requires_human_approval,
)
from data_ai_agents_sdk.tools import sensitive_tool_needs_approval


def test_policy_detects_sensitive_actions_and_secret_like_text():
    assert requires_human_approval("prepare deployment to production")
    assert appears_to_contain_secret("contains " + "sk" + "-testvalue")
    assert not appears_to_contain_secret("ordinary evidence summary")


def test_policy_blocks_unsupported_claims_without_evidence():
    assert claims_unsupported_completion("model benchmark passed")
    assert not claims_unsupported_completion("model benchmark passed with evidence from test run")


def test_approval_tool_is_attached_to_coordinator_only():
    agents = build_data_ai_agents()

    assert agents["data-ai-orchestrator"].tools
    for slug, agent in agents.items():
        if slug != "data-ai-orchestrator":
            assert not agent.tools


def test_approval_predicate_requires_human_review_for_sensitive_tool_calls():
    result = asyncio.run(
        sensitive_tool_needs_approval(
            None,
            {"action": "publish model release", "reason": "production launch"},
            "call_1",
        )
    )

    assert result is True
