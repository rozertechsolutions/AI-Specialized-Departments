# OpenCode - Software Development

The Software Development department is a human-reviewed OpenCode specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package uses OpenCode native rules, JSONC config, specialist agents, Skills, and commands. It is safe by default: fallback permissions ask, Bash and web fetch are denied, edits require approval, and no MCP, provider, endpoint, credential, hook, or automation is included.

## Department Overview

<<<<<<< HEAD
- `AGENTS.md` defines the primary Software Development Lead behavior.
- `opencode.jsonc` sets explicit project permissions: broad fallback ask, Task ask, Bash denied, web fetch denied, edits ask.
- `.opencode/agents/` contains seven specialist subagents.
- `.opencode/skills/` contains fourteen preserved capability Skills.
- `.opencode/commands/` contains eleven prompt-only workflow commands.
=======
Use this department for stack-agnostic software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Web Development and Mobile Development remain separate. The package does not select a framework, database, provider, model, endpoint, or account.
>>>>>>> feature/software-development

## Possible Uses

<<<<<<< HEAD
OpenCode tools may otherwise be broadly available, so this package uses explicit least-privilege permissions. All specialists deny Task to prevent recursive delegation. Planners, architects, testers, reviewers, risk reviewers, and documentation/release specialists deny edit, Bash, and web. The implementation specialist may request edits only after the primary Lead has approved scope; it still denies Task, Bash, web, Git, MCP, deployment, publication, signing, release, and external actions.
=======
- Requirements analysis, acceptance criteria, constraints, risks, and planning.
- New feature development, bug investigation, maintenance, and controlled refactoring.
- Architecture review, API/library evolution, dependency review, security remediation, performance/reliability improvement, technical-debt reduction, compatibility updates, and release-readiness review.
>>>>>>> feature/software-development

## Included Components

- `AGENTS.md`: native OpenCode project instructions for the primary Lead session.
- `opencode.jsonc`: native JSONC config with fallback ask, Bash deny, web fetch deny, and edit ask.
- `.opencode/agents/*.md`: seven native specialist subagents; there is intentionally no Lead subagent.
- `.opencode/skills/*/SKILL.md`: native Agent Skills packages.
- `.opencode/commands/*.md`: native prompt-only workflow commands.

## Prerequisites

You need OpenCode with repository rules, config, agents, Skills, and commands support. User, workspace, and parent configuration can affect final permissions. Human approval is expected before edits, shell commands, external access, dependency changes, Git mutation, deployment, publication, signing, release, or destructive actions.

## Installation or Setup

1. Copy the contents of `opencode/software-development/` into the target repository root so `AGENTS.md`, `opencode.jsonc`, and `.opencode/` land at the root.
2. Merge with existing `AGENTS.md`, `opencode.jsonc`, `.opencode/agents/`, `.opencode/skills/`, and `.opencode/commands/`.
3. Open the target repository in OpenCode and confirm the agents, Skills, commands, and permissions are visible.
4. Do not add MCP servers, plugins, hooks, scripts, wrappers, global paths, providers, models, endpoints, credentials, or release/deployment automation.

## Usage

Use the primary OpenCode session as the Software Development Lead. Invoke commands or specialists for bounded responsibilities, then return evidence to the Lead.

Example requests:

- "Use the planning specialist to prepare acceptance criteria and risks."
- "Run the dependency-update command as a prompt workflow; do not edit files."
- "Implement the approved change, then request code-quality and risk review."

## Operating Model

The Lead owns intake, scope, routing, approvals, dependency control, and final evidence aggregation. Specialists return evidence, cannot recursively delegate, and cannot claim final completion. Implementation, code-quality review, engineering-risk review, and documentation/release readiness remain distinct.

## Safety and Human Review

Use least privilege and protect secrets. OpenCode permission config reduces risk but does not replace user approval or managed policy. Do not allow automatic Git mutation, deployment, publication, signing, release, external messages, spending, submissions, destructive actions, credential use, or authentication without explicit task-specific approval.

## Platform Limitations

OpenCode feature support varies by installed version and parent config. This package intentionally omits `.opencode/agents/software-development-lead.md`, MCP, plugins, hooks, scripts, wrappers, global paths, provider/model pins, endpoints, credentials, Bash/web grants, deployment automation, publication automation, signing automation, and release automation.

## Project-dependent configuration

Adapt repository/module paths, source/test/resource directories, languages, frameworks, libraries, build/test/lint/type-check commands, package manager, dependency policy, architecture boundaries, API contracts, database/storage choices, supported runtime versions, quality gates, CI/CD conventions, branch/release conventions, generated-code directories, documentation paths, test strategy, and project-specific security or compliance rules after copying the package into the target repository root. These values must come from repository files, project documentation, maintainers, and review evidence, not from this generic package.

## User- or organization-dependent configuration

OpenCode account or CLI availability, model/provider choice, permission settings, enabled tools, plugins/MCP, credentials, private endpoints, organization policies, reviewer identities, deployment/release authorization, billing/spending approval, telemetry, and privacy choices remain controlled by the user, team, or administrator. Secrets and credentials must not be stored in this open-source package.

## What must remain fixed in the department package

Responsibility separation, no self-review, no circular delegation, human review for sensitive actions, least privilege, evidence-based completion, no secret exposure, no automatic destructive/external/release action, and honest representation of OpenCode limitations are department invariants.

## Updating and Removal

To update, merge `AGENTS.md`, `opencode.jsonc`, and `.opencode/` changes while preserving local customizations. To remove, delete only this department's copied OpenCode files and empty directories created solely for them. Integrations and credentials are not stored here.
