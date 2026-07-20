# DevOps and Cloud for Qwen Code

This package is a repository-native DevOps and Cloud department for Qwen Code. It uses `QWEN.md`, Qwen subagents, Agent Skills, and commands to cover DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance with plan-mode read-only defaults.

The package is static and safe by default. The Qwen Code implementation is a repository-native Qwen Code package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

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

- `QWEN.md`: project guidance and parent permission caveats.
- `.qwen/agents/*.md`: twenty subagent profiles with YAML frontmatter.
- `.qwen/skills/*/SKILL.md`: ten Agent Skills.
- `.qwen/commands/*.md`: manual static command prompts.
- No MCP, shell automation, write tools, external integrations, or credentials are included.

## Installation and Setup

Place `qwen-code/devops-cloud/` contents at the repository root opened by Qwen Code. Keep `QWEN.md` and `.qwen/` together so agents, commands, and Skills can be discovered by versions that support those features.

This package does not install Qwen Code, configure models, providers, credentials, or global approval modes. Parent-session permissive settings can still affect behavior, so keep the parent session in a safe approval mode.

## Usage

Ask Qwen Code for a section or select a subagent, for example "use the Site Reliability Engineer to review error-budget policy." Use commands only when manually requested and Skills for detailed procedures.

Use Assurance only after primary work exists. Generated output remains static unless separately authorized outside this package.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove `QWEN.md` and `.qwen/` entries belonging to this package from the target repository. Preserve unrelated Qwen Code configuration.
