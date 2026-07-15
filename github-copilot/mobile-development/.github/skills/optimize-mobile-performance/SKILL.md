---
name: optimize-mobile-performance
description: Optimizes a measured mobile performance problem by establishing a reproducible baseline, profiling, identifying a supported bottleneck, applying one targeted change through the technology owner, remeasuring, checking regressions, and independently reviewing the result.
---

# Optimize mobile performance

## Objective

Improve a defined user-visible performance metric through equivalent before/after measurement and a targeted, evidence-supported change without trading away correctness, security, accessibility, battery, or maintainability.

## Trigger

Use only for an explicit performance problem or optimization request with a measurable target. Do not use for speculative cleanup described as performance work.

## Inputs

- symptom, user scenario, metric, target threshold, and business impact;
- affected technology, platform, OS, device class, build mode, data size, and network/storage conditions;
- existing traces, benchmarks, regressions, size reports, or monitoring evidence;
- acceptable trade-offs, constraints, and validation environments.

## Preconditions

- Read applicable instructions, relevant architecture/code, existing benchmarks/profiling setup, build variants, test commands, and current changes.
- Define a reproducible scenario, tooling, warm-up, repetitions, aggregation, and noise controls before changing code.
- Use a representative non-debug build where available without real signing, upload, or distribution.
- Obtain approval before adding benchmarking dependencies, tools, instrumentation, or persistent telemetry.

## Ownership

Primary workflow owner: `mobile-performance-reviewer`, which remains read-only and owns measurement validity and bottleneck assessment. The selected technology engineer is the sole owner of the targeted code change. Test, security, UI/accessibility, and code reviewers support independently.

## Sequence and intermediate gates

1. **Metric gate:** define the exact scenario and metric for startup, frame/rendering, memory/leaks, battery/background work, network, storage, or package size. Stop if success cannot be measured.
2. **Baseline gate:** the technology owner runs the agreed measurement under recorded conditions for enough repetitions to expose variance. Preserve raw summaries and do not discard inconvenient runs without reason.
3. Profile the relevant path using existing platform tools. Correlate traces and code to distinguish bottleneck evidence from hypotheses.
4. **Bottleneck gate:** the performance reviewer records the supported bottleneck, confidence, alternative explanations, and regression risks. Stop before edits if evidence is insufficient.
5. Design one smallest targeted change, expected causal effect, guardrails, rollback, and affected tests. Obtain approval for any architecture/dependency change.
6. The technology owner implements the change without unrelated refactoring.
7. Run correctness, security, accessibility, lifecycle, battery/network/storage, and platform regression checks relevant to the change.
8. **Remeasurement gate:** repeat the same scenario, device class, OS, build mode, data, tooling, warm-up, repetitions, and aggregation. If any condition changes, justify it and do not present a direct comparison as equivalent.
9. Compare baseline, after values, variance, threshold, trade-offs, and regressions. Revert is a recommendation for the human/owner if the target is not met; do not use destructive Git operations.
10. Invoke `mobile-code-reviewer` and applicable domain reviewers. Resolve findings and rerun affected correctness and performance evidence.

## Errors and stop conditions

- If the toolchain, representative build/device, or stable baseline is unavailable, report that performance impact is unverified and stop before claiming improvement.
- Do not infer improvement from reduced code, a microbenchmark unrelated to the user scenario, or debug-only measurements.
- Stop when variance overwhelms the result, the target is missed, or a correctness/security/accessibility/battery regression appears.
- Do not enable production telemetry or connect monitoring services without separate approval.

## Completion classification

Classify every coordinator criterion. Requirements/metric traceability, affected configuration, compilation, correctness tests, static checks, security, measured performance domains, warnings, regression evidence, and independent review are normally required. Dependencies, UI/accessibility/localization/adaptive/offline/recovery behavior, documentation, and broader test levels become required when the optimization intersects them.

## Outputs and evidence

Return the measurement protocol, raw baseline/after summaries, variance and comparison, profiler evidence, bottleneck and confidence, changed files and causal rationale, correctness/regression results, reviews, unavailable checks, residual risks, and completion-classification table.

## Acceptance criteria

- Baseline and after measurements are equivalent, reproducible, and tied to the user-visible scenario.
- Evidence supports the bottleneck and causal change.
- The agreed threshold is met without an unresolved correctness, security, accessibility, battery, maintainability, or other performance regression.
- Independent review has no unresolved blocking finding.

## Human review requirements

Humans approve measurement targets, tools/dependencies, representative environments, trade-offs, architecture changes, acceptance of inconclusive results, and any production observability work.

## Prohibited actions

Do not fabricate measurements, compare mismatched conditions as equivalent, add telemetry/tools without approval, weaken correctness/security/accessibility, use production credentials, publish/sign/deploy, destructively revert, or self-approve.
