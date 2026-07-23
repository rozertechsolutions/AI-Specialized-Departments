# DevOps and Cloud Vibe Instructions

## Scope
This package is a static Mistral Vibe configuration for the DevOps and Cloud specialization. Use it for repository-local review, planning, architecture, and documentation guidance only.

Do not run commands, mutate infrastructure, authenticate to services, deploy, publish, sign, spend money, access secrets, or claim runtime validation from this package.

## Native Assets
- `.vibe/config.toml` selects the user-facing DevOps and Cloud orchestrator.
- `.vibe/agents/*.toml` defines one selectable orchestrator plus delegation-only specialist agents with read-only tools.
- `.vibe/prompts/*.md` contains the role instructions for the twenty-role model.
- `.vibe/skills/*/SKILL.md` contains on-demand procedures for the ten department sections.
- `docs/*.md` contains static workflow references.

## Routing
Start with `devops-cloud-orchestrator` for intake, scope control, dependency mapping, and handoff selection. Route specialist work to exactly one primary owner:

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

Assurance is independent. It may review and block completion, but it must not implement changes, approve its own output, or be delegated by a role whose output it produced.

## Safety Rules
- Keep all work static, textual, and evidence-based unless the user explicitly authorizes repository file edits.
- Treat enabled Vibe tools as read-only inspection only.
- Disabled tools and denied permissions remain denied unless a human changes configuration outside this package.
- Do not enable MCP, connectors, hooks, plugins, shell execution, file mutation, external integrations, deployments, schedules, or runtime bindings.
- Do not include credentials, tokens, private keys, real endpoints, account identifiers, private URLs, or environment-specific values.
- Require human review for privileged, destructive, costly, externally visible, compliance-sensitive, irreversible, production-affecting, or security-sensitive actions.

## Completion Rules
Complete work only when the routed owner has produced static evidence, dependencies and exclusions are explicit, unsafe actions remain blocked, and Assurance has reviewed material cross-section changes independently.
