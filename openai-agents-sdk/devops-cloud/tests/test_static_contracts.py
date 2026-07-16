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

def test_ci_cd_release_engineering_static_contracts():
    from devops_cloud_department.ci_cd_release_engineering import QUALITY_GATES, ROLE_INSTRUCTIONS
    assert 'ci-cd-engineer' in ROLE_INSTRUCTIONS
    assert 'release-and-deployment-engineer' in ROLE_INSTRUCTIONS
    assert 'No pipeline or deployment is claimed to have run' in QUALITY_GATES

def test_containers_platform_engineering_static_contracts():
    from devops_cloud_department.containers_platform_engineering import QUALITY_GATES, ROLE_INSTRUCTIONS
    assert 'container-and-orchestration-engineer' in ROLE_INSTRUCTIONS
    assert 'platform-product-and-developer-experience-engineer' in ROLE_INSTRUCTIONS
    assert 'The platform is treated as a product with measurable users and outcomes' in QUALITY_GATES
