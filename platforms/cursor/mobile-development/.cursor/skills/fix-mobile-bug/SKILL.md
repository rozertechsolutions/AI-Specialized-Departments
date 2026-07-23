---
name: fix-mobile-bug
description: Diagnose and fix a mobile bug in Android, iOS, KMP, Flutter, or React Native code.
---

# fix-mobile-bug

Objective: reproduce or reason from evidence, fix root cause narrowly, and prevent regression.

Trigger: user reports a bug, failing test, crash, incorrect behavior, or regression.

Inputs: bug report, reproduction steps, expected/actual behavior, logs, stack traces, affected platforms, and existing validation output.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: inspect current changes and relevant files; detect platform; identify owner; determine whether bug is reproducible locally without credentials, production data, destructive device operations, or external writes.

Primary owner: selected by affected runtime boundary.

Reviewers: `mobile-test-engineer` for regression coverage, `mobile-security-reviewer` if security/privacy involved, `mobile-ui-accessibility-reviewer` for UI bugs, `mobile-performance-reviewer` for performance bugs, and `mobile-code-reviewer`.

Steps:

1. Capture reproduction evidence or exact reason reproduction is unavailable.
2. Locate root cause within ownership boundary.
3. Classify completion criteria.
4. Make the smallest safe fix.
5. Add or update regression coverage where feasible.
6. Run targeted failing checks first, then broader relevant checks when reasonable.
7. Correct failures caused by the fix.
8. Hand off independent review.

Validation gates: reproduction or evidence-based diagnosis, regression test when feasible, platform build/checks, static analysis/lint/typecheck, secret/security scan when touched, and independent review.

Failures: cannot reproduce and evidence is insufficient, missing tooling, pre-existing unrelated failure, approval-required change, or validation failure.

Stop conditions: production credentials/data, destructive device/simulator operation, signing, publishing, dependency change without approval, or out-of-scope architecture change.

Evidence: reproduction details, root cause, changed files, commands and results, regression coverage, unavailable infrastructure, and criteria classification.

Outputs: bug fix, test update or gap explanation, validation report, and residual risks.

Acceptance criteria: root cause is addressed, regression risk is covered or documented, and required checks pass or blockers are reported.

Human approvals: dependencies, lockfiles, security/privacy behavior, external systems, destructive reproduction, signing/release, or public contract changes.

Prohibited actions: masking failures, disabling tests, broad catches, arbitrary defaults, unrelated cleanup, signing, publishing, uploading, deployment, or final self-review.
