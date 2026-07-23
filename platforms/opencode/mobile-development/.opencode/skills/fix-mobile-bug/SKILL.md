---
name: fix-mobile-bug
description: Diagnose and fix a mobile bug using reproduction evidence, scoped ownership, regression tests, and validation.
compatibility: opencode
metadata:
  owner: coordinator
---

# fix-mobile-bug

- Objective: reproduce, diagnose, and fix a mobile defect without changing unrelated behavior.
- Trigger: user reports a bug or failing mobile check.
- Inputs: symptoms, logs, failing tests, affected platform, reproduction steps, expected behavior.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: enough evidence exists to identify or safely reproduce the bug; affected technology is detected.
- Primary owner: route by root-cause file boundary.
- Reviewers: `mobile-test-engineer` and `mobile-code-reviewer`; specialized reviewers for sensitive surfaces.
- Steps: collect evidence; reproduce when feasible; identify root cause; make smallest fix; add regression test; run failing check first; run related checks; review.
- Conditional steps: ask for missing reproduction data if bug cannot be derived safely.
- Validation gates: original failure passes; regression test exists or test gap is justified; relevant compile/lint/test checks classified.
- Failures: stop on non-reproducible issue unless a safe static fix is evident; report pre-existing failures separately.
- Stop conditions: destructive reproduction, production data, credentials, external writes, unsupported tooling.
- Evidence: reproduction command/output, root cause, changed files, checks.
- Outputs: fix, regression coverage, validation report.
- Acceptance criteria: root cause addressed and no unrelated behavior change is introduced.
- Human approvals: sensitive config changes, dependencies, lockfiles, external services.
- Prohibited actions: speculative rewrites, weakening validation, hiding errors, signing, publishing, destructive commands.
