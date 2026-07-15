# Native Junie Sources

Official Junie documentation checked on 2026-07-15:

- Guidelines and memory: `https://junie.jetbrains.com/docs/guidelines-and-memory.html`
- Custom subagents: `https://junie.jetbrains.com/docs/junie-cli-subagents.html`
- Agent skills: `https://junie.jetbrains.com/docs/agent-skills.html`
- Custom slash commands: `https://junie.jetbrains.com/docs/custom-slash-commands.html`
- Hooks: `https://junie.jetbrains.com/docs/junie-cli-hooks.html`
- MCP configuration: `https://junie.jetbrains.com/docs/junie-cli-mcp-configuration.html`

Implementation decision: use `.junie/AGENTS.md`, `.junie/config.json`, `.junie/agents/*.md`, `.junie/skills/*/SKILL.md`, and `.junie/commands/*.md`. Omit MCP servers, hooks, executable scripts, external integrations, authentication, scans, deployment, publication, and live-system actions because this package is static guidance only.
