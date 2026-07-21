# Cline Quality and Completion

A task is complete only when:

1. Requirements, scope, assumptions, exclusions, and acceptance criteria are explicit.
2. Changes are limited to approved scope and existing repository conventions.
3. Validation evidence or checks not run are listed clearly.
4. Independent code-quality review follows implementation.
5. Engineering-risk review occurs when security, dependencies, performance, concurrency, reliability, data integrity, architecture, or public contracts are affected.
6. Documentation, migration, compatibility, and versioning implications are addressed.
7. Remaining risks, limitations, and human decisions are explicit.
8. Release readiness is assessed without publishing, deploying, signing, submitting, or releasing.

The same phase must not both implement a substantive change and independently certify it.
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
