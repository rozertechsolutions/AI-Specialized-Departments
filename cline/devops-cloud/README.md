# DevOps and Cloud for Cline

This package is a repository-native DevOps and Cloud department for Cline. It uses Cline rules, Agent Skills, and manual workflows to cover DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance without enabling automation by default.

The package is static and safe by default. The Cline implementation is a repository-native Cline package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

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

- `.clinerules/*.md`: persistent Cline rules for section routing and safety.
- `.cline/skills/*/SKILL.md`: ten on-demand Agent Skills.
- `.cline/workflows/*.md`: manual workflow prompts for repeatable static procedures.
- No hooks, MCP, external integrations, runtime bindings, or unsupported subagent simulation is included.

## Installation and Setup

Place `cline/devops-cloud/` contents at the root of the repository opened by Cline so `.clinerules/` and `.cline/` remain in their discovery paths. The workspace must be opened in Cline; this package installs no extension, dependency, provider, or model.

Keep auto-approval and external integrations disabled unless a human configures them outside this package.

## Usage

Ask Cline for the relevant section or workflow, such as "use the Containers and Platform Engineering Skill to review Kubernetes manifests." Use rules for durable boundaries, Skills for detailed section procedures, and workflows only when manually requested.

Request Assurance after a primary plan or review exists. Static output must not be used as proof that Cline ran a command, changed infrastructure, or validated runtime behavior.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove `.clinerules/` entries and `.cline/skills/` or `.cline/workflows/` files for this package from the target repository. Leave unrelated Cline files intact.
