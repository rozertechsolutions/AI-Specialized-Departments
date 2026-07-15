---
name: add-mobile-screen
description: Add a mobile screen or flow with explicit navigation, state ownership, complete loading/empty/error/content/recovery states, adaptive accessibility, localization, tests, and platform conventions.
user-invocable: true
---

# Add Mobile Screen

## Objective

Add a platform-consistent screen or flow whose navigation, state ownership, UI states, accessibility, localization, adaptation, and tests are complete and traceable.

## Trigger

Use when the requested unit is primarily a new screen, route, destination, or small UI flow in an existing mobile project.

## Inputs

- Entry/exit navigation and deep-link expectations.
- Content, actions, state transitions, validation, and complete state behavior.
- Supported devices/orientations/input methods, localization, accessibility, analytics/privacy, and test expectations.
- Approved visual/design source and explicit non-goals.

## Preconditions

- Inspect instructions, status/diff, current navigation, UI toolkit, state architecture, design system, resources/localizations, adaptive conventions, neighboring screens, previews/snapshots, and tests.
- Verify any supplied design reference; do not invent missing product behavior or assets.
- Resolve navigation and state ownership before editing.

## Ownership

- Primary owner: the relevant platform UI engineer (`android-engineer`, `ios-engineer`, `flutter-engineer`, `react-native-engineer`, or `kmp-engineer` only for existing Compose Multiplatform UI).
- `mobile-test-engineer` owns test strategy; UI/accessibility review is required; security and performance review are conditional; `mobile-code-reviewer` reviews last.
- Native host changes remain with native owners.

## Tool and permission boundary

Use read/search for discovery; edit only assigned UI/navigation/state/resource/test paths under normal approval. Use discovered local checks only. No design-service MCP, asset download, dependency install, credentials, external writes, signing, or publishing.

## Sequence and gates

1. **Behavior gate:** Define route identity, arguments/results, entry/exit, back behavior, deep links, state owner/lifetime, content/actions, validation, and loading/empty/error/content/retry/recovery/disabled/permission states as applicable.
2. **Convention gate:** Inspect neighboring screens, design tokens/components, navigation, state, localization, analytics, and test conventions. Record exact reusable paths.
3. **Ownership gate:** Assign one UI primary and separate any shared/native/data area. Stop on ambiguous state or navigation ownership.
4. **Accessibility/adaptation design:** Define semantics, labels/roles/values, reading/focus order, text scaling, target sizes, gesture alternatives, keyboard/switch input, contrast/non-color cues, safe areas, supported size/orientation classes, RTL, and locale formatting.
5. **Implementation gate:** Add route/navigation, state holder, UI and actions, all applicable states, resources/localizations, and lifecycle/cancellation behavior in the smallest project-consistent form.
6. **Data/security gate:** Integrate only approved data contracts; prevent sensitive logs/screenshots/clipboard exposure and unsafe deep-link/input handling as applicable.
7. **Test gate:** Add deterministic state/render/navigation tests at the lowest effective levels, including accessibility semantics and failure/recovery where supported. Update snapshots only after semantic review.
8. **Validation gate:** Run targeted formatting/lint/type checks, compilation/non-publishing build, UI/unit/widget/component tests, and project snapshot checks. Review warnings and resources/localizations.
9. **Independent review gate:** Obtain UI/accessibility review, conditional security/performance review, and final code review. Correct and fully repeat after findings.
10. **Completion gate:** Classify all `QWEN.md` criteria and identify manual screen-reader, text-scale, locale/RTL, orientation/device, and input-method checks not performed.

## Errors and stop conditions

Stop on missing product behavior, unverified design/assets, navigation/state conflict, unapproved dependency/component framework, required external design access, inaccessible required target, failed validation, unexplained snapshot change, or unresolved accessibility/security blocker.

## Outputs and evidence

- Screen behavior/state/navigation contract and owner map.
- Exact changed UI/state/navigation/resource/test paths.
- State-to-test matrix and accessibility/adaptation/localization coverage.
- Exact commands, exit codes, targets, and observed results.
- Completion ledger, reviewer findings/corrections, manual checks, and limitations.

## Acceptance criteria

- Navigation and state lifetime are deterministic and preserve platform back/lifecycle conventions.
- Every applicable UI state and recovery path exists and is tested proportionately.
- Accessibility, localization, adaptive behavior, and platform conventions have code evidence plus explicit manual gaps.
- Required checks and independent reviews pass without unresolved blocker.

## Human review requirements

Humans approve missing product/design behavior, assets/licensing, navigation contract changes, analytics, permissions, dependencies, and final visual/accessibility acceptance on real supported devices.

## Prohibited actions

Do not invent designs/assets/copy, add a UI/state framework without approval, hardcode user-facing strings or sensitive data, omit failure states, suppress overflow/accessibility issues, fetch private designs, sign, publish, or self-approve.
