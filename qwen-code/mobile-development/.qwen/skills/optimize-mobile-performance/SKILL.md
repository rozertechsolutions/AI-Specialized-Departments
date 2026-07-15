---
name: optimize-mobile-performance
description: Establish a reproducible mobile performance baseline, profile a measured bottleneck, apply one targeted correction, compare before and after, and validate correctness regressions.
user-invocable: true
---

# Optimize Mobile Performance

## Objective

Improve a defined user-relevant performance metric by addressing a measured bottleneck while preserving correctness, accessibility, security, battery, memory, and data freshness.

## Trigger

Use for an explicit optimization request with a measurable concern such as startup, rendering, memory, battery, background work, network/storage efficiency, or application size. Do not use for speculative cleanup.

## Inputs

- User-visible scenario, metric, target, affected platforms/devices, and known regressions.
- Allowed build modes, datasets, profiling tools, repetitions, and resource budgets.
- Behavior and quality constraints that cannot regress.

## Preconditions

- Read instructions, status/diff, relevant code/tests/configuration, existing metrics/profiles, and current changes.
- Define a reproducible scenario, comparable environment, metric, and baseline method before editing.
- Confirm profiling is local, non-production, non-sensitive, safe, and available.

## Ownership

- Primary implementation owner: the technology engineer owning the measured bottleneck.
- `mobile-performance-reviewer` independently owns measurement-plan and evidence review.
- `mobile-test-engineer` supports regression strategy; security/accessibility review is conditional; `mobile-code-reviewer` reviews last.

## Tool and permission boundary

Use read/search and approved local profiler/project commands. Edit only the measured bottleneck's assigned paths. Do not install profilers/dependencies, access production, collect personal data, upload profiles, use MCP, sign, publish, or deploy.

## Sequence and gates

1. **Metric gate:** Define scenario, metric/unit, target, device/hardware, OS, build mode, data state, cold/warm conditions, sampling/repetitions, variance handling, and correctness constraints.
2. **Baseline gate:** Measure before changes with the defined method. Store only non-sensitive evidence in approved temporary/local locations. Stop if the baseline is not reproducible or comparable.
3. **Profile gate:** Use the existing platform-appropriate profiler/instrumentation to locate the dominant cost. Correlate the profile with exact code paths; reject code-shape guesses.
4. **Hypothesis gate:** State the bottleneck mechanism, expected metric effect, risks/trade-offs, and single targeted change. Obtain approval for contract, dependency, caching, data-freshness, or architecture changes.
5. **Implementation gate:** Apply the smallest change that tests the hypothesis. Preserve behavior, cancellation/lifecycle, accessibility, security, offline correctness, memory ownership, and battery/network constraints.
6. **Correctness gate:** Run affected tests, compilation/non-publishing build, analysis, and relevant manual behavior checks before accepting measurements.
7. **Comparison gate:** Repeat the same baseline method and environment. Report raw summary, sample count, variance, absolute/relative difference, and limitations. Do not cherry-pick runs.
8. **Regression gate:** Measure or reason explicitly about adjacent memory, battery, startup/rendering, network/storage, bundle size, and data-freshness costs as applicable; run regression tests.
9. **Independent review gate:** `mobile-performance-reviewer` evaluates comparability and claim support; then final code review runs. Any correction invalidates the measurements and requires a new full baseline/comparison.
10. **Completion gate:** Classify every `QWEN.md` criterion and state whether the claim is supported, unsupported, or inconclusive.

## Errors and stop conditions

Stop when no stable baseline exists, the profiler/environment is unavailable, data is sensitive, the suspected cost is not measured, a change requires unapproved architecture/dependency/behavior, correctness validation fails, comparison is not equivalent, improvement is within noise, or another quality regresses.

## Outputs and evidence

- Metric/scenario/environment contract and raw baseline summary.
- Profile evidence tied to exact paths and bottleneck hypothesis.
- Exact changed paths and trade-offs.
- Before/after results with samples/variance and exact commands/tools.
- Correctness/regression evidence, completion ledger, independent decision, and limitations.

## Acceptance criteria

- Baseline and comparison are reproducible and equivalent enough for the stated claim.
- The change addresses the measured bottleneck and meets the agreed threshold beyond noise.
- Required correctness/build/analysis/tests pass and no material adjacent quality regresses.
- Independent performance and code reviews support the evidence with no unresolved blocker.

## Human review requirements

Humans approve metric/target, profiling of sensitive scenarios, cache/freshness or architecture trade-offs, dependencies/tools, device labs, and acceptance of inconclusive or adjacent-regression risk.

## Prohibited actions

Do not claim improvement without measurements, compare different environments/build modes, cherry-pick samples, benchmark debug versus release, alter behavior silently, trade accessibility/security/correctness for speed, upload profiles/project data, install tools, or self-approve.
