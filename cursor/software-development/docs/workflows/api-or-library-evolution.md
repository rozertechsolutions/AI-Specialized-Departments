# API or Library Evolution

Identifier: `api-or-library-evolution`

## Purpose

Evolve contracts with compatibility, migration, and examples.

## Common Lifecycle

- Primary Cursor Agent confirms scope, constraints, exclusions, approvals, and applicable rule/Skill guidance.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- consumer impact analysis
- contract, schema, source, binary, and behavioral compatibility
- versioning and deprecation plan
- migration notes and examples
- contract tests or explicit untested areas

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
