# Native Source Verification

Official sources checked on 2026-07-15:

- Cline Rules: `https://docs.cline.bot/customization/cline-rules`
- Cline Skills: `https://docs.cline.bot/customization/skills`
- Cline Subagents: `https://docs.cline.bot/features/subagents`
- Cline configuration documentation: `https://docs.cline.bot/configuration`

## Decisions

- Workspace rules are represented in `.clinerules/`.
- Reusable procedures are represented as `.cline/skills/*/SKILL.md`.
- Separate subagent files, hooks, MCP, scheduled work, and external integrations are omitted because this static package does not require them and must not execute or connect anything.

