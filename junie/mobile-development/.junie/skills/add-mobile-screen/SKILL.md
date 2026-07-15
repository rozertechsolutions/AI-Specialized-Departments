---
name: "add-mobile-screen"
description: "Add a mobile screen using existing platform UI, navigation, state, accessibility, localization, complete UI states, tests, and validation evidence."
---
# Add Mobile Screen

Use this skill when the user asks to add a screen, route, view, page, flow, widget, Compose screen, SwiftUI/UIKit view controller, Flutter screen, or React Native screen.

## Workflow Definition

Objective: add a complete, accessible, localized, adaptive screen within existing UI conventions.

Trigger: explicit screen or UI flow request.

Inputs: screen purpose, fields/content, actions, navigation entry/exit, supported platforms, data states, accessibility requirements, localization requirements, and acceptance criteria.

Supported technologies: Android, iOS, Kotlin Multiplatform when UI is present, Flutter, and React Native.

Preconditions:

- Inspect existing UI patterns, navigation, state management, resources, localization, and tests.
- Identify primary UI owner by platform.
- Ask approval for new dependencies, permissions, analytics, telemetry, deep links, privacy behavior, or release-impacting config.

Primary owner: matching platform UI engineer.

Reviewers: `mobile-ui-accessibility-reviewer`, `mobile-test-engineer`, `mobile-security-reviewer` when the screen handles sensitive data, and `mobile-code-reviewer`.

## Steps

1. Trace required UI states: loading, empty, content, error, retry, disabled, cancellation, recovery, and offline when applicable.
2. Add screen code using existing navigation and state conventions.
3. Add resources/localization and accessibility semantics/labels/traversal/focus behavior.
4. Preserve adaptive layouts, orientation behavior, dynamic text, and platform interaction conventions.
5. Add tests or snapshots at the project's established level.
6. Run relevant format/lint/analyze/typecheck/build/test commands.
7. Request UI/accessibility and final code review.

## Validation Gates

- Screen is reachable through existing navigation.
- Text/resources fit localization and dynamic text requirements.
- Sensitive data handling is reviewed.
- UI states are covered by implementation and tests or not-applicable reasons.

## Failures And Stop Conditions

Stop for missing UX requirements, absent navigation ownership, unapproved sensitive data handling, unavailable assets, dependency requests without approval, credentials, destructive commands, or release actions.

## Evidence And Outputs

Output changed files, navigation path, UI states handled, accessibility/localization notes, tests, commands run, results, screenshots when available, and residual risk.

Acceptance criteria: screen is functional, accessible, consistent with existing UI, validated where possible, and independently reviewed.

Human approvals: required for accessibility exceptions, privacy-sensitive UI, analytics/telemetry, permissions, dependencies, deep links, and release-impacting changes.

Prohibited actions: decorative placeholder screens, unsupported UI frameworks, replacing existing navigation/state architecture without approval, release actions, and self-review.
