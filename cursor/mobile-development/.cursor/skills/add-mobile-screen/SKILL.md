---
name: add-mobile-screen
description: Add a mobile screen or view in Android, iOS, Flutter, or React Native while preserving navigation, state, accessibility, and UI conventions.
---

# add-mobile-screen

Objective: add the requested screen with complete states, accessible interactions, and existing navigation/state conventions.

Trigger: request to add a screen, page, view, route, flow step, or UI state.

Inputs: screen purpose, supported platforms, navigation entry point, data requirements, UI states, localization needs, design references, and acceptance criteria.

Supported technologies: Android, iOS, Flutter, React Native. KMP applies only to shared logic behind the screen.

Preconditions: inspect existing UI patterns, routing, state management, resources/localization, tests, and current changes; obtain approval for permissions, deep links, telemetry, dependencies, or native host changes.

Primary owner: platform UI owner selected by detected technology.

Reviewers: `mobile-ui-accessibility-reviewer`, `mobile-test-engineer`, `mobile-security-reviewer` for data/privacy, `mobile-performance-reviewer` for heavy UI, and `mobile-code-reviewer`.

Steps:

1. Map route/state/data ownership.
2. Classify criteria including accessibility, localization, adaptive layouts, and UI states.
3. Implement screen and navigation integration.
4. Cover loading, empty, error, retry, cancellation, and recovery states when applicable.
5. Add or update tests/snapshots where the project supports them.
6. Run relevant UI, lint/analyze/type, and build checks.
7. Review accessibility and adaptive behavior.

Validation gates: compile/build, route/navigation validation, tests, static checks, accessibility semantics, localization resources when applicable, adaptive layout/orientation evidence, and independent review.

Failures: missing design/API contract, unsupported UI framework, inaccessible state, layout ambiguity, unavailable simulator/emulator, or validation failure.

Stop conditions: new dependency, permission, deep link, WebView, telemetry, auth/privacy change, signing, publishing, external service, or destructive action.

Evidence: changed UI files, routes, resource changes, commands and results, screenshots if available, reviewer findings, and criteria classification.

Outputs: screen implementation, tests or gaps, validation report, and remaining decisions.

Acceptance criteria: screen is reachable, follows conventions, handles expected states, and required validation does not fail.

Human approvals: dependencies, permissions, deep links, WebViews, telemetry, privacy/auth changes, visual trade-offs, signing/release actions.

Prohibited actions: marketing-only placeholder UI, invented backend data, inaccessible controls, unapproved integrations, signing, publishing, upload, deployment, or final self-review.
