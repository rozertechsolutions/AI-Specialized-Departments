# Web Development - Devin Desktop Cascade

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- `AGENTS.md` for concise location-scoped guidance shared by Cascade and Devin Local.
- `.windsurf/rules/*.md` workspace rules for Cascade, retained as the documented legacy/fallback path.
- `.windsurf/skills/*/SKILL.md` project skills for Cascade and Devin Local.
- `.windsurf/workflows/*.md` manual slash-command workflows for Cascade only.

## Intentionally omitted or disabled
- No Cascade hooks or hook scripts are included.
- No MCP server configuration, App Deploys, external integrations, Enterprise system rules, browser automation, or deployment automation is included.
- No custom subagent, Fast Context subagent, ACP registry, cloud Devin handoff, or simulated department-agent manifest is included.
- No workflow performs automatic deployment, shell execution, Git mutation, package installation, authentication, or external side effects.

## Platform notes
Verified against official Devin/Windsurf documentation accessed on 2026-07-18. This package targets current Cascade in Devin Desktop as the primary surface. Cascade discovers `AGENTS.md`, workspace rules, skills, workflows, hooks, and MCP, but this safe static package configures only instructions, rules, skills, and manual workflows.

`AGENTS.md` is intentionally concise because root-level `AGENTS.md` is always on. Rules provide short behavioral constraints and quality gates. Skills hold reusable multi-step procedures and may be invoked by Cascade with `@skill-name`; Devin Local supports project skills and can invoke skills with `/skill-name`. Workflows are Cascade-only manual slash commands and are not available to Devin Local.

Current docs identify `.devin/rules/` as the preferred rule location and `.windsurf/rules/` as the legacy fallback. This package retains `.windsurf/rules/` because the platform prompt targets the Windsurf package and requires validation of those paths. The README makes that compatibility status explicit.

Devin Local compatibility: Devin Local supports rules/AGENTS.md and skills, uses a different permissions model, and does not support Cascade workflows, memories, App Deploys, browser previews, or conversation sharing. Fast Context may use internal exploration subagents, but there is no stable repository mechanism here for user-configured department subagents.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Temporary validation environment: not required for this static package.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://docs.devin.ai/desktop/cascade/agents-md
- https://docs.devin.ai/desktop/cascade/memories
- https://docs.devin.ai/desktop/cascade/skills
- https://docs.devin.ai/desktop/cascade/workflows
- https://docs.devin.ai/desktop/cascade/hooks
- https://docs.devin.ai/desktop/cascade/mcp
- https://docs.devin.ai/desktop/devin-local
- https://docs.devin.ai/cli/extensibility/skills/overview
- https://docs.devin.ai/cli/extensibility/rules
