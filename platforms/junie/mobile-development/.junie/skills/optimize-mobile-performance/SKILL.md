---
name: "optimize-mobile-performance"
description: "Measure and improve mobile startup, rendering, memory, battery, background work, network/storage efficiency, or binary size without unmeasured improvement claims."
---
# Optimize Mobile Performance

Use this skill for performance diagnosis, optimization, regression analysis, profiling, benchmark work, memory/battery issues, startup/rendering improvements, network/storage efficiency, or binary size.

## Workflow Definition

Objective: improve or assess performance using measurements, scoped changes, and explicit evidence.

Trigger: performance complaint, optimization request, regression, profiler/benchmark output, or binary-size concern.

Inputs: performance goal, affected platform(s), baseline data if available, scenario, device/simulator constraints, changed files, and acceptance threshold.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, and React Native.

Preconditions:

- Establish baseline or state that baseline is unavailable.
- Discover available profiling/build/test tools.
- Ask approval for dependency changes, telemetry changes, external services, paid tools, or destructive commands.

Primary owner: `mobile-performance-reviewer` for diagnosis; matching platform engineer for implementation.

Reviewers: `mobile-test-engineer`, `mobile-security-reviewer` when telemetry/storage/network changes are involved, and `mobile-code-reviewer`.

## Steps

1. Define metric, scenario, device/runtime context, and acceptance threshold.
2. Collect or inspect baseline evidence when available.
3. Identify likely bottleneck with file-level evidence.
4. Implement the smallest safe optimization through the owning engineer.
5. Validate correctness and regression tests.
6. Re-measure or state why measurement is unavailable.
7. Compare before/after results only when both are valid.
8. Record performance evidence and residual risk.

## Validation Gates

- No improvement is claimed without measurement.
- Correctness tests still pass or unavailable checks are documented.
- Security/privacy behavior is not weakened.
- Battery/background/network/storage trade-offs are documented.

## Failures And Stop Conditions

Stop for missing baseline where claims require it, unavailable profiling with no alternative evidence, paid/production telemetry access, credentials, destructive commands, unapproved dependencies, or release actions.

## Evidence And Outputs

Output metric, baseline, changes, validation commands, before/after measurements when available, correctness evidence, unavailable tooling, and residual risk.

Acceptance criteria: either measured improvement/risk reduction is demonstrated or limitations are explicit; correctness and review gates are complete.

Human approvals: required for accepting unmeasured risk, telemetry, dependencies, background behavior, storage/network trade-offs, and release-impacting changes.

Prohibited actions: unmeasured improvement claims, disabling safeguards, speculative rewrites, publishing, signing, deployment, and self-review.
