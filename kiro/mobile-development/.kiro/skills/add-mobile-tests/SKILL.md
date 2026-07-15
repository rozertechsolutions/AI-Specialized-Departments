---
name: add-mobile-tests
description: Add or improve mobile tests across Android, iOS, KMP, Flutter, or React Native without changing production behavior merely to pass tests.
---

# add-mobile-tests

Objective: add focused, deterministic tests that protect the requested behavior or regression surface.

Trigger: request to add tests, improve coverage, document gaps, or validate a change.

Inputs: behavior under test, affected files, existing test framework, fixtures, expected outcomes, platform constraints.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: inspect existing test conventions and project commands; identify deterministic boundaries; do not change production behavior solely to pass tests; obtain approval for dependencies, lockfiles, test infrastructure, or device/simulator destructive operations.

Primary owner: `mobile-test-engineer`; implementation owner assists when production seams are legitimately required.

Reviewers: affected implementation owner and `mobile-code-reviewer`.

Ordered steps:

1. Trace behavior to test level and owner.
2. Classify criteria and existing coverage.
3. Inspect test framework, fixtures, naming, and commands.
4. Add or update focused tests and safe fixtures.
5. Run targeted tests and relevant broader checks.
6. Triage failures to current change vs pre-existing issue.
7. Document gaps and unavailable infrastructure.

Conditional steps: request owner support for legitimate production changes; stop before dependencies, lockfiles, destructive device actions, or external services.

Validation gates: targeted tests pass, affected compile/build when needed, lint/typecheck/analyze where configured, deterministic fixture review, final code review.

Failures: missing tooling, flaky or nondeterministic test, production behavior mismatch, unavailable infrastructure, or validation failure.

Stop conditions: weakening tests, disabling checks, dependency/lockfile change without approval, external service credentials, production writes, destructive commands.

Evidence: tests added, commands discovered/run, results, flakiness assessment, criteria classification.

Outputs: tests, fixtures, validation report, gaps, reviewer findings.

Acceptance criteria: tests cover the requested behavior or gap is justified, deterministic checks pass where available, and no legitimate validation is weakened.

Human approvals: dependencies, lockfiles, test infrastructure, device destructive operations, credentials, external systems.

Prohibited actions: changing production behavior merely for tests, fabricated fixtures outside test scope, disabled checks, publication, signing, uploading, deployment.
