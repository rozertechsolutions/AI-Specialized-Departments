# Security Remediation

Identifier: `security-remediation`

## Purpose

Correct a software weakness without unsafe disclosure or broad churn.

## Common Lifecycle

- Primary Codex session confirms scope, constraints, exclusions, approvals, and specialist routing.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- threat or weakness statement
- affected trust boundary and exploitability assumptions
- secret-safe handling and disclosure-safe reporting
- least-change remediation
- regression evidence for the weakness and related behavior

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

## Codex Routing

- The primary session remains Lead and may delegate once to a matching specialist under `[agents].max_depth = 1`.
- Specialists return evidence to the primary session and never delegate recursively.
- Workflow guidance is auxiliary documentation and is not auto-loaded as a Codex workflow engine.
