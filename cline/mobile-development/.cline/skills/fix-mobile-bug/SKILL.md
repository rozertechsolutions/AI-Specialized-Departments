---
name: fix-mobile-bug
description: Workflow for diagnosing and fixing mobile bugs with regression tests and evidence.
---

# Fix Mobile Bug

## Objective

Reproduce, isolate, fix, and validate a mobile defect without broad unrelated changes.

## Trigger

Use when the user reports a bug, crash, regression, flaky behavior, or failing test.

## Inputs

Bug report, reproduction steps, logs, affected platform, expected behavior, actual behavior, changed files, and test output.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native when present.

## Preconditions

Inspect relevant code and tests. Attempt local reproduction when feasible. Identify primary owner.

## Primary Owner

The engineer matching the defect surface.

## Reviewers

`mobile-test-engineer`, security/accessibility/performance reviewers when affected, and `mobile-code-reviewer`.

## Steps

1. Confirm scope and reproduction evidence.
2. Identify regression range or likely cause from code and tests.
3. Add or update a failing regression test when feasible.
4. Implement the smallest fix.
5. Run the regression test and relevant validation.
6. Check for adjacent platform impacts.
7. Perform final independent review.

## Conditional Steps

- Crash: inspect lifecycle, threading, nullability, and platform logs.
- Network bug: inspect retries, cancellation, serialization, auth, and offline behavior.
- UI bug: inspect adaptive layouts, dynamic text, and accessibility states.

## Validation Gates

Bug no longer reproduces locally or limitation is documented; regression coverage exists when feasible; caused failures are fixed.

## Failures

Stop on unreproducible issue with insufficient evidence, unsupported infrastructure, missing approval, or unrelated failure.

## Stop Conditions

Do not guess at fixes without code evidence or user-provided reproduction when local reproduction is impossible.

## Evidence

Reproduction notes, test added/updated, commands run, before/after result, and unavailable infrastructure.

## Outputs

Bug fix, regression coverage, and validation report.

## Acceptance Criteria

The reported bug is fixed within scope and validation evidence is concrete.

## Human Approvals

Required for sensitive, dependency, lockfile, external, destructive, or production-connected changes.

## Prohibited Actions

Do not mask errors, weaken tests, perform unrelated cleanup, fabricate reproduction, self-review, publish, sign, or deploy.
