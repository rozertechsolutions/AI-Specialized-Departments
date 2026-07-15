---
name: optimize-mobile-performance
description: Measures and improves a mobile performance bottleneck with reproducible evidence. Use for Android, iOS, KMP, Flutter, or React Native optimization.
---

# Optimize Mobile Performance

## Objective

Improve one defined mobile performance metric by addressing an evidence-backed bottleneck and proving the result under a reproducible, comparable workload without sacrificing correctness, accessibility, privacy, battery, or maintainability.

## Trigger

Use when the user requests optimization and supplies a symptom or objective that can be measured. Do not use for speculative cleanup or an unmeasured claim.

## Inputs

- user-impact statement, metric, target, and acceptable trade-offs;
- reproducible scenario, device or simulator, OS, build mode, data set, network condition, and sample policy;
- baseline traces or authorization to collect them;
- relevant source and recent changes;
- constraints for startup, rendering, memory, leaks, battery, background work, network, storage, and binary size.

## Supported technologies

Android, iOS, KMP, Flutter, and React Native with their project-configured profilers and performance tests.

## Preconditions

- Metric, scenario, environment, threshold, and success criterion are explicit.
- A safe profiler or measurement method is available.
- Baseline and candidate can run under comparable conditions.
- No production data, live-user traffic, real credential, or destructive device action is required.
- Resource-intensive, paid, networked, or device runs have human approval.

## Primary owner and reviewers

mobile-performance-reviewer is the primary workflow owner for measurement design, diagnosis, and result assessment and remains read-only. After a bottleneck and change are approved, the coordinator assigns the production slice to exactly one technology owner. mobile-test-engineer reviews functional and performance-test reliability. mobile-security-reviewer reviews data, background, network, and storage trade-offs. mobile-ui-accessibility-reviewer reviews perceived behavior and reduced-motion or interaction impacts. mobile-code-reviewer is final.

## Ordered workflow

1. Define user impact, metric, threshold, scenario, environment, sample count, variance handling, and non-goals.
2. Inspect repository status, relevant source, existing benchmarks, profilers, build modes, feature flags, telemetry, and prior measurements.
3. Collect or validate a baseline without changing production behavior. Record raw measurements, warm-up, samples, aggregation, and confounders.
4. Use traces or profiles to localize the bottleneck. Separate hypotheses from measured evidence.
5. Rank candidate changes by expected impact, correctness risk, complexity, battery, memory, network, storage, binary size, accessibility, and maintenance.
6. Select the smallest evidence-backed candidate and obtain approval for any dependency, architecture, cache, background, data, or behavior trade-off.
7. Have the selected technology owner implement only the approved production slice and its functional regression tests.
8. Run targeted functional checks before measuring performance.
9. Measure the candidate with the same environment, build mode, workload, sample policy, and tool as the baseline.
10. Compare distributions or aggregates, account for noise, verify the target, and inspect regressions in related resource metrics.
11. Revert the recommendation, not user files, if evidence is inconclusive; do not claim improvement.
12. Obtain specialist and final reviews, correct through the technology owner, and repeat baseline-comparable measurement.
13. Complete criterion ledger, triple review, and final verification.

## Conditional steps

- Startup: separate cold, warm, and hot starts; control process and cache state without destructive device resets.
- Rendering: inspect frame timing, recomposition or layout, main-thread work, images, lists, animations, and dropped frames.
- Memory or leaks: define lifecycle, retention window, heap evidence, and repeated navigation or workload.
- Battery or background: use approved duration and tooling; account for radios, sensors, wakeups, scheduling, and OS policy.
- Network or storage: measure request count, bytes, latency, cache hit rate, serialization, database or file work, and offline trade-offs.
- Binary size: compare equivalent build configurations without signing or publication.

## Validation gates

- Gate 1: baseline method is reproducible and relevant to user impact.
- Gate 2: trace evidence identifies a plausible bottleneck.
- Gate 3: candidate and trade-offs have human approval.
- Gate 4: functional behavior and tests pass before performance comparison.
- Gate 5: before and after evidence is comparable and improvement exceeds noise without unacceptable regression.
- Gate 6: independent final review and triple validation pass.

## Failures

If measurements are noisy, non-comparable, or unavailable, report no conclusion. If functionality regresses, stop and restore correctness through the technology owner before further measurement. Do not cherry-pick runs, change methodology after seeing results, or substitute simulator results for device claims without disclosure.

## Stop conditions

Stop for absent baseline, undefined metric, inaccessible profiler, non-comparable environment, production-only workload, personal data, unapproved resource-intensive run, required architecture or dependency change, unacceptable trade-off, signing, deployment, or cost.

## Evidence

Record tool and version, device or simulator, OS, build mode, scenario, data set, network, warm-up, samples, raw values, aggregation, variance, traces, changed files, functional tests, related resource metrics, and reviewer findings.

## Outputs

- reproducible baseline and bottleneck analysis;
- scoped approved optimization when evidence supports it;
- before-and-after comparison and functional regression evidence;
- trade-offs, residual risks, and criterion ledger.

## Acceptance criteria

The target metric improves beyond expected noise under comparable conditions, correctness and required quality criteria remain satisfied, no unsupported performance claim is made, and the final review accepts the evidence.

## Human approvals

Require approval for measurement targets, devices, long or costly runs, network access, background work, caches, dependencies, architecture, behavior trade-offs, telemetry, production-like data, and any persistent change.

## Prohibited actions

Do not claim unmeasured improvement, cherry-pick samples, use live-user data, run production load, hide correctness regressions, add unapproved caches or dependencies, self-review implementation, sign, publish, deploy, spend money, or run Git write commands.
