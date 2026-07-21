# GitHub Copilot - Software Development

The Software Development department is a human-reviewed GitHub Copilot specialization for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package uses Copilot repository instructions, modular instructions, custom agents, prompt files, and Skills where supported by the active Copilot surface. It is safe by default: no GitHub Actions, issue automation, PR automation, release automation, or deployment configuration is included.

## Department Overview

Use this department for stack-agnostic software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, and documentation. Web Development and Mobile Development remain separate. The package does not choose a framework, model, provider, database, endpoint, or workflow platform.

## Possible Uses

- Requirements analysis, acceptance criteria, and implementation planning.
- Feature implementation, bug investigation, maintenance, and refactoring.
- Architecture review, API/library evolution, dependency review, security remediation, performance/reliability improvement, technical-debt reduction, and release-readiness review.

## Included Components

- `.github/copilot-instructions.md`: native repository-wide Copilot instructions for supported IDE/CLI/cloud surfaces.
- `.github/instructions/software-development.instructions.md`: native modular repository instruction file.
- `.github/agents/*.agent.md`: seven native custom agent profiles; there is intentionally no Lead agent profile.
- `.github/prompts/*.prompt.md`: native prompt files for repeatable workflow requests.
- `.github/skills/*/SKILL.md`: native Agent Skills packages where Copilot Skills are supported.

## Prerequisites

You need GitHub Copilot access in a supported IDE, Copilot CLI, or Copilot cloud-agent surface that supports the component you intend to use. Custom agents, prompt files, Skills, and repository instructions can be account-, organization-, IDE-, and plan-dependent. Human approval is expected before edits, terminal commands, Git operations, issue/PR actions, deployment, publication, signing, release, or destructive actions.

## Installation or Setup

1. Copy the contents of `github-copilot/software-development/` into the target repository root so `.github/` lands at the root.
2. Merge with existing `.github/copilot-instructions.md`, `.github/instructions/`, `.github/agents/`, `.github/prompts/`, and `.github/skills/` content.
3. Open the target repository in a supported Copilot surface and confirm repository customizations are enabled.
4. Do not add GitHub Actions, issue templates, PR automation, MCP servers, credentials, endpoints, deployment config, or release config as part of this package.

## Usage

Use the primary Copilot chat/agent session as the Software Development Lead. Select specialist custom agents or prompt files from the Copilot UI/CLI where supported, and ask for evidence before completion.

Example requests:

- "Use the planning prompt to produce requirements, risks, and a validation plan."
- "Run the code-quality reviewer agent against this proposed change; do not edit files."
- "Use the release-readiness prompt to summarize blockers and checks not run."

## Operating Model

The Lead remains the primary session and owns scope, routing, approvals, dependency control, and final evidence aggregation. Custom agents are specialists and must return bounded findings to the Lead. Implementation and independent review are separate; engineering-risk review is required for security, dependencies, performance, concurrency, reliability, data integrity, architecture, public contracts, or operations.

## Safety and Human Review

Use least privilege and do not expose secrets. Copilot customization text cannot enforce all IDE, CLI, or GitHub-hosted actions. Do not allow automatic commits, pushes, PR creation/merge, issue updates, deployment, publication, signing, release, external messages, spending, submissions, destructive operations, credential use, or authentication without explicit task-specific authorization.

## Platform Limitations

Copilot customization support varies by IDE, CLI, GitHub.com cloud agent, organization policy, and plan. Agent profiles and Skills may not be available in every surface. This package intentionally contains no GitHub Actions, issue automation, PR automation, release automation, MCP config, hooks, provider/model pins, endpoints, credentials, or Lead agent profile.

## Project-dependent configuration

Adapt repository/module paths, source/test/resource directories, languages, frameworks, libraries, build/test/lint/type-check commands, package manager, dependency policy, architecture boundaries, API contracts, database/storage choices, supported runtime versions, quality gates, CI/CD conventions, branch/release conventions, generated-code directories, documentation paths, test strategy, and project-specific security or compliance rules after copying the package into the target repository root. These values must come from repository files, project documentation, maintainers, and review evidence, not from this generic package.

## User- or organization-dependent configuration

GitHub Copilot account, plan, repository or organization policy, model choice, IDE/GitHub surface availability, enabled tools, MCP/connectors, credentials, private endpoints, reviewer identities, deployment/release authorization, billing/spending approval, telemetry, and privacy choices remain controlled by the user, team, or administrator. Secrets and credentials must not be stored in this open-source package.

## What must remain fixed in the department package

Responsibility separation, no self-review, no circular delegation, human review for sensitive actions, least privilege, evidence-based completion, no secret exposure, no automatic destructive/external/release action, and honest representation of GitHub Copilot limitations are department invariants.

## Updating and Removal

To update, merge changed `.github/` customization files while preserving local repository policy. To remove, delete only this department's copied Copilot instruction, agent, prompt, and Skill files. Integrations, credentials, and GitHub app settings are not stored here.
