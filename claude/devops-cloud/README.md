# DevOps and Cloud for Claude

This package is a manual/import-only DevOps and Cloud department for Claude Projects, project instructions, project knowledge, and Claude Skills where available. It covers DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance while staying static and safe by default.

The package is static and safe by default. The Claude implementation is a manual/import-only Claude package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

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

- `project/project-instructions.md`: Claude Project instructions for routing, boundaries, and completion.
- `project/knowledge/*.md`: ten section knowledge files for manual upload to Project knowledge.
- `skills/*/SKILL.md`: Agent Skill bundles for Claude surfaces that support Skills.
- No Claude Code files, hooks, MCP, connectors, or automatic repository-loading configuration is included.

## Installation and Setup

Create or open a Claude Project, set `project/project-instructions.md` as the Project instructions, and upload selected `project/knowledge/*.md` or Skill bundles as allowed by the current plan and workspace policy. Claude Projects do not automatically load this repository.

Keep connector setup absent unless a human configures it separately in Claude. Do not mix this package with Claude Code workspace files.

## Usage

Ask within the configured Claude Project for a specific section or role, such as "review the Terraform module using Cloud Foundation and Infrastructure." Use Skills for detailed section workflows where Skills are available.

Ask for Assurance only after a primary artifact exists. Treat all responses as static advice and not evidence that infrastructure, deployments, rollbacks, scans, or tests succeeded.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove the uploaded knowledge files, clear Project instructions, or remove imported Skills in Claude. Repository files remain unchanged.
