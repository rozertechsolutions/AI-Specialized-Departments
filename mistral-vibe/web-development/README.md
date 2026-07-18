# Web Development — Mistral Vibe

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- Project `AGENTS.md` instructions, loaded only from trusted project folders
- Project Skills in `.vibe/skills/`, exposed as slash commands with `user-invocable: true`
- Project custom agents in `.vibe/agents/*.toml`
- Project custom agent prompts in `.vibe/prompts/*.md`

## Intentionally omitted or disabled
- MCP servers, connectors, custom executable tools, and hooks are not configured
- Shell execution is disabled in the project agents
- No provider or model is pinned

## Platform notes
Verified against Mistral Vibe 2.21.0 documentation, changelog, and package metadata accessed on 2026-07-18. Vibe loads project-level configuration only from trusted folders. This package is intended to be copied to a project root and reviewed before that project is trusted.

Vibe receives the department through project `AGENTS.md`, project Skills, and project custom agents. Skills are instruction-only workflows or review procedures; they do not execute commands by themselves. Custom agents are project-scoped and avoid `active_model`, provider authentication, MCP, connectors, executable hooks, custom tools, telemetry settings, and endpoint configuration.

Tool-name documentation is not perfectly consistent between the current hosted docs and the package README. Agent and Skill allow-lists include the documented read/search names used across those sources while explicitly disabling write and shell tools for reviewers. Hooks are stable in Vibe 2.21.0 but are intentionally omitted here because they execute around tool calls.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- Mistral Docs, "Agents": https://docs.mistral.ai/vibe/code/cli/agents
- Mistral Docs, "Skills": https://docs.mistral.ai/vibe/code/cli/skills
- Mistral Docs, "Safety, approvals, and permissions": https://docs.mistral.ai/vibe/code/safety-approvals-permissions
- Mistral Docs, "Commands and shortcuts": https://docs.mistral.ai/vibe/code/cli/commands-shortcuts
- Mistral AI GitHub repository README: https://github.com/mistralai/mistral-vibe
- Mistral AI GitHub changelog: https://github.com/mistralai/mistral-vibe/blob/main/CHANGELOG.md
- PyPI package metadata for stable release 2.21.0: https://pypi.org/project/mistral-vibe/
