---
name: add-mobile-screen
description: Add a mobile UI screen with navigation, states, accessibility, localization, and tests for Android, iOS, Flutter, or React Native.
---

# add-mobile-screen

Objective: add a complete mobile screen using existing UI, navigation, state, and localization conventions.

Trigger: request to add a screen, view, route, page, or UI flow.

Inputs: screen purpose, supported platforms, route/navigation contract, UI states, copy, accessibility labels, data requirements, design constraints.

Supported technologies: Android, iOS, Flutter, React Native; KMP only for shared non-UI logic.

Preconditions: inspect UI framework and navigation/state conventions; confirm required copy and route behavior; obtain approval for new permissions, telemetry, dependencies, native host changes, or API contracts.

Primary owner: `android-engineer`, `ios-engineer`, `flutter-engineer`, or `react-native-engineer`; `kmp-engineer` only for shared logic.

Reviewers: `mobile-ui-accessibility-reviewer`, `mobile-test-engineer`, `mobile-security-reviewer` for sensitive data, and `mobile-code-reviewer`.

Ordered steps:

1. Trace screen requirements and route ownership.
2. Classify criteria including UI states and accessibility.
3. Inspect existing components, theme, navigation, localization, and test patterns.
4. Implement the screen and route using current conventions.
5. Cover loading, empty, error, retry, cancellation, and recovery states when applicable.
6. Add focused unit/widget/UI/snapshot tests where supported.
7. Run relevant validation.
8. Complete UI/accessibility and final code review.

Conditional steps: request design clarification when copy/states are missing; stop for permissions, telemetry, auth, privacy, dependency, or public navigation contract changes.

Validation gates: compile/build, UI/widget/snapshot tests where configured, accessibility labels/focus/dynamic text/adaptive layout review, localization check, security review for sensitive UI, and final code review.

Failures: missing UI requirements, route conflict, unsupported framework, validation failure, accessibility blocker, or missing tooling.

Stop conditions: dependency/lockfile change without approval, real endpoints, credentials, permissions/privacy changes, signing/publishing/upload/deployment, destructive commands.

Evidence: files changed, UI states implemented, commands run, screenshots or visual inspection when available, reviewer findings, criteria classification.

Outputs: screen implementation, tests or test-gap explanation, validation and review report.

Acceptance criteria: screen matches stated behavior, respects platform conventions, handles required states, and has honest validation evidence.

Human approvals: dependencies, lockfiles, permissions, telemetry, privacy, auth, route contracts beyond request, native host changes.

Prohibited actions: generic decorative UI unrelated to request, invented copy when user must supply it, inaccessible controls, publication, signing, uploading, deployment, self-review as final review.
