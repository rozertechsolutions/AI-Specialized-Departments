---
name: "add-mobile-tests"
description: "Add mobile unit, integration, UI, snapshot, or end-to-end tests with deterministic fixtures, project command discovery, and validation evidence."
---
# Add Mobile Tests

Use this skill when adding, improving, or reviewing tests for mobile behavior.

## Workflow Definition

Objective: add reliable tests that cover meaningful behavior without changing production solely to pass tests.

Trigger: request for tests, coverage, regression coverage, flakiness investigation, or validation evidence.

Inputs: behavior under test, affected files, existing test conventions, platform(s), commands, fixtures, device/simulator/emulator availability, and acceptance criteria.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, and React Native.

Preconditions:

- Inspect existing test layout and command scripts.
- Choose the lowest reliable test level first.
- Ask approval before deleting/weakening tests, changing dependencies/lockfiles, installing tools, or using external services.

Primary owner: `mobile-test-engineer`.

Reviewers: matching platform engineer for production behavior, `mobile-security-reviewer` for security tests, `mobile-ui-accessibility-reviewer` for UI/accessibility tests, and `mobile-code-reviewer`.

## Steps

1. Classify applicable test levels as required, conditionally-required, or not-applicable with reasons.
2. Discover project commands and tool availability.
3. Add deterministic fixtures, mocks, fakes, or test data without real secrets or production service calls.
4. Add tests following existing naming, structure, and assertions.
5. Stabilize synchronization for UI/e2e tests without arbitrary sleeps when better primitives exist.
6. Run targeted tests first, then broader relevant checks when reasonable.
7. Report flaky, unavailable, or pre-existing failures separately.

## Validation Gates

- Tests assert behavior, not implementation details unless justified.
- No production behavior is changed merely to pass tests.
- No real credentials or production services are used.
- Relevant commands pass or failures are clearly attributed.

## Failures And Stop Conditions

Stop for missing behavior definition, no safe way to run required tests, external service dependence, credentials, unapproved dependency/tool installs, destructive commands, or requests to weaken validation.

## Evidence And Outputs

Output test files, test level classification, commands discovered and run, results, unavailable infrastructure, flaky/pre-existing failures, and residual risk.

Acceptance criteria: meaningful tests exist or not-applicable reasons are concrete, validations are evidenced, and independent review is complete.

Human approvals: required for deleting tests, weakening assertions, new dependencies, lockfiles, external services, tool installation, or production changes for testability.

Prohibited actions: fabricated coverage, arbitrary waits without justification, production service calls, disabling tests, weakening validation, release actions, and self-review.
