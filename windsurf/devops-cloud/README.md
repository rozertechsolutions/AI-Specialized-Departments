# DevOps and Cloud for Windsurf

This package is a repository-native DevOps and Cloud department for Windsurf Cascade. It uses workspace rules, Agent Skills, manual workflows, and `AGENTS.md` to cover DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance safely by default.

The package is static and safe by default. The Windsurf implementation is a repository-native Windsurf package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

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
- `.windsurf/rules/*.md`: workspace rules with frontmatter and activation triggers.
- `.windsurf/skills/*/SKILL.md`: ten Agent Skills.
- `.windsurf/workflows/*.md`: manual slash-invoked workflow prompts.
- No hooks, MCP, external integrations, automatic workflow execution, deployments, or credentials are included.

## Installation and Setup

Place `windsurf/devops-cloud/` contents at the root of the workspace opened in Windsurf. Keep `.windsurf/rules/`, `.windsurf/skills/`, `.windsurf/workflows/`, and `AGENTS.md` together so workspace rules, Skills, and workflows resolve.

This package installs no extension, provider, model, dependency, or integration. Windsurf Code mode can edit and run commands, but this package's policy is static unless a human separately authorizes action.

## Usage

Ask Cascade for a section, for example "use CI/CD and Release Engineering to review this promotion workflow." Rules provide routing and safety, Skills provide detailed procedures, and workflows are manual prompts only.

Request Assurance after primary work exists. Static output is not proof of runtime validation, deployment, rollback, scan, or production state.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove this package's `AGENTS.md`, `.windsurf/rules/`, `.windsurf/skills/`, and `.windsurf/workflows/` entries from the target workspace. Preserve unrelated Windsurf files.
