---
name: create-mobile-project
description: Workflow for creating a new mobile project across Android, iOS, Kotlin Multiplatform, Flutter, or React Native with native tooling and safe validation.
---

# Create Mobile Project

## Objective

Create a mobile project using stable native tooling for the requested technology without secrets, real endpoints, signing material, publishing, or unsupported scaffolding.

## Trigger

Use when the user asks to create, scaffold, initialize, or configure a new mobile project.

## Inputs

Target technology, app name, package or bundle identifier, supported platforms, minimum versions, UI approach, test expectations, and local tooling constraints.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native when their official local tooling is available.

## Preconditions

Confirm target platform, inspect destination, discover installed tooling and project commands, and ask before dependency downloads or external templates.

## Primary Owner

`mobile-architect`

## Reviewers

Platform engineer for each target, `mobile-test-engineer`, `mobile-security-reviewer`, and `mobile-code-reviewer`.

## Steps

1. Verify destination path and no conflicting project exists.
2. Detect native tooling and versions from local commands or report unavailable.
3. Choose official stable project creation mechanism.
4. Create only required project files.
5. Configure tests and non-secret example configuration only when officially supported.
6. Run formatting, static analysis, build, and tests that are locally available.
7. Perform security and final code review.

## Conditional Steps

- KMP: validate source sets and targets.
- Flutter/RN: validate package manager and host projects.
- iOS: discover schemes and avoid signing with real credentials.
- Android: validate Gradle tasks and manifests.

## Validation Gates

Project opens with native tooling, builds without publishing when tooling is available, tests are discoverable, no secrets exist, and unsupported infrastructure is documented.

## Failures

Stop on missing required tooling, conflicting destination, unsupported template, required external service, or approval denial.

## Stop Conditions

Do not continue if project identity, destination, or technology is ambiguous.

## Evidence

Tool versions, commands run, generated files, validation results, and unavailable checks.

## Outputs

Working project scaffold, validation report, and next steps.

## Acceptance Criteria

The project is minimal, native, reproducible, secret-free, and validated with available local checks.

## Human Approvals

Required for downloads, dependency changes beyond the official template, signing, external services, and destructive destination changes.

## Prohibited Actions

No publishing, uploading, submitting, deploying, signing with real credentials, fabricated endpoints, or placeholder-only files.
