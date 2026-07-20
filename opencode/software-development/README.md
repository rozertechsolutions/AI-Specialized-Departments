# OpenCode - Software Development

The Software Development department is a human-reviewed OpenCode specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package uses OpenCode native rules, JSONC config, specialist agents, Skills, and commands. It is safe by default: fallback permissions ask, Bash and web fetch are denied, edits require approval, and no MCP, provider, endpoint, credential, hook, or automation is included.

## Department Overview

Use this department for stack-agnostic software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Web Development and Mobile Development remain separate. The package does not select a framework, database, provider, model, endpoint, or account.

## Possible Uses

- Requirements analysis, acceptance criteria, constraints, risks, and planning.
- New feature development, bug investigation, maintenance, and controlled refactoring.
- Architecture review, API/library evolution, dependency review, security remediation, performance/reliability improvement, technical-debt reduction, compatibility updates, and release-readiness review.

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

## Updating and Removal

To update, merge `AGENTS.md`, `opencode.jsonc`, and `.opencode/` changes while preserving local customizations. To remove, delete only this department's copied OpenCode files and empty directories created solely for them. Integrations and credentials are not stored here.
