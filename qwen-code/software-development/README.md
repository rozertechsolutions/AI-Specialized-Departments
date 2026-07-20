# Qwen Code - Software Development

The Software Development department is a human-reviewed Qwen Code specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package uses Qwen Code native project memory, settings, subagents, Skills, and Markdown custom commands. It is safe by default: the parent session must stay in default approval mode, specialists deny shell execution, and no hooks, MCP, provider, endpoint, credential, or automation config is included.

## Department Overview

Use this department for stack-agnostic software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Web Development and Mobile Development remain separate. The package does not select a provider, model, endpoint, framework, database, or account.

## Possible Uses

- Requirements analysis, acceptance criteria, constraints, risks, and planning.
- New feature development, bug investigation, maintenance, and controlled refactoring.
- Architecture review, API/library evolution, dependency review, security remediation, performance/reliability improvement, technical-debt reduction, compatibility updates, and release-readiness review.

## Included Components

- `QWEN.md`: native project memory/instructions for the main Lead session.
- `.qwen/settings.json`: native project settings that keep tool approval mode at `default`.
- `.qwen/agents/*.md`: seven native specialist subagents; there is intentionally no Lead subagent.
- `.qwen/skills/*/SKILL.md`: native Agent Skills packages.
- `.qwen/commands/*.md`: native Markdown custom commands with optional YAML frontmatter.

## Prerequisites

You need Qwen Code with project settings, QWEN.md memory, subagents, Skills, and Markdown custom command support. Authentication, model/provider selection, and any paid plan are configured outside this package. Human approval is expected before edits, shell commands, external access, dependency changes, Git mutation, deployment, publication, signing, release, or destructive actions.

## Installation or Setup

1. Copy the contents of `qwen-code/software-development/` into the target repository root so `QWEN.md` and `.qwen/` land at the root.
2. Merge with existing target `QWEN.md`, `.qwen/settings.json`, `.qwen/agents/`, `.qwen/skills/`, and `.qwen/commands/`.
3. Start Qwen Code from the target repository root in `default` approval mode.
4. Do not use permissive parent modes such as auto-edit or yolo for this department.
5. Do not add TOML commands, hooks, MCP, extensions, sandbox builders, providers, model pins, endpoints, credentials, or shell helpers.

## Usage

Use the main Qwen Code session as the Software Development Lead. The Lead can delegate to named subagents or use Markdown commands where supported, then collect evidence.

Example requests:

- "Plan this bug fix and wait before writing files."
- "Use the software-architect subagent to review this migration risk."
- "/release-readiness-review summarize evidence and unresolved blockers."

## Operating Model

The Lead owns scope, routing, approvals, dependency control, and final evidence aggregation. Specialists return evidence, cannot call each other, cannot expand scope, and cannot claim final completion. Implementation must be followed by independent code-quality review, with engineering-risk review when security, dependencies, performance, concurrency, reliability, data integrity, architecture, public contracts, or operations are affected.

## Safety and Human Review

Use least privilege and protect secrets. Project settings and subagent tool allowlists do not defeat permissive parent CLI flags or managed policy. Do not allow automatic Git mutation, deployment, publication, signing, release, external messages, spending, submissions, destructive actions, credential use, authentication, or shell commands without explicit task-specific approval.

## Platform Limitations

Qwen Code feature behavior depends on installed version and configuration precedence: defaults, system defaults, user settings, project settings, system settings, environment variables, and command-line arguments. Markdown commands are current; TOML commands are deprecated. This package omits shell grants, hooks, MCP, extensions, providers, endpoints, credentials, sandbox builders, deployment automation, publication automation, signing automation, release automation, and a Lead subagent.

## Updating and Removal

To update, merge `QWEN.md` and `.qwen/` changes while preserving local customizations. To remove, delete only this department's copied Qwen files and empty directories created solely for them. Integrations and credentials are not stored here.
