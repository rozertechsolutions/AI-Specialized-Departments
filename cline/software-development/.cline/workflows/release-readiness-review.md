# Release Readiness Review

Identifier: `release-readiness-review`

## Purpose

Prepare a human release decision without releasing.

## Common Lifecycle

- Main Cline session confirms scope, constraints, exclusions, Plan/Act mode, and approval needs.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- acceptance and validation evidence
- unresolved defects and risks
- documentation, changelog, migration, artifact, and version readiness
- rollback readiness
- explicit stop before publication, deployment, signing, submission, or release

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

## Cline Execution Gates

- Begin in Plan mode for analysis, requirements, risk classification, and validation planning.
- Use built-in subagents only for read-only research or analysis; they cannot edit, browse, use MCP, or delegate.
- Request human approval before Act mode, edits, commands, browser use, external access, sensitive scope, architecture/dependency changes, destructive operations, Git actions, deployment, publication, signing, submission, or release.
- Return evidence to the main session for independent review and final reporting.
