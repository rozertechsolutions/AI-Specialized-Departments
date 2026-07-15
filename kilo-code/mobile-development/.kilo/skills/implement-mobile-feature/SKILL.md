---
name: implement-mobile-feature
description: Use when implementing a scoped feature in an existing Android, iOS, KMP, Flutter, or React Native project with owner selection, validation, and independent review.
---

# implement-mobile-feature

- Objective: Implement a requested mobile feature while preserving existing architecture, platform ownership, and validation evidence.
- Trigger: User asks to add or change product behavior in a mobile app.
- Inputs: Feature requirements, target platform(s), UI/API/data expectations, acceptance criteria, existing conventions, and test expectations.
- Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.
- Preconditions: Inspect relevant files, identify actual technology and owners, discover build/test commands, and clarify ambiguous behavior before editing.
- Primary owner: The platform engineer matching the affected technology; `mobile-architect` owns cross-module or boundary decisions.
- Reviewers: `mobile-test-engineer`, relevant risk reviewers, and `mobile-code-reviewer`.
- Steps: Trace requirements; choose owner; inspect conventions; design minimal change; ask approval for sensitive files/dependencies; edit scoped files; add or update tests; run targeted checks; broaden validation when reasonable; request independent review; fix own regressions.
- Validation gates: Requirements traceability, compile/analyze/lint/typecheck as applicable, targeted tests, UI states, error paths, and independent final review.
- Failures: Stop and report conflicting requirements, unsupported platform capability, validation failures, or need for credentials/external services.
- Stop conditions: Feature requires publishing, signing, destructive commands, external integration activation, or out-of-scope architecture changes.
- Evidence: Changed files, commands discovered and run, test results, warnings, unavailable infrastructure, reviewer findings, and corrections.
- Outputs: Implemented feature, tests, validation report, and residual risks.
- Acceptance criteria: Feature meets stated behavior, ownership is unique, tests are appropriate, and no final review is self-authored.
- Human approvals: Required for security/privacy/auth, dependencies, lockfiles, build/signing config, analytics, telemetry, WebViews, deep links, and external writes.
- Prohibited actions: Broad refactors, unsupported simulations, fabricated data, publishing, signing, deployment, destructive commands, and fabricated validation.

