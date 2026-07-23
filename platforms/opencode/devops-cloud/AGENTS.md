# DevOps and Cloud OpenCode Instructions

## Scope
This package is a static OpenCode configuration for the DevOps and Cloud specialization. Use it for repository-local planning, review, architecture, and guidance only.

Do not run commands, mutate files through OpenCode, authenticate to services, deploy, publish, sign, spend money, access secrets, or claim runtime validation from this package.

## Native Assets
- `opencode.jsonc` defines the default primary agent, specialist subagents, and least-privilege permissions.
- `.opencode/agents/*.md` contains role prompts for the complete twenty-role model.
- `.opencode/skills/*/SKILL.md` contains stable OpenCode Agent Skills for the ten department sections.
- `.opencode/commands/*.md` contains static workflow commands.

## Routing
Use `devops-cloud-orchestrator` as the default primary agent. Route specialist work to exactly one primary owner:

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

Assurance is independent. It may review and block completion, but must not implement the artifact under review, approve its own work, or silently rewrite specialist output.

## Safety
OpenCode permissions deny `edit`, `bash`, `webfetch`, `websearch`, and `external_directory` by default. Read, grep, glob, list, Skill loading, and orchestrator task delegation are the only enabled capabilities.

Do not enable plugins, MCP servers, hooks, custom tools, external integrations, schedules, deployments, or publication workflows. Human review is required for privileged, destructive, costly, externally visible, compliance-sensitive, irreversible, production-affecting, or security-sensitive actions.

## Completion
Complete only after the routed owner has produced static evidence, dependencies and exclusions are explicit, safety boundaries remain enforced, and material changes have independent Assurance review.
