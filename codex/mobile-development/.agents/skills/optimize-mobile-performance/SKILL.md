---
name: optimize-mobile-performance
description: Measure and improve a reproducible mobile startup, rendering, responsiveness, memory, battery, network, storage, or size problem with before/after evidence. Do not use for speculative micro-optimization.
---

# Optimize Mobile Performance

## Objective

Improve one measured mobile performance problem while preserving behavior, correctness, accessibility, security, maintainability, and resource trade-offs.

## Required inputs

- Reproducible scenario and affected metric.
- Target platform, OS, device/simulator, build type, dataset, and environmental controls.
- Existing performance budget or user-visible acceptance threshold.
- Baseline evidence or authorization to collect safe local evidence.
- Functional behavior and constraints that must not change.

Do not invent a target. If no formal budget exists, agree on a measurable success criterion before editing.

## Preconditions

1. Read instructions and inspect status/diff, relevant code, existing benchmarks/profiling conventions, and available local tooling.
2. Confirm measurement does not require signing, production data, credentials, uploaded traces, a paid service, destructive device resets, or unapproved tool installation.
3. Keep device/build/data conditions comparable and record known confounders.
4. Define functional, test, security, accessibility, memory/battery, and compatibility guardrails.
5. Classify every completion criterion as required, conditionally required, or not applicable with a documented reason.

## Agent ownership

`mobile-performance-reviewer` owns baseline methodology and bottleneck evidence. The coordinator assigns the resulting implementation to exactly one platform owner: `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer`. `mobile-test-engineer` owns regression benchmarks/tests. Use security and UI/accessibility reviewers when the optimization can affect their domains, and `mobile-code-reviewer` for the final diff.

The performance reviewer remains read-only and must not optimize its own finding.

## Execution

1. **Measurement contract.** Specify metric, scenario, environment, warm/cold state, data size, run count, aggregation, variance, and success threshold.
2. **Baseline.** `mobile-performance-reviewer` collects or validates reproducible local measurements. Use multiple comparable runs when practical; report median/spread rather than a single best run.
3. **Gate: evidence.** Continue only when evidence identifies a plausible bottleneck and measurements are comparable. Otherwise return a measurement plan, not a code change.
4. **Root-cause analysis.** Trace work, allocations, I/O, network, rendering, lifecycle, caching, and concurrency. Separate primary bottlenecks from correlated symptoms.
5. **Optimization plan.** The platform owner proposes the smallest change, expected mechanism, functional risks, resource trade-offs, and rollback.
6. **Implement one variable at a time.** Preserve semantics and public/persistent contracts. Avoid caches without invalidation/lifetime limits, background work without lifecycle ownership, or concurrency that introduces races.
7. **Functional gate.** Run targeted correctness/static/tests before evaluating performance. A faster incorrect result fails.
8. **Post-measurement.** Re-run the same scenario/environment and compare against baseline. Record regressions in other material metrics such as memory, battery, network, size, or UI responsiveness.
9. **Tests.** `mobile-test-engineer` adds stable regression/benchmark coverage only where the project supports meaningful thresholds; avoid noisy timing assertions in ordinary unit tests.
10. **Conditional reviews.** Run security for caching/data changes and UI/accessibility for rendering/animation changes.
11. **Code review and final gate.** `mobile-code-reviewer` checks correctness and complexity. Keep the change only if the agreed metric improves with acceptable variance and all required functional gates pass.

## Error handling and stop conditions

Stop when there is no reproducible baseline, environment/builds differ, measurements require signing or production access, simulator results cannot support a device claim, tooling is unavailable, thermal/background noise invalidates comparison, or the proposed optimization changes behavior/contracts outside scope. Report uncertainty honestly.

## Outputs

- Scenario, environment, metric, run method, and threshold.
- Before/after measurements with variance and trade-offs.
- Root cause and files changed.
- Functional, benchmark, specialist, and code-review results.
- Completion matrix with required/conditional/not-applicable status, reasons, and exact results.
- Limitations, especially simulator versus physical-device evidence.

## Acceptance criteria

- The agreed metric improves reproducibly under comparable conditions.
- Required behavior, compile/static/tests, security, accessibility, and compatibility checks pass.
- No unacceptable regression in memory, battery, network, size, responsiveness, or maintainability is introduced.
- Claims match measured evidence; unmeasured device/production behavior is not asserted.

## Prohibited actions

Do not optimize without a baseline, cherry-pick runs, use production data, upload traces, install tools without approval, sign/release builds, publish or deploy, erase devices, weaken behavior/tests/accessibility/security, add unbounded caches, or keep complexity without demonstrated benefit.
