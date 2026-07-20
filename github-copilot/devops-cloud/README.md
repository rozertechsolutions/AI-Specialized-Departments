# DevOps and Cloud for GitHub Copilot

This package is a repository-native DevOps and Cloud department for GitHub Copilot surfaces that support repository instructions, coding-agent custom agents, and Agent Skills. It covers DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance while documenting stable surface limitations.

The package is static and safe by default. The GitHub Copilot implementation is a repository-native GitHub Copilot package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

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

- `.github/copilot-instructions.md`: repository-wide Copilot instructions.
- `.github/instructions/*.instructions.md`: scoped custom instruction files.
- `.github/agents/*.agent.md`: twenty Copilot coding-agent custom agents.
- `.github/skills/*/SKILL.md`: ten Agent Skills for Copilot surfaces that support skills.
- No prompt files, MCP, hooks, actions workflows, secrets, or external integrations are included.

## Installation and Setup

Place `github-copilot/devops-cloud/` contents at the root of the GitHub repository. Repository custom instructions are used by supported Copilot experiences; coding-agent custom agents and Skills apply only on Copilot surfaces and plans where GitHub makes them available.

VS Code, Visual Studio, JetBrains, Eclipse, Xcode, GitHub.com coding agent, and Copilot CLI do not all expose the same customization features. Do not assume a file is active on a surface unless that surface documents support for it.

## Usage

Ask Copilot Chat or coding agent for a section, for example "use the DevOps and Cloud CI/CD agent to audit this workflow." Use instructions for broad guidance, custom agents for role-specific coding-agent tasks, and Skills for section procedures where supported.

Request Assurance after primary output exists. Static Copilot output does not prove that checks, deployments, rollbacks, scans, or cloud operations ran.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove this package's `.github/copilot-instructions.md`, `.github/instructions/`, `.github/agents/`, and `.github/skills/` entries from the target repository. Preserve unrelated GitHub workflow and Copilot files.
