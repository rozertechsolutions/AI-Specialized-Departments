# Web Development — Kilo Code

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- Concise root `AGENTS.md` pointer
- Kilo project config in `kilo.jsonc`
- Project rules in `.kilo/rules/*.md`
- Primary `web-development-lead` agent and specialist subagents in `.kilo/agents/*.md`
- Agent Skills in `.kilo/skills/*/SKILL.md`
- Slash-command workflows in `.kilo/commands/*.md`

## Intentionally omitted or disabled
- No legacy `.kilocodemodes` or `.kilocode/` formats
- No MCP configuration, hooks, plugins, provider keys, or external integrations
- No model is pinned

## Platform notes
This package targets the current Kilo Code VS Code and CLI surface and uses `.kilo/` plus `kilo.jsonc` rather than legacy configuration. The schema is `https://app.kilo.ai/config.json`. Commands select `web-development-lead` with `subtask: false`; the lead is a primary agent with an explicit `permission.task` allowlist for exact specialist subagents. Reviewer agents deny edit, bash, and task delegation. Implementation specialists deny bash and ask before edits.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://kilo.ai/docs/customize/custom-rules
- https://kilo.ai/docs/customize/custom-subagents
- https://kilo.ai/docs/customize/skills
- https://kilo.ai/docs/customize/agent-permissions
- https://kilo.ai/docs/automate/mcp/using-in-kilo-code
