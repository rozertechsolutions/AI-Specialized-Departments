---
name: add-mobile-screen
description: Use when adding a mobile screen, route, view, widget, Compose UI, SwiftUI/UIKit view, Flutter widget, or React Native screen with states and accessibility.
---

# add-mobile-screen

- Objective: Add a mobile screen that follows existing UI architecture, navigation, state, accessibility, localization, and complete-state conventions.
- Trigger: User asks to create or modify a screen, route, view, widget, or UI flow.
- Inputs: Screen purpose, target platform, data dependencies, navigation entry/exit, state model, loading/empty/error/retry/cancellation states, accessibility and localization needs.
- Supported technologies: Android, iOS, Flutter, React Native, and KMP only where UI technology is already present.
- Preconditions: Inspect existing UI patterns, navigation, strings, resources/assets, tests, and design conventions.
- Primary owner: Platform UI engineer for the target technology.
- Reviewers: `mobile-ui-accessibility-reviewer`, `mobile-test-engineer`, and `mobile-code-reviewer`; add security/performance review when needed.
- Steps: Locate existing UI conventions; define states; implement minimal screen and navigation; add strings/resources; preserve adaptive layout; add tests or snapshots where available; run applicable UI/analysis checks; request accessibility review.
- Validation gates: Screen compiles/analyzes, navigation works by code review or tests, all states are represented, accessibility labels/focus/dynamic text/localization are considered, and tests run or are unavailable.
- Failures: Stop on missing design requirements, inaccessible assets, unsupported UI framework, validation failures, or approval-required sensitive changes.
- Stop conditions: New dependency, telemetry, WebView, deep link, permissions, signing, publishing, destructive command, or unrelated redesign.
- Evidence: Changed files, UI state coverage, commands run, screenshots/tests if available, and unavailable visual infrastructure.
- Outputs: Screen implementation, tests, accessibility notes, validation evidence, and residual risks.
- Acceptance criteria: Screen is native to the app stack, complete states are handled, accessibility is reviewed, and no unsupported UI runtime is introduced.
- Human approvals: Required for new dependencies, permissions, privacy, telemetry, WebViews, deep links, assets with licensing uncertainty, and external writes.
- Prohibited actions: Marketing-only placeholder screens, unsupported UI simulations, broad redesigns, publishing, signing, deployment, destructive commands, and fabricated visual verification.

