---
name: fix-mobile-bug
description: Reproduce, isolate, minimally fix, and regression-test a defect in an existing Android, iOS, KMP, Flutter, or React Native project. Do not use for speculative cleanup without a reproducible failure.
---

# Fix Mobile Bug

## Objective

Correct one demonstrated defect with the smallest root-cause fix and evidence that the failure is resolved without regression.

## Required inputs

- Observed versus expected behavior and acceptance criteria.
- Reproduction steps, environment, platform, OS/device, variant, and frequency.
- Relevant logs/stack traces with sensitive values removed.
- Known regression range or recent diff when available.
- Constraints on compatibility and allowed behavior changes.

If the defect cannot yet be reproduced, treat reproduction as the first deliverable and do not guess at a fix.

## Preconditions

1. Inspect instructions, repository status, affected code, related tests, recent read-only history, and available diagnostics.
2. Preserve current user changes and establish the diff base.
3. Confirm logs contain no secrets or personal data before reading or reporting them.
4. Determine the primary platform owner and required test environment.
5. Classify every completion criterion as required, conditionally required, or not applicable with a documented reason.

## Agent ownership

The coordinator owns triage and evidence. Select one platform owner from `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer`. `mobile-test-engineer` owns the regression test. Use `mobile-architect` only if the root cause is architectural. Invoke domain reviewers only when the bug or fix touches their risk area. `mobile-code-reviewer` reviews the final diff.

## Execution

1. **Reproduce.** Execute the narrowest safe local reproduction or construct a deterministic test from the supplied evidence. Record exact environment and output.
2. **Gate: evidence.** Continue to code changes only when there is a concrete failing path or sufficiently specific static defect. Otherwise report a reproduction plan and missing evidence.
3. **Trace root cause.** Follow control/data flow from symptom to violated invariant. Separate the root cause from secondary symptoms and unrelated warnings.
4. **Regression test first when practical.** `mobile-test-engineer` adds a focused failing test that represents the expected behavior. If no suitable harness exists, document why and define manual/alternative evidence.
5. **Fix plan.** The platform owner proposes the smallest behavior-preserving correction, affected files, edge cases, and rollback path.
6. **Implement.** Change only the root-cause boundary. Do not broaden the fix into cleanup or architecture changes.
7. **Targeted gate.** Rerun the reproduction/regression test and directly affected static/compile checks. Confirm the original failure is gone for the correct reason.
8. **Edge validation.** Test adjacent success/failure, lifecycle, concurrency/cancellation, offline, persistence, and platform-version cases that can share the root cause.
9. **Specialist review.** Run security, UI/accessibility, or performance review only if the root cause/fix affects that domain.
10. **Code review.** `mobile-code-reviewer` checks the diff for masking, incomplete cleanup, new races, state inconsistency, compatibility, and missing regression coverage.
11. **Broader suite and final gate.** Run reasonable broader checks, review the final diff, and confirm no required criterion fails.

## Error handling and stop conditions

Stop if reproduction depends on production credentials/data, an unavailable paid/external service, destructive device state, signing, an unknown expected behavior, or an unapproved dependency/contract change. If the suspected cause cannot be proven, report hypotheses ranked by evidence rather than modifying code. Do not fix unrelated failures.

## Outputs

- Reproduction evidence and root cause.
- Minimal fix and affected files.
- Regression test or documented reason no automated test is possible.
- Before/after command results and relevant edge cases.
- Completion matrix with required/conditional/not-applicable status, reasons, and exact results.
- Review findings, residual risk, and any unverified environment.

## Acceptance criteria

- The original failure is reproducible before and absent after the fix, or equivalent deterministic evidence is supplied.
- A regression test protects the behavior when a supported harness exists.
- Required compile/static/test checks pass and no validation is weakened.
- The fix changes no unrelated behavior, contains no secret, and introduces no unexplained warnings.

## Prohibited actions

Do not make speculative fixes, swallow errors, add arbitrary retries/sleeps, disable tests, erase device data, use real user data, access production, add dependencies without approval, sign, publish, or include unrelated refactoring.
