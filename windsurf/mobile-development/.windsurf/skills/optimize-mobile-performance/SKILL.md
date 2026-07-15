---
name: optimize-mobile-performance
description: Investigate and optimize mobile performance with baseline measurement, scoped changes, and post-change evidence.
---

# optimize-mobile-performance

## Objective

Improve or diagnose performance only with measurable evidence and minimal scoped changes.

## Inputs

Performance symptom, target metric, affected platform(s), device/emulator context, traces/logs if available, and approved scope.

## Supported Technologies

Android, iOS, KMP, Flutter, React Native, and mixed mobile repositories.

## Preconditions

- Inspect startup, rendering, memory, leaks, battery, background work, network/storage efficiency, binary size, and existing profiling tools.
- Establish baseline measurement or clearly report why measurement is unavailable.
- Get approval before dependency, build, analytics, telemetry, or external tooling changes.

## Primary Owner

`mobile-performance-reviewer` for diagnosis; relevant technology owner for implementation after evidence identifies a scoped fix.

## Reviewers

`mobile-test-engineer` and `mobile-code-reviewer`; add security reviewer when network/storage/privacy is affected.

## Steps

1. Define metric and baseline.
2. Inspect code paths and collect available profiling evidence.
3. Identify bottleneck and propose smallest valid change.
4. Implement only approved scoped changes through the technology owner.
5. Re-measure with the same method where possible.
6. Run regression checks and independent final review.

## Validation Gates

Baseline evidence, post-change measurement, build/test/lint/type checks as applicable, regression review, memory/leak/battery/network/storage review where relevant, and binary-size review when packaging changes.

## Failures And Stop Conditions

Stop on missing measurable target, unavailable profiler with no alternative evidence, unapproved dependency/tooling change, validation failure, or requested claim without measurement.

## Evidence And Outputs

Baseline, hypothesis, changed files, post-change measurements, command results, unavailable checks, and residual risks.

## Acceptance Criteria

Performance findings and improvements are evidenced, reproducible enough for local context, and do not regress correctness.

## Prohibited Actions

No performance claims without measurement, no unrelated rewrites, no telemetry changes without approval, and no fabricated benchmark data.
