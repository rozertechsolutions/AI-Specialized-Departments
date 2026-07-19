from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RoleDefinition:
    """Static contract for one DevOps and Cloud department role."""

    slug: str
    name: str
    section: str
    mission: str
    owns: tuple[str, ...]
    delegates_to: tuple[str, ...]
    review_status: str
    implements_changes: bool
    review_only: bool = False


ROLE_REGISTRY: tuple[RoleDefinition, ...] = (
    RoleDefinition("devops-cloud-orchestrator", "DevOps and Cloud Orchestrator", "01 Leadership and Architecture", "Intake, routing, dependency control, escalation, and evidence aggregation.", ("request intake", "routing", "cross-section handoffs"), ("cloud-and-platform-architect", "cloud-foundation-engineer", "infrastructure-as-code-engineer", "cloud-network-engineer", "cloud-runtime-managed-services-engineer", "ci-cd-engineer", "release-and-deployment-engineer", "container-and-orchestration-engineer", "platform-product-and-developer-experience-engineer", "site-reliability-engineer", "observability-engineer", "resilience-and-disaster-recovery-engineer", "performance-and-capacity-engineer", "devsecops-engineer", "cloud-security-controls-engineer", "software-supply-chain-security-engineer", "finops-engineer", "cloud-sustainability-and-efficiency-analyst", "devops-and-cloud-assurance-reviewer"), "coordinates but does not self-review", False),
    RoleDefinition("cloud-and-platform-architect", "Cloud and Platform Architect", "01 Leadership and Architecture", "Provider-neutral architecture, ADRs, standards, target-state models, and technical boundaries.", ("architecture decisions", "technology tradeoffs", "standards"), (), "implementing specialist", True),
    RoleDefinition("cloud-foundation-engineer", "Cloud Foundation Engineer", "02 Cloud Foundation and Infrastructure", "Landing zones, organizations, accounts, subscriptions, projects, environment separation, and governance foundations.", ("landing-zone foundations", "environment separation", "resource lifecycle foundations"), (), "implementing specialist", True),
    RoleDefinition("infrastructure-as-code-engineer", "Infrastructure as Code Engineer", "02 Cloud Foundation and Infrastructure", "Declarative infrastructure design, modules, state, drift, idempotency, configuration management, and change plans.", ("IaC design", "module patterns", "state and drift strategy"), (), "implementing specialist", True),
    RoleDefinition("cloud-network-engineer", "Cloud Network Engineer", "02 Cloud Foundation and Infrastructure", "Cloud network design for VPC/VNet, subnets, routing, DNS, ingress, egress, connectivity, and segmentation.", ("cloud networking", "load balancing", "network segmentation"), (), "implementing specialist", True),
    RoleDefinition("cloud-runtime-managed-services-engineer", "Cloud Runtime and Managed Services Engineer", "02 Cloud Foundation and Infrastructure", "Compute, serverless, storage, managed data services, caches, queues, streams, and runtime service infrastructure.", ("managed runtime infrastructure", "service selection criteria", "runtime lifecycle handoffs"), (), "implementing specialist", True),
    RoleDefinition("ci-cd-engineer", "CI/CD Engineer", "03 CI/CD and Release Engineering", "Build automation, test stages, pipeline architecture, caching, artifacts, quality gates, and CI/CD platform configuration.", ("pipeline architecture", "quality gates", "artifact flow"), (), "implementing specialist", True),
    RoleDefinition("release-and-deployment-engineer", "Release and Deployment Engineer", "03 CI/CD and Release Engineering", "Versioning, promotion, deployment strategy design, release readiness, rollback, feature flags, and release evidence.", ("release strategy", "promotion controls", "rollback evidence"), (), "implementing specialist", True),
    RoleDefinition("container-and-orchestration-engineer", "Container and Orchestration Engineer", "04 Containers and Platform Engineering", "OCI images, Docker, Compose, Kubernetes, Helm, Kustomize, registries, and workload standards.", ("container standards", "Kubernetes workload design", "registry patterns"), (), "implementing specialist", True),
    RoleDefinition("platform-product-and-developer-experience-engineer", "Platform Product and Developer Experience Engineer", "04 Containers and Platform Engineering", "Internal developer platforms, catalogs, portals, golden paths, self-service contracts, and developer experience.", ("platform product model", "service catalog", "golden paths"), (), "implementing specialist", True),
    RoleDefinition("site-reliability-engineer", "Site Reliability Engineer", "05 SRE, Observability, and Operations", "SLIs, SLOs, error budgets, operational readiness, incident practice, postmortems, and toil reduction.", ("SLOs", "error budgets", "operational readiness"), (), "implementing specialist", True),
    RoleDefinition("observability-engineer", "Observability Engineer", "05 SRE, Observability, and Operations", "Telemetry architecture, metrics, logs, traces, dashboards, alerts, retention, and observability data quality.", ("telemetry architecture", "dashboard and alert design", "observability data quality"), (), "implementing specialist", True),
    RoleDefinition("resilience-and-disaster-recovery-engineer", "Resilience and Disaster Recovery Engineer", "06 Resilience and Disaster Recovery", "Availability patterns, backup, restore, RTO, RPO, DR, failover, failback, and chaos-experiment design.", ("resilience design", "DR strategy", "recovery evidence"), (), "implementing specialist", True),
    RoleDefinition("performance-and-capacity-engineer", "Performance and Capacity Engineer", "07 Performance, Capacity, and Efficiency", "Performance requirements, workload models, load-test plans, capacity, autoscaling, and resource efficiency.", ("performance model", "capacity plan", "autoscaling strategy"), (), "implementing specialist", True),
    RoleDefinition("devsecops-engineer", "DevSecOps Engineer", "08 DevSecOps", "Secure delivery controls, pipeline security, security gate placement, findings routing, and remediation workflows.", ("secure delivery controls", "pipeline security", "finding remediation flow"), (), "implementing specialist", True),
    RoleDefinition("cloud-security-controls-engineer", "Cloud Security Controls Engineer", "08 DevSecOps", "Cloud IAM, secrets controls, policy as code, cloud hardening, and least-privilege DevOps patterns.", ("cloud IAM controls", "secrets control design", "policy as code"), (), "implementing specialist", True),
    RoleDefinition("software-supply-chain-security-engineer", "Software Supply Chain Security Engineer", "08 DevSecOps", "Dependency and artifact integrity, SBOM, provenance, signing design, verification, and build isolation.", ("SBOM and provenance", "artifact integrity", "supply-chain controls"), (), "implementing specialist", True),
    RoleDefinition("finops-engineer", "FinOps Engineer", "09 FinOps and Sustainability", "Cost visibility, allocation, forecasts, budgets, anomaly response, unit economics, rightsizing, and commitments.", ("cost allocation", "forecasting and budgets", "optimization recommendations"), (), "implementing specialist", True),
    RoleDefinition("cloud-sustainability-and-efficiency-analyst", "Cloud Sustainability and Efficiency Analyst", "09 FinOps and Sustainability", "Measured resource efficiency, sustainability analysis, carbon-aware tradeoffs, and evidence-based recommendations.", ("sustainability analysis", "resource-efficiency evidence", "carbon-aware tradeoffs"), (), "implementing specialist", True),
    RoleDefinition("devops-and-cloud-assurance-reviewer", "DevOps and Cloud Assurance Reviewer", "10 Assurance and Independent Review", "Independent review of DevOps and Cloud artifacts, evidence, ownership, waivers, and completion gates.", ("independent assurance", "finding classification", "completion gating"), (), "independent reviewer", False, True),
)


ROLE_BY_SLUG = {role.slug: role for role in ROLE_REGISTRY}

