# Web Development — JetBrains Junie

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- Primary Junie project guidelines in `.junie/AGENTS.md`
- Root `AGENTS.md` pointer to avoid duplicate guideline loading
- Project Agent Skills in `.junie/skills/*/SKILL.md`

## Intentionally omitted or disabled
- No custom subagents are included because current subagent configuration is documented with EAP enablement requirements
- No hooks, MCP, provider keys, model configuration, commands, remote agents, or workflow automation are included
- IDE and account settings remain manual

## Platform notes
Junie CLI discovers project guidelines in this order: `.junie/AGENTS.md`, then root `AGENTS.md`, then legacy `.junie/guidelines.md` or `.junie/guidelines/`. This package uses `.junie/AGENTS.md` as the only full guideline source. The root `AGENTS.md` is only a short pointer. Junie CLI and Junie in JetBrains IDEs discover project skills from `.junie/skills/<skill-name>/SKILL.md`.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://junie.jetbrains.com/docs/guidelines-and-memory.html
- https://junie.jetbrains.com/docs/agent-skills.html
- https://junie.jetbrains.com/docs/junie-cli-subagents.html
