---
name: optimize-mobile-performance
description: Optimize mobile startup, rendering, memory, battery, background work, network/storage efficiency, or binary size with measurements.
---

# optimize-mobile-performance

Objective: improve or assess mobile performance using measured evidence and scoped changes.

Trigger: request to optimize, profile, reduce startup time, improve rendering, lower memory/battery/network/storage cost, or reduce binary size.

Inputs: performance goal, affected platforms, baseline evidence, devices/simulators, profiling tools, current files, acceptance thresholds.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: inspect performance-sensitive paths; identify measurement method; obtain baseline where possible; require approval for dependencies, build config, telemetry, background behavior, or external services.

Primary owner: implementation owner for code changes; `mobile-performance-reviewer` owns measurement and read-only review.

Reviewers: `mobile-performance-reviewer`, `mobile-test-engineer`, `mobile-security-reviewer` for telemetry/background/network, and `mobile-code-reviewer`.

Ordered steps:

1. Define metric, baseline, and measurement environment.
2. Classify criteria and unavailable infrastructure.
3. Inspect hot paths and existing performance conventions.
4. Implement the smallest optimization only after baseline or clear correctness issue.
5. Re-measure or report why measurement is unavailable.
6. Run regression checks.
7. Record performance review and residual risk.

Conditional steps: if no baseline is possible, do not claim improvement; if optimization changes architecture or dependencies, request approval.

Validation gates: before/after measurement where possible, compile/build, relevant tests, static analysis, performance reviewer evidence, battery/background/network review when relevant, final code review.

Failures: missing baseline for improvement claim, measurement unavailable, validation failure, regression, or out-of-scope architecture/dependency change.

Stop conditions: production telemetry, external services, dependency/lockfile change without approval, destructive profiling action, signing/publishing/upload/deployment.

Evidence: metric, tool, environment, baseline, after result, files changed, commands run, criteria classification.

Outputs: optimization or measurement report, validation evidence, residual risks.

Acceptance criteria: no performance claim lacks measurement, correctness is preserved, and required checks pass.

Human approvals: dependencies, lockfiles, telemetry, background behavior, release configuration, external services, destructive device actions.

Prohibited actions: unmeasured improvement claims, broad rewrites, disabled validation, publication, signing, uploading, deployment.
