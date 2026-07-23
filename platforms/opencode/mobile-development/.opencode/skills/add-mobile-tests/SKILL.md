---
name: add-mobile-tests
description: Add focused mobile tests with deterministic fixtures, platform-appropriate levels, evidence, and no production behavior changes solely for tests.
compatibility: opencode
metadata:
  owner: mobile-test-engineer
---

# add-mobile-tests

- Objective: add or improve tests for existing mobile behavior.
- Trigger: user asks for tests or validation coverage.
- Inputs: behavior under test, existing test structure, platform, known gaps, acceptance criteria.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: behavior is known; test infrastructure is detected or limitations are documented.
- Primary owner: `mobile-test-engineer`.
- Reviewers: implementation owner and `mobile-code-reviewer`; specialized reviewers for security/UI/performance test surfaces.
- Steps: inspect existing test patterns; choose test level; create deterministic fixtures; add tests; run targeted tests; run related broader checks when reasonable.
- Conditional steps: request approval before adding dependencies, lockfile changes, real services, device-destructive operations.
- Validation gates: new tests fail before fix when feasible or directly assert known behavior; pass after implementation; no weakened checks.
- Failures: report unavailable runners, flaky infrastructure, pre-existing failures.
- Stop conditions: production data, credentials, real external writes, unavailable required tool.
- Evidence: test files, commands, output, coverage rationale.
- Outputs: tests, fixtures, validation report, remaining gaps.
- Acceptance criteria: tests cover requested behavior and are deterministic within available infrastructure.
- Human approvals: dependencies, live services, destructive device/simulator operations.
- Prohibited actions: changing production behavior merely to pass tests, broad suppressions, fabricated success.
