---
name: add-mobile-screen
description: Add a mobile screen using the detected UI framework, existing navigation and state patterns, complete UI states, tests, and accessibility review.
compatibility: opencode
metadata:
  owner: coordinator
---

# add-mobile-screen

- Objective: add a screen that fits existing navigation, state, accessibility, localization, and visual conventions.
- Trigger: user asks for a new screen or UI route.
- Inputs: screen purpose, entry point, navigation contract, data sources, UI states, copy, target platform.
- Supported technologies: Android, iOS, Flutter, React Native, Compose Multiplatform when already present.
- Preconditions: route and behavior are known; existing UI framework is detected.
- Primary owner: UI platform owner by file boundary.
- Reviewers: `mobile-ui-accessibility-reviewer`, `mobile-test-engineer`, `mobile-security-reviewer` when data is sensitive, `mobile-code-reviewer`.
- Steps: inspect navigation/state patterns; define screen states; implement scoped UI; wire navigation; add tests/snapshots when available; validate accessibility and layout.
- Conditional steps: stop for product copy, API contracts, permissions, or telemetry approval when missing.
- Validation gates: compile/type check; relevant UI/unit tests; localization/adaptive layout/accessibility criteria classified.
- Failures: report unavailable screenshots, simulators, or UI test infrastructure.
- Stop conditions: unknown navigation contract, missing data contract, credential or production access need.
- Evidence: changed files, tests, visual/accessibility review findings, commands.
- Outputs: screen implementation, tests, validation report.
- Acceptance criteria: screen is reachable as requested, handles complete states, and respects platform conventions.
- Human approvals: UX wording uncertainty, telemetry, permissions, auth, sensitive data display.
- Prohibited actions: invented endpoints, hidden loading/error states, signing, publishing, external writes.
