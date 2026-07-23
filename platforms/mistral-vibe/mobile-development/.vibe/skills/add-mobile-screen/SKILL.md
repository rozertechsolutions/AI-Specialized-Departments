---
name: add-mobile-screen
description: Use when adding a defined screen or view to an existing mobile app with navigation, complete states, adaptive layout, accessibility, localization readiness, and tests.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - todo
  - ask_user_question
  - task
  - write_file
  - edit
  - bash
---

# Add Mobile Screen

## Objective and trigger

Add one platform-consistent screen and its navigation/state integration, covering loading, empty, error, content, retry, offline, interruption, and recovery states as applicable.

## Inputs

- Screen purpose, entry/exit/navigation behavior, supported platforms/sizes/orientations, data/actions, state owner, designs or explicit behavior, localization content, analytics/privacy needs, and acceptance criteria.
- Required large-text, assistive-technology, keyboard/input, animation, and platform convention behavior.

## Preconditions and ownership

Inspect instructions, status/diff, navigation/state/component/design systems, representative screens/tests, localization/resources, and platform constraints. Partition every affected runtime into non-overlapping units and assign one platform owner per unit: shared KMP, framework UI, and native host/UI files retain their matrix owners. Each platform owner owns its screen tests unless the coordinator explicitly separates a bounded test-only unit for `mobile-test-engineer`. Use `mobile-architect` only for a new navigation/state boundary. UI/accessibility review is required; security/performance review is conditional; code review is final.

## Sequence and gates

1. State/navigation gate: define route identity, arguments/results, back/deep-link behavior, state lifetime/owner, restoration, cancellation, and every UI state. Obtain approval for contract changes.
2. Layout/accessibility plan: map adaptive breakpoints/window sizes, orientation, insets, scalable text, semantics, focus/traversal, touch targets, contrast evidence, motion, alternative input, and bidirectional/localized content.
3. Implement with existing components, themes, navigation, state, and resource patterns. Keep business/data logic at established boundaries.
4. Implement actions, validation, concurrency/race prevention, lifecycle cleanup, and loading/empty/error/retry/offline/recovery behavior.
5. Intermediate UI/accessibility review blocks on missing semantics, focus, large-text, adaptive, localization, or state behavior. Security review any sensitive input/data/deep link/WebView; performance review heavy rendering/media/lists.
6. The assigned test owner adds deterministic state, navigation, interaction, failure, accessibility, and snapshot/UI coverage where supported; `mobile-test-engineer` validates level selection, synchronization, fixtures, and flakiness risk.
7. Run discovered format/static/lint/compile/tests and reasonable UI validation. Record device/simulator, locale, font scale, size/orientation, and limitations.
8. Independent code review; correct, rerun, and inspect final diff.

## Errors and stop conditions

Stop on missing behavior/design/navigation/state decisions, unapproved dependencies or new framework, unknown platform support, sensitive behavior awaiting approval, unavailable required test environment, conflicting user edits, signing/production needs, or unrelated failures.

## Outputs and evidence

Provide state/navigation contract, changed files, adaptive/accessibility/localization decisions, screenshots/manual evidence if supplied, tests, commands/results, criterion matrix, reviews, limitations, and blockers.

## Acceptance and human review

All defined states and transitions work; navigation/restoration/lifecycle are correct; required adaptive/accessibility/localization checks pass; tests and safe platform validation pass; independent review is clear; no new dependency or unrelated change exists. Humans approve new navigation/public contracts, sensitive input/data behavior, permissions, or analytics.

## Prohibited actions

Do not invent design/content, add a UI/state framework without approval, hard-code user-visible strings, omit failure/recovery states, weaken accessibility/tests, use production data, sign/publish/deploy, or claim untested devices/locales passed.
