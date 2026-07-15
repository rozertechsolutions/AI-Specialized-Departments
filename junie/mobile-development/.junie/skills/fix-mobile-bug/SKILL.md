---
name: "fix-mobile-bug"
description: "Diagnose and fix a mobile defect with reproduction, root cause, regression coverage, validation evidence, and independent review."
---
# Fix Mobile Bug

Use this skill when the user reports a mobile defect, crash, regression, flaky behavior, or broken validation.

## Workflow Definition

Objective: fix the defect at its root cause without unrelated refactoring.

Trigger: bug report, failing test, crash log, regression, or user-described incorrect behavior.

Inputs: expected behavior, actual behavior, reproduction steps, logs/crash traces, affected platform(s), recent changes, tests, and environment details.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, and React Native.

Preconditions:

- Reproduce or reason from concrete evidence before editing.
- Identify affected technology and owner.
- Preserve user changes and do not discard local work.
- Ask approval for sensitive or destructive actions.

Primary owner: matching platform engineer or `kmp-engineer` for shared KMP logic.

Reviewers: `mobile-test-engineer` and `mobile-code-reviewer`; add security/UI/performance reviewers when the bug touches those domains.

## Steps

1. Gather reproduction evidence and affected paths.
2. Inspect relevant code, tests, config, and recent local changes.
3. State root cause or the strongest supported hypothesis before editing.
4. Implement the smallest fix in the owning layer.
5. Add regression coverage that fails before the fix when practical.
6. Run targeted validation first, then broader relevant checks when reasonable.
7. Confirm the fix does not weaken error handling, security, accessibility, or performance.
8. Request independent final review.

## Validation Gates

- Root cause is documented.
- Fix is scoped to the owning layer.
- Regression test exists or a concrete not-applicable reason is recorded.
- Failing checks caused by the change are corrected before completion.

## Failures And Stop Conditions

Stop for irreproducible high-risk bugs without enough evidence, missing approval for sensitive changes, unrelated pre-existing failures, credentials, destructive commands, or release actions.

## Evidence And Outputs

Output root cause, changed files, regression tests, commands run, results, unresolved pre-existing failures, unavailable infrastructure, and residual risk.

Acceptance criteria: bug is fixed or bounded by evidence, relevant checks pass or are unavailable, and independent review is complete.

Human approvals: required for deleting tests, changing public contracts, dependencies, lockfiles, auth/privacy/security behavior, signing, external services, and destructive commands.

Prohibited actions: masking errors, broad exception swallowing, arbitrary defaults, weakening tests, unrelated cleanup, release actions, and self-review.
