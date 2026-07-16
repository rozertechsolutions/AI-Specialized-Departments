---
name: optimize-mobile-performance
description: Workflow for measured mobile performance optimization across startup, rendering, memory, battery, background work, network/storage, and binary size.
---

# Optimize Mobile Performance

## Objective

Improve mobile performance only with scoped hypotheses, measurements, and validation.

## Trigger

Use when the user asks to optimize, profile, reduce size, speed up startup/rendering, reduce memory/battery use, or fix performance regressions.

## Inputs

Performance concern, target platform/device, baseline data, affected code, profiling tools, and acceptance criteria.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native.

## Preconditions

Establish available metrics and baseline. If baseline cannot be collected, state that limitation before changing code.

## Primary Owner

`mobile-performance-reviewer` for analysis, then affected implementation engineer for changes.

## Reviewers

`mobile-test-engineer`, `mobile-security-reviewer` for telemetry/network changes, platform owner, and `mobile-code-reviewer`.

## Steps

1. Define metric and target.
2. Capture baseline or document why unavailable.
3. Identify likely bottleneck from evidence.
4. Implement the smallest optimization.
5. Re-measure with the same method when available.
6. Run regression tests and build checks.
7. Report results and residual risk.

## Conditional Steps

- Startup/rendering: inspect main-thread work, layout, rendering, and initialization.
- Memory/leaks: inspect lifecycles, subscriptions, references, caches, and native bridges.
- Battery/background: inspect scheduling, wakeups, network, and storage.
- Binary size: inspect assets, dependencies, and build config.

## Validation Gates

Baseline and after metrics are present or explicitly unavailable; no unmeasured improvement claim is made; regressions are checked.

## Failures

Stop on unavailable metrics for claimed improvement, unrelated failures, missing approval, or unacceptable trade-off.

## Stop Conditions

Do not make speculative broad rewrites without measurement or explicit approval.

## Evidence

Metrics, commands, profiler summaries, changed files, tests, and unavailable infrastructure.

## Outputs

Optimization, measurement report, and residual risk.

## Acceptance Criteria

Performance objective is met with evidence or limitations are explicitly reported.

## Human Approvals

Required for dependencies, build config, telemetry, long profiling runs, or broad architecture changes.

## Prohibited Actions

No unmeasured claims, publishing, signing, uploading, deployment, or validation bypass.
