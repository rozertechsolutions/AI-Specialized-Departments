# Web Development — Warp / Oz

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- AGENTS.md project instructions
- Project Agent Skills in `.agents/skills/`

## Intentionally omitted or disabled
- No repository-scoped custom agent or subagent manifests are simulated
- No Oz cloud runs, schedules, environments, triggers, integrations, API or SDK code are configured
- No MCP, Warp Drive object IDs, saved prompt IDs, terminal commands or workflows requiring cloud objects are preconfigured
- No publication or sharing metadata is included for Warp Drive

## Platform notes
Verified against Warp/Oz docs accessed on 2026-07-18. This package targets Warp's interactive local agent experience through project `AGENTS.md` rules and project Skills in `.agents/skills/`. It intentionally does not configure Oz cloud automation.

Skills are manual, reusable instruction sets discoverable from the current working directory and invocable by slash command, for example `/workflow-plan-web-change`. They are not autonomous agents, subagents, saved cloud runs, schedules, workflows, or command-execution grants.

Warp/Oz also supports local terminal use, MCP, Warp Drive context, Oz CLI/API/SDK, cloud agents, integrations, schedules, environments and agent profiles. Those surfaces require explicit user selection, permissions, external trust, object IDs, or credentials and are intentionally omitted here.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://docs.warp.dev/agent-platform
- https://docs.warp.dev/agent-platform/getting-started/agents-in-warp
- https://docs.warp.dev/agent-platform/capabilities
- https://docs.warp.dev/agent-platform/capabilities/skills
- https://docs.warp.dev/agent-platform/capabilities/rules
- https://docs.warp.dev/agent-platform/capabilities/mcp
- https://docs.warp.dev/reference/cli
