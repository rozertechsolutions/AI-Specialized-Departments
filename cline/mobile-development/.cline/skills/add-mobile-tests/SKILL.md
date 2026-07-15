---
name: add-mobile-tests
description: Workflow for adding mobile unit, integration, UI, snapshot, or end-to-end tests with deterministic fixtures and validation evidence.
---

# Add Mobile Tests

## Objective

Add or improve mobile tests that are deterministic, scoped, and aligned with project conventions.

## Trigger

Use when the user asks to add tests, improve coverage, reproduce a bug, or validate behavior.

## Inputs

Behavior under test, target platform, existing test structure, commands, fixtures, mocks, and risk areas.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native.

## Preconditions

Discover existing test levels, tools, naming, fixtures, and command conventions before editing.

## Primary Owner

`mobile-test-engineer`

## Reviewers

Affected platform engineer and `mobile-code-reviewer`; security/accessibility/performance reviewers when tests cover those concerns.

## Steps

1. Map behavior to the smallest useful test level.
2. Reuse existing fixtures and helpers.
3. Add deterministic tests.
4. Avoid production changes unless explicitly required and reviewed.
5. Run targeted tests.
6. Run broader checks when reasonable.
7. Document remaining gaps.

## Conditional Steps

- UI tests: handle synchronization and flakiness.
- Snapshot tests: minimize churn and require visual rationale.
- API tests: use local fixtures/mocks unless external calls are approved.

## Validation Gates

Tests fail for the defect or cover the feature, pass after implementation, and do not weaken existing assertions.

## Failures

Stop on missing test infrastructure, flaky/unreliable setup, unrelated pre-existing failures, or approval-gated changes.

## Stop Conditions

Do not rewrite test infrastructure or update broad snapshots without approval.

## Evidence

Tests added/changed, commands run, pass/fail output, flakiness notes, and unavailable checks.

## Outputs

Test changes and validation report.

## Acceptance Criteria

Tests are meaningful, deterministic, scoped, and runnable with documented commands.

## Human Approvals

Required for broad snapshot updates, infrastructure changes, dependency changes, or external services.

## Prohibited Actions

No weakened assertions, skipped legitimate tests, fabricated results, or production behavior changes merely to pass tests.
