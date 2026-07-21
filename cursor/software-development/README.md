# Cursor - Software Development

The Software Development department is a human-reviewed Cursor specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package uses Cursor project instructions, rules, subagents, Skills, and auxiliary workflow references. It is safe by default: Cursor remains under human approval and no file here enables background automation, hooks, MCP, credentials, or external actions.

## Department Overview

<<<<<<< HEAD
- `AGENTS.md` makes the primary Cursor Agent the Software Development Lead.
- `.cursor/agents/` contains the seven native Cursor project specialist subagents. There is no Lead subagent.
- `.cursor/rules/` contains Cursor project rules.
- `.cursor/skills/` contains static reusable Skills.
- `docs/workflows/` contains auxiliary workflow references, not a guaranteed native workflow engine.

## Project Subagents

The primary Cursor Agent remains the Software Development Lead. It delegates to seven project subagents for requirements/planning, architecture, implementation/maintenance, test/quality, code-quality review, engineering-risk review, and documentation/release readiness. Only the implementation specialist is writable; the other six are read-only. Implementation must be followed by independent review before final evidence aggregation.
=======
Use this department for stack-agnostic software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Browser-specific frontend work belongs in Web Development; mobile-platform work belongs in Mobile Development. The package does not select a framework, provider, database, model, or endpoint.

## Possible Uses

- Requirements analysis, acceptance criteria, and implementation planning.
- New feature development, bug investigation, correction, maintenance, and controlled refactoring.
- Architecture review, API/library evolution, dependency review, security remediation, performance/reliability improvement, technical-debt reduction, and release-readiness review.
>>>>>>> feature/software-development

## Included Components

- `AGENTS.md`: project guidance for the primary Cursor Agent/CLI/cloud-agent surface where AGENTS.md is supported.
- `.cursor/rules/*.mdc`: native Cursor project rules with MDC frontmatter.
- `.cursor/agents/*.md`: native Cursor specialist subagents. Six specialists are marked `readonly: true`; the implementation specialist is not read-only but remains approval-bound by the Lead and Cursor's normal human review.
- `.cursor/skills/*/SKILL.md`: native Agent Skills packages when Skills are supported by the installed Cursor surface.
- `docs/workflows/*.md`: auxiliary workflow references; not a guaranteed native workflow engine.

## Prerequisites

You need Cursor Desktop, Cursor CLI, Cursor web/cloud-agent access, or another Cursor surface that supports the selected components. Rules, subagents, and Skills depend on product version, account plan, workspace settings, and managed policy. Human approval is expected before edits, terminal commands, external actions, Git mutation, dependency changes, deployment, publication, signing, release, or destructive work.

## Installation or Setup

1. Copy the contents of `cursor/software-development/` into the target repository root so `AGENTS.md`, `.cursor/`, and `docs/` land at the root.
2. Merge with any existing `AGENTS.md`, `.cursor/rules/`, `.cursor/agents/`, `.cursor/skills/`, and `docs/workflows/` content.
3. Open the target repository in Cursor and confirm the relevant rules, subagents, and Skills are visible in the Cursor customization UI.
4. Do not create legacy `.cursorrules`, hooks, MCP config, background-agent automation, credentials, endpoints, or shell helpers for this package.

## Usage

Use the primary Cursor Agent as the Software Development Lead. Ask it to plan, route bounded work to the specialist subagents when useful, apply rules and Skills, and collect independent review evidence before completion.

Example requests:

- "Plan this API change and identify compatibility, migration, and validation risks."
- "Investigate this bug and propose a smallest safe fix before editing."
- "Review this refactor for code quality and reliability without changing files."

## Operating Model

The Lead owns intake, scope, routing, approvals, dependency control, and final evidence aggregation. Specialist responsibilities are represented through subagents, rules, Skills, and requested review stages. Implementation must not certify itself; code-quality and engineering-risk review remain independent.

## Safety and Human Review

Use least privilege and keep secrets out of prompts and files. Cursor instructions cannot enforce every IDE, CLI, or cloud action, so human approval and workspace policy remain authoritative. Do not allow automatic Git mutation, deployment, publication, signing, release, spending, submissions, destructive operations, external authentication, or credential use without explicit task-specific approval.

## Platform Limitations

Cursor feature availability varies across Desktop, CLI, web/cloud agents, account plan, and managed settings. Skills and subagent support may require a current Cursor version and can be limited by managed policy. This package intentionally omits a Lead subagent, legacy `.cursorrules`, hooks, MCP config, automatic approvals, background automation, provider/model pins, endpoints, and credentials.

## Updating and Removal

To update, merge changes in `AGENTS.md`, `.cursor/rules/`, `.cursor/agents/`, `.cursor/skills/`, and `docs/workflows/` while preserving local customizations. To remove, delete only this department's copied Cursor files and empty directories created solely for it. No integrations or credentials are stored here.
