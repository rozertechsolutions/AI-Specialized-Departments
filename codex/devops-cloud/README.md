# DevOps and Cloud for Codex

This package uses stable Codex repository customization surfaces: `AGENTS.md`, project `.codex/config.toml`, project custom agents in `.codex/agents/`, repo-scoped Skills in `.agents/skills/`, and static workflow references in `docs/`.

It is static and safe by default. The project config keeps the sandbox read-only, keeps web search disabled, and does not configure hooks, MCP servers, plugins, connectors, shell automation, deployment, signing, publication, billing changes, or external runtime bindings.

## Sections Covered

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

- `AGENTS.md`: concise persistent routing, safety, human-review, and completion guidance.
- `.codex/config.toml`: least-privilege project defaults for future Codex sessions.
- `.codex/agents/*.toml`: twenty read-only custom agent profiles with exclusive role ownership and stop conditions.
- `.agents/skills/*/SKILL.md`: ten on-demand section Skills that hold detailed procedures without bloating persistent context.
- `docs/*.md`: static workflow references for the Skills and specialist roles.

## Role Model

The package preserves the complete twenty-role DevOps and Cloud model through Codex custom agents. `devops_cloud_orchestrator` owns intake and routing; section specialists own architecture, infrastructure, delivery, platform, reliability, resilience, performance, DevSecOps, FinOps, and sustainability work; `devops_and_cloud_assurance_reviewer` performs independent non-implementing review.

## Safety Model

All work is design, review, planning, or documentation unless a future user explicitly authorizes a separate action. Human review is required for privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, irreversible, signing, spending, or publication decisions. Static inspection must not be described as runtime validation.
