# Warp - Software Development

The Software Development department is a human-reviewed Warp specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package uses `WARP.md` plus Warp Drive rule, Skill, and workflow source material without pretending every file auto-loads in every Warp surface. It is safe by default: there are no cloud-agent schedules, Oz jobs, terminal launchers, MCP servers, connectors, credentials, or automatic execution assets.

## Department Overview

Use this department for stack-agnostic software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Web Development and Mobile Development remain separate. The package does not select a shell command, provider, model, endpoint, framework, database, or account.

## Possible Uses

- Requirements analysis, acceptance criteria, constraints, risks, and planning.
- Bug investigation, feature work, maintenance, and controlled refactoring.
- Architecture review, API/library evolution, dependency review, security remediation, performance/reliability improvement, technical-debt reduction, compatibility updates, and release-readiness review.

## Included Components

- `WARP.md`: project guidance for the primary Warp Agent where project guidance loading is supported.
- `warp-drive/rules/*.md`: manual-import or supported Warp Drive rule source material.
- `warp-drive/skills/*/SKILL.md`: manual-import or supported Warp Agent Skill source packages.
- `warp-drive/workflows/*.md`: manual-import or supported Warp Drive workflow source material.

There are no repository custom-agent files.

## Prerequisites

You need Warp with the relevant Agent, Warp Drive, rules, Skills, or workflows surface enabled for your account/workspace. Some capabilities may be local, cloud/Oz, plan-dependent, or workspace-dependent. Human approval is expected before terminal commands, edits, Git actions, external access, dependency changes, deployment, publication, signing, release, or destructive actions.

## Installation or Setup

1. Copy `WARP.md` to the target repository root if the active Warp surface reads project guidance from that file.
2. Import `warp-drive/rules/`, `warp-drive/skills/`, and `warp-drive/workflows/` manually through the supported Warp or Warp Drive UI when available.
3. Keep source files in the target repository only if your team uses them as shared import material.
4. Do not create cloud-agent schedules, Oz background runs, terminal scripts, launchers, MCP servers, connectors, credentials, endpoints, or auto-approval settings for this package.

## Usage

Use the primary Warp Agent as the Software Development Lead. Ask it to apply imported rules, invoke relevant Skills, or follow a workflow reference while keeping human approval gates explicit.

Example requests:

- "Use the software-development rules to plan this reliability fix before commands."
- "Apply the independent-code-review Skill to this patch; do not edit files."
- "Use the release-readiness workflow to list blockers and checks not run."

## Operating Model

The Lead owns intake, scope, routing, approvals, dependency control, and final evidence aggregation. Specialist responsibilities are represented through rules, Skills, workflows, and requested review stages rather than custom repository agents. Implementation, code-quality review, engineering-risk review, and release readiness remain separate.

## Safety and Human Review

Use least privilege and protect secrets. Warp instructions and imported assets do not replace terminal confirmation, workspace controls, or human review. Do not allow automatic Git mutation, deployment, publication, signing, release, external messages, spending, submissions, destructive actions, credential use, authentication, or terminal commands without explicit task-specific approval.

## Platform Limitations

Warp and Oz capabilities vary by product surface, plan, and workspace. Warp Drive source files may require manual import and are not guaranteed to auto-load from a repository checkout. This package intentionally omits cloud-agent schedules, Oz/background jobs, MCP, connectors, hooks, terminal launchers, provider/model pins, endpoints, credentials, release automation, and fake repository agents.

## Project-dependent configuration

Adapt repository/module paths, source/test/resource directories, languages, frameworks, libraries, build/test/lint/type-check commands, package manager, dependency policy, architecture boundaries, API contracts, database/storage choices, supported runtime versions, quality gates, CI/CD conventions, branch/release conventions, generated-code directories, documentation paths, test strategy, and project-specific security or compliance rules after copying or importing the Warp Drive assets into the target workspace. These values must come from repository files, project documentation, maintainers, and review evidence, not from this generic package.

## User- or organization-dependent configuration

Warp account, workspace availability, model/provider choices exposed by Warp, terminal preferences, approval settings, enabled integrations, credentials, private endpoints, organization policies, reviewer identities, deployment/release authorization, billing/spending approval, telemetry, and privacy choices remain controlled by the user, team, or administrator. Secrets and credentials must not be stored in this open-source package.

## What must remain fixed in the department package

Responsibility separation, no self-review, no circular delegation, human review for sensitive actions, least privilege, evidence-based completion, no secret exposure, no automatic destructive/external/release action, and honest representation of Warp Drive limitations are department invariants.

## Updating and Removal

To update, merge `WARP.md` and refresh imported Warp Drive rules, Skills, and workflows while preserving local customizations. To remove, delete this department's copied `WARP.md` content and imported Warp Drive assets only. Integrations and credentials are not stored here.
