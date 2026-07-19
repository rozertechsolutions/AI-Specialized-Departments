# DevOps and Cloud for Claude Code

This package uses stable Claude Code project surfaces for a static DevOps and Cloud specialization. It does not enable hooks, MCP, shell execution, external integrations, deployment, or runtime validation.

## Native Surfaces

- `CLAUDE.md`: concise department routing and safety rules.
- `.claude/settings.json`: project settings with plan mode, bypass prevention, and deny rules for shell, mutation, web, MCP, and sensitive reads.
- `.claude/agents/*.md`: twenty native subagents covering the complete role model.
- `.claude/skills/*/SKILL.md`: on-demand Skills for the ten sections.
- `docs/*.md`: section workflow references.

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

## Role Model

The package includes twenty role subagents. Each role defines mission, ownership, inputs, outputs, permissions, handoffs, stop conditions, failure behavior, completion criteria, human-review boundaries, and prohibited actions. The Assurance Reviewer is independent and may block completion but must not self-review or silently rewrite specialist output.

## Safety

All work is static source review, design, or planning. The project settings deny shell, mutation, web, MCP, and sensitive-file access by default. Human review is required for privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, or irreversible decisions.
