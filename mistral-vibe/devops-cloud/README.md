# DevOps and Cloud for Mistral Vibe

This package is a repository-native DevOps and Cloud department for Mistral Vibe. It uses Vibe TOML configuration, selectable agents, prompt files, Agent Skills, and static workflow references to cover DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance.

The package is static and safe by default. The Mistral Vibe implementation is a repository-native Mistral Vibe package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

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

- `AGENTS.md`: package guidance and safety boundaries.
- `.vibe/config.toml`: Vibe project configuration and default user-facing agent selection.
- `.vibe/agents/*.toml`: one orchestrator plus specialist agent configurations.
- `.vibe/prompts/*.md`: twenty role prompts referenced by agent configs.
- `.vibe/skills/*/SKILL.md`: ten Agent Skills.
- `docs/*.md`: referenced static workflow support documents.

## Installation and Setup

Place `mistral-vibe/devops-cloud/` contents at the repository root used by Mistral Vibe. Keep `.vibe/config.toml`, `.vibe/agents/`, `.vibe/prompts/`, `.vibe/skills/`, `AGENTS.md`, and `docs/` together so prompt references resolve.

This package does not install Vibe, configure credentials, enable MCP, connect providers, or start external integrations.

## Usage

Select the DevOps Cloud orchestrator or a specialist agent in Vibe, then ask for a section, such as "review this Argo CD promotion model." Agents provide role behavior, Skills provide procedures, and docs provide static references.

Use Assurance only after primary work exists. Treat `safety` metadata as documentation, not proof of enforcement by itself.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove `.vibe/`, `AGENTS.md`, and `docs/` files belonging to this package from the target repository, or select another Vibe agent/config outside this package.
