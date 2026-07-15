---
name: add-mobile-tests
description: Use when adding Android, iOS, KMP, Flutter, or React Native unit, integration, UI, snapshot, component, or end-to-end tests with deterministic evidence.
---

# add-mobile-tests

- Objective: Add deterministic tests that match the repository's existing frameworks and risk profile.
- Trigger: User asks to add tests, improve coverage, cover a feature, reproduce a bug, or validate a mobile workflow.
- Inputs: Target behavior, platform, existing tests, fixtures, CI hints, desired test level, and known flakiness constraints.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: Inspect existing test frameworks and commands. Do not add new dependencies unless explicitly approved.
- Primary owner: `mobile-test-engineer`.
- Reviewers: Platform owner and `mobile-code-reviewer`.
- Steps: Choose the narrowest effective test level; add fixtures without secrets; implement deterministic tests; avoid sleeps and external services; run targeted tests; report unavailable devices/simulators/emulators; update evidence.
- Validation gates: Tests compile/run where infrastructure exists, fixtures are deterministic, failure modes are covered, and production code changes are owned by platform engineers.
- Failures: Stop on unavailable framework requiring dependency change, nondeterministic external service need, or production behavior change requirement.
- Stop conditions: Credentialed external services, paid infrastructure, destructive setup, dependency/lockfile change without approval, publishing, signing, or deployment.
- Evidence: Test files changed, commands discovered/run, results, skipped/unavailable infrastructure, and regression coverage rationale.
- Outputs: Tests, fixtures, command evidence, and residual coverage gaps.
- Acceptance criteria: Tests are deterministic, scoped to risk, integrated with existing tooling, and validated or reported unavailable.
- Human approvals: Required for new dependencies, lockfiles, external services, paid resources, credentials, device farm use, and production behavior changes.
- Prohibited actions: Fabricated tests, sleeps as synchronization without justification, weakening assertions, changing production solely for tests, publishing, signing, destructive commands, and fabricated pass results.

