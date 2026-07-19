# DevOps and Cloud for Kilo Code

This package provides a static Kilo Code configuration for the complete DevOps and Cloud specialization. It uses current Kilo project instructions, Markdown agents, Agent Skills, and project rules without enabling execution, hooks, MCP, plugins, cloud integrations, or deployment automation.

## Native Assets
- `kilo.jsonc`: project configuration with the current schema URL, `instructions`, and singular `permission` defaults.
- `AGENTS.md`: concise persistent routing and safety guidance.
- `.kilo/agents/*.md`: twenty Kilo Markdown agents with native `mode` and `permission` frontmatter.
- `.kilo/skills/*/SKILL.md`: ten on-demand Agent Skills, one per department section.
- `.kilo/rules/*.md`: compact project rules referenced from `kilo.jsonc`.
- `docs/*.md`: static workflow references used by the Skills and agents.

## Department Coverage
1. Leadership and Architecture
2. Cloud Foundation and Infrastructure
3. CI/CD and Release Engineering
4. Containers and Platform Engineering
5. SRE, Observability, and Operations
6. Resilience and Disaster Recovery
7. Performance, Capacity, and Efficiency
8. DevSecOps
9. FinOps and Sustainability
10. Assurance and Independent Review

## Agent Model
`devops-cloud-orchestrator` is the primary routing agent. The remaining specialist roles are configured as subagents with read-only permissions and no shell, mutation, web, or external execution access. The orchestrator may request delegated specialist review through Kilo's `task` permission, while specialists and Assurance are not allowed to delegate in ways that create cycles.

The three FinOps, Sustainability, and Assurance profiles include complete native frontmatter rather than copied metadata. All profiles use Kilo `permission` mappings instead of foreign `tools` declarations.

## Safety Model
The package denies shell and unsafe mutation by default. Agent permissions allow only repository-local read/search/skill discovery capabilities unless human approval is required by Kilo for a delegated task. No platform agent is authorized to deploy, publish, sign, spend, mutate infrastructure, run scanners, execute cloud tools, authenticate to services, or claim runtime validation.

Human review is required before privileged, destructive, costly, externally visible, compliance-sensitive, or irreversible actions.

## Stable-Only Scope
This package does not use legacy `.kilocodemodes`, deprecated orchestrator modes, MCP servers, plugins, hooks, external integrations, hosted execution, schedules, or generated runtime bindings. Long-lived detail is kept in Skills and static workflow references rather than oversized persistent instructions.
