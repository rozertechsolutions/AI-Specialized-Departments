---
description: Aggregate readiness evidence and stop before publication, deployment, signing, or release.
---

# Release-Readiness Review

## Purpose

Aggregate readiness evidence and stop before publication, deployment, signing, or release.

## Workflow-specific gates

- acceptance evidence
- unresolved defects and risks
- documentation, changelog, and migration readiness
- artifact and version implications
- rollback readiness
- explicit stop before publication, deployment, signing, or release

## Risk triggers

- missing evidence
- known critical issue
- unreviewed change
- incomplete documentation

Any trigger requires Lead classification, possible human approval, and Engineering Risk Reviewer participation where relevant.

## Prompt-only workflow

Route this command through the primary Software Development Lead in `AGENTS.md`. The Lead may use specialist subagents for bounded evidence, but specialists must return to the Lead, cannot recursively delegate, cannot expand scope, and cannot claim final completion.

## Common gates

1. Lead confirms objective, authorized scope, constraints, exclusions, and approval requirements.
2. Requirements and Planning Specialist defines requirements, acceptance criteria, assumptions, and plan when needed.
3. Software Architect provides boundaries, contracts, alternatives, migrations, and compatibility evidence when triggered.
4. Implementation and Maintenance Engineer performs only approved edits and records implementation evidence.
5. Test and Quality Engineer records validation evidence and checks not run.
6. Code Quality Reviewer performs independent review after implementation.
7. Engineering Risk Reviewer reviews security, dependency, performance, reliability, data-integrity, or operational risk when triggered.
8. Documentation and Release Readiness Specialist records documentation, migration, compatibility, versioning, and readiness evidence.
9. Lead aggregates evidence, blockers, limitations, and human decisions.

## Stop conditions

Stop on missing approval, conflicting requirements, secret exposure, unsupported platform behavior, unbounded scope, insufficient evidence, self-review, circular delegation, or any requested Bash, web, Git, MCP, deployment, publication, signing, release, submission, account, credential, purchase, spending, or external communication action.

## Completion evidence

- Requirement-to-change traceability.
- Workflow-specific evidence listed above.
- Validation evidence and checks not run.
- Independent code-quality review.
- Engineering-risk review when triggered.
- Documentation, compatibility, migration, versioning, and readiness status.
- Human decisions and unresolved limitations.
- Lead-controlled final summary with no automatic release, deployment, publication, signing, submission, or Git mutation.
