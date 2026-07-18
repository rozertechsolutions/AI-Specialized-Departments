# Web Development - Claude Code

This directory is a project-scoped Claude Code Web Development specialization. Copy the contents of this directory to a target repository root only after review. Claude Code discovers `CLAUDE.md`, `.claude/agents/`, and `.claude/skills/` through its native project mechanisms.

## Native Components Included

| Component | Status |
| --- | --- |
| `CLAUDE.md` | Native project memory with concise orchestration and safety guidance. |
| `.claude/agents/web-development-lead.md` | Main-session coordinator with explicit `Agent(...)` allowlist and workflow Skill access. |
| `.claude/agents/*specialist*.md` | Native project subagents with least-privilege file tools and preloaded role Skills. |
| `.claude/skills/*/SKILL.md` | Native project Skills. Domain Skills are preloaded by agents; workflow Skills are available to the lead through `Skill(...)`. |
| `.claude/settings.json` | Omitted because no project setting is materially required. |
| `.mcp.json` | Omitted because no MCP server is required or configured. |
| Hooks | Omitted because this package must not add executable lifecycle scripts. |

## Delegation Model

1. Start with `web-development-lead` for coordinated work.
2. The lead runs discovery and architecture before implementation when material.
3. The lead delegates implementation only to `frontend-specialist`, `backend-api-specialist`, and `web-architecture-specialist` as appropriate.
4. Security/privacy and accessibility/performance/SEO reviewers run after relevant changes and remain read-only.
5. `quality-release-reviewer` runs last and issues the final evidence-based readiness verdict.
6. Specialist agents do not have the `Agent` tool, preventing recursive delegation.

## Safety Baseline

- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- No agent has Bash access.
- Review the files before trusting or copying them into a real project.

## Static Verification Checklist

- PASS: Lead can invoke only the exact approved specialists through `Agent(agent_type)`.
- PASS: Domain Skills are preloaded through agent `skills` fields, and workflow Skills are exposed through lead `Skill(...)` entries.
- PASS: Reviewers have only `Read`, `Grep`, and `Glob`; implementers have only file read/edit/write/search tools and no Bash.
- PASS: Empty `.mcp.json` and hook-disabling project settings are omitted.
- NOT EXECUTED: Runtime checks, builds, tests, browser checks, hook execution, MCP connections, Skill invocation, and live Claude Code loading.

## Official Documentation Baseline

Accessed July 18, 2026:

- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/slash-commands
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/mcp
