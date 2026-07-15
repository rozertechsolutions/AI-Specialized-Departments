---
name: optimize-mobile-performance
description: Measure and optimize mobile startup, rendering, memory, battery, network, storage, or binary size with evidence.
---

# Optimize Mobile Performance

## Objective

Improve a defined mobile performance target only with baseline and after-change evidence.

## Trigger

Use when the user asks to optimize startup, rendering, memory, leaks, battery, background work, network/storage efficiency, or binary size.

## Inputs

Performance concern, affected platform, target metric, reproduction path, acceptable trade-offs, and available profiling tools.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native.

## Preconditions

Inspect existing code, performance tooling, build variants, profiling configuration, and measurement feasibility. Establish a baseline before editing.

## Primary Owner

`mobile-performance-reviewer` owns measurement design. The relevant platform engineer owns implementation after measurement scope is defined.

## Reviewers

`mobile-code-reviewer`, `mobile-test-engineer`, and security/UI reviewers when the change affects their surfaces.

## Steps

1. Define the metric and scenario.
2. Collect baseline measurement or report why measurement is unavailable.
3. Identify likely bottleneck from evidence.
4. Implement the smallest scoped optimization.
5. Re-run the same measurement and relevant correctness checks.
6. Report trade-offs, confidence, and residual risks.

## Conditional Steps

- If baseline measurement is unavailable, stop implementation unless the user approves a code-inspection-only change.
- If optimization affects UI, networking, storage, background work, or battery, run the matching conditional checks.
- If architecture or dependency changes appear necessary, stop for approval.
- If measurements are noisy, report confidence limits and avoid claiming definitive improvement.

## Validation Gates

Required: baseline or exact blocker, post-change measurement or exact blocker, correctness tests, compile/build where relevant, static analysis/lint when configured, and code review. Conditional: memory leak, battery, startup, rendering, network, storage, and binary-size checks.

## Failures and Stop Conditions

Stop if measurement would require production traffic, paid services, credentials, destructive device actions, unavailable tools, or changing architecture/dependencies without approval.

## Evidence

Record device/simulator context when used, build variant, commands/tools, baseline, after measurement, files changed, and confidence limits.

## Outputs

Optimization, measurement evidence, correctness validation, and remaining performance risks.

## Acceptance Criteria

The target metric improves or the blocker is explicit, correctness is preserved, and no improvement is claimed without evidence.

## Human Approvals

Required for dependency changes, architecture changes, background behavior, telemetry, production profiling, external writes, or paid tooling.

## Prohibited Actions

Do not claim improvement without measurements, remove features silently, weaken tests, hide errors, sign, publish, upload, deploy, or use production data.
