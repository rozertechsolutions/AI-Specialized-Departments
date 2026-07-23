from devops_cloud_department.agents import (
    ASSURANCE_AGENT_SLUG,
    ENTRY_AGENT_SLUG,
    INPUT_GUARDRAILS,
    OUTPUT_GUARDRAILS,
    ROLE_INSTRUCTIONS,
    build_department_agents,
)
from devops_cloud_department.models import ROLE_BY_SLUG, ROLE_REGISTRY


EXPECTED_ROLES = {
    "devops-cloud-orchestrator",
    "cloud-and-platform-architect",
    "cloud-foundation-engineer",
    "infrastructure-as-code-engineer",
    "cloud-network-engineer",
    "cloud-runtime-managed-services-engineer",
    "ci-cd-engineer",
    "release-and-deployment-engineer",
    "container-and-orchestration-engineer",
    "platform-product-and-developer-experience-engineer",
    "site-reliability-engineer",
    "observability-engineer",
    "resilience-and-disaster-recovery-engineer",
    "performance-and-capacity-engineer",
    "devsecops-engineer",
    "cloud-security-controls-engineer",
    "software-supply-chain-security-engineer",
    "finops-engineer",
    "cloud-sustainability-and-efficiency-analyst",
    "devops-and-cloud-assurance-reviewer",
}


def test_role_registry_is_authoritative_and_complete():
    assert {role.slug for role in ROLE_REGISTRY} == EXPECTED_ROLES
    assert len(ROLE_REGISTRY) == 20
    assert len({role.name for role in ROLE_REGISTRY}) == 20
    assert set(ROLE_BY_SLUG) == EXPECTED_ROLES
    assert set(ROLE_INSTRUCTIONS) == EXPECTED_ROLES


def test_all_ten_sections_are_represented():
    sections = {role.section for role in ROLE_REGISTRY}
    assert len(sections) == 10
    assert any(section.startswith("01 ") for section in sections)
    assert any(section.startswith("10 ") for section in sections)


def test_exactly_twenty_sdk_agents_are_constructed():
    agents = build_department_agents()
    assert set(agents) == EXPECTED_ROLES
    assert len(agents) == 20
    assert len({agent.name for agent in agents.values()}) == 20


def test_entry_agent_reaches_all_specialists_without_self_handoff():
    agents = build_department_agents()
    entry = agents[ENTRY_AGENT_SLUG]
    targets = {getattr(handoff_item, "agent_name", None) for handoff_item in entry.handoffs}
    expected_names = {agents[slug].name for slug in EXPECTED_ROLES - {ENTRY_AGENT_SLUG}}
    assert targets == expected_names
    assert agents[ENTRY_AGENT_SLUG].name not in targets


def test_handoff_graph_is_acyclic_and_star_shaped():
    for role in ROLE_REGISTRY:
        assert role.slug not in role.delegates_to
        if role.slug != ENTRY_AGENT_SLUG:
            assert role.delegates_to == ()


def test_assurance_is_independent_and_non_implementing():
    assurance = ROLE_BY_SLUG[ASSURANCE_AGENT_SLUG]
    assert assurance.review_only is True
    assert assurance.implements_changes is False
    assert "independent" in assurance.review_status
    assert assurance.delegates_to == ()


def test_no_self_review_or_circular_delegation_policy():
    orchestrator = ROLE_BY_SLUG[ENTRY_AGENT_SLUG]
    assert ASSURANCE_AGENT_SLUG in orchestrator.delegates_to
    for role in ROLE_REGISTRY:
        assert role.slug not in role.delegates_to
        assert ASSURANCE_AGENT_SLUG not in ROLE_BY_SLUG[ASSURANCE_AGENT_SLUG].delegates_to


def test_guardrails_are_attached_to_every_agent():
    agents = build_department_agents()
    assert INPUT_GUARDRAILS
    assert OUTPUT_GUARDRAILS
    for agent in agents.values():
        assert agent.input_guardrails == INPUT_GUARDRAILS
        assert agent.output_guardrails == OUTPUT_GUARDRAILS
        assert agent.tools == []
        assert agent.mcp_servers == []


def test_safety_patterns_are_present_in_source():
    import devops_cloud_department.agents as source

    assert "SECRET_PATTERNS" in source.__dict__
    assert "MUTATION_PATTERNS" in source.__dict__
    assert "PRIVILEGED_PATTERNS" in source.__dict__
    assert "RUNTIME_CLAIM_PATTERNS" in source.__dict__
    assert "terraform apply" in source.MUTATION_PATTERNS
    assert "sign the artifact" in source.PRIVILEGED_PATTERNS
    assert "runtime validation completed" in source.RUNTIME_CLAIM_PATTERNS


def test_static_contracts_preserve_specialization_boundaries():
    joined = "\n".join(ROLE_INSTRUCTIONS.values())
    assert "Do not authenticate to cloud accounts" in joined
    assert "No pipeline or deployment is claimed to have run" in joined
    assert "DevSecOps does not absorb Cybersecurity" in joined
    assert "Static review is never represented as runtime validation" in joined

