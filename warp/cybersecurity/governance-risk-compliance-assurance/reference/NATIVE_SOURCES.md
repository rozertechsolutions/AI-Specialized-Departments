# Native Configuration Sources

These official sources define the native Warp mechanisms used by this package. Review them again before installation because product behavior can change.

- `https://docs.warp.dev/agent-platform/capabilities/rules/`
- `https://docs.warp.dev/agent-platform/capabilities/skills/`
- `https://docs.warp.dev/agent-platform/agent-context/model-context-protocol-mcp/`
- `https://docs.warp.dev/agent-platform/capabilities/profiles-and-permissions/`
- `https://docs.warp.dev/oz/quickstart/scheduled-agents/`
- `https://docs.warp.dev/oz/quickstart/integrations/`

## Decisions

- `AGENTS.md` is used because Warp project rules use `AGENTS.md` by default.
- `.warp/skills/*/SKILL.md` is used because Warp scans supported project Skill directories, including `.warp/skills/`.
- `.warp/.mcp.json` is omitted because no approved project MCP server is needed for this static package.
- Cloud schedules, integrations, profiles, executable hooks, and external automations are omitted because they are not static repository-local governance artifacts for this package.
