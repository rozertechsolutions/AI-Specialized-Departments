---
name: "create-mobile-project"
description: "Create or plan a new Android, iOS, Kotlin Multiplatform, Flutter, or React Native project using current stable native tooling and explicit human approvals."
---
# Create Mobile Project

Use this skill when the user asks to create, initialize, scaffold, or plan a mobile project.

## Workflow Definition

Objective: create or plan a functional mobile project without secrets, active external integrations, publication, signing, uploads, or fabricated validation.

Trigger: explicit user request for a new mobile project or module.

Inputs: target technology, app name/package/bundle identifiers, supported platforms, minimum OS/SDK targets, UI approach, state/navigation preference if already chosen, test expectations, and release constraints.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, and React Native. Treat any other framework as unsupported unless the repository already uses it and the user explicitly scopes it.

Preconditions:

- Confirm the target technology and destination path.
- Inspect the destination before creating files.
- Detect installed SDKs and project creation commands when available.
- Ask for human approval before dependency installation, external templates, credential use, signing setup, destructive commands, or writes outside scope.

Primary owner: `mobile-architect`.

Reviewers: matching platform engineer, `mobile-test-engineer`, `mobile-security-reviewer` for permissions/privacy/network/auth, `mobile-ui-accessibility-reviewer` for UI requirements, and `mobile-code-reviewer` for final review.

## Steps

1. Classify scope as `required`, `conditionally-required`, or `not-applicable` for each technology requested.
2. Discover local SDK/tool availability and project commands without assuming names.
3. Inspect the target path and refuse to overwrite user files without explicit approval.
4. Choose the stable native project mechanism for the selected technology.
5. Create only files required for a runnable project and relevant tests/docs.
6. Configure no secrets, real endpoints, credentials, signing keys, provisioning profiles, keystores, analytics, telemetry, or external integrations by default.
7. Add initial tests only where the native project format supports them and the tools are available.
8. Run lightweight validation first, then broader non-publishing validation when available and approved.
9. Request independent review and report evidence.

## Validation Gates

- Project files exist only under the approved destination.
- Generated project uses stable native tooling.
- No real credentials or active external integrations.
- Non-publishing build/test/analyze commands are discovered and run when available.
- Unavailable SDKs, devices, simulators, emulators, or commands are reported as unavailable.

## Failures And Stop Conditions

Stop for ambiguous target technology, existing files that would be overwritten, missing required SDKs with no approved alternative, external downloads requiring approval, credentials, signing, publishing, uploads, deployment, cost, or destructive operations.

## Evidence And Outputs

Output project path, created files, detected SDK/tool versions where available, commands run, validation results, not-applicable criteria with reasons, unsupported components omitted, and remaining limitations.

Acceptance criteria: the project is scoped, non-secret, native to the selected platform, validated where possible, and independently reviewed.

Human approvals: required for dependency installation, external templates, writes outside scope, auth/privacy/security-sensitive configuration, dependencies/lockfiles, signing, publishing, upload, deployment, or destructive actions.

Prohibited actions: fake scaffolding, placeholder-only files, unsupported adapters, real signing, store submission, deployment, publishing, spending money, and self-review.
