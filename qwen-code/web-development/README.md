# Web Development — Qwen Code

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- QWEN.md project context
- Project subagents in `.qwen/agents/`
- Project Agent Skills
- Project settings with bounded nested subagent depth

## Intentionally omitted or disabled
- Experimental agent teams are not enabled
- No hooks, extensions, MCP, channels, worktrees, providers, loops or scheduled tasks
- No model is pinned
- No auto-edit or yolo approval mode

## Platform notes
Verified against Qwen Code docs last updated July 2, 2026, the hooks page last updated July 7, 2026, and current weekly update navigation accessed on 2026-07-18. Qwen Code discovers project context from `QWEN.md`, project subagents from `.qwen/agents/`, project Skills from `.qwen/skills/`, and project settings from `.qwen/settings.json`.

This package uses a lead-subagent topology because the native `agent` tool supports subagent delegation and current weekly docs include nested subagents. `model.maxSubagentDepth` is set to exactly `2`: root session to `web-development-lead`, then lead to one approved specialist layer. The lead has the native `agent` tool and instructions limiting delegation to the six approved specialists. Specialists do not have the `agent` tool.

Only implemented subagent frontmatter fields are used: `name`, `description`, `model`, `approvalMode`, `tools`, and `disallowedTools`. Planned declarative-agent fields such as `effort`, `memory`, `initialPrompt`, `skills`, and `isolation` are omitted. Hooks are omitted because hook commands are executable and documented per-agent hooks have v1 global firing limitations while an agent is running.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://qwenlm.github.io/qwen-code-docs/en/users/configuration/settings/
- https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/
- https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/
- https://qwenlm.github.io/qwen-code-docs/en/developers/tools/task/
- https://qwenlm.github.io/qwen-code-docs/en/users/features/hooks/
- https://qwenlm.github.io/qwen-code-docs/en/blog/
