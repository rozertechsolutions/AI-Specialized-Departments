---
name: add-mobile-tests
description: Add or plan deterministic mobile tests across supported platforms without weakening production behavior.
---

# Add Mobile Tests

## Inputs

- Behavior under test, changed files, target platform, existing test framework, fixtures, and acceptance criteria.

## Preconditions

- Identify existing test style and commands from supplied files.
- Do not change production behavior merely to make tests pass.
- ChatGPT cannot run repository builds, tests, devices, simulators, signing, or release actions unless a separately enabled native tool supplies verifiable evidence.

## Owner And Reviewers

- Owner: `mobile-test-engineer` for test-only work; platform engineer owns inseparable production changes.
- Reviewers: relevant platform owner and `mobile-code-reviewer`.

## Steps

1. Choose the smallest test level that proves the behavior.
2. Use deterministic local fixtures and avoid external services.
3. Cover success, error, edge, cancellation, offline, localization, accessibility, or performance cases as applicable.
4. Identify exact commands for manual execution.
5. Require independent review of test adequacy.

## Validation Gates

- Evidence: test files, covered behavior, known gaps, fixture safety, and pending manual commands.
- Completion: tests are meaningful, deterministic, and traceable to requirements.

## Prohibited Actions

- Do not use real secrets or production data, add flaky timing, weaken assertions, run unapproved external tests, or claim unrun tests passed.
