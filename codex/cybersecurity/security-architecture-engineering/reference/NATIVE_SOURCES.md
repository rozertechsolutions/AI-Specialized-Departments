# Native Source Verification

Official sources checked on 2026-07-15:

- Codex manual: `https://developers.openai.com/codex/codex-manual.md`
- Codex customization guidance for `AGENTS.md`, custom agents, skills, MCP, hooks, approvals, sandboxing, and `config.toml` was checked through the manual.

## Decisions

- `AGENTS.md` is used for durable repository instructions.
- `.codex/config.toml` is used for conservative project settings.
- `.codex/agents/*.toml` is used for project custom agents.
- MCP, hooks, plugins, executable Skills, and external integrations are omitted because this static package must not connect tools or execute lifecycle automation.
