# DevOps and Cloud for OpenCode

This package is a repository-native DevOps and Cloud department for OpenCode. It uses `opencode.jsonc`, project agents, Agent Skills, commands, and `AGENTS.md` to cover DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance with read-only static defaults.

The package is static and safe by default. The OpenCode implementation is a repository-native OpenCode package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

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

- `AGENTS.md`: package-level routing and safety guidance.
- `opencode.jsonc`: OpenCode configuration, default agent, modes, permissions, and references.
- `.opencode/agents/*.md`: twenty role prompt files.
- `.opencode/skills/*/SKILL.md`: ten Agent Skills.
- `.opencode/commands/*.md`: manual static workflow commands.
- No plugins, MCP servers, hooks, external integrations, or credentials are included.

## Installation and Setup

Place `opencode/devops-cloud/` contents at the repository root opened by OpenCode. Keep `opencode.jsonc`, `.opencode/`, and `AGENTS.md` together so referenced agents, commands, and Skills resolve.

This package does not install OpenCode, providers, dependencies, models, or credentials.

## Usage

Use the default DevOps Cloud orchestrator or choose a specialist agent, then request a section such as "audit the Helm chart with Containers and Platform Engineering." Commands are manual prompts, Skills provide procedures, and permissions keep package behavior static.

Ask Assurance only after primary work exists. Static output is not runtime proof.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove `opencode.jsonc`, `AGENTS.md`, and `.opencode/` entries belonging to this package from the target repository. Preserve unrelated OpenCode assets.
