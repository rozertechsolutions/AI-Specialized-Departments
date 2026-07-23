---
name: optimize-mobile-performance
description: Optimize mobile startup, rendering, memory, battery, background work, network/storage efficiency, or binary size with measurement evidence.
---

# optimize-mobile-performance

Objective: make performance changes only when supported by baseline and after-change evidence or explicitly document unavailable measurement.

Trigger: request to optimize, profile, reduce latency, improve startup/rendering/memory/battery/network/storage, or shrink binary size.

Inputs: performance goal, target metric, affected platform, baseline evidence, profiling tools, and acceptable trade-offs.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: inspect current code; identify measurable target; obtain approval for profiling external services, telemetry changes, dependencies, production data, background behavior, or release config changes.

Primary owner: implementation owner selected by affected runtime; `mobile-performance-reviewer` designs and reviews measurements read-only.

Reviewers: `mobile-performance-reviewer`, `mobile-test-engineer`, `mobile-security-reviewer` for telemetry/privacy, and `mobile-code-reviewer`.

Steps:

1. Establish baseline or record why it is unavailable.
2. Classify criteria including memory, battery, network, storage, and binary size.
3. Identify narrow bottleneck and owner.
4. Implement minimal change.
5. Run correctness checks.
6. Re-measure using comparable conditions when possible.
7. Report measured change or unavailable infrastructure honestly.

Validation gates: correctness tests/build, static analysis, baseline/after measurement when available, performance reviewer evidence, security/privacy review for telemetry, and independent code review.

Failures: no measurable target, profiling requires production credentials/data, unapproved telemetry/dependency change, validation failure, or claimed improvement without measurement.

Stop conditions: production profiling, external upload, credentials, dependency/lockfile change, destructive device action, signing, publishing, deployment, or privacy/security change without approval.

Evidence: baseline, changed files, commands/tools, after measurement, limitations, reviewer findings, and criteria classification.

Outputs: optimized code, measurement report, correctness validation, and residual risks.

Acceptance criteria: correctness remains intact and any performance claim is backed by measurement or clearly marked unmeasured.

Human approvals: telemetry, production data, dependencies, background behavior, privacy/security trade-offs, release/signing changes, or external services.

Prohibited actions: fabricating metrics, sacrificing correctness silently, broad suppressions, production uploads, signing, publishing, deployment, or final self-review.
