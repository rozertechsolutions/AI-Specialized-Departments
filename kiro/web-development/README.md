# Web Development — Kiro

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- Steering files
- Custom agents
- Agent Skills

## Intentionally omitted or disabled
- Agent hooks are omitted
- No command hooks or external integrations
- No MCP settings, powers, shell access, wildcard tools, or broad built-in access
- No model is pinned

## Platform notes
Always-loaded steering establishes the department rules and quality gates. Skills in `.kiro/skills/*/SKILL.md` provide on-demand procedures. The lead agent has `read`, `write`, and `subagent`; implementation specialists have `read` and `write`; reviewers have `read` only. Kiro's `read` category includes file reading, directory listing, and searching, so no unsupported `grep` or `glob` tags are used.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://kiro.dev/docs/custom-agents/
- https://kiro.dev/docs/chat/subagents/
- https://kiro.dev/docs/skills/
- https://kiro.dev/docs/powers/create/
- https://kiro.dev/docs/autonomous-agent/sandbox/mcp/
