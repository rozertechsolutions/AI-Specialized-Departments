---
name: add-mobile-screen
description: Workflow for adding a mobile screen with navigation, state, accessibility, localization, UI states, and tests.
---

# Add Mobile Screen

## Objective

Add a user-facing mobile screen that fits existing navigation, state, styling, accessibility, localization, and test conventions.

## Trigger

Use when the user asks to add a screen, page, view, route, tab, or form.

## Inputs

Screen purpose, platform, navigation entry point, data requirements, UI states, localization needs, and acceptance criteria.

## Supported Technologies

Android, iOS, Flutter, React Native, and Compose Multiplatform when present.

## Preconditions

Inspect existing navigation, UI components, state management, theme, localization, and tests before editing.

## Primary Owner

The platform UI engineer matching the project.

## Reviewers

`mobile-architect` for navigation/state impact, `mobile-ui-accessibility-reviewer`, `mobile-test-engineer`, `mobile-security-reviewer` if sensitive data is shown, and `mobile-code-reviewer`.

## Steps

1. Locate navigation and UI patterns.
2. Define state ownership and data flow.
3. Implement the screen with complete states.
4. Add localization and accessibility semantics where applicable.
5. Add tests or snapshots according to project conventions.
6. Run relevant UI, lint, build, and test checks.
7. Perform accessibility and final review.

## Conditional Steps

- Form screen: validate input, error display, keyboard/focus, and submission states.
- Data screen: handle loading, empty, error, retry, cancellation, and offline behavior.
- Sensitive data: include security review.

## Validation Gates

Navigation works, UI states are complete, text is accessible/localizable, tests cover key behavior, and checks pass or are unavailable.

## Failures

Stop on missing navigation requirements, absent design/content, approval-gated sensitive display, or unavailable critical infrastructure.

## Stop Conditions

Do not invent product copy, endpoints, or business rules when required information is missing.

## Evidence

Changed files, screenshots/tests when available, commands run, accessibility notes, and unavailable checks.

## Outputs

Screen implementation, tests, and validation report.

## Acceptance Criteria

The screen is reachable, usable, accessible, localized as applicable, and validated.

## Human Approvals

Required for broad UX changes, sensitive data display, analytics/telemetry, dependencies, or native permissions.

## Prohibited Actions

No placeholder UI, fabricated APIs, unsupported routes, self-review, publishing, signing, or deployment.
