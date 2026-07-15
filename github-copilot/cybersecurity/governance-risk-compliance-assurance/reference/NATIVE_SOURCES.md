# Native Source Summary

Official GitHub Docs checked on 2026-07-15:

- Adding repository custom instructions for GitHub Copilot: documents `.github/copilot-instructions.md`, path-specific `.instructions.md`, and `AGENTS.md`.
- Creating custom agents for Copilot cloud agent: documents `.github/agents/*.agent.md` agent profiles with YAML frontmatter, required `description`, tools, and behavioral instructions.
- Adding agent skills for GitHub Copilot: documents project skills under `.github/skills/<skill>/SKILL.md`, required `SKILL.md` name, YAML frontmatter, and skill activation.
- GitHub Copilot hooks documentation: documents `.github/hooks/*.json` hook configuration and shell command execution during agent sessions.
- Copilot CLI customization pages were checked to confirm related custom agents and Skills support across CLI-capable surfaces.

## Native Components Used

- `.github/copilot-instructions.md` for durable area guidance.
- `.github/agents/*.agent.md` for custom specialist agents.
- `.github/skills/*/SKILL.md` for project agent skills.

## Components Omitted

- Hooks are omitted because they execute shell commands during agent sessions.
- MCP servers and integrations are omitted because this area must not connect to external services or live evidence systems.
- Extensions, commands, scripts, and automations are omitted because Skills already cover the reusable workflows without execution.

