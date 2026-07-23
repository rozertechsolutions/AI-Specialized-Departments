---
name: fix-mobile-bug
description: Use when diagnosing and correcting a reproducible or evidence-backed mobile defect with the smallest safe change and regression coverage.
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

# Fix Mobile Bug

## Objective and trigger

Reproduce or otherwise establish credible evidence, identify the root cause, apply the smallest safe correction, add regression coverage, and verify the affected platform. Do not change code based only on an untested guess when better evidence is obtainable.

## Inputs

- Observed versus expected behavior, reproduction steps/frequency, affected versions/platforms/devices, logs or failing tests, first-known version, and acceptance criteria.
- Relevant environment/build variant, data/state prerequisites, and constraints on behavior/contracts.

## Preconditions and ownership

Inspect instructions, status/diff, issue evidence, relevant history read-only, code paths, tests, and available safe reproduction environment. Redact sensitive logs. Partition a cross-runtime failure path into non-overlapping cause/fix units and assign the matrix owner to each; do not assign one owner to an entire mixed-project fix. Each platform owner owns regression tests in its unit unless the coordinator explicitly separates a bounded test-only unit for `mobile-test-engineer`. Use risk reviewers as applicable and independent code review always.

## Sequence and gates

1. Evidence gate: write a precise reproduction or failing test and control variables. If reproduction is impossible, state the evidence level and require a falsifiable root-cause hypothesis.
2. Trace the failing path through inputs, state, lifecycle/concurrency, platform boundaries, errors, persistence, and recent changes. Distinguish cause from symptom.
3. Root-cause gate: explain why the cause produces the evidence and which alternatives were ruled out. Do not edit until the hypothesis is testable.
4. Implement the smallest correction preserving public/persistent behavior and established architecture. Avoid broad fallback/catch/suppression logic.
5. The assigned test owner adds a regression test that fails for the original defect and passes for the correction; `mobile-test-engineer` validates level, determinism, fixtures, and relevant edge/failure/cancellation/lifecycle coverage.
6. Run the reproduction, targeted static/build/test checks, then the reasonable affected suite. Compare behavior to the baseline and record warnings.
7. Invoke security, UI/accessibility, or performance review if the fix touches those domains.
8. Independent code review verifies root cause, scope, regression risk, and test quality. Correct and rerun until clear.

## Errors and stop conditions

Stop when expected behavior is unclear, reproduction needs production data/credentials/destructive device state, the root cause requires an unapproved dependency/contract/architecture change, required tooling is unavailable, user edits conflict, or failures are unrelated. Return evidence and the decision needed.

## Outputs and evidence

Provide reproduction/evidence, root cause, alternatives ruled out, changed files, regression tests, exact commands/results, criterion matrix, review findings, residual risk, and unreproduced environments.

## Acceptance and human review

The original evidence is resolved; regression coverage proves the failure path; required affected-platform checks pass; behavior/contracts are preserved; independent review is clear; and no unrelated change or hidden warning remains. Human review is mandatory for sensitive/configuration/contract changes.

## Prohibited actions

Do not mask symptoms with arbitrary defaults, delete data, reset devices, use production credentials/data, weaken tests, add dependencies without approval, change unrelated code, sign/publish/deploy, or claim an unreproduced environment passed.
