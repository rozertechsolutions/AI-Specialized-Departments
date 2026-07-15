# Native Configuration Sources

Official sources checked on 2026-07-15:

- Cline Config: `https://docs.cline.bot/getting-started/config`.
- Cline Rules: `https://docs.cline.bot/customization/cline-rules`.
- Cline Skills: `https://docs.cline.bot/customization/skills`.
- Cline Subagents: `https://docs.cline.bot/features/subagents`.
- Cline Hooks: `https://docs.cline.bot/customization/hooks`.
- Cline `.clineignore`: `https://docs.cline.bot/customization/clineignore`.

## Current native surface

Cline supports project configuration under `.cline/`, including project rules, skills, hooks, agents, plugins, and cron specs. Rules provide persistent instructions. Skills are directories with required `SKILL.md` files and YAML frontmatter. Subagents are experimental read-only research agents that cannot edit files, access MCP servers, use the browser, or spawn nested subagents.

## Implementation decision

This package uses project rules and project Skills only. Hooks and plugins are omitted because they can execute code. MCP and connectors are omitted because this area must not connect external systems. Project agent definitions are omitted because the stable role behavior needed here is covered by rules and Skills, while documented subagents are read-only research behavior rather than persistent production role files.

