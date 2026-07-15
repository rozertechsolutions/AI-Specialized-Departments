---
name: add-mobile-screen
description: Add a mobile screen using existing navigation, state, UI, accessibility, and test conventions.
---

# Add Mobile Screen

## Objective

Add a screen that fits the detected platform, navigation model, state management, design conventions, and accessibility requirements.

## Trigger

Use when the user asks to add a view, screen, route, page, tab, flow, or UI state.

## Inputs

Screen purpose, route or navigation entry, data needs, states, design references, localization requirements, and acceptance criteria.

## Supported Technologies

Android, iOS, Flutter, React Native, and KMP only when Compose Multiplatform or shared UI is already present.

## Preconditions

Inspect existing UI patterns, navigation, state management, resources, localization, tests, and accessibility conventions. Ask for missing UX or route decisions when unsafe to infer.

## Primary Owner

Platform UI owner: `android-engineer`, `ios-engineer`, `flutter-engineer`, or `react-native-engineer`. Use `kmp-engineer` only for existing shared UI surfaces.

## Reviewers

`mobile-ui-accessibility-reviewer`, `mobile-test-engineer`, `mobile-code-reviewer`, and security/performance reviewers when data or rendering risk exists.

## Steps

1. Locate existing screen patterns and navigation registration.
2. Define all UI states: loading, empty, content, error, retry, disabled, offline, and cancellation when applicable.
3. Implement UI with existing components and resource conventions.
4. Add accessibility labels, focus/traversal behavior, dynamic text handling, localization hooks, and adaptive layout support.
5. Add or update tests/snapshots where configured.
6. Run targeted UI/build/static checks.
7. Complete accessibility and code review.

## Conditional Steps

- If design or route decisions are ambiguous, stop and ask before inventing them.
- If localization exists, add strings through the established resource system.
- If screenshots or snapshot tests are configured, update them only for intentional UI changes.
- If the screen uses network, auth, WebView, deep link, telemetry, or permissions, invoke security review.

## Validation Gates

Required: compile/build or exact blocker, UI state coverage, affected tests, accessibility inspection, formatting/lint/static analysis when configured, and code review. Conditional: screenshots, localization, snapshot, performance, and navigation deep-link checks.

## Failures and Stop Conditions

Stop for missing route ownership, unclear UX, unavailable design assets, required dependency additions, permissions/privacy changes, or validation failures.

## Evidence

Record files changed, states implemented, accessibility review, tests, screenshots if available, and commands run.

## Outputs

Implemented screen, navigation integration, tests, review findings, and limitations.

## Acceptance Criteria

The screen is reachable, handles expected states, follows existing conventions, is accessible, and has relevant validation evidence.

## Human Approvals

Required for new dependencies, analytics/telemetry, permissions, deep links, WebViews, auth, privacy behavior, or external service writes.

## Prohibited Actions

Do not add decorative placeholder screens, hardcode secrets/endpoints, bypass localization conventions, disable accessibility, or publish/sign/upload.
