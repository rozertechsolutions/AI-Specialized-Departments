# Web Development — Cursor

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- Cursor Project Rules in `.cursor/rules/*.mdc`
- Concise root `AGENTS.md` pointer for Cursor CLI/root instruction discovery
- Direct specialist subagents in `.cursor/agents/*.md`
- Project Skills in `.cursor/skills/*/SKILL.md`

## Intentionally omitted or disabled
- Hooks are omitted
- MCP is omitted because this package does not require a concrete external tool integration
- No model is pinned
- No cloud agent publication or GitHub integration is configured

## Platform notes
Project Rules apply in the Cursor IDE and Cursor CLI; the CLI also reads root `AGENTS.md`, so that file only points back to the rules to avoid duplicate always-on instructions. Subagents and Skills are project-scoped Cursor assets. The package uses direct specialist subagents rather than a lead subagent because no separate coordinator is required for this static package. Read-only reviewer subagents use Cursor's `readonly: true` field. Background/Web agents and cloud runs are user-controlled surfaces and are not configured here.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://docs.cursor.com/context/rules-for-ai
- https://docs.cursor.com/en/cli/using
- https://docs.cursor.com/context/model-context-protocol
- https://docs.cursor.com/background-agent
- https://www.cursor.com/en/changelog
