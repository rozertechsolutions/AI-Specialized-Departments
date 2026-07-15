---
name: create-mobile-project
description: Create or initialize a scoped Android, iOS, KMP, Flutter, or React Native mobile project with safe validation gates.
---

# Create Mobile Project

## Objective

Create or initialize a mobile project only after the platform, name, package or bundle identifiers, targets, and acceptance criteria are explicit.

## Trigger

Use when the user asks to create, initialize, scaffold, or add a new mobile project.

## Inputs

Project name, target technology, package or bundle identifiers, minimum OS versions, desired modules, UI framework, test expectations, and constraints.

## Supported Technologies

Android, iOS, Kotlin Multiplatform, Flutter, and React Native.

## Preconditions

- Inspect the destination and existing files before writing.
- Verify toolchain availability with safe read-only commands.
- Confirm identifiers and signing-related values with the user; never invent them.
- Classify any requested generator, template, external service, or integration as native, conditionally native, or unsupported.

## Primary Owner

`mobile-architect` owns structure. The platform engineer owns platform-specific files after architecture is approved.

## Reviewers

`mobile-security-reviewer`, `mobile-test-engineer`, and `mobile-code-reviewer`. Add `mobile-release-engineer` only for variants or release metadata.

## Steps

1. Inspect repository layout, status, docs, and applicable `AGENTS.md`.
2. Identify the exact project surface and current tool versions.
3. Choose the smallest native structure that satisfies the request.
4. Stop for human approval before dependency, SDK, signing, publishing, external integration, lockfile, or credential changes.
5. Generate or create files only through native stable tooling or explicit repository conventions.
6. Add minimal tests and documentation required by the project convention.
7. Run targeted validation, then broader reasonable checks.
8. Collect independent review findings and correct in-scope issues.

## Conditional Steps

- If required identifiers, signing values, or product decisions are missing, stop and ask the user.
- If a requested generator or integration is unsupported, omit it and record the omission.
- If a dependency or lockfile change is necessary, stop for human approval before editing.
- If validation infrastructure is unavailable, report it as unavailable with the exact blocker.

## Validation Gates

Project configuration, dependency resolution, unsigned compile/build where available, unit tests, static analysis, formatting/lint, secret review, and independent code review are required. UI/accessibility, localization, performance, and release checks are conditional on project scope.

## Failures and Stop Conditions

Stop on missing identifiers, unavailable toolchains, ambiguous ownership, requested unsupported capability, credentials, signing, publication, destructive operations, conflicting user changes, or validation failures not caused by this work.

## Evidence

Record detected tools and versions, files created, commands run, command results, skipped checks with reasons, and official docs consulted.

## Outputs

A working scoped project, validation evidence, responsibility assignment, and remaining human actions.

## Acceptance Criteria

The project is native to the selected platform, builds or reports exact blockers, includes required tests/docs, contains no secrets, and has no active external integration.

## Human Approvals

Required for dependency additions, lockfiles, identifiers if absent, signing config, credentials, external writes, paid services, destructive actions, and publication.

## Prohibited Actions

Do not sign, publish, upload, submit, deploy, distribute, spend money, use real credentials, or fabricate validation.
