# Claude - Software Development

The Software Development department is a human-reviewed specialization for requirements, planning, architecture, implementation support, validation, independent code review, engineering risk review, documentation, and release readiness. This Claude package represents the department as manual Claude Project, Project knowledge, optional Skill, and connector-policy source material. It is safe by default: no repository file auto-loads in Claude, no connector is enabled here, and external actions require explicit human approval.

## Department Overview

Use this department for general software engineering across backend services, APIs, desktop apps, command-line apps, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, and documentation. Browser-specific Web Development and mobile-platform Mobile Development remain separate. The package is stack-agnostic and does not prescribe a language, framework, database, provider, or model.

## Possible Uses

- Define requirements, acceptance criteria, assumptions, exclusions, and a plan.
- Investigate a bug and produce a safe correction strategy.
- Review architecture, API/library evolution, dependency changes, security remediation, performance/reliability work, or technical-debt reduction.
- Prepare validation evidence, compatibility notes, documentation updates, and release-readiness findings.

## Included Components

- `project/project-instructions.md`: manual Claude Project instructions; paste into the Project instructions field.
- `project/knowledge/`: manual Project knowledge files for operating model, quality gates, safety policy, and workflows.
- `project/review-checklists.md`: auxiliary Project knowledge for manual review checks.
- `skills/`: conditional Claude Skill source packages; import only where Skills are available for the account/workspace.
- `connectors/connectors-policy.md`: manual policy text for connector use; it does not enable pre-built or custom connectors.

This package intentionally contains no Claude Code files.

## Prerequisites

You need Claude with Projects for the Project setup, an account/workspace that supports Skills before importing `skills/`, and administrator permission where connector or workspace policy applies. You need authorization to share the selected repository or project context. Human review is required before edits, tool use, connector authorization, Git mutation, deployment, publication, signing, release, or destructive work.

## Installation or Setup

1. Create or open the destination Claude Project in the Claude UI.
2. Paste `project/project-instructions.md` into the Project instructions field.
3. Add selected files from `project/knowledge/` and `project/review-checklists.md` as Project knowledge.
4. If Claude Skills are supported and allowed, import each `skills/<skill-name>/` folder through the current Skill UI.
5. Keep `connectors/connectors-policy.md` as manual policy text. Enable no connector unless a human approves that exact connector in Claude.

Do not copy credentials, private endpoints, account identifiers, or secrets into Claude setup fields.

## Usage

Start a chat inside the configured Claude Project or Skill-enabled surface. Ask the Lead to confirm objective, scope, exclusions, approvals, and evidence needs before any implementation guidance.

Example requests:

- "Convert this request into requirements, acceptance criteria, risks, and a staged implementation plan."
- "Review this dependency update for compatibility and supply-chain risk; do not change files."
- "Assess release readiness from these validation notes and identify unresolved blockers."

## Operating Model

The Claude conversation acts as the Software Development Lead. The Lead routes work through the seven specialist responsibilities, keeps implementation separate from code-quality and risk review, and aggregates final evidence. Specialists are represented through Project instructions, knowledge, Skills, and requested review phases rather than autonomous Claude Code subagents.

## Safety and Human Review

Use least privilege and only upload context needed for the task. Claude textual instructions cannot enforce every product action, so users and workspace admins must control file access, connectors, code execution, and external integrations. Do not allow automatic Git mutation, deployment, publication, signing, release, spending, submissions, destructive operations, or credential handling without explicit task-specific approval.

## Platform Limitations

Claude Projects and Skills are account-, plan-, workspace-, and policy-dependent. Connectors are configured in Claude, not by these files. This package does not include `CLAUDE.md`, `.claude/`, Claude Code settings, Claude Code subagents, hooks, MCP server config, shell helpers, or repository-native automation.

## Updating and Removal

To update, replace the pasted Project instructions, selected Project knowledge, and imported Skills after preserving local edits. To remove, delete only this department's Project instructions, knowledge files, Skills, and connector-policy text from Claude. No integrations, credentials, or account settings are stored in this package.
