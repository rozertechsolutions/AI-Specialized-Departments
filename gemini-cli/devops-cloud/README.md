# DevOps and Cloud for Gemini CLI

This package is a repository-native DevOps and Cloud department for Gemini CLI. It uses `GEMINI.md`, Gemini subagents, Agent Skills, and referenced workflows to cover DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance in static read-only form.

The package is static and safe by default. The Gemini CLI implementation is a repository-native Gemini CLI package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

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

- `GEMINI.md`: project instructions for Gemini CLI.
- `.gemini/agents/*.md`: twenty Markdown subagent profiles with YAML frontmatter.
- `.gemini/skills/*/SKILL.md`: ten Agent Skills.
- `docs/*.md`: referenced workflow support documents.
- No shell, mutation, MCP, connector, deployment, or runtime automation files are included.

## Installation and Setup

Place `gemini-cli/devops-cloud/` contents at the repository root opened by Gemini CLI. Keep `.gemini/`, `GEMINI.md`, `docs/`, and this README together so subagents and Skills can be discovered by the CLI version that supports them.

This package does not install Gemini CLI, models, authentication, dependencies, or external tools.

## Usage

Use Gemini CLI with a section request or select a subagent when appropriate, for example "ask the observability engineer to design alerts." Load the matching Skill for procedures and use `docs/` only as referenced support material.

Ask Assurance after primary work exists. Output remains static and advisory unless a human authorizes a separate command or change outside this package.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove `GEMINI.md`, `.gemini/`, and `docs/` files belonging to this package from the target repository. Leave unrelated Gemini CLI files intact.
