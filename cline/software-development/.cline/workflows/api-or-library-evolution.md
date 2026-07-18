# API or Library Evolution

Identifier: `api-or-library-evolution`

## Purpose

Evolve contracts with compatibility, migration, and examples.

## Common Lifecycle

- Main Cline session confirms scope, constraints, exclusions, Plan/Act mode, and approval needs.
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

## Cline Execution Gates

- Begin in Plan mode for analysis, requirements, risk classification, and validation planning.
- Use built-in subagents only for read-only research or analysis; they cannot edit, browse, use MCP, or delegate.
- Request human approval before Act mode, edits, commands, browser use, external access, sensitive scope, architecture/dependency changes, destructive operations, Git actions, deployment, publication, signing, submission, or release.
- Return evidence to the main session for independent review and final reporting.
