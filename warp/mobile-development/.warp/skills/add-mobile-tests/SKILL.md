---
name: add-mobile-tests
description: Add deterministic mobile tests across unit, integration, UI, snapshot, or end-to-end levels using existing tooling.
---

# Add Mobile Tests

## Objective

Add meaningful regression coverage without changing production behavior merely to pass tests.

## Trigger

Use when the user asks to add tests, improve coverage, reproduce a bug, or validate a mobile behavior.

## Inputs

Behavior under test, platform, existing test framework, fixtures, test level, determinism constraints, and acceptance criteria.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native.

## Preconditions

Inspect existing test layout, naming, fixtures, runners, mocks, CI scripts, and configured commands. Do not add dependencies without approval.

## Primary Owner

`mobile-test-engineer`.

## Reviewers

Relevant platform engineer and `mobile-code-reviewer`; add security or UI/accessibility reviewers when tests cover those surfaces.

## Steps

1. Identify the correct test level and framework from the project.
2. Design deterministic cases for success, failure, boundary, and regression behavior.
3. Reuse existing fixtures, fake clocks, schedulers, dispatchers, and mock servers where available.
4. Add test-only code only inside established test boundaries.
5. Run the new tests, then relevant neighboring tests.
6. Report coverage limits and unavailable infrastructure.

## Conditional Steps

- If a bug reproduction exists, ensure at least one test fails before the fix when feasible.
- If UI or end-to-end infrastructure is unavailable, add the nearest deterministic lower-level test and report the gap.
- If test helpers require production-code changes, stop unless the user requested that design change.
- If new dependencies or runners are required, stop for approval.

## Validation Gates

Required: new test passes, related tests pass, production behavior unchanged except requested behavior, no broad sleeps/flaky timing, and code review. Conditional: UI/snapshot/e2e runs when configured and safe.

## Failures and Stop Conditions

Stop if tests require production credentials, paid services, destructive device actions, signing, publication, unavailable simulators/emulators, or dependency additions without approval.

## Evidence

Record tests added, cases covered, commands run, outputs, fixtures used, flakiness controls, and skipped checks with reasons.

## Outputs

Deterministic tests, test evidence, and residual coverage gaps.

## Acceptance Criteria

Tests fail for the old bug or validate the requested behavior, pass locally where infrastructure is available, and do not weaken existing validation.

## Human Approvals

Required for dependencies, lockfiles, external services, credentials, emulator/device destructive actions, or long/resource-intensive suites.

## Prohibited Actions

Do not change production code only for test convenience, disable tests, add arbitrary sleeps, use fabricated success, access production data, sign, publish, upload, or deploy.
