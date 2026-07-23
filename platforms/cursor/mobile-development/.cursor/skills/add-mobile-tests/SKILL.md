---
name: add-mobile-tests
description: Add focused mobile tests across unit, integration, UI, snapshot, or end-to-end levels.
---

# add-mobile-tests

Objective: add deterministic tests that cover requested behavior or regression risk without changing production behavior solely for tests.

Trigger: request to add tests, improve coverage, reproduce a regression, or validate a mobile change.

Inputs: target behavior, affected files, existing tests, supported test levels, fixtures, and validation commands.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: inspect existing test structure and commands; identify available SDKs/simulators/emulators; obtain approval for dependencies, external services, device-destructive actions, or credentialed tests.

Primary owner: `mobile-test-engineer`.

Reviewers: implementation owner for behavior consistency and `mobile-code-reviewer`; `mobile-security-reviewer` when fixtures touch sensitive data.

Steps:

1. Map risk to test level.
2. Classify criteria and unavailable infrastructure.
3. Add minimal deterministic tests and fixtures.
4. Avoid real secrets, production data, private endpoints, and live-user data.
5. Run targeted tests first.
6. Run broader configured tests when reasonable.
7. Report gaps and flaky risks.

Validation gates: targeted test pass, broader suite when reasonable, fixture review, secret scan, no production-only changes, and independent review.

Failures: unsupported test infrastructure, unavailable simulator/emulator, dependency needed without approval, flaky test, unrelated pre-existing failure, or production behavior change required.

Stop conditions: credentials, production services, paid services, destructive device operations, signing, publishing, dependency/lockfile changes without approval, or validation failure not caused by current work.

Evidence: test files changed, commands and results, unavailable infrastructure, fixture sources, criteria classification, and gaps.

Outputs: tests, fixtures, validation report, and residual coverage gaps.

Acceptance criteria: tests are scoped to risk, deterministic, pass where runnable, and do not weaken validation.

Human approvals: dependencies, external services, credentials, destructive device actions, lockfiles, or production behavior changes.

Prohibited actions: disabling tests, broad timeouts without reason, fabricated fixtures that misrepresent behavior, production-only changes, signing, publishing, upload, deployment, or self-approval.
