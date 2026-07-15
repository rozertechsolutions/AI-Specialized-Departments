---
name: implement-mobile-feature
description: Implement a scoped mobile feature across Android, iOS, KMP, Flutter, React Native, or mixed codebases with tests and independent review.
---

# implement-mobile-feature

## Objective

Implement the requested feature with minimal, maintainable changes that match existing architecture and technology ownership boundaries.

## Inputs

Feature requirements, affected platform(s), acceptance criteria, designs/API contracts if available, target files, and user-approved scope.

## Supported Technologies

Android, iOS, Kotlin Multiplatform, Flutter, React Native, and mixed mobile repositories.

## Preconditions

- Inspect existing architecture, state/navigation patterns, UI conventions, tests, error handling, current changes, and command scripts.
- Select exactly one primary implementation owner by touched technology.
- Get human approval for auth, privacy, manifests, entitlements, network security, deep links, WebViews, analytics, telemetry, dependencies, lockfiles, build/signing configuration, or external writes.

## Primary Owner

`android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer`.

## Reviewers

`mobile-test-engineer`, `mobile-security-reviewer` when security/privacy/network/storage is touched, `mobile-ui-accessibility-reviewer` when UI is touched, `mobile-performance-reviewer` when performance-sensitive paths are touched, and `mobile-code-reviewer`.

## Steps

1. Trace requirements to files and platform behavior.
2. Confirm ownership and delegation boundaries.
3. Implement the smallest complete change using existing patterns.
4. Handle loading, empty, error, retry, cancellation, offline, recovery, and invalid states where applicable.
5. Add or update focused tests and fixtures.
6. Run discovered relevant checks.
7. Complete independent final review.

## Validation Gates

Compilation/build, unit/integration/UI/snapshot/e2e tests as applicable, lint, static analysis, formatting, type checking, secret detection, accessibility/localization/adaptive layout, security/privacy review, regression review, and evidence capture.

## Failures And Stop Conditions

Stop on ambiguous requirements, conflicting ownership, unsupported platform capability, missing approval, validation failure, suspected secret exposure, or need for unrelated refactor.

## Evidence And Outputs

Changed files, requirement traceability, test coverage, command results, unavailable checks, reviewer findings, and residual risks.

## Acceptance Criteria

Feature behavior meets acceptance criteria, validations are evidenced or reported unavailable, ownership boundaries are respected, and no implementation role performs final independent review.

## Prohibited Actions

No broad rewrites, unrelated formatting, dependency changes without approval, release actions, hidden failures, or fabricated evidence.
