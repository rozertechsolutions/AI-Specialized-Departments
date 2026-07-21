# Kilo Code - Software Development

The Software Development department is a human-reviewed Kilo Code specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package uses Kilo Code native AGENTS.md guidance, project JSONC config, rules, subagents, Skills, and prompt commands. It is safe by default: broad actions ask, Bash and web fetch are denied, edits are approval-gated, and no hooks, MCP, provider endpoints, or credentials are included.

## Department Overview

Use this department for stack-agnostic software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Web Development and Mobile Development remain separate. The package does not select a language, framework, database, provider, model, or endpoint.

## Possible Uses

- Requirements analysis, acceptance criteria, constraints, risks, and planning.
- New feature development, bug investigation, maintenance, and controlled refactoring.
- Architecture review, API/library evolution, dependency review, security remediation, performance/reliability improvement, technical-debt reduction, compatibility updates, and release-readiness review.

## Included Components

- `AGENTS.md`: native project instructions for the primary Kilo Code Lead.
- `kilo.jsonc`: native JSONC project config with fallback ask, Bash deny, web fetch deny, and edit ask.
- `.kilo/rules/*.md`: native project rules referenced by `kilo.jsonc`.
- `.kilo/agents/*.md`: seven native specialist agents; there is intentionally no Lead subagent.
- `.kilo/skills/*/SKILL.md`: native Agent Skills packages.
- `.kilo/commands/*.md`: native prompt-only workflow commands.

## Prerequisites

You need Kilo Code in a supported IDE, CLI, or cloud surface with project rules/config, agents, commands, and Skills support. Parent/user/workspace approval settings may override or add restrictions. Human approval is expected before edits, shell commands, external access, dependency changes, Git mutation, deployment, publication, signing, release, or destructive actions.

## Installation or Setup

1. Copy the contents of `kilo-code/software-development/` into the target repository root so `AGENTS.md`, `kilo.jsonc`, and `.kilo/` land at the root.
2. Merge with existing target `AGENTS.md`, `kilo.jsonc`, `.kilo/rules/`, `.kilo/agents/`, `.kilo/skills/`, and `.kilo/commands/`.
3. Open the target repository in Kilo Code and confirm the project rules, agents, Skills, and commands are discovered.
4. Do not add legacy `.kilocodemodes`, hooks, MCP config, providers, model pins, endpoints, credentials, shell helpers, or auto-approval settings.

## Usage

Use the primary Kilo Code session as the Software Development Lead. Invoke native commands or specialist agents only for bounded responsibilities and keep final evidence aggregation in the Lead.

Example requests:

- "Use the requirements specialist to plan this feature before any edits."
- "Run the security-remediation command as a planning workflow; do not change files."
- "Have implementation make the approved fix, then request independent code-quality review."

## Operating Model

The Lead owns intake, scope, routing, approvals, dependency control, and final evidence aggregation. Specialists return evidence, cannot recursively delegate, and cannot claim final completion. Implementation must be independently reviewed, and risk review is required for security, dependencies, performance, concurrency, reliability, data integrity, architecture, public contracts, or operational risk.

## Safety and Human Review

Use least privilege and keep secrets out of context. `kilo.jsonc` is a project safety layer, not a replacement for human review or managed policy. Do not allow automatic Git mutation, deployment, publication, signing, release, external messages, spending, submissions, destructive actions, credentials use, or authentication without explicit task-specific approval.

## Platform Limitations

Kilo Code feature support varies by surface and version. No exact official schema URI is declared in `kilo.jsonc`. This package intentionally omits legacy `.kilocodemodes`, hooks, MCP, Bash/web grants, providers, model pins, endpoints, credentials, deployment automation, publication automation, signing automation, release automation, and a Lead subagent.

## Project-dependent configuration

Adapt repository/module paths, source/test/resource directories, languages, frameworks, libraries, build/test/lint/type-check commands, package manager, dependency policy, architecture boundaries, API contracts, database/storage choices, supported runtime versions, quality gates, CI/CD conventions, branch/release conventions, generated-code directories, documentation paths, test strategy, and project-specific security or compliance rules after copying the package into the target repository root. These values must come from repository files, project documentation, maintainers, and review evidence, not from this generic package.

## User- or organization-dependent configuration

Kilo Code account or extension availability, model/provider choice, IDE preferences, permission settings, enabled tools, MCP/connectors, credentials, private endpoints, organization policies, reviewer identities, deployment/release authorization, billing/spending approval, telemetry, and privacy choices remain controlled by the user, team, or administrator. Secrets and credentials must not be stored in this open-source package.

## What must remain fixed in the department package

Responsibility separation, no self-review, no circular delegation, human review for sensitive actions, least privilege, evidence-based completion, no secret exposure, no automatic destructive/external/release action, and honest representation of Kilo Code limitations are department invariants.

## Updating and Removal

To update, merge `AGENTS.md`, `kilo.jsonc`, and `.kilo/` changes while preserving local customizations. To remove, delete only this department's copied Kilo files and empty directories created solely for them. Integrations and credentials are not stored here.
