---
name: add-mobile-tests
description: Add deterministic mobile unit, integration, UI, snapshot, or end-to-end tests without changing production behavior merely to pass tests.
---

# add-mobile-tests

## Objective

Add or improve tests that cover meaningful mobile behavior while preserving production correctness.

## Inputs

Behavior to cover, affected platform(s), current test gaps, bug/feature context, and approved scope.

## Supported Technologies

Android unit/instrumented/UI tests, iOS unit/UI tests, KMP shared/platform tests, Flutter unit/widget/integration tests, React Native unit/component/e2e tests.

## Preconditions

- Inspect current test frameworks, fixtures, synchronization, CI scripts, naming conventions, and flaky-test notes.
- Identify the production behavior under test before editing.
- Do not alter production behavior solely to make tests pass.

## Primary Owner

`mobile-test-engineer`

## Reviewers

Relevant technology owner and `mobile-code-reviewer`; add security/accessibility/performance reviewers when tests cover those areas.

## Steps

1. Select the minimum useful test level.
2. Add deterministic fixtures, mocks, snapshots, or synchronization using existing conventions.
3. Cover success, failure, edge, loading, empty, retry, cancellation, offline, recovery, and invalid states where relevant.
4. Run targeted tests and broader affected checks when reasonable.
5. Report flakes, unavailable infrastructure, and gaps.
6. Complete independent final review.

## Validation Gates

Target test pass, affected suite pass where reasonable, build/type/lint/static checks when touched, fixture determinism, no weakened assertions, and no production-only-for-test behavior.

## Failures And Stop Conditions

Stop on missing test harness, external service dependence, flaky synchronization, need for production behavior change, missing approval for dependency/lockfile changes, or unrelated failures.

## Evidence And Outputs

Tests added/updated, commands run, failures, unavailable infrastructure, determinism notes, and coverage rationale.

## Acceptance Criteria

Tests meaningfully cover requested behavior, run deterministically in available infrastructure, and do not weaken validation.

## Prohibited Actions

No disabling tests, weakening assertions, broad sleeps for synchronization, fabricated pass results, or unrelated production changes.
