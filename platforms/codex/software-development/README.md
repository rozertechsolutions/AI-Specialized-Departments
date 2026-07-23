# Codex - Software Development

The Software Development department is a human-reviewed Codex specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package uses Codex-native `AGENTS.md`, project `config.toml`, subagents, Skills, and auxiliary workflow references. It is safe by default: the primary Codex session is the Lead, delegation depth is bounded, network is disabled in workspace-write sandboxing, and sensitive actions require approval.

## Department Overview

Use this department for general software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Web Development and Mobile Development remain separate for browser-specific and mobile-platform-specific work. The package is stack-, database-, provider-, model-, and vendor-neutral.

## Possible Uses

- Requirements decomposition, acceptance criteria, and implementation planning.
- New feature development, bug fixes, maintenance, and controlled refactoring.
- Architecture review, API/library evolution, dependency review, security remediation, performance/reliability improvement, technical-debt reduction, and release-readiness review.

## Included Components

- `AGENTS.md`: native Codex project instructions; auto-discovered by Codex when in scope.
- `.codex/config.toml`: native project config with `approval_policy = "on-request"`, `sandbox_mode = "workspace-write"`, network disabled for workspace-write, and `[agents].max_depth = 1`.
- `.codex/agents/*.toml`: seven native specialist agents; there is intentionally no Lead agent.
- `.codex/skills/*/SKILL.md`: native project Skills following the Agent Skills format.
- `docs/workflows/*.md`: auxiliary references; not a Codex hook or workflow engine.

## Prerequisites

You need Codex CLI, IDE extension, or app support for repository instructions, project config, project agents, and Skills. Managed settings or surface-specific restrictions may override repository config. You need authorized repository access and explicit human approval for edits, commands, Git mutation, dependency changes, external services, deployment, publication, signing, release, or destructive work.

## Installation or Setup

1. Copy the contents of `codex/software-development/` into the target repository root so `AGENTS.md`, `.codex/`, and `docs/` land at the root.
2. Merge with any existing target `AGENTS.md`, `.codex/config.toml`, `.codex/agents/`, `.codex/skills/`, or `docs/workflows/` files.
3. Open the target repository with Codex from the repository root or an in-scope subdirectory.
4. Do not add hooks, MCP servers, provider/model pins, endpoints, credentials, or user-global paths as part of this package.

## Usage

Begin with the primary Codex session as the Lead. Ask it to clarify scope, route bounded work to specialists when useful, and collect evidence before completion.

Example requests:

- "Plan this feature and identify architecture, risk, and validation gates before edits."
- "Use the code-quality and engineering-risk reviewers on this proposed refactor."
- "Implement the approved fix only, then report tests and checks not run."

## Operating Model

The Lead owns intake, scope, routing, approvals, dependency control, and final evidence aggregation. Specialists return evidence and do not recursively delegate. Implementation and independent review are separate. Risk review is required for security, dependency, performance, concurrency, reliability, data integrity, architecture, public-contract, or operational-risk changes.

## Safety and Human Review

Use least privilege and keep secrets out of context. Codex config helps constrain behavior, but user approval, sandboxing, and managed policy remain authoritative. Do not allow automatic Git mutation, deployment, publication, signing, release, external messages, spending, destructive actions, credentials use, or authentication without explicit task-specific approval.

## Platform Limitations

Codex discovery depends on the active Codex surface and project root. `docs/workflows/` is auxiliary, not auto-executed. This package intentionally contains no hooks, MCP entries, executable helpers, provider/model pins, endpoint pins, credentials, release automation, or Lead subagent.

## Project-dependent configuration

Adapt repository/module paths, source/test/resource directories, languages, frameworks, libraries, build/test/lint/type-check commands, package manager, dependency policy, architecture boundaries, API contracts, database/storage choices, supported runtime versions, quality gates, CI/CD conventions, branch/release conventions, generated-code directories, documentation paths, test strategy, and project-specific security or compliance rules after copying the package into the target repository root. These values must come from repository files, project documentation, maintainers, and review evidence, not from this generic package.

## User- or organization-dependent configuration

Codex account, plan, workspace availability, model choice, CLI preferences, approval settings, enabled tools, MCP/connectors, credentials, private endpoints, organization policies, reviewer identities, deployment/release authorization, billing/spending approval, telemetry, and privacy choices remain controlled by the user, team, or administrator. Secrets and credentials must not be stored in this open-source package.

## What must remain fixed in the department package

Responsibility separation, no self-review, no circular delegation, human review for sensitive actions, least privilege, evidence-based completion, no secret exposure, no automatic destructive/external/release action, and honest representation of Codex limitations are department invariants.

## Updating and Removal

To update, merge the copied `AGENTS.md`, `.codex/`, and `docs/workflows/` content while preserving target customizations. To remove, delete only this department's copied Codex files and any empty directories created solely for it. Integrations and credentials are not stored here.
