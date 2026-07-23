---
name: add-mobile-screen
description: Add one mobile screen or route, including UI states, navigation, state integration, accessibility, and tests, to an existing Android, iOS, KMP-hosted, Flutter, or React Native app. Do not use for non-UI features.
---

# Add Mobile Screen

## Objective

Implement one complete screen and its navigation/state boundary using the existing design system and platform conventions, with accessible behavior across supported devices and states.

## Required inputs

- Screen purpose, content, actions, navigation entry/exit, and acceptance criteria.
- Design reference or precise behavior/layout description.
- Supported platforms, form factors, orientations/window sizes, localization, and OS versions.
- Data source, state owner, loading/empty/error/offline/retry behavior, and analytics expectations.
- Existing design-system components and navigation/state conventions.

Use Figma only when the user explicitly enabled and approved the relevant MCP reads. A design image does not authorize external upload or write-back.

## Preconditions

1. Inspect status/diff, navigation graph, adjacent screens, design system, state/data flow, resources, localization, accessibility conventions, and UI tests.
2. Identify exactly one primary platform owner and any native host boundary.
3. Confirm no new dependency, permission, deep-link/public route, or architecture change is required; otherwise obtain approval.
4. Define UI states and the validation matrix before editing. Classify every completion criterion as required, conditionally required, or not applicable with a documented reason.

## Agent ownership

The coordinator chooses `android-engineer`, `ios-engineer`, `flutter-engineer`, or `react-native-engineer` for screen implementation. `kmp-engineer` owns only shared state/domain work explicitly required by a KMP architecture. `mobile-ui-accessibility-reviewer` is mandatory after implementation. `mobile-test-engineer` owns tests. Use security review for sensitive fields/data and performance review for large/complex rendering. `mobile-code-reviewer` performs final correctness review.

## Execution

1. **Screen contract.** Record all states, actions, navigation outcomes, focus/keyboard behavior, text scaling, localization, orientation/window adaptation, and error recovery.
2. **Trace patterns.** Select existing components and the nearest comparable screen. Do not create a parallel design system or navigation pattern.
3. **Architecture gate.** If new shared state, route contract, or module boundary is needed, obtain a `mobile-architect` decision before implementation.
4. **Implement state boundary.** The platform owner wires state/data with explicit lifecycle and cancellation handling. KMP shared work, if any, is separately owned.
5. **Implement UI.** Cover loading, content, empty, error, disabled, and offline states as applicable. Reuse tokens/components/resources and provide semantics/labels, focus order, minimum targets, text scaling, and localization.
6. **Navigation gate.** Validate back behavior, restoration, repeated navigation, deep links when in scope, and argument validation. Do not silently change existing route contracts.
7. **Tests.** `mobile-test-engineer` adds state/unit tests and supported UI/navigation/accessibility tests for critical behavior.
8. **UI/accessibility review.** `mobile-ui-accessibility-reviewer` checks all supported states and available form factors. The platform owner fixes accepted findings.
9. **Conditional reviews.** Run security for sensitive input/data and performance for measurable list/image/animation/rendering risk.
10. **Code review and verification.** Run `mobile-code-reviewer`, targeted compile/static/tests, and reasonable broader checks. Inspect visual evidence when available; do not claim pixel parity without it.
11. **Final gate.** Confirm every state and acceptance criterion is implemented, reviewed, and verified or explicitly blocked.

## Error handling and stop conditions

Stop on missing design/behavior decisions, inaccessible private design, unknown route or state ownership, unapproved dependency/deep-link/public-contract changes, unavailable required platform tool, conflicting user edits, signing, or production access. Do not fabricate assets or copy copyrighted/private assets from unauthorized sources.

## Outputs

- Screen/navigation/state files changed.
- Implemented UI-state matrix and supported form factors.
- Tests and verification results.
- Completion matrix with required/conditional/not-applicable status, reasons, and exact results.
- Accessibility/UI findings and fixes.
- Conditional security/performance findings and remaining visual limitations.

## Acceptance criteria

- All defined states and navigation paths behave correctly, including restoration/back/cancellation where applicable.
- Reused design-system patterns, resources, and localization are correct.
- Required compile/static/test checks pass.
- Accessibility review covers semantics, focus, scaling, targets, contrast evidence, motion, and adaptive layout as applicable.
- No secret, unauthorized asset, new dependency, signing, publication, or unrelated change exists.

## Prohibited actions

Do not invent product behavior, add dependencies without approval, bypass the design system, hardcode secrets/private URLs, write to Figma, sign/publish, use production data, weaken accessibility, or claim unverified visual fidelity.
