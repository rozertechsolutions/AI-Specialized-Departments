# Review Checklists

Use these checklists as Claude Project knowledge. They support the authoritative operating model and do not define separate repository agents.

## Code-Quality Review

- Requirements and scope are traceable.
- Correctness, readability, complexity, duplication, architecture fit, and compatibility are assessed.
- The reviewer did not implement the substantive change under review.
- Findings include severity, evidence, and required correction or acceptance rationale.

## Engineering-Risk Review

- Security, trust boundaries, input handling, dependencies, supply chain, performance, concurrency, failure handling, reliability, and data integrity are assessed when applicable.
- Findings distinguish verified facts from inferences.
- Sensitive details are reported without exposing secrets or exploit-enabling payloads unnecessarily.

## Release Readiness

- Validation evidence, independent reviews, documentation, migrations, versioning implications, remaining risks, and unexecuted checks are explicit.
- Artifact, compatibility, rollback, and human decision implications are clear.
- No publication, deployment, signing, submission, or release is performed.
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
