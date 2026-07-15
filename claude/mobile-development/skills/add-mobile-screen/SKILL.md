---
name: add-mobile-screen
description: Adds a mobile screen or route with complete states and accessibility. Use for Android, iOS, KMP, Flutter, or React Native UI work.
---

# Add Mobile Screen

## Objective

Add one approved screen, destination, or route using existing UI, navigation, state, design-system, localization, and platform conventions, with complete accessible and adaptive states.

## Trigger

Use when the primary request is a new screen, destination, route, modal, tab, or comparable user-visible view. Use implement-mobile-feature when the request spans a broader domain feature.

## Inputs

- screen purpose, entry and exit paths, user journeys, and acceptance criteria;
- approved design source, content, states, interactions, analytics requirements, and platform differences;
- navigation contract, state owner, data source, error behavior, permissions, and deep-link behavior;
- supported devices, window sizes, orientations, text sizes, input methods, and locales;
- existing UI components, design tokens, test conventions, and screenshots when safe.

## Supported technologies

Android Compose or Views, iOS SwiftUI or UIKit, Compose Multiplatform only when present, Flutter, and React Native.

## Preconditions

- Design and behavior are authoritative and sufficiently complete.
- Existing navigation, state, component, localization, and theme conventions are inspected.
- Target platforms and adaptive conditions are known.
- No placeholder content, invented copy, or fabricated data is required.
- One UI technology owner is selected.

## Primary owner and reviewers

android-engineer, ios-engineer, kmp-engineer for existing shared Compose Multiplatform UI, flutter-engineer, or react-native-engineer owns the screen. mobile-ui-accessibility-reviewer is mandatory. mobile-test-engineer reviews UI and state coverage. mobile-security-reviewer reviews input, permissions, deep links, WebViews, auth, privacy, or sensitive display. mobile-performance-reviewer reviews image, list, animation, or startup-sensitive screens. mobile-code-reviewer is final.

## Ordered workflow

1. Trace screen requirements, navigation entry and exit, user actions, states, platform differences, and non-goals.
2. Inspect repository status, relevant UI components, theme, navigation, state management, localization, analytics, tests, and design evidence.
3. Define the screen contract: inputs, outputs, state owner, events, side effects, navigation behavior, restoration, and error recovery.
4. Inventory required states: initial, loading, content, empty, partial, error, retry, offline, permission-denied, cancellation, and recovery. Mark each required or not applicable with a reason.
5. Define accessibility and adaptive acceptance: semantics, labels, roles, focus, traversal, dynamic text, contrast evidence, touch targets, orientation, keyboard, screen reader, locale expansion, and reduced motion when applicable.
6. Reuse existing components and design tokens. Obtain approval before introducing a component, dependency, asset pipeline, analytics event, permission, or navigation contract.
7. Implement the smallest platform-appropriate screen and route integration, separating host code and shared code by ownership.
8. Add state, navigation, UI, snapshot or golden, and accessibility tests supported by the project.
9. Run targeted formatter, analysis, compilation, and tests for the affected UI.
10. Inspect representative sizes, orientations, locales, text scaling, focus behavior, and complete states using available tools. Mark missing devices or assistive technology unavailable.
11. Obtain UI, security, performance, test, and final code reviews as applicable; return findings to the owner.
12. Rerun validation, triple review, and final verification.

## Conditional steps

- Deep link: require validation, authorization, navigation, fallback, and security review.
- WebView: require origin, navigation, JavaScript bridge, file access, cookie, download, and external-link review.
- Form: require input validation, keyboard behavior, autofill, error association, submission state, retry, and privacy review.
- Lists or media: require performance, memory, pagination, cancellation, placeholder policy, and offline behavior.
- KMP shared UI: validate each configured target and keep platform-specific behavior behind explicit boundaries.

## Validation gates

- Gate 1: design, copy, navigation, state, and target conditions are explicit.
- Gate 2: all UI states and accessibility requirements are classified.
- Gate 3: implementation reuses established components and introduces no unapproved dependency or contract.
- Gate 4: applicable UI, state, navigation, localization, and accessibility checks pass.
- Gate 5: reviewers have no unresolved required finding.
- Gate 6: final evidence covers every acceptance state and target, or labels it unavailable.

## Failures

If design and behavior conflict, stop and request a product decision. If a UI test or rendering check fails, preserve evidence and fix the owned UI rather than weakening assertions or hardcoding a device-specific layout. Never claim accessibility from source review alone when runtime evidence is required.

## Stop conditions

Stop for missing design or copy, undefined navigation or state ownership, unknown target conditions, unapproved analytics, permission, deep link, WebView, dependency, asset license, sensitive display, inaccessible required design source, or conflicting user changes.

## Evidence

Record design source and freshness, changed files, component reuse, state mapping, routes, screenshots or accessibility-tree evidence when available, locales, sizes, text scale, commands, tests, warnings, reviewer findings, and unavailable conditions.

## Outputs

- screen and route changes;
- complete state and interaction handling;
- localized and accessible content using project conventions;
- relevant tests and documentation;
- criterion ledger and review evidence.

## Acceptance criteria

The screen matches approved behavior, integrates with existing navigation and state, handles all applicable states, is accessible and adaptive on supported targets, introduces no unauthorized analytics or permission, and passes independent final review.

## Human approvals

Require approval for design or copy decisions, navigation contracts, analytics, permissions, deep links, WebViews, new components or dependencies, assets or licenses, privacy behavior, and unverified accessibility waivers.

## Prohibited actions

Do not invent copy or data, use placeholders as production output, add unapproved analytics or dependencies, ignore UI states, claim accessibility without evidence, expose sensitive content, self-review, sign, publish, upload, deploy, or run Git write commands.
