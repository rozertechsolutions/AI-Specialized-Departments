---
name: create-mobile-project
description: Create or initialize a scoped Android, iOS, KMP, Flutter, React Native, or mixed mobile project with architecture, security, test, and validation gates.
---

# create-mobile-project

## Objective

Create a new mobile project or module only within the user-approved path, using the target ecosystem's stable tooling and existing repository conventions.

## Inputs

- Target technology, app/module name, package or bundle identifier, supported platforms, minimum OS/SDK targets, architecture constraints, and approved destination path.

## Supported Technologies

Android, iOS, Kotlin Multiplatform, Flutter, React Native, and mixed mobile repositories.

## Preconditions

- Inspect repository layout, current changes, existing build systems, package managers, templates, and documentation.
- Confirm the destination path is in scope and does not overwrite existing user work.
- Get explicit approval before adding dependencies, lockfiles, external templates, network downloads, signing configuration, credentials, analytics, telemetry, or store-facing configuration.

## Primary Owner

`mobile-architect`

## Reviewers

`android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer` as applicable; always include `mobile-test-engineer`, `mobile-security-reviewer`, and `mobile-code-reviewer`.

## Steps

1. Trace requirements to target platforms and project boundaries.
2. Discover available local generators and official project commands without assuming tools.
3. Select architecture, module boundaries, dependency direction, state, navigation, and shared/platform boundaries.
4. Create only required files and configuration.
5. Add initial tests and documentation when the ecosystem convention requires them.
6. Run safe discovered validation commands where available.
7. Perform independent final review.

## Validation Gates

Project configuration, dependency resolution, compilation/build validation, unit tests, lint/static analysis/formatting, secret detection, permissions/manifests/entitlements/privacy review, accessibility/localization/adaptive-layout baseline, and unsupported-infrastructure reporting.

## Failures And Stop Conditions

Stop on unclear destination, existing file conflict, missing required approval, unavailable generator, dependency or network requirement, signing material request, or failed validation that cannot be corrected within scope.

## Evidence And Outputs

Created files, commands discovered, commands run, validation results, unavailable checks, approvals required, and final review notes.

## Acceptance Criteria

The project is created in scope, contains no placeholders or secrets, follows native conventions, and has evidence for all required and conditionally required checks.

## Prohibited Actions

No publishing, signing with real credentials, upload, deploy, submit, distribution, destructive cleanup, external service activation, or fabricated validation evidence.
