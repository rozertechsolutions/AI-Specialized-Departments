---
name: add-mobile-screen
description: Add a mobile screen or route with explicit navigation, state ownership, complete UI states, accessibility, localization, adaptive behavior, and tests.
when_to_use: Use when the main deliverable is a new screen, page, view, route, or destination in Android, iOS, Flutter, React Native, or existing Compose Multiplatform UI.
argument-hint: "[screen, route, and behavior]"
model: inherit
---

# Objective

Implement the screen in `$ARGUMENTS` using the project's existing UI/navigation architecture and platform conventions, with complete observable states and evidence.

# Required input and supported scope

Require entry/exit routes, user goals/actions, displayed data, state transitions, loading/empty/error/content/recovery behavior, supported devices/orientations/input, localization copy or source, analytics/privacy requirements, and acceptance criteria. Do not invent missing product or visual requirements.

# Preconditions and inspection

Read instructions and inspect status, UI framework, navigation graph/router, state ownership, design system/components/tokens, localization, adaptive patterns, data/domain interfaces, accessibility conventions, previews/stories, and tests. Confirm whether shared Compose Multiplatform UI actually exists before assigning KMP UI work.

# Ownership

The technology UI engineer is primary; `kmp-engineer` owns existing shared Compose Multiplatform UI. Use `mobile-architect` for unresolved state/navigation boundaries, `mobile-test-engineer` for coverage, `mobile-ui-accessibility-reviewer` for independent UI review, security/performance reviewers when relevant, and `mobile-code-reviewer` last.

# Procedure and gates

1. Trace navigation entry, arguments, deep-link implications, back/exit behavior, state owner, data source, and side effects. Gate: lifecycle and ownership are unambiguous.
2. Define a state model containing all applicable loading, empty, error, content, retry/recovery, refresh, offline, and permission states.
3. Reuse existing design-system and platform components. Implement adaptive layout, safe areas/insets, text scaling, orientation/window-size behavior, and input methods as required.
4. Add semantics, labels/roles/states, focus/traversal, touch targets, reduced-motion behavior where applicable, and localization without hard-coded user text contrary to project conventions.
5. Integrate navigation and data without creating hidden global state or unrelated architecture changes.
6. Add deterministic state/unit tests and the lowest sufficient UI/navigation tests, including failure and accessibility assertions supported by the project.
7. Run discovered compile/build, UI/static checks, tests, lint, and formatting validation for affected targets.
8. Obtain UI/accessibility review and any security/performance review, fix findings, rerun evidence, and obtain independent final code review.

# Failure and stop handling

Stop when navigation/state/product/design requirements materially conflict, required data contracts are absent, the screen needs an unapproved dependency/design-system/architecture change, or required checks fail. Return a precise question or blocker; do not fabricate copy, assets, or behavior.

# Evidence and acceptance

Return requirements-to-state/test trace, route/state ownership, changed files, screenshots only if genuinely produced, exact commands/results, manual device/screen-reader checks still required, applicability classification, reviews, and residual risk.

Report every considered universal and technology-specific completion criterion as `required`, `conditionally-required`, or `not-applicable`; give a concrete reason for every `not-applicable`, and label unavailable infrastructure `unavailable` rather than passed.

Accept only when every applicable UI state and navigation path is implemented, localization/adaptive/accessibility foundations are present, tests/checks pass where required, unavailable device validation is explicit, and independent review has no blocker.

# Human review and prohibited actions

Require human review for visual/product acceptance, new routes/deep links, analytics/privacy, design-system changes, and device/screen-reader behavior. Never invent design requirements, hardcode secrets, replace UI/navigation/state libraries, suppress accessibility, publish/sign/deploy, or claim manual checks were performed when they were not.
