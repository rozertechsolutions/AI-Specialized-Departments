---
name: add-mobile-tests
description: Add deterministic, risk-based mobile unit, integration, UI, snapshot, or end-to-end tests using the repository's existing frameworks and conventions.
when_to_use: Use to add missing coverage, a regression test, or a focused test suite for Android, iOS, KMP, Flutter, React Native, or hybrid behavior without changing the production requirement.
argument-hint: "[scope and risks]"
model: inherit
---

# Objective

Add the smallest reliable test coverage that proves the behavior and risks in `$ARGUMENTS`, and execute it with project-native tooling.

# Required input and supported scope

Require expected behavior, changed or risky scope, target technologies/platforms, known regressions, environment constraints, and acceptance criteria. Clarify whether the request includes production testability changes; do not assume authorization.

# Preconditions and inspection

Read instructions; inspect status/diff, production behavior and boundaries, existing test frameworks/layout/naming, runners and scripts, fixtures/fakes/mocks, async/UI synchronization, CI capabilities, snapshots, coverage conventions, and related tests. Discover actual commands and target/device requirements.

# Ownership

`mobile-test-engineer` is primary. Relevant technology owners explain behavior and make any separately authorized production changes. Use security, UI/accessibility, and performance reviewers for domain-specific assertions; `mobile-code-reviewer` independently reviews changed tests and any production seam.

# Procedure and gates

1. Build a risk matrix covering success, failure, boundaries, lifecycle/concurrency, cancellation, offline/network, recovery, state, and platform differences as applicable.
2. Select the lowest sufficient level: unit for isolated logic, integration for owned boundaries, UI/component for rendered interactions, snapshot only for stable visual contracts, and end-to-end only for unique cross-system risk. Gate: each test level has a distinct purpose.
3. Reuse existing helpers and create minimal deterministic fixtures/fakes. Use mocks only at explicit boundaries; avoid implementation-detail assertions and fabricated production data.
4. Control clocks, randomness, schedulers, network, storage, locale, and device state where the framework permits. Use condition-based UI synchronization, never arbitrary sleeps.
5. Add tests that fail for the missing behavior or regression before relying on their pass result. Include negative and edge cases proportional to risk.
6. If production code is untestable, propose the smallest behavior-preserving seam and obtain scope approval before assigning it to the technology owner.
7. Run the new tests repeatedly where flakiness risk exists, then adjacent suites, compilation/type checks, lint, and formatting validation discovered in the project.
8. Investigate every failure. Do not retry away flakes, skip assertions, or update snapshots without reviewing the semantic diff.

# Failure and stop handling

Stop when expected behavior is undefined, tests require credentials/production/paid services without approval, deterministic observation is impossible, a production change is unapproved, or existing unrelated failures obscure evidence. Report the blocker and a concrete safe test plan.

# Evidence and acceptance

Return risk-to-test mapping, chosen levels/rationale, fixtures/seams, changed files, exact commands/results/repetition evidence, existing unrelated failures, applicability classification, coverage gaps, and final review.

Report every considered universal and technology-specific completion criterion as `required`, `conditionally-required`, or `not-applicable`; give a concrete reason for every `not-applicable`, and label unavailable infrastructure `unavailable` rather than passed.

Accept only when tests would detect the target regression, are deterministic under available runs, follow conventions, required suites/checks pass, and no production behavior was altered outside approval. `not-applicable` and unavailable criteria require concrete reasons.

# Human review and prohibited actions

Require human approval for production-connected tests, paid device farms, destructive fixtures, broad snapshot changes, and production seams. Never weaken/delete/skip tests, hide flakes with retries/sleeps, assert implementation details without need, use real personal data, publish/sign/deploy, or claim unexecuted coverage.
