---
name: fix-mobile-bug
description: Use when diagnosing and fixing a mobile bug in Android, iOS, KMP, Flutter, or React Native with reproduction, root cause, regression tests, and evidence.
---

# fix-mobile-bug

- Objective: Reproduce, diagnose, and fix a mobile bug with minimal scoped changes and regression evidence.
- Trigger: User reports a defect, crash, flaky behavior, UI issue, build break, or platform-specific regression.
- Inputs: Bug report, reproduction steps, logs, platform, expected/actual behavior, affected versions, and recent changes.
- Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.
- Preconditions: Inspect relevant code/config, identify owner, discover reproduction and validation commands, and avoid assumptions when evidence is missing.
- Primary owner: Platform engineer matching the defect; `mobile-test-engineer` owns regression strategy.
- Reviewers: `mobile-security-reviewer` for security/privacy bugs, `mobile-performance-reviewer` for performance bugs, `mobile-ui-accessibility-reviewer` for UI/accessibility bugs, and `mobile-code-reviewer`.
- Steps: Reproduce or explain why unavailable; isolate root cause; choose minimal fix; ask approval for sensitive changes; implement; add regression test or evidence-backed reason if not possible; run targeted checks; review diff; request independent review.
- Validation gates: Reproduction evidence, root-cause explanation, regression coverage or reason, affected checks passing or unavailable, and no unrelated changes.
- Failures: Stop on non-reproducible critical ambiguity, validation failure caused by fix, missing infrastructure, or credentialed external dependency.
- Stop conditions: Fix requires publishing, signing, destructive commands, external integration activation, or unrelated refactor.
- Evidence: Reproduction details, changed files, commands run, test output, logs summarized without secrets, and unavailable infrastructure.
- Outputs: Bug fix, regression test or rationale, validation report, and residual risk.
- Acceptance criteria: Defect is addressed with minimal scope, regression risk is covered, and independent review is complete.
- Human approvals: Required for auth/privacy/security, dependencies, lockfiles, build/signing config, production endpoints, telemetry, and external writes.
- Prohibited actions: Masking errors, weakening validation, broad exception swallowing, unrelated cleanup, publishing, signing, deployment, destructive commands, and fabricated pass results.

