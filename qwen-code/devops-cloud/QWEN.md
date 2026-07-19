# DevOps and Cloud Qwen Code Instructions

## Scope
This package is a static Qwen Code configuration for the DevOps and Cloud specialization. Use it for repository-local planning, review, architecture, and guidance only.

Do not run commands, mutate files, authenticate to services, deploy, publish, sign, spend money, access secrets, or claim runtime validation from this package.

## Native Assets
- `.qwen/agents/*.md` contains twenty project subagents with current YAML frontmatter.
- `.qwen/skills/*/SKILL.md` contains stable Agent Skills for the ten department sections.
- `.qwen/commands/*.md` contains Markdown command workflows.
- `QWEN.md` provides persistent routing and safety guidance.

## Routing
Start with `devops-cloud-orchestrator` for intake, dependency control, and owner selection. Route specialist work to exactly one primary owner:

1. Leadership and Architecture: `devops-cloud-orchestrator`, `cloud-and-platform-architect`
2. Cloud Foundation and Infrastructure: `cloud-foundation-engineer`, `infrastructure-as-code-engineer`, `cloud-network-engineer`, `cloud-runtime-managed-services-engineer`
3. CI/CD and Release Engineering: `ci-cd-engineer`, `release-and-deployment-engineer`
4. Containers and Platform Engineering: `container-and-orchestration-engineer`, `platform-product-and-developer-experience-engineer`
5. SRE, Observability, and Operations: `site-reliability-engineer`, `observability-engineer`
6. Resilience and Disaster Recovery: `resilience-and-disaster-recovery-engineer`
7. Performance, Capacity, and Efficiency: `performance-and-capacity-engineer`
8. DevSecOps: `devsecops-engineer`, `cloud-security-controls-engineer`, `software-supply-chain-security-engineer`
9. FinOps and Sustainability: `finops-engineer`, `cloud-sustainability-and-efficiency-analyst`
10. Assurance and Independent Review: `devops-and-cloud-assurance-reviewer`

Assurance is independent. It may review and block completion, but it must not implement the artifact under review, approve its own work, or be part of a circular delegation path.

## Qwen Permission Boundary
Every subagent declares `approvalMode: plan`, read-only `tools`, and `disallowedTools` for `write_file`, `edit`, and `run_shell_command`.

Qwen Code documentation states that a permissive parent mode can override a subagent mode. This repository policy requires plan/read-only operation regardless of parent mode. Do not use auto-edit, auto, or yolo parent modes for this package.

## Safety
Do not enable MCP, hooks, extensions, scheduled tasks, channels, external integrations, shell execution, file mutation, deployments, signing, publication, spending, or infrastructure mutation. Human review is required for privileged, destructive, costly, externally visible, compliance-sensitive, irreversible, production-affecting, or security-sensitive actions.

## Completion
Complete only when the routed owner has produced static evidence, dependencies and exclusions are explicit, unsafe actions remain blocked, and material changes have independent Assurance review.
