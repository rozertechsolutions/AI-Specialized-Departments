---
description: Improve performance or resilience from an observed baseline or explicitly stated absence of one.
---

# Performance and Reliability Improvement

## Purpose

Improve performance or resilience from an observed baseline or explicitly stated absence of one.

## Workflow-specific gates

- observed baseline or absence of baseline
- hypothesis
- resource, concurrency, and failure analysis
- correctness guardrails
- evidence
- regression risk

## Risk triggers

- concurrency
- resource consumption
- failure handling
- data integrity

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
## Operational Notes

- Purpose / mission: This component supports the Software Development department responsibility described above and keeps that responsibility separate from planning, implementation, independent review, risk review, documentation, and release authority.
- When it is used: Use it only when the installed platform surface loads this file natively or when the Lead explicitly imports, invokes, or references it for a scoped software-development task.
- Inputs / expected context: Provide the target project objective, authorized paths, relevant source/test/resource directories, language, framework, package manager, commands, architecture constraints, API contracts, dependency policy, and acceptance criteria from the target repository.
- Outputs / completion evidence: Return concrete findings, plans, edits, validation results, review notes, limitations, and checks not run to the Lead; final completion requires evidence rather than assumption.
- Concrete example: Ask for a scoped API compatibility review, a bug-fix plan, an approved implementation step, or an independent code-quality review without secrets or external actions.
- Project-dependent elements: Repository layout, build/test/lint/type-check commands, generated-code areas, supported runtimes, CI/CD conventions, documentation paths, test strategy, and security/compliance requirements must be discovered from the target project.
- User- or organization-dependent elements: Account or plan availability, model/provider selection, permission mode, tools, connectors, MCP servers, credentials, private endpoints, reviewers, billing, telemetry, and deployment/release authority remain controlled outside this package.
- Fixed department constraints: Preserve responsibility boundaries, no self-review, no circular delegation, least privilege, human review for sensitive changes, no secret exposure, no automatic destructive/external/release action, and evidence-based completion.
- Limitations: Textual instructions cannot override platform permissions, managed policy, product availability, or human approval requirements.
