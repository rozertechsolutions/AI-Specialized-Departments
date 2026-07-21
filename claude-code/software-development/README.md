# Claude Code - Software Development

The Software Development department is a human-reviewed Claude Code specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package uses Claude Code repository-native guidance, project settings, subagents, Skills, and auxiliary workflow references. It is safe by default: the primary session remains the Lead, specialists are bounded, and destructive or external actions require human approval.

## Department Overview

Use this department for general software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. It is separate from browser-specific Web Development and mobile-platform Mobile Development. It does not prescribe a stack, provider, database, or model.

## Possible Uses

- Requirements analysis and implementation planning.
- New feature development, bug investigation, maintenance, and controlled refactoring.
- Architecture review, API/library evolution, dependency review, security remediation, performance/reliability improvement, technical-debt reduction, and release-readiness review.

## Included Components

- `CLAUDE.md`: native project memory/instructions; auto-read by Claude Code when in scope.
- `.claude/settings.json`: native project settings with deny rules for destructive, Git, deployment, publication, signing, secret-read, and external-auth actions.
- `.claude/agents/*.md`: seven native specialist subagents. There is no Lead subagent because the primary Claude Code session is the Lead.
- `.claude/skills/*/SKILL.md`: native Claude Code Skills loaded when relevant or invoked by the user.
- `docs/workflows/*.md`: auxiliary workflow references; not a Claude Code command or hook system.

## Prerequisites

You need Claude Code on a supported surface and a target repository where you can copy project-local files. Subagent and Skill availability can depend on the installed Claude Code surface and organization policy. Human approval remains required for edits, commands, external access, dependency changes, Git mutation, deployment, publication, signing, release, or destructive actions.

## Installation or Setup

1. From this source package, copy the contents of `claude-code/software-development/` into the target repository root so `CLAUDE.md` and `.claude/` land at the root.
2. Preserve any existing target `CLAUDE.md` or `.claude/` customizations by merging intentionally instead of overwriting blindly.
3. Start Claude Code from the target repository root or a subdirectory covered by these files.
4. Do not add hooks, MCP servers, credentials, provider endpoints, or shell wrappers as part of this setup.

## Usage

Begin with the primary Claude Code session and ask it to act as the Software Development Lead. The Lead may delegate bounded work to the seven subagents, then require independent review and evidence before completion.

Example requests:

- "Plan this bug fix, identify risks, and wait for approval before edits."
- "Use the architecture and risk reviewers to assess this API migration."
- "Implement the approved change, then run independent code-quality and risk review."

## Operating Model

The Lead owns intake, scope, routing, approvals, dependency control, and evidence aggregation. Specialists return evidence to the Lead, cannot recursively delegate, and cannot claim final completion. Implementation must be reviewed independently by the Code Quality Reviewer, with Engineering Risk Review when security, dependencies, performance, concurrency, reliability, data integrity, architecture, or public contracts are involved.

## Safety and Human Review

Use least privilege and keep secrets out of prompts and files. `.claude/settings.json` provides a project deny layer, but Claude Code permissions and managed settings may also apply. Do not allow automatic Git mutation, deployment, publication, signing, release, submissions, spending, destructive operations, or external authentication without explicit user approval for the task.

## Platform Limitations

Claude Code settings are not a substitute for organization policy or human review. This package intentionally contains no hooks, MCP config, executable helpers, provider/model pins, endpoints, credentials, release automation, or Lead subagent. `docs/workflows/` is reference material only.

## Project-dependent configuration

Adapt repository/module paths, source/test/resource directories, languages, frameworks, libraries, build/test/lint/type-check commands, package manager, dependency policy, architecture boundaries, API contracts, database/storage choices, supported runtime versions, quality gates, CI/CD conventions, branch/release conventions, generated-code directories, documentation paths, test strategy, and project-specific security or compliance rules after copying the package into the target repository root. These values must come from repository files, project documentation, maintainers, and review evidence, not from this generic package.

## User- or organization-dependent configuration

Claude Code account, plan, workspace availability, model choice, IDE/CLI preferences, permission mode, enabled tools, MCP/connectors, credentials, private endpoints, organization policies, reviewer identities, deployment/release authorization, billing/spending approval, telemetry, and privacy choices remain controlled by the user, team, or administrator. Secrets and credentials must not be stored in this open-source package.

## What must remain fixed in the department package

Responsibility separation, no self-review, no circular delegation, human review for sensitive actions, least privilege, evidence-based completion, no secret exposure, no automatic destructive/external/release action, and honest representation of Claude Code limitations are department invariants.

## Updating and Removal

To update, merge new `CLAUDE.md`, `.claude/settings.json`, `.claude/agents/`, `.claude/skills/`, and `docs/workflows/` content while preserving target customizations. To remove, delete only those copied department files and empty directories created solely for this package. Credentials and integrations are not stored here.
