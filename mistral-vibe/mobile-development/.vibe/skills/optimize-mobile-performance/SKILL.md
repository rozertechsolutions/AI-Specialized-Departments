---
name: optimize-mobile-performance
description: Use only for a reproducible mobile performance problem with a defined metric and authorization to collect comparable local before/after evidence; not for speculative micro-optimization.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - todo
  - ask_user_question
  - task
  - write_file
  - edit
  - bash
---

# Optimize Mobile Performance

## Objective and trigger

Improve one measured startup, rendering, responsiveness, memory, battery, background-work, network, storage, or size problem while preserving correctness, accessibility, security, compatibility, and maintainability.

## Inputs

- Reproducible scenario, metric, affected platform, device/simulator and OS, build type, dataset, warm/cold state, environmental controls, baseline, target/budget, and behavior that must not change.
- Existing profiling/benchmark conventions and authorization for safe local measurement.

## Preconditions and ownership

Inspect instructions, status/diff, relevant code/build files, existing performance evidence and tooling. Confirm measurement needs no signing, production data/credentials, uploaded traces, paid service, destructive resets, or tool installation. If no agreed metric/threshold or comparable environment exists, return a measurement plan without editing.

`mobile-performance-reviewer` owns read-only methodology and evidence evaluation. Partition cross-runtime changes into non-overlapping units; exactly one platform owner implements each unit and owns its platform-specific benchmark/test code. `mobile-test-engineer` owns regression strategy, determinism/flakiness review, and only a separately assigned test-only unit; security and UI/accessibility review are conditional; final code review is independent.

## Sequence and gates

1. Measurement contract: fix scenario, metric, environment, run count, aggregation/variance, confounders, guardrails, and success threshold.
2. Baseline gate: platform owner collects approved local measurements; reviewer validates comparability. Use multiple runs where practical and report median/spread, never the best run alone.
3. Evidence gate: continue only when evidence identifies a plausible bottleneck. Otherwise stop with the next discriminating measurement.
4. Trace work, allocations, I/O, network, rendering, lifecycle, caching, concurrency, background scheduling, and build output to establish root cause.
5. Plan the smallest change, expected mechanism, functional/resource trade-offs, compatibility risk, and rollback. Obtain approval for contract/dependency/architecture changes.
6. Implement one variable at a time. Avoid unbounded caches, unowned background work, unsafe concurrency, or changed semantics.
7. Functional gate: targeted correctness/static/tests must pass before performance comparison.
8. Re-run the same measurement contract. Compare baseline/post results and material secondary metrics such as memory, battery, network, size, and responsiveness.
9. Add stable benchmark/regression coverage only where the project supports meaningful thresholds; avoid noisy wall-clock assertions in ordinary unit tests.
10. Required domain reviews and independent code review; correct, rerun functional checks and the complete measurement contract.

## Errors and stop conditions

Stop on no reproducible baseline, mismatched environments/builds/data, simulator-only evidence for a device claim, invalid thermal/background conditions, unavailable tools, production/paid/credential needs, signing, destructive preparation, unapproved contract/dependency/architecture changes, or functional regressions.

## Outputs and evidence

Provide measurement contract, raw/aggregated before-after results and variance, root cause, changed files, trade-offs, functional/benchmark commands/results, reviewer findings, secondary regressions, criterion matrix, rollback, and limitations.

## Acceptance and human review

The agreed metric improves reproducibly under comparable conditions; all required functional/security/accessibility/compatibility checks pass; secondary costs are acceptable; independent review is clear; and claims match evidence. Humans approve resource/behavior trade-offs, device/production validation, new tooling, dependencies, and architecture changes.

## Prohibited actions

Do not optimize without a baseline, cherry-pick runs, upload traces, use production data, install tools, erase devices, weaken correctness/tests/accessibility/security, add unbounded caches, sign/publish/deploy, or retain complexity without demonstrated benefit.
