# Web Development — Gemini CLI

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- GEMINI.md hierarchical project context
- Project custom commands in `.gemini/commands/`
- Project subagents in `.gemini/agents/`
- Project Agent Skills in `.gemini/skills/`

## Intentionally omitted or disabled
- No shell interpolation is used in commands
- No extensions, hooks or external tools
- No settings file is included because no non-empty project setting is required
- No MCP, A2A, remote agents, or hook automation is configured

## Platform notes
Every command is prompt-only TOML and passes user input through `{{args}}` as task context. Commands guide the root session but do not enforce approvals or perform execution by themselves. Local subagents are project-scoped specialists; implementation agents omit shell tools, and reviewers are read-only by tool selection. Users remain responsible for folder trust, approvals, and any runtime command execution. This package assumes the current Gemini CLI project surfaces documented in the official repository as of 2026-07-18.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html
- https://google-gemini.github.io/gemini-cli/docs/cli/custom-commands.html
- https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/subagents.md
- https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md
- https://google-gemini.github.io/gemini-cli/docs/cli/trusted-folders.html
- https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server.html
