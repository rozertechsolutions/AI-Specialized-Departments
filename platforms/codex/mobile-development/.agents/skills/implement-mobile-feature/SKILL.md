---
name: implement-mobile-feature
description: Implement a complete, scoped feature in an existing Android, iOS, KMP, Flutter, or React Native project, including tests and risk-based specialist review. Do not use for project creation or release preparation.
---

# Implement Mobile Feature

## Objective

Deliver one defined mobile feature end to end while preserving existing architecture, contracts, user changes, supported targets, security, and quality gates.

## Required inputs

- Feature behavior, user-visible states, non-goals, and acceptance criteria.
- Target platform/module/variant and supported OS/device matrix.
- Relevant API, navigation, persistence, analytics, and design contracts.
- Error, loading, empty, cancellation, retry, and offline expectations where applicable.
- Existing verification commands and any approved dependency/public-contract changes.

Derive these from authoritative code and documentation where possible. Ask before proceeding if a missing decision materially changes behavior.

## Preconditions

1. Inspect applicable instructions, status/diff, architecture, affected code, tests, manifests, dependencies, and generated-file boundaries.
2. Reproduce or document current behavior and identify the smallest implementation boundary.
3. Confirm there is no conflicting user work.
4. Classify validation criteria as required, conditional, or not applicable.
5. Confirm no signing, publishing, production credential, paid service, destructive device, or unapproved dependency action is needed.

## Agent ownership

The coordinator selects exactly one primary platform owner: `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer`. Use `mobile-architect` only for cross-module/public-contract or unclear-boundary decisions. `mobile-test-engineer` owns test artifacts. Invoke `mobile-security-reviewer` for sensitive data/auth/network/storage/permissions, `mobile-ui-accessibility-reviewer` for UI, and `mobile-performance-reviewer` for measurable hot-path impact. `mobile-code-reviewer` performs the independent final review.

Sequence overlapping writes. Reviewers remain read-only and do not approve their own work.

## Execution

1. **Contract.** Restate the exact behavior, supported states, affected boundary, non-goals, and done conditions.
2. **Trace current flow.** Follow entry points, state/data flow, lifecycle, persistence, networking, and existing tests. Record evidence; do not guess.
3. **Architecture gate.** If the change crosses established boundaries, have `mobile-architect` recommend the minimal design. Stop if it requires an unapproved API, persistent format, dependency, target, or architecture change.
4. **Implementation plan.** The platform owner lists files to change, failure paths, compatibility concerns, and test seams before editing.
5. **Implement.** Make the smallest complete production change using existing abstractions. Preserve backward compatibility and platform conventions. Do not add placeholder code or broad suppressions.
6. **Intermediate gate.** Inspect the focused diff. Confirm only assigned files changed, state/lifecycle/error paths are complete, and no sensitive configuration changed without human review.
7. **Tests.** `mobile-test-engineer` adds or updates deterministic tests for core success, failure, boundary, cancellation/lifecycle, and regression cases as applicable. Production testability requests return to the platform owner.
8. **Targeted verification.** Run the narrowest compile/type/lint/test commands that cover the change. Fix change-caused failures and rerun.
9. **Risk-based review.** Run required security, UI/accessibility, and performance reviewers. Each returns evidence-based findings; the platform owner implements accepted fixes.
10. **Independent code review.** `mobile-code-reviewer` reviews the full scoped diff for correctness, regression, concurrency, lifecycle, error handling, maintainability, and missing tests.
11. **Broader verification.** Run the relevant broader local suite when reasonable and safe. For UI, validate supported sizes, text scaling, localization, navigation, and error/loading/empty states. For network/data work, validate offline and failure behavior.
12. **Final gate.** Review the final diff and validation matrix. Do not complete while any required check or review is failing or unresolved.

## Error handling and stop conditions

Stop on ambiguous acceptance behavior, conflicting user edits, missing required tools, unavailable required test environment, unapproved dependency/API/persistence/architecture change, sensitive action requiring user direction, production access, signing/publication, or unrelated failures that prevent attribution. Report exact evidence and the smallest decision needed.

## Outputs

- Behavior implemented and file list.
- Architecture decision used or reason it was unnecessary.
- Tests added and scenarios covered.
- Commands/checks with pass/fail/not-run status.
- Specialist and code-review findings, fixes, and residual risks.
- Any blocked human decision or unverified condition.

## Acceptance criteria

- Every stated acceptance criterion is implemented and traceable to code/tests or explicit manual evidence.
- Required compile, static, and test checks pass without weakened validation.
- Applicable security, accessibility, performance, network/offline, lifecycle, and documentation criteria pass.
- The final diff is minimal, contains no secret or unauthorized configuration, and introduces no unexplained warning or regression.

## Prohibited actions

Do not add dependencies or change public/persistent contracts without approval, sign or publish, use production credentials/data, run destructive device commands, bypass validation, fabricate test evidence, edit generated files outside their supported workflow, or include unrelated cleanup.
