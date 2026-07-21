# Mistral Vibe - Software Development

The Software Development department is a human-reviewed Mistral Vibe specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package uses Vibe project guidance, config, agents, prompts, Skills, and workflow references while keeping provider, model, endpoint, Bash, web, MCP, and credential configuration out of scope. It is safe by default: select the Lead explicitly, keep specialist delegation bounded, and require human approval for sensitive actions.

## Department Overview

Use this department for stack-agnostic software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Web Development and Mobile Development remain separate. The package does not select a language, framework, database, provider, model, endpoint, or account.

## Possible Uses

- Requirements analysis, acceptance criteria, constraints, risks, and planning.
- Feature work, bug investigation, maintenance, and controlled refactoring.
- Architecture review, API/library evolution, dependency review, security remediation, performance/reliability improvement, technical-debt reduction, compatibility updates, and release-readiness assessment.

## Included Components

- `AGENTS.md`: repository-scoped department instructions for Vibe.
- `.vibe/config.toml`: project-local config naming `software-development-lead` as the intended default agent.
- `.vibe/agents/software-development-lead.toml`: native Lead agent with read/search plus bounded `task` delegation.
- `.vibe/agents/*.toml`: seven native specialist agents; only implementation has write tools.
- `.vibe/prompts/*.md`: native role prompts paired with the agent definitions.
- `.vibe/skills/*/SKILL.md`: native Agent Skills packages.
- `docs/workflows/*.md`: auxiliary workflow references.

## Prerequisites

You need Mistral Vibe CLI or VS Code extension support for project config, agents, prompts, and Skills. Account, plan, model, provider, and authentication setup are external to this package. Human approval is expected before edits, shell/process execution, external access, dependency changes, Git mutation, deployment, publication, signing, release, or destructive actions.

## Installation or Setup

1. Copy the contents of `mistral-vibe/software-development/` into the target repository root so `AGENTS.md`, `.vibe/`, and `docs/` land at the root.
2. Merge with existing `.vibe/config.toml`, `.vibe/agents/`, `.vibe/prompts/`, `.vibe/skills/`, and `docs/workflows/` content.
3. In interactive use, select `software-development-lead` before starting Software Development work.
4. In programmatic use, explicitly select `software-development-lead`; do not rely on ambient defaults or auto-approval behavior.
5. Do not add Bash, web, MCP, connectors, providers, models, endpoints, credentials, hooks, installers, or launchers.

## Usage

Start with the Lead agent. The Lead can call specialists through `task`, collect evidence, require independent review after implementation, and stop before release actions.

Example requests:

- "Use the Lead to plan this dependency update and identify approval gates."
- "Route this proposed API change to the architect and risk reviewer."
- "Implement only the approved fix, then request code-quality review."

## Operating Model

The Lead owns scope, routing, approvals, dependency control, separation of duties, and final evidence aggregation. Specialists return evidence to the Lead and cannot delegate further. Implementation, code-quality review, engineering-risk review, and documentation/release readiness remain distinct phases.

## Safety and Human Review

Use least privilege and protect secrets. `safety = "safe"` metadata is not an enforcement mechanism; tool allowlists and human review carry the safety boundary. Do not allow automatic Git mutation, deployment, publication, signing, release, external messages, spending, submissions, destructive actions, credential use, or authentication without explicit task-specific approval.

## Platform Limitations

Vibe behavior can vary by CLI, extension, account, and host policy. Programmatic approval limits are explicit: callers must select the safe Lead and enforce approvals. This package intentionally omits Bash, web, MCP, connectors, provider/model pins, endpoints, credentials, hooks, installers, launchers, deployment automation, publication automation, signing automation, release automation, and Git tools.

## Project-dependent configuration

Adapt repository/module paths, source/test/resource directories, languages, frameworks, libraries, build/test/lint/type-check commands, package manager, dependency policy, architecture boundaries, API contracts, database/storage choices, supported runtime versions, quality gates, CI/CD conventions, branch/release conventions, generated-code directories, documentation paths, test strategy, and project-specific security or compliance rules after copying the package into the target repository root. These values must come from repository files, project documentation, maintainers, and review evidence, not from this generic package.

## User- or organization-dependent configuration

Mistral Vibe account, workspace availability, model/provider choices exposed by the product, IDE/CLI preferences, approval settings, enabled tools, connectors/MCP, credentials, private endpoints, organization policies, reviewer identities, deployment/release authorization, billing/spending approval, telemetry, and privacy choices remain controlled by the user, team, or administrator. Secrets and credentials must not be stored in this open-source package.

## What must remain fixed in the department package

Responsibility separation, no self-review, no circular delegation, human review for sensitive actions, least privilege, evidence-based completion, no secret exposure, no automatic destructive/external/release action, and honest representation of Mistral Vibe limitations are department invariants.

## Updating and Removal

To update, merge `AGENTS.md`, `.vibe/`, and `docs/workflows/` changes while preserving local customizations. To remove, delete only this department's copied Vibe files and empty directories created solely for them. Integrations and credentials are not stored here.
