# DevOps and Cloud for Cursor

This package uses stable Cursor project customization surfaces: `AGENTS.md`, Project Rules in `.cursor/rules/`, Agent Skills in `.cursor/skills/`, and static workflow references in `docs/`.

It is static and safe by default. It does not configure MCP, hooks, cloud agents, external integrations, terminals, deployment, signing, publication, billing changes, or runtime bindings. Repository files are guidance, not permission grants.

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

- `AGENTS.md`: concise persistent Cursor guidance.
- `.cursor/rules/00-devops-cloud-leadership-architecture.mdc`: always-on routing and safety.
- `.cursor/rules/10-*.mdc` through `.cursor/rules/90-*.mdc`: agent-requested section rules with explicit frontmatter.
- `.cursor/skills/*/SKILL.md`: on-demand section procedures.
- `docs/*-workflows.md`: static workflow references for detailed steps.

## Role Model

The complete twenty-role model is represented through section rules and Agent Skills. Additional custom subagent files are intentionally omitted because they would duplicate the same ownership model without adding exclusive value in this static package. Assurance remains independent and non-implementing.

## Safety Model

All outputs are design, review, planning, or documentation unless a future user explicitly authorizes separate action. Human review is required for privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, irreversible, signing, spending, or publication decisions. Static inspection must not be described as runtime validation.
