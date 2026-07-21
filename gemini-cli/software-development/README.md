# Gemini CLI - Software Development

The Software Development department is a human-reviewed Gemini CLI specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package uses Gemini CLI project context, settings, subagents, custom commands, and Skills without enabling providers, endpoints, MCP, hooks, extensions, shell automation, or credentials. It is safe by default: the main Gemini CLI agent is the Lead, specialists are bounded, and approval mode remains human-controlled.

## Department Overview

Use this department for stack-agnostic software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Browser-specific Web Development and mobile-platform Mobile Development remain separate. The package does not choose a model, provider, database, framework, or endpoint.

## Possible Uses

- Requirements decomposition, acceptance criteria, risk identification, and planning.
- Feature work, bug investigation, maintenance, and controlled refactoring.
- Architecture review, API/library evolution, dependency review, security remediation, performance/reliability work, technical-debt reduction, and release-readiness review.

## Included Components

- `GEMINI.md`: native Gemini CLI project context for the main Lead agent.
- `.gemini/settings.json`: native project settings that set default approval mode and enable Plan mode without adding credentials or integrations.
- `.gemini/agents/*.md`: seven native subagents exposed to the main agent as delegation tools; there is no Lead subagent.
- `.gemini/commands/software-development/*.toml`: native project custom slash commands in Gemini CLI TOML format.
- `.gemini/skills/*/SKILL.md`: native Agent Skills packages when Skills are supported by the installed Gemini CLI.

## Prerequisites

You need Gemini CLI with project settings, custom commands, subagents, and Skills support. Authentication and model selection are configured by the user outside this package. Human approval is required for edits, shell commands, external access, dependency changes, Git mutation, deployment, publication, signing, release, or destructive actions.

## Installation or Setup

1. Copy the contents of `gemini-cli/software-development/` into the target repository root so `GEMINI.md` and `.gemini/` land at the root.
2. Merge with existing target `.gemini/settings.json`, `.gemini/agents/`, `.gemini/commands/`, and `.gemini/skills/` files.
3. Start Gemini CLI from the target repository root.
4. Use `/commands reload` if the running session needs to pick up changed custom command files.
5. Do not add MCP servers, hooks, extensions, sandbox builders, providers, model pins, endpoints, credentials, or shell helpers for this package.

## Usage

Use the main Gemini CLI session as the Software Development Lead. The Lead may auto-delegate or be prompted to call a specialist subagent with `@<agent-name>` where supported, and workflow commands are available under the `software-development` namespace.

Example requests:

- "Plan this feature and wait for approval before edits."
- "@software-architect review this API migration for compatibility risk."
- "/software-development:release-readiness-review summarize evidence and blockers."

## Operating Model

The Lead owns scope, routing, approvals, dependency control, and final evidence aggregation. Specialists return evidence, do not recursively delegate, and do not claim final completion. Implementation must be followed by independent code-quality review, with engineering-risk review when security, dependencies, performance, concurrency, reliability, data integrity, architecture, public contracts, or operations are affected.

## Safety and Human Review

Use least privilege and protect secrets. Gemini CLI settings and subagent tool allowlists help guide behavior, but parent CLI flags, user settings, and system settings can override project expectations. Do not allow automatic Git mutation, deployment, publication, signing, release, spending, submissions, destructive operations, credential use, external authentication, or shell commands without explicit approval.

## Platform Limitations

Gemini CLI custom command, subagent, and Skill behavior depends on the installed version and active settings. This package intentionally omits ineffective workspace policy files, hooks, MCP, extensions, providers, model pins, endpoints, credentials, sandbox builders, deployment automation, publication automation, signing automation, and release automation.

## Updating and Removal

To update, merge `GEMINI.md` and `.gemini/` changes while preserving local settings and commands. To remove, delete only this department's copied Gemini files and empty directories created solely for them. Authentication, providers, credentials, and integrations are not stored here.
