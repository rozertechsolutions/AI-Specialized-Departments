# DevOps and Cloud for Kiro IDE

This package provides a static Kiro IDE configuration for the complete DevOps and Cloud specialization. It uses only workspace `AGENTS.md`, Kiro steering, Kiro Markdown custom agents, and workspace Agent Skills.

## Native Assets
- `AGENTS.md`: always-included workspace guidance for routing, safety, native asset discovery, and assurance independence.
- `.kiro/steering/*.md`: concise steering with current Kiro inclusion frontmatter.
- `.kiro/agents/*.md`: twenty workspace custom agents using IDE Markdown frontmatter, read-only tool tags, `includeMcpJson: false`, and explicit shell/sensitive-file denials.
- `.kiro/skills/*/SKILL.md`: ten Agent Skills, one per department section.
- `docs/*-workflows.md`: static workflow references.

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
The `devops-cloud-orchestrator` agent is the routing entry point and has `read`, `context`, and `subagent` tags. Specialist and Assurance agents have `read` and `context` tags only. No agent includes `write`, `shell`, `web`, `@mcp`, `@builtin`, `*`, or inline `mcpServers`.

Skills are workspace-level assets that Kiro can activate by description or users can invoke directly as slash commands. Detailed procedures live in `.kiro/skills/` and `docs/`, while steering remains concise.

## Safety Model
All output is static guidance or review. The package does not run tools, authenticate, mutate files or infrastructure, deploy, publish, sign, spend, scan, execute hooks, use MCP, or claim runtime validation.

Human review is required before privileged, destructive, costly, externally visible, compliance-sensitive, or irreversible actions.

## Stable-Only Scope
This package intentionally excludes Kiro CLI JSON agents, hooks, powers, MCP servers, external integrations, executable specs, schedules, and hosted automation. It uses the Kiro IDE Markdown custom-agent surface consistently and does not mix IDE and CLI schemas.
