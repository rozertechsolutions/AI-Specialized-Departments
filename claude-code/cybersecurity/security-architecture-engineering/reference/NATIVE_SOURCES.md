# Native Source Verification

Official sources checked on 2026-07-15:

- Claude Code settings and project scope: `https://code.claude.com/docs/en/settings`
- Claude Code subagents: `https://code.claude.com/docs/en/sub-agents`
- Claude Code Skills: `https://code.claude.com/docs/en/skills`
- Claude Code MCP: `https://code.claude.com/docs/en/mcp`

## Decisions

- `CLAUDE.md` is used for repository instructions.
- `.claude/agents/*.md` is used for project subagents.
- `.claude/skills/*/SKILL.md` is used for project Skills.
- MCP, hooks, and executable settings are omitted because this package is static and must not connect tools or run lifecycle automation.
