---
name: implement-mobile-feature
description: Implement a scoped mobile feature with deterministic platform ownership, tests, security review triggers, and evidence.
compatibility: opencode
metadata:
  owner: coordinator
---

# implement-mobile-feature

- Objective: implement a requested feature with one primary owner per affected runtime boundary.
- Trigger: user asks for new mobile behavior.
- Inputs: requirements, acceptance criteria, target platform(s), relevant files, API contracts, UI states, tests.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: behavior is unambiguous; project technology and commands are detected; no conflicting user changes.
- Primary owner: route by affected files and runtime boundary.
- Reviewers: `mobile-test-engineer`, `mobile-security-reviewer` when sensitive, `mobile-ui-accessibility-reviewer` for UI, `mobile-performance-reviewer` when performance-sensitive, `mobile-code-reviewer`.
- Steps: inspect current behavior; map requirements to files; choose owner; implement smallest complete change; add/update tests; run targeted checks; run broader reasonable checks; perform independent review.
- Conditional steps: stop for approval before dependencies, lockfiles, permissions, entitlements, auth, privacy, telemetry, signing, external writes, or public contract changes.
- Validation gates: compile/type check; relevant tests; lint/static analysis/format where available; UI/accessibility/security/performance criteria as applicable.
- Failures: fix failures caused by the change; report unrelated pre-existing failures.
- Stop conditions: ambiguous behavior, unavailable required tool, required credential/signing/publish step, out-of-scope architecture change.
- Evidence: diff, commands, outputs, criteria classification, reviewer findings.
- Outputs: implementation, tests, validation report, limitations.
- Acceptance criteria: requested behavior implemented within scope and required checks pass or are blocked with evidence.
- Human approvals: sensitive surfaces, dependencies, external writes, release impacts.
- Prohibited actions: fabricated behavior, hidden errors, broad suppressions, signing, publishing, destructive commands, self-final-review.
