---
name: independent-code-review
description: Review a change independently for correctness, maintainability, architecture fit, and unintended effects.
---

# Independent Code Review

## Mission

Review a change independently for correctness, maintainability, architecture fit, and unintended effects.

## Use when

- completed implementation
- refactor
- bug fix

## Inputs

- change set
- requirements
- repository conventions

## Preconditions

- The task scope and authorized repository area are known.
- Required human approvals are available before sensitive actions.
- Existing project conventions take precedence over generic preferences.

## Procedure

1. Confirm scope, constraints, assumptions, and exclusions.
2. Gather only the evidence necessary for this Skill.
3. Apply the smallest complete professional method.
4. Record findings and distinguish facts from inferences.
5. Escalate decisions outside this Skill's exclusive scope.
6. Return structured evidence to the owning role.

## Outputs

- review findings
- severity and evidence
- approval or correction request

## Failure behavior

Stop without fabricating a result when evidence, permissions, product support, or required context is missing. State exactly what remains unresolved.

## Human review

Human approval is mandatory for destructive, external, dependency, architecture, public-contract, migration, release, deployment, publication, signing, submission, credential, or permission changes.

## Prohibited actions

- Silent scope expansion or unrelated modifications.
- Secret or credential exposure.
- Invented validation results.
- Automatic Git, release, deployment, publication, signing, submission, installation, authentication, or destructive operations.

## Completion criteria

The output is scoped, traceable, evidence-based, compatible with project conventions, explicit about unexecuted checks, and ready for independent review.
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
