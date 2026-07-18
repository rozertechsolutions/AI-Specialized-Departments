# Claude - Software Development

This directory is a static manual source package for configuring a Claude Project Software Development specialization. It is intentionally separate from Claude Code.

## Native and Conditional Surfaces

- `project/project-instructions.md` and `project/knowledge/` are the primary Claude Project source material.
- `project/review-checklists.md` provides manual review checklists for Claude Project knowledge.
- `skills/` contains static Skill source packages only when Claude Skills are available for the account or workspace.
- `connectors/` is policy source only; it does not enable or configure integrations.

No file in this repository is automatically loaded by Claude. Copy or attach only the surfaces supported by the target account, plan, administrator policy, and current product behavior.

## Department Scope

The package covers fourteen capability areas: requirements analysis, architecture, implementation and maintenance, defect correction, controlled refactoring, testing, code quality, engineering risk, software security, dependencies and supply chain, performance and reliability, API/library evolution, technical documentation, and release readiness.

## Omitted Claude Code Surfaces

This target must not contain `CLAUDE.md`, `.claude/`, repository subagents, commands, hooks, settings, MCP configuration, local shell automation, or automatic connector authentication.

## Safety Defaults

The package contains no executable hooks, scripts, active MCP configuration, credentials, endpoints, installers, launchers, deployment assets, release automation, or automatic authentication. Human approval is required for destructive, sensitive, external, architectural, dependency, permission, trust-boundary, migration, public-contract, Git, deployment, publication, signing, submission, and release actions.

Runtime loading, product acceptance, connector behavior, and Skill availability have not been executed or verified from this repository.
