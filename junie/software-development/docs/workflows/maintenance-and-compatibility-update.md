# Maintenance and Compatibility Update

Identifier: `maintenance-and-compatibility-update`

## Purpose

Keep supported environments and contracts working during maintenance.

## Common Lifecycle

- Main Junie agent confirms scope, constraints, exclusions, approvals, and applicable Skill/workflow guidance.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- supported environment and contract matrix
- migration, deprecation, data, and configuration implications
- fallback behavior
- compatibility evidence
- explicit non-goals for unrelated modernization

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

## Junie Routing

- The main Junie agent remains Software Development Lead and routes work through responsibility phases rather than repository subagents.
- Use `.junie/skills/` for reusable procedures; this workflow file is auxiliary unless Junie natively loads it in the target environment.
- Request human approval before sensitive scope, architecture/dependency changes, edits, command execution, external access, destructive operations, Git actions, deployment, publication, signing, submission, or release.
