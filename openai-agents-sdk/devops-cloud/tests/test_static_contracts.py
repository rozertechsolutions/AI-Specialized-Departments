from devops_cloud_department.agents import ROLE_INSTRUCTIONS


def test_section_roles_are_present():
    assert "devops-cloud-orchestrator" in ROLE_INSTRUCTIONS
    assert "cloud-and-platform-architect" in ROLE_INSTRUCTIONS
    assert "cloud-foundation-engineer" in ROLE_INSTRUCTIONS
    assert "infrastructure-as-code-engineer" in ROLE_INSTRUCTIONS
    assert "cloud-network-engineer" in ROLE_INSTRUCTIONS
    assert "cloud-runtime-managed-services-engineer" in ROLE_INSTRUCTIONS


def test_cloud_foundation_quality_gates_are_static():
    text = "\n".join(ROLE_INSTRUCTIONS.values())
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

def test_sre_observability_operations_static_contracts():
    from devops_cloud_department.sre_observability_operations import QUALITY_GATES, ROLE_INSTRUCTIONS
    assert 'site-reliability-engineer' in ROLE_INSTRUCTIONS
    assert 'observability-engineer' in ROLE_INSTRUCTIONS
    assert 'Alerts are actionable, owned and tied to service objectives' in QUALITY_GATES

def test_resilience_disaster_recovery_static_contracts():
    from devops_cloud_department.resilience_disaster_recovery import QUALITY_GATES, ROLE_INSTRUCTIONS
    assert 'resilience-and-disaster-recovery-engineer' in ROLE_INSTRUCTIONS
    assert 'RTO and RPO are justified by service requirements' in QUALITY_GATES

def test_performance_capacity_efficiency_static_contracts():
    from devops_cloud_department.performance_capacity_efficiency import QUALITY_GATES, ROLE_INSTRUCTIONS
    assert 'performance-and-capacity-engineer' in ROLE_INSTRUCTIONS
    assert 'No benchmark result is invented or inferred without execution evidence' in QUALITY_GATES

def test_devsecops_static_contracts():
    from devops_cloud_department.devsecops import QUALITY_GATES, ROLE_INSTRUCTIONS
    assert 'devsecops-engineer' in ROLE_INSTRUCTIONS
    assert 'cloud-security-controls-engineer' in ROLE_INSTRUCTIONS
    assert 'software-supply-chain-security-engineer' in ROLE_INSTRUCTIONS
    assert 'No secret values or real identifiers are committed' in QUALITY_GATES


def test_finops_sustainability_static_contracts():
    from devops_cloud_department.finops_sustainability import QUALITY_GATES, ROLE_INSTRUCTIONS
    assert 'finops-engineer' in ROLE_INSTRUCTIONS
    assert 'cloud-sustainability-and-efficiency-analyst' in ROLE_INSTRUCTIONS
    assert 'Financial decisions remain human-owned' in QUALITY_GATES
    assert 'Sustainability claims require measurable evidence' in QUALITY_GATES


def test_assurance_review_static_contracts():
    from devops_cloud_department.assurance_review import QUALITY_GATES, ROLE_INSTRUCTIONS
    assert 'devops-and-cloud-assurance-reviewer' in ROLE_INSTRUCTIONS
    assert 'Reviewer independence is explicit' in QUALITY_GATES
    assert 'Static review is never represented as runtime validation' in QUALITY_GATES
