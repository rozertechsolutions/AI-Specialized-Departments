---
name: add-mobile-tests
description: Add deterministic unit, integration, UI, contract, accessibility, snapshot, or benchmark tests to an existing mobile project using its current test stack. Do not use to hide production defects or introduce a new test framework without approval.
---

# Add Mobile Tests

## Objective

Add the smallest high-value test coverage for defined behavior using existing project tools, without changing production behavior, contacting live services, or creating flaky/non-diagnostic tests.

## Required inputs

- Behavior, defect, risk, or coverage gap to prove.
- Expected outcomes and important boundaries/failure modes.
- Target platform/module/variant and available test runners/devices.
- Existing test conventions, fixtures, and acceptable test duration.

If expected behavior is ambiguous, stop and obtain it before encoding a test.

## Preconditions

1. Inspect instructions, status/diff, production behavior, current tests/runners, test dependencies, fixtures, CI conventions, and generated snapshots.
2. Identify the lowest stable boundary that proves the behavior.
3. Confirm no new dependency/runner, production credential/data, destructive reset, signing, or external service is required.
4. Record pre-existing failures and establish the exact command baseline.
5. Classify every completion criterion as required, conditionally required, or not applicable with a documented reason.

## Agent ownership

`mobile-test-engineer` owns all test and test-only configuration changes. The relevant platform owner may provide read-only behavior/testability evidence and must own any production-code seam requested by the test engineer. Use `mobile-ui-accessibility-reviewer` for accessibility assertions, `mobile-security-reviewer` for security expectations, and `mobile-performance-reviewer` for benchmark methodology. The coordinator approves any production or dependency change.

## Execution

1. **Test contract.** Define the behavior, inputs, observable outputs, failure message, isolation boundary, and why this test type is appropriate.
2. **Baseline.** Run the narrow existing test command or demonstrate the missing coverage. For a regression, confirm the proposed test fails for the intended reason before the fix when feasible.
3. **Select level.** Prefer unit tests for logic, integration/contract tests for boundaries, UI tests for user flows, accessibility tests for semantics, and benchmarks only for stable measurable budgets. Avoid duplicating the same assertion at every level.
4. **Design deterministic data.** Use minimal fabricated fixtures/fakes, fixed clocks/schedulers/IDs when supported, controlled network/storage, and explicit cleanup. Never use real secrets or personal/production data.
5. **Implement tests.** Follow naming, structure, matcher, async, and resource-cleanup conventions. Make failures identify the violated behavior.
6. **Production-seam gate.** If testing requires a production change, stop and request a minimal seam from the platform owner. Do not change production code yourself unless the coordinator explicitly reassigns that exact file and scope.
7. **Run targeted tests repeatedly.** Confirm deterministic pass behavior and that no arbitrary sleeps/retries are needed. For snapshots/goldens, inspect every changed artifact and keep only intentional changes.
8. **Negative check.** Where practical, perturb/revert the behavior locally or verify the test's assertion path to show the test would catch the defect. Do not leave temporary changes.
9. **Broader checks.** Run the relevant test group and static/compile checks. Identify unrelated pre-existing failures without changing them.
10. **Final review.** Inspect the test-only diff for over-mocking, implementation coupling, missing edge cases, leaked resources, broad snapshots, and unrelated fixture churn.

## Error handling and stop conditions

Stop on ambiguous expected behavior, unavailable required runner/device, production access, real credentials/data, dependency/runner changes without approval, a test that can only pass through arbitrary timing, destructive device setup, or pre-existing failures that make attribution impossible. Report a testability recommendation rather than writing a misleading test.

## Outputs

- Test matrix with level and rationale.
- Test/test-only files changed.
- Baseline, targeted, repeated, and broader command results.
- Completion matrix with required/conditional/not-applicable status, reasons, and exact results.
- Production seam or dependency requests not implemented.
- Flakiness, device, snapshot, or environment limitations.

## Acceptance criteria

- Each test protects a stated behavior and fails diagnostically when violated.
- Tests are isolated, deterministic, clean up resources, and contain only fabricated non-sensitive data.
- Targeted and relevant broader test/static checks pass.
- No production behavior, dependency, validation strength, or unrelated snapshot/fixture changed without approval.

## Prohibited actions

Do not call live services, use real secrets/data, add arbitrary sleeps or blanket retries, disable/quarantine tests, accept snapshots without inspection, mock the subject under test, add dependencies without approval, mutate production code silently, erase devices, sign, or publish.
