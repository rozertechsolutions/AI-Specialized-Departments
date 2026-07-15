---
name: fix-mobile-bug
description: Diagnose and fix a mobile bug in Android, iOS, KMP, Flutter, or React Native with regression evidence.
---

# fix-mobile-bug

Objective: reproduce, isolate, and fix the reported bug with the smallest safe change.

Trigger: bug report, failing test, crash, regression, incorrect behavior, or platform-specific defect.

Inputs: observed behavior, expected behavior, reproduction steps, logs, affected platform, crash data when safe, current files, and validation expectations.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: inspect relevant files and user changes; detect technology; reproduce or explain why reproduction is unavailable; identify owner; protect secrets and production data in logs.

Primary owner: selected by deterministic routing in `AGENTS.md`; `mobile-test-engineer` owns regression tests.

Reviewers: `mobile-test-engineer`, affected security/UI/performance reviewer when relevant, and `mobile-code-reviewer`.

Ordered steps:

1. Preserve the failure evidence and expected behavior.
2. Classify completion criteria.
3. Reproduce locally when safe and possible.
4. Identify root cause and affected ownership boundary.
5. Implement the narrow fix.
6. Add or update a regression test where practical.
7. Run targeted validation and broader checks when reasonable.
8. Record remaining gaps and independent review.

Conditional steps: scrub sensitive logs; ask before using production credentials or external systems; stop if the fix needs dependencies, public contract changes, or release/signing changes.

Validation gates: reproduction evidence or explicit unavailable reason, regression test, compile/build, affected tests, lint/typecheck/analyze/format where configured, security review for sensitive paths, and final code review.

Failures: cannot reproduce and no safe inference, ambiguous expected behavior, missing tooling, validation failure, out-of-scope change, or user change conflict.

Stop conditions: credentials, production data, destructive commands, dependency/lockfile change without approval, signing/publishing/upload/deployment, or security/privacy change needing review.

Evidence: reproduction command/output, root cause, files changed, regression checks, validation results, unavailable infrastructure, criteria classification.

Outputs: bug fix, regression coverage or test-gap explanation, validation report, reviewer findings.

Acceptance criteria: reported behavior is corrected or blocker is documented, regression evidence exists where possible, and no required check fails.

Human approvals: dependencies, lockfiles, permissions, entitlements, privacy, auth, telemetry, production data, external writes, destructive operations.

Prohibited actions: masking failures, broad suppressions, unrelated refactors, fabricated reproduction, publication, signing, uploading, deployment, self-review as final review.
