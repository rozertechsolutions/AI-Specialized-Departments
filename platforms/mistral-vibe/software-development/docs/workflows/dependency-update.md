# Dependency Update

## Purpose

Change dependencies only after need, provenance, compatibility, and rollback are clear.

## Entry conditions

- A named human-requested objective exists.
- The authorized repository scope is known.
- Acceptance criteria or the maintenance objective can be verified.
- Required approvals are identified before any sensitive or irreversible action.

## Workflow-specific focus

- demonstrated need for the dependency action
- provenance, maintenance status, license signals, and vulnerability context
- transitive dependency and lockfile impact
- compatibility evidence for supported environments
- rollback plan

## Risk triggers

- new transitive dependencies
- major version
- license change
- security advisory

Any trigger requires Engineering Risk Reviewer participation and may require explicit human approval before implementation.

## Common stages

1. **Intake - Software Development Lead:** confirm objective, authorized scope, exclusions, constraints, and required human approvals.
2. **Requirements - Requirements and Planning Specialist:** define requirements, acceptance criteria, assumptions, and unresolved questions.
3. **Context analysis - assigned specialist:** inspect only necessary repository context and return factual evidence to the Lead.
4. **Risk classification - Software Development Lead:** identify required reviews, approval checkpoints, and stop conditions.
5. **Design or plan - Software Architect or Requirements and Planning Specialist:** define contracts, ordered changes, validation strategy, and rollback considerations where applicable.
6. **Human checkpoint:** obtain explicit approval before sensitive, irreversible, dependency, architecture, public-contract, migration, permission, trust-boundary, or scope-changing decisions.
7. **Implementation - Implementation and Maintenance Engineer:** make only approved changes and return implementation evidence.
8. **Validation - Test and Quality Engineer:** evaluate acceptance, regression, edge cases, and every unexecuted check.
9. **Independent code review - Code Quality Reviewer:** review correctness, maintainability, architecture fit, compatibility, and unintended effects.
10. **Independent risk review - Engineering Risk Reviewer when triggered:** review security, dependencies, supply chain, performance, concurrency, reliability, data integrity, and operational risk.
11. **Documentation/readiness - Documentation and Release Readiness Specialist:** update required documentation and assess readiness without release execution.
12. **Close - Software Development Lead:** aggregate returned evidence, blockers, limitations, and human decisions.

## Stop conditions

Stop and escalate on missing approval, conflicting requirements, secret exposure, unsupported behavior, unbounded scope, unavailable evidence, failed critical validation, circular delegation, self-review, or any requested Bash, web, MCP, Git, deployment, publication, signing, release, submission, account, credential, or external communication action.

## Completion evidence

- Requirement-to-change traceability.
- Workflow-specific evidence listed above.
- Acceptance and validation matrix.
- Independent code-quality outcome.
- Engineering-risk outcome when triggered.
- Documentation, compatibility, migration, and readiness status.
- Explicit list of tests and checks not run.
- Human-controlled release-readiness verdict aggregated only by the Software Development Lead.
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
