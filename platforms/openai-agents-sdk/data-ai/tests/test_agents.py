from data_ai_agents_sdk import ROLE_INSTRUCTIONS, build_data_ai_agents, build_run_config


EXPECTED_AGENTS = {
    "data-ai-orchestrator",
    "data-ai-solution-governance-reviewer",
    "data-architecture-dataset-reviewer",
    "data-platform-analytics-reviewer",
    "ml-genai-evaluation-reviewer",
    "ai-ops-risk-reviewer",
    "data-ai-assurance-reviewer",
}


def test_agents_construct_offline_and_are_complete():
    agents = build_data_ai_agents()

    assert set(agents) == EXPECTED_AGENTS
    assert set(ROLE_INSTRUCTIONS) == EXPECTED_AGENTS
    assert agents["data-ai-orchestrator"].name == "Data and AI Orchestrator"


def test_handoffs_are_coordinator_only_and_acyclic():
    agents = build_data_ai_agents()
    coordinator = agents["data-ai-orchestrator"]

    assert len(coordinator.handoffs) == 6
    for slug, agent in agents.items():
        if slug != "data-ai-orchestrator":
            assert not agent.handoffs


def test_structured_outputs_and_guardrails_are_configured():
    agents = build_data_ai_agents()

    for agent in agents.values():
        assert agent.output_type is not None
        assert agent.input_guardrails
        assert agent.output_guardrails


def test_run_config_disables_tracing_and_sensitive_capture():
    run_config = build_run_config()

    assert run_config.tracing_disabled is True
    assert run_config.trace_include_sensitive_data is False
