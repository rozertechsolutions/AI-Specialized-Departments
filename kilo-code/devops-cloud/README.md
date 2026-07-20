# DevOps and Cloud for Kilo Code

This package is a repository-native DevOps and Cloud department for Kilo Code. It uses `kilo.jsonc`, Kilo agents, Agent Skills, project rules, and workflow references to cover DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance with safe static defaults.

The package is static and safe by default. The Kilo Code implementation is a repository-native Kilo Code package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

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

- `AGENTS.md`: package-level guidance.
- `kilo.jsonc`: Kilo project configuration and referenced rules/Skills.
- `.kilo/agents/*.md`: twenty Kilo role agents with mode and permission frontmatter.
- `.kilo/skills/*/SKILL.md`: ten Agent Skills.
- `.kilo/rules/*.md` and `docs/*.md`: persistent rules and referenced static workflows.

## Installation and Setup

Place `kilo-code/devops-cloud/` contents at the root of the repository opened by Kilo Code. Keep `kilo.jsonc`, `.kilo/`, `AGENTS.md`, and `docs/` together so referenced paths resolve.

This package does not install Kilo Code, providers, models, MCP servers, dependencies, or credentials.

## Usage

Use the configured DevOps Cloud orchestrator for intake or request a specific section, for example "route this to the FinOps engineer." Agents provide role prompts, Skills provide section procedures, and rules keep static safety boundaries.

Use Assurance after primary work exists. Static output is not proof of runtime validation or production state.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove `kilo.jsonc`, `AGENTS.md`, `.kilo/`, and `docs/` entries belonging to this package from the target repository. Preserve unrelated Kilo configuration.
