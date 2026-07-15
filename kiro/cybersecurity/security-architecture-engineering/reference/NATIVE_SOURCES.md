# Native Kiro Sources

Official Kiro documentation checked on 2026-07-15:

- Kiro documentation: `https://kiro.dev/docs/`
- Steering: `https://kiro.dev/docs/steering/`
- Skills: `https://kiro.dev/docs/skills/`
- Specs: `https://kiro.dev/docs/specs/`
- Hooks: `https://kiro.dev/docs/hooks/`
- MCP: `https://kiro.dev/docs/mcp/`
- CLI custom agents: `https://kiro.dev/docs/cli/custom-agents/`

Implementation decision: use `AGENTS.md`, `.kiro/steering/*.md`, `.kiro/agents/*.json`, and `.kiro/skills/*/SKILL.md`. Omit hooks, MCP servers, Specs, Powers, executable scripts, external integrations, authentication, scans, deployment, publication, and live-system actions because this package is static guidance only.
