# Web Development — OpenCode

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- AGENTS.md instructions
- Project configuration with disabled sharing and current `permission` rules
- Custom agents
- Agent Skills
- Custom commands

## Intentionally omitted or disabled
- No MCP, plugins or custom tools
- No model is pinned
- Bash, web fetch/search, external directories and MCP-style integrations are denied
- Editing is denied globally and allowed only by primary lead or implementation specialists through agent permission overrides

## Platform notes
Verified against OpenCode docs last updated July 17, 2026 and accessed on 2026-07-18. OpenCode uses `AGENTS.md` for project rules, `.opencode/agents/*.md` for Markdown agents, `.opencode/commands/*.md` for custom slash commands, `.opencode/skills/*/SKILL.md` for Agent Skills, and `permission` for current approval policy.

`web-development-lead` is the only primary custom agent. Commands target that primary agent with `subtask: false` so the lead keeps coordinator context. The lead may invoke only the approved specialist subagents through the native `task` permission allow-list. Reviewer agents deny edits, bash, external directories, web fetch/search and nested task delegation.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://opencode.ai/docs/rules/
- https://opencode.ai/docs/agents/
- https://opencode.ai/docs/skills/
- https://opencode.ai/docs/commands/
- https://opencode.ai/docs/permissions/
- https://opencode.ai/docs/config/
