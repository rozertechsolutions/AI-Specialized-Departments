---
name: fix-mobile-bug
description: Diagnose and fix a scoped mobile bug with reproduction, root cause, regression coverage, validation evidence, and independent review.
---

# fix-mobile-bug

## Objective

Fix the reported defect at its root cause without masking errors or changing unrelated behavior.

## Inputs

Bug report, expected and actual behavior, affected platform(s), logs or stack traces, reproduction steps, and approved scope.

## Supported Technologies

Android, iOS, Kotlin Multiplatform, Flutter, React Native, and mixed mobile repositories.

## Preconditions

- Inspect relevant code, tests, configuration, current changes, and available commands.
- Reproduce or reason from concrete evidence before editing.
- Select the owner by defective component.

## Primary Owner

The technology owner responsible for the defective code: `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer`.

## Reviewers

`mobile-test-engineer` and `mobile-code-reviewer`; add security, accessibility, or performance reviewers when the defect touches those areas.

## Steps

1. Capture reproduction evidence or explain why reproduction is unavailable.
2. Identify root cause and blast radius.
3. Implement the smallest fix.
4. Add regression coverage that fails for the bug when practical.
5. Run targeted checks first, then broader relevant checks when reasonable.
6. Perform independent final review.

## Validation Gates

Regression test, affected test suite, build/type/lint/static checks, platform-specific validation, secret detection for touched files, and review of loading/error/retry/offline/cancellation states where relevant.

## Failures And Stop Conditions

Stop on irreproducible symptoms with insufficient evidence, missing approval, risky production behavior change solely for tests, unrelated failure, or out-of-scope architectural change.

## Evidence And Outputs

Root cause summary, changed files, regression coverage, command results, unavailable checks, and final review.

## Acceptance Criteria

The bug is fixed in scope, regression risk is covered, and no unrelated behavior is changed.

## Prohibited Actions

No broad exception swallowing, arbitrary defaults, test weakening, unrelated cleanup, publishing, signing, deployment, or fabricated success.
