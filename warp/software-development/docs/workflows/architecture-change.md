# Architecture Change

## Purpose

Change architecture only with decision evidence, migration controls, risk review, rollback, and independent architecture approval.

## Workflow-specific gates

- decision record
- alternatives and trade-offs
- boundaries and contracts
- migration stages
- compatibility plan
- risk review
- rollback
- independent architecture approval

## Risk triggers

- boundary change
- new architectural pattern
- migration
- compatibility risk

Any trigger requires primary Lead classification, possible human approval, and engineering-risk review where relevant.

## Documentation boundary

This is auxiliary Software Development process reference documentation. It is not a native Warp Drive Workflow object, not imported automatically, not auto-loaded as Project Rules or Skills, and not executable.

## Common lifecycle

1. Primary Warp Agent confirms objective, authorized scope, constraints, exclusions, and approval requirements.
2. Requirements stage defines requirements, acceptance criteria, assumptions, and plan when needed.
3. Architecture stage provides boundaries, contracts, alternatives, migrations, and compatibility evidence when triggered.
4. Implementation stage performs only explicitly approved edits and records implementation evidence.
5. Validation stage records acceptance, regression, edge-case evidence, and checks not run.
6. Independent code-quality stage reviews after implementation.
7. Engineering-risk stage reviews security, dependency, performance, reliability, data-integrity, or operational risk when triggered.
8. Documentation/readiness stage records documentation, migration, compatibility, versioning, and readiness evidence.
9. Primary Lead aggregates evidence, blockers, limitations, and human decisions.

## Stop conditions

Stop on missing approval, conflicting requirements, secret exposure, unsupported Warp behavior, unbounded scope, insufficient evidence, self-review, circular routing, or any requested terminal command, edit, Git action, external action, MCP, connector, cloud/background schedule, deployment, publication, signing, release, submission, account, credential, purchase, spending, or external communication action without explicit interactive human approval.

## Completion evidence

- Requirement-to-change traceability.
- Workflow-specific evidence listed above.
- Validation evidence and checks not run.
- Independent code-quality review.
- Engineering-risk review when triggered.
- Documentation, compatibility, migration, versioning, and readiness status.
- Human decisions and unresolved limitations.
- Primary Lead final summary with no automatic terminal command, edit, Git mutation, external action, release, deployment, publication, signing, or submission.
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
