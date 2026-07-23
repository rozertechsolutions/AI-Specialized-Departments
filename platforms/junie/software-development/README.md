# JetBrains Junie - Software Development

The Software Development department is a human-reviewed Junie specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package targets the stable Junie guideline and Skill surfaces instead of mixing IDE and preview schemas. It is safe by default: the main Junie task remains the Lead, Skills are reusable guidance, and no hooks, MCP, custom commands, or simulated subagents are included.

## Department Overview

Use this department for stack-agnostic software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Browser-specific Web Development and mobile-platform Mobile Development remain separate. The package does not prescribe a JetBrains IDE, language, framework, provider, model, database, or endpoint.

## Possible Uses

- Requirements analysis, acceptance criteria, risks, and implementation planning.
- New feature development, bug investigation, maintenance, and controlled refactoring.
- Architecture review, dependency review, security remediation, performance/reliability work, technical-debt reduction, compatibility updates, and release-readiness review.

## Included Components

- `.junie/AGENTS.md`: stable project guideline file for Junie CLI and compatible Junie guideline import behavior.
- `.junie/skills/*/SKILL.md`: native Agent Skills packages for Junie where Skills are supported.
- `.aiignore`: project ignore file for secrets, credentials, generated outputs, and heavy irrelevant artifacts.
- `docs/workflows/*.md`: auxiliary workflow references; not a native Junie workflow engine.

## Prerequisites

You need JetBrains Junie in a supported IDE or Junie CLI surface. Skills and guideline loading depend on the installed Junie product, IDE integration, account access, and workspace policy. Human approval is expected before edits, command execution, external access, dependency changes, Git mutation, deployment, publication, signing, release, or destructive actions.

## Installation or Setup

1. Copy the contents of `junie/software-development/` into the target repository root so `.junie/`, `.aiignore`, and `docs/` land at the root.
2. Merge with existing `.junie/AGENTS.md`, `.junie/skills/`, `.aiignore`, and `docs/workflows/` content.
3. Open the target repository in the selected Junie IDE or CLI surface.
4. Confirm the guidelines and Skills are recognized by that surface before relying on them.

## Usage

Start a Junie task with the main agent as the Software Development Lead. Ask it to clarify scope, route responsibility phases, and stop for approval before implementation.

Example requests:

- "Plan this maintenance update and list acceptance criteria before changing files."
- "Use the independent-code-review Skill to review this patch."
- "Assess release readiness and identify checks not run."

## Operating Model

The Lead owns intake, routing, approvals, dependency control, and final evidence. Specialist responsibilities are represented through guidelines, Skills, and requested phases rather than stable repository subagent files. Implementation must be followed by independent review, and risk review is required when security, dependencies, performance, concurrency, reliability, data integrity, architecture, public contracts, or operations are affected.

## Safety and Human Review

Use least privilege and do not expose secrets. `.aiignore` and guidelines are not complete enforcement controls. Do not allow automatic Git mutation, deployment, publication, signing, release, external messages, spending, submissions, destructive operations, credential use, or authentication without explicit task-specific approval.

## Platform Limitations

This package deliberately uses a stable subset and omits Early Access custom subagents, command schemas, extensions, MCP, Brave-mode configuration, automatic approvals, hooks, provider/model pins, endpoints, credentials, deployment automation, publication automation, signing automation, and release automation. IDE and CLI behavior may differ; verify in the selected surface.

## Project-dependent configuration

Adapt repository/module paths, source/test/resource directories, languages, frameworks, libraries, build/test/lint/type-check commands, package manager, dependency policy, architecture boundaries, API contracts, database/storage choices, supported runtime versions, quality gates, CI/CD conventions, branch/release conventions, generated-code directories, documentation paths, test strategy, and project-specific security or compliance rules after copying the package into the target repository root. These values must come from repository files, project documentation, maintainers, and review evidence, not from this generic package.

## User- or organization-dependent configuration

Junie account, IDE availability, model/provider choices exposed by JetBrains, approval settings, enabled tools, credentials, private endpoints, organization policies, reviewer identities, deployment/release authorization, billing/spending approval, telemetry, and privacy choices remain controlled by the user, team, or administrator. Secrets and credentials must not be stored in this open-source package.

## What must remain fixed in the department package

Responsibility separation, no self-review, no circular delegation, human review for sensitive actions, least privilege, evidence-based completion, no secret exposure, no automatic destructive/external/release action, and honest representation of Junie limitations are department invariants.

## Updating and Removal

To update, merge `.junie/AGENTS.md`, `.junie/skills/`, `.aiignore`, and `docs/workflows/` changes while preserving target customizations. To remove, delete only this department's copied Junie files and empty directories created solely for them. Integrations and credentials are not stored here.
