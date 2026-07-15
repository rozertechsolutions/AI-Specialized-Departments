---
name: optimize-mobile-performance
description: Use when investigating or improving mobile startup, rendering, memory, battery, background work, network/storage efficiency, binary size, or profiling evidence.
---

# optimize-mobile-performance

- Objective: Investigate and improve mobile performance only with scoped changes and measurement-backed claims.
- Trigger: User asks to optimize startup, rendering, memory, leaks, battery, background work, network/storage, binary size, or performance regressions.
- Inputs: Performance symptom, target platform, baseline measurements if available, affected flows, constraints, and acceptable tradeoffs.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: Identify actual technology, available profiling tools, baseline evidence, and affected code before editing.
- Primary owner: `mobile-performance-reviewer` for analysis; platform engineer for implementation.
- Reviewers: `mobile-test-engineer`, `mobile-code-reviewer`, and `mobile-security-reviewer` when data/network/privacy is affected.
- Steps: Establish baseline or report unavailable; identify likely causes; choose smallest measurable change; implement via owning platform engineer; run measurements/checks; compare against baseline; record residual risk.
- Validation gates: Measurement method documented, improvement claims backed by measurements, compile/test checks run or unavailable, and no UX/security regression.
- Failures: Stop when measurements are unavailable for an improvement claim, profiling requires paid/external infrastructure, or validation fails.
- Stop conditions: Unapproved dependency/build changes, destructive commands, publishing, signing, deployment, or privacy/security changes without approval.
- Evidence: Baseline, post-change results, commands/tools, changed files, measurement limitations, and unavailable infrastructure.
- Outputs: Analysis, scoped optimization, measurement comparison, validation report, and residual tradeoffs.
- Acceptance criteria: Claims are measured, changes are scoped, and reviewers confirm no unacceptable regression.
- Human approvals: Required for UX tradeoffs, dependencies, lockfiles, build configuration, privacy/security changes, paid infrastructure, and external writes.
- Prohibited actions: Unmeasured improvement claims, broad rewrites, hidden behavior changes, publishing, signing, deployment, destructive commands, and fabricated metrics.

