# Dependency Update

Identifier: `dependency-update`

## Purpose

Change dependencies only with need, provenance, and rollback evidence.

## Common Lifecycle

- Primary Cursor Agent confirms scope, constraints, exclusions, approvals, and applicable rule/Skill guidance.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- demonstrated need for the dependency change
- provenance, maintenance, license, and vulnerability signals
- transitive and lockfile impact
- compatibility validation
- rollback path to the previous dependency state

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

## Cursor Routing

- The primary Cursor Agent remains Lead and routes specialist work through native project subagents.
- Use `.cursor/rules/` and `.cursor/skills/` as native guidance; treat this workflow file as auxiliary unless the environment natively loads it.
- Request human approval before sensitive scope, architecture/dependency changes, edits, command execution, external access, destructive operations, Git actions, deployment, publication, signing, submission, or release.
