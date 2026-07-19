# DevOps and Cloud for GitHub Copilot

This package uses stable GitHub Copilot customization surfaces: repository custom instructions, scoped `.instructions.md`, custom agents in `.github/agents/`, and Agent Skills in `.github/skills/`.

It is static and safe by default. It does not configure MCP, hooks, prompt files, cloud agent automation, external integrations, terminal automation, deployment, signing, publication, billing changes, or runtime bindings. Prompt files are intentionally absent because Copilot prompt files are public preview.

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

- `.github/copilot-instructions.md`: concise repository guidance.
- `.github/instructions/devops-cloud-leadership-architecture.instructions.md`: scoped routing and safety guidance.
- `.github/agents/*.agent.md`: twenty custom agents with YAML frontmatter and read/search tools.
- `.github/skills/*/SKILL.md`: ten on-demand section Skills.

## Role Model

The complete twenty-role DevOps and Cloud model is represented through custom agents and Skills. Each role has exclusive ownership and static review or planning boundaries. Assurance is independent, non-implementing, and cannot self-review.

## Safety Model

All outputs are design, review, planning, or documentation unless a future user explicitly authorizes separate action. Human review is required for privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, irreversible, signing, spending, or publication decisions. Static inspection must not be described as runtime validation.
