# Web Development — Codex

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- Root session orchestration instructions in `AGENTS.md`
- Direct specialist custom agents in `.codex/agents/`
- On-demand Agent Skills in `.agents/skills/`
- Project agent concurrency and depth configuration in `.codex/config.toml`

## Intentionally omitted or disabled
- Hooks are omitted because executable automation is not safe by default
- MCP servers are not configured
- Models and providers are inherited

## Platform notes
Copy the contents to the target repository root. The root Codex session coordinates the package and may request specialist agents directly. `agents.max_depth = 1` is intentional: it allows the root session to use specialist agents while preventing nested coordinator patterns. The architecture, frontend, and backend specialists use workspace-write sandbox intent only for approved implementation work; independent reviewers are read-only. Parent approval and sandbox controls still apply.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://developers.openai.com/codex/agent-configuration/agents-md
- https://developers.openai.com/codex/subagents
- https://developers.openai.com/codex/skills
- https://developers.openai.com/codex/config-basic
- https://developers.openai.com/codex/hooks
