---
name: add-mobile-tests
description: Adds deterministic mobile regression coverage at the lowest effective configured test level, including failures and edge cases, fixture control, flakiness prevention, execution evidence, and independent review. Use for explicit test additions or test-quality work.
---

# Add mobile tests

## Objective

Add maintainable tests that prove the requested behavior at the lowest effective configured level, control nondeterminism, cover relevant failures and edges, and provide reproducible execution evidence.

## Trigger

Use for explicit requests to add unit, integration, component/widget, UI, snapshot/golden, or end-to-end tests; improve regression coverage; or correct test flakiness.

## Inputs

- behavior or defect to prove and acceptance criteria;
- affected technology, target, module, and supported environment;
- risk cases, failure modes, boundaries, lifecycle/concurrency, offline, locale, accessibility, and performance concerns;
- existing test frameworks, commands, fixtures, CI constraints, and current failures.

## Preconditions

- Read applicable instructions, production contract and implementation, nearest existing tests/helpers/fixtures, test configuration, CI commands, and current changes.
- Confirm whether production behavior is correct. Route legitimate production changes to the technology owner rather than hiding them in test work.
- Do not add a framework, runner, dependency, emulator/device service, or snapshot system without explicit approval.

## Ownership

Primary owner: `mobile-test-engineer`. The technology owner clarifies production behavior and makes any separately approved production fix. Domain reviewers and `mobile-code-reviewer` remain independent.

## Sequence and intermediate gates

1. **Behavior gate:** translate requirements into observable assertions and identify false positives/negatives. Stop if expected behavior is ambiguous.
2. **Level gate:** choose the lowest level that proves the behavior. Record why higher and lower levels are unnecessary or insufficient. Reuse configured frameworks.
3. Map success, failure, edge, null/empty, cancellation, retry, offline, lifecycle, state-restoration, concurrency, locale, accessibility, and regression cases that are applicable.
4. Design minimal fixtures and control time, randomness, scheduling, IDs, storage, network, locale/time zone, device dimensions, animation, and global state.
5. Implement tests using behavior-oriented assertions and existing helpers. Avoid duplicating production algorithms in expected values.
6. For UI tests, use condition/idling-based synchronization and stable semantic identifiers only where project conventions support them; never add arbitrary sleeps.
7. For snapshots/goldens, confirm deterministic fonts, locale, OS/rendering baseline, dimensions, and approved update procedure before changing baselines.
8. **Execution gate:** run the smallest new test set, demonstrate the regression relationship when feasible, repeat flake-sensitive cases reasonably, then run adjacent and configured broader tests.
9. Record skips, retries, duration, environment, device/simulator, seed, and every failure. Do not discard a failure as flaky without evidence.
10. **Review gate:** invoke the technology owner for semantic confirmation and `mobile-code-reviewer` for independent review. Resolve findings and rerun affected tests.

## Errors and stop conditions

- If the correct test level requires unavailable infrastructure, report it and implement a lower-level substitute only if it proves the same contract; otherwise stop.
- Do not weaken assertions, increase timeouts arbitrarily, retry until green, share mutable state, or use live services/credentials.
- A test that cannot fail for the intended regression is not acceptance evidence.
- Do not edit production behavior under this Skill without separate explicit scope and ownership.

## Completion classification

Classify every coordinator criterion. Requirements, affected configuration, selected test levels, compilation/type/static checks for test code, fixture/dependency review, security of test data, warnings, regression evidence, and independent review are normally required. Production compilation/suites, UI/accessibility/localization/adaptive/offline/performance/recovery behavior and documentation are conditionally required according to what the tests cover; give concrete reasons.

## Outputs and evidence

Return the risk-to-test map, level decision, fixtures and nondeterminism controls, changed test files, exact commands/environments/repetitions/results, regression demonstration, skips/unavailable infrastructure, flakiness assessment, review findings, and completion-classification table.

## Acceptance criteria

- Tests prove the confirmed behavior and relevant failures without duplicating implementation logic.
- Fixtures are minimal, deterministic, isolated, and free of real sensitive data or live-service dependence.
- Tests pass consistently in the available supported environment and fail for the intended regression when that can be demonstrated safely.
- Independent review has no unresolved blocking finding.

## Human review requirements

Humans approve new test dependencies/frameworks, snapshot baseline changes, production testability changes, use of external/device infrastructure, unavailable required levels, and accepted flakiness or coverage gaps.

## Prohibited actions

Do not use real credentials/data, live production services, arbitrary sleeps, retry-until-pass logic, weakened assertions, unapproved dependencies, destructive device resets, publication/signing, or self-approval.
