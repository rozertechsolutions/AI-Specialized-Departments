---
name: add-mobile-screen
description: Adds a mobile screen using the existing navigation and state architecture with complete UI states, adaptive layout, accessibility, localization readiness, platform conventions, tests, and independent review. Use for explicit screen or route implementation.
---

# Add a mobile screen

## Objective

Add a complete, navigable screen that follows the existing architecture and platform conventions and handles all applicable data, state, accessibility, localization, adaptive-layout, error, and recovery behavior.

## Trigger

Use when the user explicitly requests a new screen, page, view, route, destination, or substantial new UI flow. Use `implement-mobile-feature` when UI is incidental to a broader domain feature.

## Inputs

- screen purpose, entry/exit routes, parameters, deep-link behavior, and back behavior;
- data/actions, state owner, lifecycle, persistence, and refresh rules;
- required loading, empty, error, retry, offline, content, disabled, success, cancellation, and recovery states;
- supported devices, sizes, orientations, input methods, locales, and accessibility requirements;
- visual references and design tokens already available in the repository;
- acceptance criteria and test environments.

## Preconditions

- Read applicable instructions, navigation and state architecture, analogous screens, design system/theme, resources/strings, data/domain APIs, tests, and current changes.
- Confirm that supplied visual references are authorized project inputs; do not use an external design integration unless separately approved.
- Identify the technology owner and the existing navigation/state pattern. Obtain approval before changing either.
- Resolve ambiguous screen states, route contract, or destructive user actions before editing.

## Ownership

Primary owner: the technology engineer owning the screen. `mobile-ui-accessibility-reviewer` reviews but does not implement. Android/iOS specialists own host changes for Flutter/React Native, and `kmp-engineer` owns only shared KMP behavior.

## Sequence and intermediate gates

1. **Contract gate:** record route name, typed parameters, entry/exit/back/deep-link behavior, state machine, actions, data dependencies, and acceptance criteria.
2. **Architecture gate:** place navigation, state ownership, side effects, persistence, and domain calls in existing boundaries. Stop if adding the screen requires an unapproved navigation or state framework.
3. Define every applicable UI state and transition, including loading, empty, error, retry, offline/stale, content, disabled, progress, success, cancellation, and recovery.
4. Implement the route and screen with existing components, tokens, resources, and conventions. Avoid duplicating domain logic in the view.
5. Implement adaptive layout for supported window sizes, orientations, safe areas/insets, text expansion, keyboard/input, and platform interaction patterns.
6. Implement accessibility semantics, name/role/value/state, grouping, traversal, focus and restoration, announcements, gesture alternatives, target sizes, dynamic text, reduced motion, and error identification as applicable.
7. Externalize user-visible text and use project locale-aware formatting. Check expansion and bidirectional layout where supported.
8. Add deterministic state/unit/component/widget/UI/snapshot tests at the lowest configured levels that prove navigation and relevant states.
9. **Validation gate:** run targeted compile/type/static checks and tests, then available broader affected checks. Capture device/simulator, size, locale, orientation, and assistive-technology evidence actually used.
10. **Review gate:** invoke `mobile-ui-accessibility-reviewer`, security reviewer for sensitive data/input/navigation, performance reviewer for complex rendering, and `mobile-code-reviewer`. Resolve findings and repeat affected checks.

## Errors and stop conditions

- Do not fabricate assets, design values, text, navigation contracts, or backend behavior.
- If a required state cannot be represented by the existing domain API, stop and request an approved contract change.
- If UI/runtime environments are unavailable, report source/test evidence separately from unperformed visual or assistive-technology checks.
- A failed route, required state, accessibility blocker, or unresolved review finding blocks completion.

## Completion classification

Classify every coordinator criterion. Requirements, affected configuration, compilation/type checks, applicable UI tests, static checks, security, accessibility/localization, adaptive layout, complete UI states, warnings, regression evidence, and independent review are normally required. Dependencies, integration/snapshot/end-to-end levels, offline behavior, performance, storage/network, and documentation become required when the screen uses them.

## Outputs and evidence

Return the route/state contract, ownership, changed files, state-transition coverage, adaptive/accessibility/localization decisions, tests, exact commands and runtime environments, screenshots or traces only when actually produced, review findings, unavailable checks, and completion-classification table.

## Acceptance criteria

- Navigation, parameters, back/deep-link behavior, and all applicable states match the confirmed contract.
- The screen follows existing architecture and design conventions without duplicate domain logic.
- Required accessibility, localization, adaptive behavior, and platform conventions have evidence.
- Required checks pass and independent review has no unresolved blocking finding.

## Human review requirements

Humans approve visual/design interpretation, navigation or state architecture changes, destructive actions, permissions, user-facing copy when not supplied, unavailable device/accessibility validation, and accepted residual risk.

## Prohibited actions

Do not invent designs or content, enable Figma or another external integration, add frameworks/dependencies without approval, weaken accessibility, use sensitive data in previews/tests, publish/sign/deploy, or self-approve.
