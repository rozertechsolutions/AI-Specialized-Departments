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

Any trigger requires Cascade Lead classification, possible human approval, and engineering-risk review where relevant.

## Common lifecycle

1. Cascade Lead confirms objective, authorized scope, constraints, exclusions, and approval requirements.
2. Requirements stage defines requirements, acceptance criteria, assumptions, and plan when needed.
3. Architecture stage provides boundaries, contracts, alternatives, migrations, and compatibility evidence when triggered.
4. Implementation stage performs only approved edits and records implementation evidence.
5. Validation stage records acceptance, regression, edge-case evidence, and checks not run.
6. Independent code-quality stage reviews after implementation.
7. Engineering-risk stage reviews security, dependency, performance, reliability, data-integrity, or operational risk when triggered.
8. Documentation/readiness stage records documentation, migration, compatibility, versioning, and readiness evidence.
9. Cascade Lead aggregates evidence, blockers, limitations, and human decisions.

## Stop conditions

Stop on missing approval, conflicting requirements, secret exposure, unsupported Windsurf behavior, unbounded scope, insufficient evidence, self-review, circular routing, or any requested edit of sensitive scope, architecture change, dependency change, command execution, external access, MCP, hook, background job, deployment, publication, signing, release, destructive operation, Git mutation, account action, credential action, purchase, spending, or external communication without explicit human approval.

## Completion evidence

- Requirement-to-change traceability.
- Workflow-specific evidence listed above.
- Validation evidence and checks not run.
- Independent code-quality review.
- Engineering-risk review when triggered.
- Documentation, compatibility, migration, versioning, and readiness status.
- Human decisions and unresolved limitations.
- Cascade Lead final summary with no automatic command execution, external access, destructive operation, Git mutation, deployment, publication, signing, release, or submission.
