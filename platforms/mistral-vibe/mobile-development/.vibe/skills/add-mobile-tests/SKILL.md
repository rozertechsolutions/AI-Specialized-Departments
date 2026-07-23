---
name: add-mobile-tests
description: Use when adding deterministic mobile regression, unit, integration, component/widget, snapshot, UI, or end-to-end coverage using the project's existing test stack.
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

# Add Mobile Tests

## Objective and trigger

Add the lowest, most reliable test coverage that proves defined behavior and failure paths without changing production semantics or introducing a new test framework.

## Inputs

- Behavior/contract to prove, regression scenario, supported platforms/versions, risk and acceptance criteria, existing test stack/conventions, environment constraints, and known safe commands.
- Required success, boundary, error, cancellation, retry/offline, lifecycle, accessibility, and concurrency cases.

## Preconditions and ownership

Inspect instructions, status/diff, production behavior, existing tests/fixtures/utilities, manifests/build scripts, CI declarations, and available local test environments. The relevant platform owner owns platform-specific test files by default. `mobile-test-engineer` owns strategy, level selection, reusable fixtures, determinism, and flakiness review; it owns test files only when the coordinator explicitly records a bounded, non-overlapping standalone test-only unit and transfers that unit. The platform owner retains every production change as a separate unit. Code review is independent; security/UI/performance review is conditional on test scope.

## Sequence and gates

1. Test-plan gate: map each acceptance criterion/risk to the appropriate level. Prefer unit/component tests; justify integration/UI/end-to-end cost and avoid duplicated assertions.
2. Confirm observability and seams. If production behavior is untestable, request the smallest seam from the platform owner and obtain approval before any production edit.
3. Create deterministic local fixtures/fakes/builders following project conventions. Use no live network, production data, real time, shared global state, real credentials, or order dependence.
4. The recorded test-file owner implements tests for the defined success and relevant error/boundary/cancellation/lifecycle/concurrency/accessibility paths with behavior-focused assertions.
5. Synchronization gate: replace arbitrary sleeps with framework-supported idling, clocks, schedulers, await conditions, or controlled dispatchers.
6. Run the narrow test first. Demonstrate regression value when possible, then run the reasonable affected suite and repeat susceptible tests to assess flakiness.
7. Run related static/type/lint/compile validation when test code participates in those gates; preserve warnings and environment details.
8. Independent code review checks correctness, false-positive/negative risk, maintainability, isolation, and coverage gaps. Correct and rerun.

## Errors and stop conditions

Stop on ambiguous expected behavior, absent seam requiring unapproved production change, unavailable framework/toolchain/simulator, required live/paid/production access, real secrets/data, destructive reset, unapproved dependency/plugin, generated-test restrictions, conflicting user edits, or unrelated failures.

## Outputs and evidence

Provide criterion-to-test map, explicit ownership or transfer record, chosen levels and rationale, files/fixtures, exact commands/environment/results, repeat/flakiness evidence, uncovered risks, requested production seams, criterion matrix, review findings, and blockers.

## Acceptance and human review

Tests deterministically prove the requested behavior and relevant failures, fail for the intended regression when demonstrable, pass through discovered commands, introduce no unexplained warning, and pass independent review. Humans approve new frameworks/dependencies, production seams, destructive simulator setup, or external test infrastructure.

## Prohibited actions

Do not alter production behavior merely for a pass, weaken/skip/quarantine tests, add arbitrary sleeps, call live services, use credentials/real user data, install a framework, erase devices, sign/publish/deploy, or report tests not run.
