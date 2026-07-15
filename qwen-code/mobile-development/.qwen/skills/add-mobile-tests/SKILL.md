---
name: add-mobile-tests
description: Add deterministic mobile unit, integration, UI, widget, component, snapshot, or end-to-end tests at the lowest effective level with controlled fixtures and flakiness prevention.
user-invocable: true
---

# Add Mobile Tests

## Objective

Add the smallest deterministic test set that proves the requested behavior and failures at the lowest effective levels without changing production behavior or weakening validation.

## Trigger

Use when the user explicitly asks to add, improve, or repair tests or regression coverage. Use `fix-mobile-bug` when diagnosis and a production correction are also requested.

## Inputs

- Behavior/contract to prove, defect history, affected platforms/targets, and desired confidence.
- Existing test conventions, CI constraints, supported devices, and known flakiness.
- Approved test-only paths and any explicitly approved production testability seam.

## Preconditions

- Read instructions, status/diff, behavior implementation, existing tests/runners/configuration, fixtures/helpers, CI commands, and current user changes.
- Establish expected behavior from code/specification; tests must not silently redefine it.
- Discover available SDKs, simulators/emulators/devices, and local services without installing or starting external infrastructure.

## Ownership

- Primary owner: `mobile-test-engineer` for strategy, fixtures, determinism, and test-only implementation assigned by the coordinator.
- Relevant platform engineer owns any platform-specific production seam and may own tightly coupled platform test files under an explicit boundary.
- `mobile-code-reviewer` independently reviews final test quality; security/accessibility/performance review is conditional on tested behavior.

## Tool and permission boundary

Use read/search first, then edit only approved test/fixture/config paths. Run narrow project-defined local tests under normal approval. No production behavior change, package install, external/production data, credentials, service writes, validation bypass, signing, or publishing.

## Sequence and gates

1. **Contract gate:** Map each requested behavior to an observable assertion and identify success, boundary, invalid, error, cancellation, retry/recovery, lifecycle, concurrency, offline, and accessibility cases as applicable.
2. **Level gate:** Compare unit, integration, component/widget, UI, snapshot, and end-to-end levels. Choose the lowest level proving each contract and justify every higher-level test.
3. **Convention gate:** Inspect existing runners, naming, setup/teardown, fixtures, mocks/fakes, matchers, synchronization, snapshot policy, and CI commands. Preserve them.
4. **Determinism gate:** Control clock, randomness, locale, timezone, scheduler, network, storage, filesystem, animation, and device state as applicable. Define isolation and cleanup without deleting uncertain data.
5. **Implementation gate:** Add focused tests with meaningful assertions. Mock only genuine boundaries, keep fixtures minimal/non-sensitive, and avoid coupling to implementation details unless the contract requires it.
6. **Flakiness gate:** Use condition-based UI synchronization, deterministic dispatchers/clocks, independent setup, and bounded controlled retries only when the system contract itself retries. Never add arbitrary sleeps or order dependence.
7. **Execution gate:** Run the narrow test, repeat when nondeterminism is plausible, then run the relevant suite. Record command, target/device, repetitions, exit codes, duration when useful, and failures.
8. **Coverage gate:** Confirm the new test fails for the missing/regressed behavior when feasible without destructive source manipulation; otherwise explain the causal evidence. Review snapshot changes semantically.
9. **Independent review gate:** Verify assertions, failure sensitivity, fixtures, isolation, test level, coverage gaps, and no production behavior changes. Correct and fully repeat after findings.
10. **Completion gate:** Classify every `QWEN.md` criterion; distinguish unavailable device/integration/E2E infrastructure from passed tests.

## Errors and stop conditions

Stop if expected behavior is ambiguous, a production change is needed but unapproved, the runner/dependency is missing, test execution needs credentials/production/external writes, fixtures contain sensitive data, validation requires weakening, flakiness cannot be controlled, or required tests fail.

## Outputs and evidence

- Behavior-to-assertion and test-level matrix.
- Exact test/fixture/config paths changed; production paths must be explicit or `none`.
- Determinism and synchronization design.
- Exact commands, targets/devices, repetitions, exit codes, and observed results.
- Completion ledger, review findings/corrections, coverage gaps, and unavailable infrastructure.

## Acceptance criteria

- Each test proves an agreed behavior and fails meaningfully when that behavior is absent.
- Fixtures are deterministic, minimal, isolated, and non-sensitive; UI tests use condition-based synchronization.
- Relevant tests pass repeatedly as justified, and no validation/test standard is weakened.
- Independent review has no unresolved blocker and production behavior was not changed merely for tests.

## Human review requirements

Humans resolve expected-behavior ambiguity, approve production testability seams, snapshot semantics, external/device lab use, credentials, dependencies, and accepted infrastructure gaps.

## Prohibited actions

Do not change production behavior solely for tests, over-mock the subject, use arbitrary sleeps, hide flakes with retries/quarantine, weaken assertions/coverage, update snapshots blindly, use real personal/production data, install tools, or self-approve.
