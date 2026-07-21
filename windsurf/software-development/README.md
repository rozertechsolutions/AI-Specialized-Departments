# Windsurf - Software Development

The Software Development department is a human-reviewed Windsurf/Devin Desktop Cascade specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package uses repository-scoped AGENTS.md, rules, Skills, and workflows without custom-agent files or automation. It is safe by default: Cascade remains human-reviewed and no hooks, MCP, shell helpers, background jobs, credentials, or automatic terminal execution are included.

## Department Overview

Use this department for stack-agnostic software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Browser-specific Web Development and mobile-platform Mobile Development remain separate. The package does not select a provider, model, endpoint, framework, database, account, or deployment target.

## Possible Uses

- Requirements analysis, acceptance criteria, constraints, risks, and planning.
- New feature development, bug investigation, maintenance, and controlled refactoring.
- Architecture review, API/library evolution, dependency review, security remediation, performance/reliability improvement, technical-debt reduction, compatibility updates, and release-readiness review.

## Included Components

- `AGENTS.md`: native Cascade project guidance, processed as a rule when supported.
- `.windsurf/rules/*.md`: native legacy workspace rules; current Devin Desktop documentation prefers `.devin/rules/` but still documents `.windsurf/rules/` as a fallback.
- `.windsurf/skills/*/SKILL.md`: native workspace Skills.
- `.windsurf/workflows/*.md`: native workflow prompt files for manual slash-command use where supported.

There are no repository custom-agent files.

## Prerequisites

You need Windsurf Cascade or Devin Desktop with AGENTS.md/rules, Skills, and workflows support. Feature availability can depend on product generation, plan, account, enterprise policy, and whether `.windsurf/` fallback discovery is enabled. Human approval is expected before edits, terminal commands, external access, dependency changes, Git mutation, deployment, publication, signing, release, or destructive actions.

## Installation or Setup

1. Copy the contents of `windsurf/software-development/` into the target repository root so `AGENTS.md` and `.windsurf/` land at the root.
2. Merge with existing `AGENTS.md`, `.windsurf/rules/`, `.windsurf/skills/`, and `.windsurf/workflows/` content.
3. In Devin Desktop environments that require the preferred path, migrate rules to `.devin/rules/` in the target repository while preserving this package's content.
4. Open the target repository in Cascade and confirm rules, Skills, and workflows are discovered.
5. Do not add hooks, MCP config, auto-run config, shell helpers, connectors, provider/model pins, endpoints, credentials, deployment automation, publication automation, signing automation, or release automation.

## Usage

Use the primary Cascade session as the Software Development Lead. Apply rules, invoke Skills by relevance or mention, and use workflows as prompt templates while keeping approvals explicit.

Example requests:

- "Plan this maintenance change and wait for approval before editing."
- "Use the secure-software-review Skill to assess this patch."
- "Use the release-readiness workflow to list evidence and blockers."

## Operating Model

The Lead owns intake, scope, routing, approvals, dependency control, and final evidence aggregation. Specialist responsibilities are represented through rules, Skills, workflows, and requested review stages rather than custom agents. Implementation must be separated from independent code-quality review, and engineering-risk review is required when security, dependencies, performance, concurrency, reliability, data integrity, architecture, public contracts, or operations are affected.

## Safety and Human Review

Use least privilege and protect secrets. Cascade rules and Skills do not replace user confirmation or enterprise controls. Do not allow automatic Git mutation, deployment, publication, signing, release, external messages, spending, submissions, destructive actions, credential use, authentication, or terminal command execution without explicit task-specific approval.

## Platform Limitations

Windsurf/Devin Desktop terminology and paths are evolving; `.devin/` is preferred in current Devin Desktop docs while `.windsurf/` remains documented as fallback. This package intentionally omits simulated custom agents, hooks, MCP, terminal launch automation, auto-run config, provider/model pins, endpoints, credentials, deployment automation, publication automation, signing automation, and release automation.

## Project-dependent configuration

Adapt repository/module paths, source/test/resource directories, languages, frameworks, libraries, build/test/lint/type-check commands, package manager, dependency policy, architecture boundaries, API contracts, database/storage choices, supported runtime versions, quality gates, CI/CD conventions, branch/release conventions, generated-code directories, documentation paths, test strategy, and project-specific security or compliance rules after copying the package into the target repository root. These values must come from repository files, project documentation, maintainers, and review evidence, not from this generic package.

## User- or organization-dependent configuration

Windsurf account, plan, workspace availability, model choice, IDE preferences, approval settings, enabled tools, MCP/connectors, credentials, private endpoints, organization policies, reviewer identities, deployment/release authorization, billing/spending approval, telemetry, and privacy choices remain controlled by the user, team, or administrator. Secrets and credentials must not be stored in this open-source package.

## What must remain fixed in the department package

Responsibility separation, no self-review, no circular delegation, human review for sensitive actions, least privilege, evidence-based completion, no secret exposure, no automatic destructive/external/release action, and honest representation of Windsurf limitations are department invariants.

## Updating and Removal

To update, merge `AGENTS.md`, rules, Skills, and workflows while preserving target customizations and any `.devin/` migration your workspace uses. To remove, delete only this department's copied Windsurf files and empty directories created solely for them. Integrations and credentials are not stored here.
