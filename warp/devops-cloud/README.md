# DevOps and Cloud for Warp

This package is a static DevOps and Cloud department for Warp using project rules in `AGENTS.md`, Agent Skills, and referenced workflow documents. It covers DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance without configuring Warp cloud agents, schedules, triggers, environments, or integrations.

The package is static and safe by default. The Warp implementation is a manual/repository-guidance Warp package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

## Possible Uses

- Designing a cloud target architecture.
- Reviewing landing zones and environment separation.
- Designing or auditing IaC.
- Designing Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, Argo CD, or Flux workflows.
- Designing Docker, OCI, Kubernetes, Helm, and Kustomize configurations.
- Creating SLI, SLO, error-budget, alerting, and observability plans.
- Preparing incident, rollback, backup, restore, RTO, RPO, and disaster-recovery plans.
- Reviewing performance, capacity, scaling, and resource efficiency.
- Performing static DevSecOps and software supply-chain reviews.
- Performing FinOps, cost allocation, forecasting, rightsizing, and sustainability analysis.
- Performing independent operational-readiness and assurance reviews.

## Department Coverage

1. Leadership and Architecture.
2. Cloud Foundation and Infrastructure.
3. CI/CD and Release Engineering.
4. Containers and Platform Engineering.
5. SRE, Observability, and Operations.
6. Resilience and Disaster Recovery.
7. Performance, Capacity, and Efficiency.
8. DevSecOps.
9. FinOps and Sustainability.
10. Assurance and Independent Review.

## Native Assets

- `AGENTS.md`: Warp project rule guidance for routing and safety.
- `.agents/skills/*/SKILL.md`: ten Agent Skills.
- `docs/*-workflows.md`: static workflow references used by Skills.
- No repository-native Warp agent profiles, MCP, cloud-agent execution, schedules, triggers, environments, or connector configuration is included.

## Installation and Setup

Place `warp/devops-cloud/` contents in the repository you open from Warp. Use `AGENTS.md` as project guidance and keep `.agents/skills/` and `docs/` available for agents that support local Agent Skills.

Warp account, UI, and workspace settings may control which rules, Skills, and agent features are available. This repository package installs no Warp integration or runtime permission profile.

## Usage

Ask Warp Agent for a section, such as "use FinOps and Sustainability to review cost allocation." Load the matching Skill for procedure detail and use `docs/` only as referenced support.

Ask Assurance after primary work exists. Do not use this package as evidence that Warp executed commands, cloud agents, schedules, or integrations.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove `AGENTS.md`, `.agents/skills/`, and this package's `docs/` files from the target repository or stop referencing them in Warp. Account-scoped Warp settings must be changed in Warp, not in this repository.
