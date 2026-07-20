# Kiro IDE - Software Development

The Software Development department is a human-reviewed Kiro IDE specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package targets the Kiro IDE surface with steering files, custom agents, Skills, and auxiliary workflow references. It is safe by default: the primary Kiro chat remains the Lead, specialists are bounded, and no specs, hooks, MCP, credentials, or deployment automation are included.

## Department Overview

Use this department for stack-agnostic software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Browser-specific Web Development and mobile-platform Mobile Development remain separate. The package does not prescribe a framework, database, provider, model, endpoint, or runtime.

## Possible Uses

- Requirements analysis, acceptance criteria, risks, and planning.
- New feature development, bug investigation, maintenance, and controlled refactoring.
- Architecture review, API/library evolution, dependency review, security remediation, performance/reliability improvement, technical-debt reduction, compatibility updates, and release-readiness review.

## Included Components

- `.kiro/steering/*.md`: native Kiro IDE steering files for primary Lead behavior.
- `.kiro/agents/*.md`: seven Kiro IDE custom agents in Markdown frontmatter format; there is no Lead custom agent.
- `.kiro/skills/*/SKILL.md`: native Agent Skills packages for Kiro.
- `docs/workflows/*.md`: auxiliary workflow references; not Kiro specs or executable automation.

## Prerequisites

You need Kiro IDE with steering, custom agents, and Skills support. Kiro CLI custom-agent JSON is a different surface and is not used by this package. Human approval is expected before edits, command execution, external access, dependency changes, Git mutation, deployment, publication, signing, release, or destructive actions.

## Installation or Setup

1. Copy the contents of `kiro/software-development/` into the target repository root so `.kiro/` and `docs/` land at the root.
2. Merge with existing `.kiro/steering/`, `.kiro/agents/`, `.kiro/skills/`, and `docs/workflows/` content.
3. Open the target repository in Kiro IDE and confirm steering, custom agents, and Skills are visible.
4. Do not add `.kiro/specs/`, CLI JSON agents, hooks, MCP, providers, endpoints, credentials, deployment automation, publication automation, signing automation, or release automation.

## Usage

Use the primary Kiro IDE chat as the Software Development Lead. Select specialist custom agents or Skills when useful, and keep final scope and evidence decisions in the Lead.

Example requests:

- "Use steering to plan this compatibility update and list risks before editing."
- "Ask the code-quality reviewer agent to inspect this design without changing files."
- "Use the release-readiness workflow reference to summarize blockers."

## Operating Model

The Lead owns intake, scope, routing, approvals, dependency control, and final evidence aggregation. Specialists return evidence, cannot recursively delegate, and cannot claim final completion. Implementation must be independently reviewed, and engineering-risk review is required for security, dependencies, performance, concurrency, reliability, data integrity, architecture, public contracts, or operations.

## Safety and Human Review

Use least privilege and protect secrets. Kiro file instructions and agent tool settings do not replace user approval or workspace policy. Do not allow automatic Git mutation, deployment, publication, signing, release, external messages, spending, submissions, destructive actions, credential use, or authentication without explicit task-specific approval.

## Platform Limitations

This package deliberately selects Kiro IDE and does not mix in Kiro CLI custom-agent schemas. `docs/workflows/` is auxiliary and `.kiro/specs/` is intentionally absent. Hooks, MCP, providers, model pins, endpoints, credentials, deployment automation, publication automation, signing automation, release automation, and a Lead custom agent are omitted.

## Updating and Removal

To update, merge `.kiro/steering/`, `.kiro/agents/`, `.kiro/skills/`, and `docs/workflows/` changes while preserving local customizations. To remove, delete only this department's copied Kiro files and empty directories created solely for them. Integrations and credentials are not stored here.
