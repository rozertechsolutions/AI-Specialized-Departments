from devops_cloud_department.agents import ROLE_INSTRUCTIONS


def test_section_roles_are_present():
    assert "devops-cloud-orchestrator" in ROLE_INSTRUCTIONS
    assert "cloud-and-platform-architect" in ROLE_INSTRUCTIONS
    assert "cloud-foundation-engineer" in ROLE_INSTRUCTIONS
    assert "infrastructure-as-code-engineer" in ROLE_INSTRUCTIONS
    assert "cloud-network-engineer" in ROLE_INSTRUCTIONS
    assert "cloud-runtime-managed-services-engineer" in ROLE_INSTRUCTIONS


def test_cloud_foundation_quality_gates_are_static():
    text = "
".join(ROLE_INSTRUCTIONS.values())
    assert "Do not authenticate to cloud accounts" in text
    assert "State, drift, rollback" in text
