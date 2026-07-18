# Controlled Refactoring

Identifier: `controlled-refactoring`

## Purpose

Improve structure while preserving external behavior.

## Common Lifecycle

- Main Cline session confirms scope, constraints, exclusions, Plan/Act mode, and approval needs.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- explicit invariants and public behavior that must not change
- bounded transformation plan
- compatibility evidence before and after
- regression checks focused on unchanged behavior
- rollback or reversal plan

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
