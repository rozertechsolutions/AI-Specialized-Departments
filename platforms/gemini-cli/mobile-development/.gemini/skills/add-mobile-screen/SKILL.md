---
name: add-mobile-screen
description: Adds a scoped mobile screen with navigation, state ownership, complete loading/empty/error/content/recovery states, adaptive layout, accessibility, localization, tests, and platform conventions. Use for a new screen or route in an existing mobile app.
---

# Add Mobile Screen

## Objective and trigger

Add one complete screen/route to an existing mobile application while preserving
navigation, architecture, design-system, state, accessibility, localization, and
platform conventions. Activate when the primary outcome is a screen; use the
feature Skill when substantial domain/data behavior dominates.

Activation does not grant tools. Use only project-allowed read/write tools and
approved local validation commands; do not use MCP or external design services.

## Inputs

- User journey, entry/exit navigation, acceptance criteria, and non-goals.
- Content/actions, state/data source, permissions, analytics policy, and deep links.
- Supported platforms, device classes, orientations, accessibility/localization,
  screenshots/design references, and existing design system.
- Required loading, empty, error, retry, content, disabled, offline, cancellation,
  and recovery behavior.

## Preconditions and ownership

Inspect instructions, repository status, navigation graph/router, neighboring
screens, state/data layer, themes/components/resources, tests, and platform
conventions. Resolve missing behavior rather than inventing product decisions.

Select one primary owner: `android-engineer` for Android, `ios-engineer` for iOS,
`flutter-engineer` for Flutter, or `react-native-engineer` for React Native.
`kmp-engineer` may own shared presentation logic only when already architectural;
Android/iOS owners retain explicit native-host files.
`mobile-ui-accessibility-reviewer` and `mobile-test-engineer` are required;
security/performance reviewers are conditional; `mobile-code-reviewer` is final.

## Workflow and gates

1. **Journey gate:** define entry, back/up/dismiss behavior, deep-link/re-entry,
   state restoration, actions, success/failure, and navigation ownership.
2. **State gate:** specify one state owner and an exhaustive state/transition
   matrix, including loading, empty, error, retry, content, disabled, offline,
   cancellation, and recovery where applicable.
3. **Design/accessibility gate:** map existing components/tokens; define semantic
   names/roles/states, traversal/focus, announcements, touch targets, alternate
   input, font scaling, reduced motion, contrast evidence, safe areas, sizes,
   orientations, RTL, string expansion, and platform interaction conventions.
4. **Architecture/ownership gate:** assign disjoint UI, shared, navigation, and
   native files. Ask `mobile-architect` before changing navigation/state boundaries.
5. **Implementation:** primary owner adds only necessary route, screen, state
   integration, resources, and previews/fixtures already conventional. Preserve
   lifecycle/cancellation and prevent sensitive logging.
6. **Test gate:** `mobile-test-engineer` adds deterministic state logic and
   applicable UI/widget/component/navigation tests, including failure/recovery
   and accessibility assertions supported by the project.
7. **Review gate:** UI/accessibility reviewer checks all states and adaptations.
   Add security/performance review for permissions, sensitive data, WebViews,
   deep links, expensive rendering/assets, or background/network work.
8. **Validation gate:** run discovered compile, lint/static/format, targeted tests,
   and available platform UI validation. Final independent code review follows.

## Completion classification

Classify requirements/journey; navigation/state/configuration; compilation;
unit/integration/UI/snapshot/E2E tests; lint/static/formatting; dependencies;
security/secrets; accessibility/localization/adaptive layout; performance;
network/storage/offline; every UI/recovery state; documentation; warnings;
regressions; independent review; and platform-native checks as `required`,
`conditionally-required`, or `not-applicable`, each with a concrete reason.

## Errors and stop conditions

Stop for undefined product states/navigation, missing designs with material UI
choices, ambiguous state ownership, unapproved architecture/dependency changes,
credentials/external services, destructive operations, conflicting edits,
security uncertainty, or unfixable validation failures.

## Outputs, evidence, and acceptance

Return journey/state matrix, owner/files, navigation/state contracts, adaptive/
accessibility/localization decisions, tests, commands/results, review findings,
completion ledger, screenshots/runtime checks available or unavailable, warnings,
and residual risks.

Acceptance requires every applicable state and transition, platform-consistent
navigation, adaptive accessible/localizable UI, deterministic tests, successful
available validation, resolved blockers, and independent review.

## Human review and prohibited actions

Humans decide missing product/design behavior and sensitive permissions. Never
invent product states, add frameworks/dependencies, upload designs/code, access
external services, use secrets, sign/publish/deploy/submit, destroy data, or make
Git writes without exact authorization.
