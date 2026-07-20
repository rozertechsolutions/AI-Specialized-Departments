# DevOps and Cloud for Cursor

This package is a repository-native DevOps and Cloud department for Cursor. It uses `AGENTS.md`, Cursor Project Rules, Agent Skills, and static workflow references to cover DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance safely by default.

The package is static and safe by default. The Cursor implementation is a repository-native Cursor package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

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

- `AGENTS.md`: concise persistent Cursor guidance.
- `.cursor/rules/*.mdc`: Project Rules with YAML frontmatter and explicit activation.
- `.cursor/skills/*/SKILL.md`: ten Agent Skills with valid `name` and `description` frontmatter.
- `docs/*-workflows.md`: static workflow references used by Skills.
- No Cursor cloud-agent setup, MCP, hooks, connector, or terminal automation is enabled.

## Installation and Setup

Place `cursor/devops-cloud/` contents at the root of the repository opened in Cursor so `AGENTS.md`, `.cursor/rules/`, `.cursor/skills/`, and `docs/` are available. Cursor workspace discovery depends on opening the repository in Cursor and on the user's product version and workspace settings.

This package installs no extension, dependency, plugin, MCP server, or provider configuration.

## Usage

Ask Cursor Agent for a section, such as "use the Performance, Capacity, and Efficiency Skill to review autoscaling risks." Project Rules provide routing and safety; Skills provide on-demand procedures; `docs/` files are supporting references.

Request Assurance only after a primary artifact exists. Do not treat static review output as proof that Cursor executed tests, scans, deployments, or infrastructure operations.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove this package's `AGENTS.md`, `.cursor/rules/`, `.cursor/skills/`, and referenced `docs/` files from the target repository. Preserve unrelated Cursor settings.
