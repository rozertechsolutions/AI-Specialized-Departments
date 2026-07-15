# Native Configuration Sources

Official sources checked on 2026-07-15:

- Claude Code settings: `https://code.claude.com/docs/en/settings`.
- Claude Code subagents: `https://code.claude.com/docs/en/sub-agents`.
- Claude Code skills: `https://code.claude.com/docs/en/skills`.
- Claude Code MCP: `https://code.claude.com/docs/en/mcp`.

## Current native surface

Claude Code supports project memory through `CLAUDE.md` or `.claude/CLAUDE.md`, project subagents in `.claude/agents/`, project Skills in `.claude/skills/<skill-name>/SKILL.md`, project settings in `.claude/settings.json`, hooks through settings, and project MCP servers through `.mcp.json`.

## Implementation decision

This package uses project memory, project subagents, and project Skills. It omits hooks because lifecycle commands would create executable behavior. It omits `.mcp.json` because this area must not connect external tools, and project MCP servers require user approval before use. It omits settings because no permission widening or tool configuration is required for the static package.

