---
name: add-mobile-tests
description: Adds deterministic test-only coverage for mobile behavior. Use for Android, iOS, KMP, Flutter, or React Native testing work.
---

# Add Mobile Tests

## Objective

Add the smallest deterministic test-only coverage that proves approved mobile behavior, catches a stated regression or risk, and respects existing test architecture without changing production semantics.

## Trigger

Use when the primary request is to add, improve, organize, or diagnose tests and fixtures without implementing new production behavior.

## Inputs

- behavior and acceptance criteria to prove;
- risk, regression, or coverage gap;
- current production code and existing tests;
- configured test levels, runners, targets, destinations, fixtures, coverage conventions, and commands;
- allowed environments, devices, simulators, services, and data;
- known flakiness or timing evidence.

## Supported technologies

Android unit and instrumented or UI tests, iOS unit and UI tests, KMP shared and platform tests, Flutter unit, widget, golden and integration tests, and React Native unit, component and configured end-to-end tests.

## Preconditions

- Expected behavior is authoritative.
- Existing test infrastructure and project commands are discovered.
- The requested coverage can be achieved in test files and fixtures only.
- Fixtures contain no secret, production personal data, or live credential.
- Required devices or services are safe and explicitly approved.

## Primary owner and reviewers

mobile-test-engineer is primary. The relevant technology owner reviews expected behavior and platform conventions but does not transfer production work into this Skill. mobile-security-reviewer reviews sensitive fixtures, auth, network, storage, and external services. mobile-ui-accessibility-reviewer reviews UI and accessibility assertions. mobile-code-reviewer performs final read-only review.

## Ordered workflow

1. Map each acceptance criterion or risk to the lowest reliable test level.
2. Inspect repository instructions, status, production behavior, test directories, helpers, fixtures, synchronization, naming, runners, and commands.
3. Run the narrowest existing test or safe observation to establish current behavior and infrastructure.
4. Define test cases, inputs, outputs, failure reason, isolation boundary, deterministic clock or scheduler needs, and cleanup.
5. Prefer existing fixtures and helpers. Obtain approval before new dependency, test plugin, external service, emulator image, snapshot update, or production test hook.
6. Implement only test code and clearly synthetic fixtures. Keep mocks at real boundaries and avoid reproducing the implementation algorithm in assertions.
7. Confirm a regression test fails for the intended reason before a known fix when safe evidence is available. Do not manufacture a failure by altering production.
8. Run the smallest test target and inspect complete output, duration, warnings, skips, retries, and generated snapshots.
9. Run adjacent suites and repeat timing-sensitive tests enough to assess determinism when authorized.
10. Validate cleanup, ordering independence, locale and timezone stability, lifecycle, concurrency, network failure, cancellation, and device state as applicable.
11. Obtain specialist and final reviews, resolve test-only findings through mobile-test-engineer, and rerun.
12. Complete criterion ledger, triple review, and final verification.

## Conditional steps

- UI tests: verify stable semantics or identifiers, focus and accessibility behavior, supported destinations, screenshots, and system UI boundaries.
- Snapshot or golden tests: require deliberate human review of expected output and stable fonts, locale, scale, and rendering environment.
- Network tests: use deterministic fakes or approved non-production fixtures; cover timeout, retry, cancellation, offline, and malformed data.
- Flaky tests: collect repeated-run evidence, identify synchronization or isolation root cause, and never hide it with arbitrary sleep or blanket retry.
- End-to-end tests: use only existing configured infrastructure, safe accounts, and non-destructive scenarios.

## Validation gates

- Gate 1: each test maps to an approved behavior or risk.
- Gate 2: test level and fixture design are justified and contain no sensitive data.
- Gate 3: tests fail and pass for the intended reason when regression evidence is available.
- Gate 4: targeted and adjacent suites pass with no unexplained skip, retry, or warning.
- Gate 5: production files and behavior remain unchanged.
- Gate 6: final review and triple validation pass.

## Failures

Classify failures as product defect, test defect, environment failure, or flakiness. Preserve exact output and do not disable, quarantine, weaken, broadly retry, or silently skip a legitimate test. Return any required production testability change to the coordinator for separate authorization.

## Stop conditions

Stop for undefined expected behavior, required production change, real credentials or personal data, production service dependency, destructive device state, unavailable required runner, unapproved dependency, paid infrastructure, or conflicting user changes.

## Evidence

Record behavior mapping, test level rationale, changed test files, fixture provenance, commands, destinations, results, duration, repetitions, skips, retries, warnings, coverage limits, and reviewer findings.

## Outputs

- test-only changes and synthetic fixtures;
- behavior-to-test traceability;
- deterministic execution evidence;
- flakiness and infrastructure assessment;
- criterion ledger and remaining gaps.

## Acceptance criteria

Tests are scoped, deterministic, meaningful, independent, aligned with project conventions, capable of catching the stated defect or risk, free of sensitive data, and do not require a production semantic change.

## Human approvals

Require approval for dependencies, production test hooks, snapshot updates, external services, accounts, paid infrastructure, device state, personal data, and destructive test scenarios.

## Prohibited actions

Do not change production behavior, use real credentials or live-user data, copy implementation logic into assertions, add arbitrary sleeps or retries, disable tests, approve snapshots without review, fabricate coverage, sign, publish, deploy, or run Git write commands.
