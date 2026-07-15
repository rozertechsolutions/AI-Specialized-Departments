---
name: optimize-mobile-performance
description: Optimize a measured mobile startup, rendering, memory, battery, background, network, storage, or size bottleneck with comparable before-and-after evidence.
when_to_use: Use only when a reproducible performance concern or regression can be measured for Android, iOS, KMP, Flutter, React Native, or hybrid code.
argument-hint: "[metric or performance problem]"
model: inherit
---

# Objective

Measure the concern in `$ARGUMENTS`, identify the bottleneck, make the smallest targeted correction, and demonstrate comparable improvement without correctness regression.

# Required input and supported scope

Require a user-relevant symptom, target metric/budget, workload, devices/OS/build mode, baseline or permission to measure, and acceptance criteria. Record simulator/emulator, thermal, network, sampling, and release/debug-mode limitations.

# Preconditions and inspection

Read instructions; inspect status/diff, affected technology/configuration, existing benchmarks/profiling scripts, critical code path, concurrency/background work, rendering, allocations, networking/cache/storage, dependencies/assets, and functional tests. Do not change code before obtaining a credible baseline.

# Ownership

`mobile-performance-reviewer` owns baseline/profiling design and independent analysis; the relevant technology engineer owns implementation. `mobile-test-engineer` protects correctness/regression behavior, security and UI reviewers assess trade-offs where relevant, and `mobile-code-reviewer` is final. The performance reviewer must re-evaluate measurements, not approve its own implementation.

# Procedure and gates

1. Define metric, units, workload, warm/cold state, sample count, environment, and noise controls. Gate: the measurement is reproducible enough to guide a decision.
2. Capture baseline using existing or official local tooling without production data, paid services, or external telemetry unless approved.
3. Profile to localize the bottleneck. Distinguish measured cause from hypothesis and test competing explanations.
4. Define one minimal intervention, expected mechanism, correctness risks, and rollback. Stop for unapproved architecture/dependency/product trade-offs.
5. Implement through the owning engineer; avoid unrelated micro-optimizations.
6. Re-run the identical measurement protocol and report distributions or representative statistics, not a cherry-picked sample.
7. Run affected functional tests, compile/build, lint/static analysis, memory/resource checks, and technology-specific regressions.
8. Have `mobile-performance-reviewer` compare raw conditions/results and `mobile-code-reviewer` inspect the change. Repeat measurement after corrections.

# Failure and stop handling

Stop when no meaningful baseline can be produced, environments are non-comparable, the bottleneck is not localized, required tooling/data is unavailable, or the proposed change sacrifices correctness/security/accessibility without approval. Return a bounded profiling plan rather than an unmeasured claim.

# Evidence and acceptance

Return protocol, environment, baseline, profile evidence, changed files, before/after results, variability/limitations, functional commands/results, applicability classification, reviews, and residual regression risk.

Report every considered universal and technology-specific completion criterion as `required`, `conditionally-required`, or `not-applicable`; give a concrete reason for every `not-applicable`, and label unavailable infrastructure `unavailable` rather than passed.

Accept only when comparable evidence meets the requested threshold or clearly documents the measured outcome, required correctness checks pass, and no performance gain is claimed beyond data. Unavailable device evidence remains unavailable.

# Human review and prohibited actions

Require human review for telemetry/profiling data, paid farms, user-experience/quality trade-offs, dependencies, and architecture changes. Never invent measurements, compare debug with release or different workloads as equivalent, disable safety/accessibility, optimize without a baseline, publish/sign/deploy, or claim simulator results represent all devices.
