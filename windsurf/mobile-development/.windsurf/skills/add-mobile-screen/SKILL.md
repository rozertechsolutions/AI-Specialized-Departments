---
name: add-mobile-screen
description: Add a mobile screen using existing Android, iOS, Flutter, React Native, or KMP UI conventions with accessibility and state coverage.
---

# add-mobile-screen

## Objective

Add a complete, accessible screen or view while preserving existing navigation, state-management, design, and platform conventions.

## Inputs

Screen purpose, route/navigation entry, design requirements, states, localization needs, target platforms, and approved scope.

## Supported Technologies

Android Compose/Views, iOS SwiftUI/UIKit, Compose Multiplatform when present, Flutter widgets, and React Native components.

## Preconditions

- Inspect UI architecture, navigation, state management, theming, localization, accessibility patterns, previews/snapshots, and tests.
- Get approval for new dependencies, route contracts that affect public APIs, permissions, deep links, analytics, telemetry, or native bridge changes.

## Primary Owner

Technology owner for the UI layer: `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer`.

## Reviewers

`mobile-ui-accessibility-reviewer`, `mobile-test-engineer`, and `mobile-code-reviewer`; add security/performance reviewers when relevant.

## Steps

1. Trace UI requirements and states.
2. Add screen, state handling, navigation wiring, resources, and localization using existing patterns.
3. Cover loading, empty, error, retry, cancellation, recovery, offline, disabled, and permission states where applicable.
4. Add previews/snapshots/component/UI tests when supported.
5. Validate accessibility, dynamic text, focus/traversal, orientation, adaptive layouts, and localization.
6. Run discovered relevant checks and complete final review.

## Validation Gates

Build/compile, UI tests or snapshots where available, accessibility review, localization review, adaptive layout/orientation review, lint/static analysis/formatting, and regression review.

## Failures And Stop Conditions

Stop on missing route contract, missing design decisions, unapproved dependency/analytics/permission/deep-link change, inaccessible UI state, or validation failure.

## Evidence And Outputs

Changed files, state coverage, screenshots or test output when available, command results, unavailable checks, and review notes.

## Acceptance Criteria

The screen is reachable, complete across expected states, accessible, localized where applicable, tested, and independently reviewed.

## Prohibited Actions

No hidden navigation side effects, unapproved telemetry, unapproved permissions, unrelated UI restyling, or fabricated visual/test evidence.
