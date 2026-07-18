# Bug Investigation and Correction

Identifier: `bug-investigation-and-correction`

## Purpose

Find the root cause, apply the smallest safe fix, and prevent regression.

## Common Lifecycle

- Primary Codex session confirms scope, constraints, exclusions, approvals, and specialist routing.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- observable symptom and reproduction path
- affected versions, paths, and inputs
- root-cause explanation before changing code
- minimal correction that does not mask symptoms
- regression evidence that the symptom is fixed

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
