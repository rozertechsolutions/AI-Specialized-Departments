---
name: add-mobile-screen
description: Add or plan a mobile screen with navigation, state coverage, accessibility, localization, and adaptive-layout review.
---

# Add Mobile Screen

## Inputs

- Screen requirements, target platform, navigation destination, UI states, design constraints, localization needs, and acceptance criteria.

## Preconditions

- Confirm UI framework and existing patterns from supplied files.
- Do not invent product copy, brand rules, API behavior, or navigation contracts.
- ChatGPT cannot run repository builds, tests, devices, simulators, signing, or release actions unless a separately enabled native tool supplies verifiable evidence.

## Owner And Reviewers

- Owner: relevant UI platform engineer.
- Reviewers: `mobile-ui-accessibility-reviewer`, `mobile-test-engineer`, and `mobile-code-reviewer`.

## Steps

1. Identify existing UI, navigation, state, theme, accessibility, and localization conventions.
2. Define loading, empty, error, content, retry, cancellation, and recovery states.
3. Scope implementation to the target screen and navigation wiring.
4. Define UI/snapshot/unit tests where supported.
5. Require accessibility/adaptive-layout review and final code review.

## Validation Gates

- Evidence: state matrix, platform conventions used, test plan, manual device/screen-reader checks still required.
- Completion: screen behavior is complete or unresolved design decisions are explicit.

## Prohibited Actions

- Do not fabricate visual validation, ignore accessibility, add analytics or permissions without approval, sign, publish, upload, deploy, or claim unrun checks passed.
