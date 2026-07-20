# DevOps and Cloud for Claude Code

This package is a repository-native DevOps and Cloud department for Claude Code. It uses project memory, settings, custom subagents, Agent Skills, and static support documents to cover DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance in a static safe-by-default form.

The package is static and safe by default. The Claude Code implementation is a repository-native Claude Code package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

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

- `CLAUDE.md`: project instructions loaded as Claude Code context.
- `.claude/settings.json`: project settings and permission denials.
- `.claude/agents/*.md`: twenty project subagents with YAML frontmatter.
- `.claude/skills/*/SKILL.md`: ten section Agent Skills.
- `docs/*.md`: referenced static workflow documents; they are support material, not automatic execution.

## Installation and Setup

Place `claude-code/devops-cloud/` contents at the root of the repository that Claude Code opens, preserving `.claude/`, `CLAUDE.md`, `docs/`, and this README. Open the workspace with Claude Code and review or trust the workspace according to local policy.

No plugin, MCP server, dependency, connector, hook, or cloud credential is installed by this package.

## Usage

Begin with the DevOps and Cloud orchestrator subagent for intake and routing, then invoke a specialist subagent or Skill for a section, for example "use the release and deployment engineer for rollback design." Use `docs/` only through the Skill or agent references that name those files.

Invoke the Assurance reviewer only after primary work exists. Generated content is advisory unless a human separately authorizes repository edits or runtime commands outside this package.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Delete or move `CLAUDE.md`, `.claude/`, and `docs/` from the target repository, or remove selected subagents/Skills. Do not remove unrelated Claude Code configuration.
