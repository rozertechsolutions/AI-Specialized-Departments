# Cline - Software Development

The Software Development department is a human-reviewed Cline specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package uses Cline project rules, Skills, workflows, and ignore rules without creating unsupported project agents. It is safe by default: Plan/Act approval remains human-controlled and no file here enables hooks, MCP, browser use, shell execution, or auto-approval.

## Department Overview

Use this department for stack-agnostic software work: backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Browser-specific frontend work belongs in Web Development; mobile-platform work belongs in Mobile Development. The package does not select a language, framework, database, provider, model, or runtime.

## Possible Uses

- Convert a request into requirements, acceptance criteria, risks, and a plan.
- Investigate a defect and prepare a safe correction.
- Execute approved feature work, maintenance, or refactoring with validation evidence.
- Review architecture, dependency, security, performance, reliability, technical-debt, compatibility, and release-readiness concerns.

## Included Components

- `.clinerules/*.md`: native Cline project rules that apply when Cline loads rules from the target workspace.
- `.cline/skills/*/SKILL.md`: native project Skill packages for reusable procedures.
- `.cline/workflows/*.md`: native workflow prompt files where supported by the installed Cline surface; otherwise useful prompt references.
- `.clineignore`: native ignore file for secrets, credentials, generated outputs, and heavy irrelevant artifacts.

There is intentionally no `.cline/agents/` directory because this package does not rely on an unsupported repository-defined agent mechanism.

## Prerequisites

You need Cline in a supported IDE or CLI surface and access to the target repository. Project rules, Skills, workflows, Plan mode, Act mode, and approval behavior depend on the installed Cline version and user settings. Keep Auto Approve, YOLO, MCP, browser, and shell capabilities disabled unless explicitly approved for a separate task.

## Installation or Setup

1. Copy the contents of `cline/software-development/` into the target repository root so `.clinerules/`, `.cline/`, and `.clineignore` land at the root.
2. Merge with any existing `.clinerules/`, `.cline/skills/`, `.cline/workflows/`, or `.clineignore` entries instead of overwriting local policy.
3. Open the target repository in Cline.
4. Confirm Cline is in Plan mode for non-trivial work and that approval settings require human review before Act-mode edits or command execution.

## Usage

Start with the main Cline session as the Software Development Lead. Ask it to plan first, route specialist responsibilities through rules/Skills/workflows, and wait for explicit approval before implementation.

Example requests:

- "Plan this refactor and list validation evidence before Act mode."
- "Use the security and dependency review guidance for this package update."
- "Investigate this bug, propose the smallest fix, and wait before editing."

## Operating Model

The main Cline session owns scope, routing, approvals, and final evidence. Implementation must be separated from independent code-quality review. Engineering-risk review is required when security, dependencies, performance, concurrency, reliability, data integrity, architecture, or public contracts are affected. Completion requires observed evidence and a list of checks not run.

## Safety and Human Review

Use least privilege. `.clineignore` reduces accidental exposure but does not replace user review. Do not allow automatic Git mutation, deployment, publication, signing, release, external messages, spending, destructive operations, credential access, browser use, MCP access, or shell commands without explicit task-specific approval.

## Platform Limitations

Cline rules are project-scoped to the workspace Cline recognizes, and multi-root behavior can affect loading. Workflow and Skill support depends on the current Cline surface. This package omits hooks, plugins, MCP configuration, Auto Approve/YOLO settings, shell helpers, credentials, endpoints, and simulated project agents.

## Updating and Removal

To update, merge changed files in `.clinerules/`, `.cline/skills/`, `.cline/workflows/`, and `.clineignore` while preserving local customizations. To remove, delete only this department's copied rules, Skills, workflows, and ignore entries; remove empty directories only if they were created solely for this package.
