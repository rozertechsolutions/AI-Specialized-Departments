---
name: optimize-mobile-performance
description: Optimizes a measured mobile performance bottleneck by establishing a reproducible baseline, profiling, applying one targeted platform-owned change, comparing before and after, and checking regressions. Use only when a concrete performance outcome is requested.
---

# Optimize Mobile Performance

## Objective and trigger

Improve one measurable mobile performance outcome without behavior regression and
without presenting hypotheses as results. Activate for a concrete startup,
rendering, memory, battery, background, network, storage, or size concern. Do not
activate for generic cleanup or an optimization without a measurable scenario.

Activation does not grant tools. Use only project-allowed repository tools and
approved local measurement commands; do not use MCP or external telemetry.

## Inputs

- User-visible scenario, metric/budget, target platform/device/OS/build mode, and
  representative data.
- Current measurement/profiling evidence, suspected component, and constraints.
- Behavior and compatibility requirements plus acceptable trade-offs.
- Available local profiler/tooling and authorization for the measurement cost.

## Preconditions and ownership

Inspect instructions, status/diff, performance-sensitive code/config/assets/tests,
and existing benchmarks. Establish a reproducible local scenario before editing.
Do not profile production or collect personal telemetry without exact approval.

`mobile-performance-reviewer` is primary owner of scenario, baseline, hypotheses,
measurement protocol, and acceptance. The targeted change belongs exclusively to
`android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or
`react-native-engineer` according to its actual platform boundary.
`mobile-test-engineer` owns regression coverage;
security/UI reviewers are conditional; `mobile-code-reviewer` is final.

## Workflow and gates

1. **Metric gate:** define metric, budget, scenario, device/OS, build mode,
   cold/warm state, dataset, repetitions, statistics, variance, and confounders.
2. **Baseline gate:** run or obtain approved raw measurements under those exact
   conditions. Record tool/version and raw results. Stop if no valid baseline.
3. **Profile gate:** collect the narrowest approved profile and rank hypotheses
   tied to code evidence. Distinguish correlation from demonstrated bottleneck.
4. **Target gate:** select one hypothesis and smallest reversible change. Define
   expected metric effect, behavior/security/accessibility risk, owner, rollback,
   and regression checks. Obtain architecture approval for boundary changes.
5. **Implementation:** platform owner changes only assigned files, with no
   unapproved framework/dependency, quality reduction, disabled behavior, or
   cached/stale result that changes the product contract.
6. **Correctness gate:** run affected functional, lifecycle, failure, UI, offline,
   and resource tests before claiming performance benefit.
7. **Comparison gate:** repeat the exact baseline protocol. Report raw before/
   after distributions, variance, percent/absolute difference, budgets, and any
   regressions. If conditions differ, results are incomparable and cannot pass.
8. **Review gate:** performance reviewer independently evaluates evidence;
   security/UI/test reviewers assess relevant trade-offs; code reviewer reviews
   correctness and evidence. Rerun from baseline if measurement method changes.

## Completion classification

Classify scenario/baseline; configuration; compilation; functional and unit/
integration/UI/snapshot/E2E tests; lint/static/formatting; dependencies; security;
accessibility/localization/adaptive UI; startup/render/memory/battery/background/
network/storage/size metrics; offline/recovery behavior; documentation; warnings;
regressions; independent review; and platform-native profiling as `required`,
`conditionally-required`, or `not-applicable` with concrete reasons.

## Errors and stop conditions

Stop for no reproducible baseline, unavailable/unauthorized profiler or device,
production/PII telemetry, incomparable conditions, excessive variance without an
explanation, unapproved behavior/architecture/dependency change, security or
accessibility regression, destructive action, conflicting edits, or failed tests.

## Outputs, evidence, and acceptance

Return scenario/protocol, raw baseline/profile/before-after evidence, hypotheses,
selected change/owner/files, correctness checks, statistics/variance, budgets,
specialist reviews, completion ledger, limitations, regressions, and rollback.

Acceptance requires comparable evidence showing the target improvement or budget,
preserved behavior, successful available validation, no blocking regression, and
independent performance and code review. Otherwise report `not_demonstrated`.

## Human review and prohibited actions

Humans approve profiling cost, production access, behavior trade-offs, architecture,
and dependencies. Never fabricate benchmarks, profile production without approval,
send telemetry externally, add dependencies, weaken behavior/security/accessibility,
sign/publish/deploy/upload, destroy data, or perform Git writes.
