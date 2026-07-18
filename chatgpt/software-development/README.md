# ChatGPT - Software Development

This directory is a static manual source package for configuring a ChatGPT Software Development specialization.

## Native and Conditional Surfaces

- `project/project-instructions.md` and `project/knowledge/` are the primary Project source material.
- `custom-gpt/` is optional source material for manually configured Custom GPTs when supported by the account and workspace.
- `skills/` contains static Skill source packages only when ChatGPT Skills are available for the account or workspace.
- `workspace-agent/` is a conditional manual Workspace Agent specification for supported workspaces.
- `apps-connectors/` is policy source only; it does not enable or configure integrations.

No file in this repository is automatically loaded by ChatGPT. Copy or attach only the surfaces supported by the target account, plan, administrator policy, and current product behavior.

## Department Scope

The package covers fourteen capability areas: requirements analysis, architecture, implementation and maintenance, defect correction, controlled refactoring, testing, code quality, engineering risk, software security, dependencies and supply chain, performance and reliability, API/library evolution, technical documentation, and release readiness.

## Safety Defaults

The package contains no executable hooks, scripts, MCP configuration, permission manifests, active connectors, credentials, endpoints, installers, launchers, deployment assets, release automation, or automatic authentication. Human approval is required for destructive, sensitive, external, architectural, dependency, permission, trust-boundary, migration, public-contract, Git, deployment, publication, signing, submission, and release actions.

## Usage

1. Create or update a ChatGPT Project manually.
2. Paste `project/project-instructions.md` into Project instructions.
3. Add selected files from `project/knowledge/` as Project knowledge.
4. Optionally adapt `custom-gpt/`, `skills/`, `workspace-agent/`, and `apps-connectors/` only when those surfaces are available and approved.

Runtime loading, product acceptance, connector behavior, and Skill availability have not been executed or verified from this repository.
