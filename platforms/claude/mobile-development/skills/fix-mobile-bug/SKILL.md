---
name: fix-mobile-bug
description: Diagnoses and fixes an evidence-backed mobile defect with a regression test. Use for Android, iOS, KMP, Flutter, or React Native bugs.
---

# Fix Mobile Bug

## Objective

Identify the root cause of a reproducible or evidence-backed defect, implement the smallest safe correction, and prove the fix without masking symptoms or changing unrelated behavior.

## Trigger

Use when the user reports incorrect existing behavior, a crash, regression, failing test, or reproducible platform issue. Do not use when desired behavior is genuinely new or undefined.

## Inputs

- observed and expected behavior;
- reproduction steps, frequency, affected versions, platforms, devices, locales, accounts, and network state;
- safe logs, stack traces, screenshots, test failures, or issue evidence with sensitive data removed;
- current repository snapshot and relevant changes;
- known last-good state when available;
- acceptance criteria for the correction.

## Supported technologies

Android, iOS, KMP, Flutter, and React Native, including native hosts and cross-platform boundaries evidenced by the defect.

## Preconditions

- Expected behavior is authoritative and not inferred.
- Evidence contains no unredacted secret or personal data.
- The relevant source, configuration, and tests are available.
- The defect can be reproduced, converted to a failing test, or bounded by credible evidence.
- One owner is selected for the failing production surface.

## Primary owner and reviewers

The owner of the root-cause production surface is primary: android-engineer, ios-engineer, kmp-engineer, flutter-engineer, or react-native-engineer. mobile-test-engineer reviews reproduction and regression coverage. Use mobile-security-reviewer for security or privacy defects, mobile-ui-accessibility-reviewer for UI defects, and mobile-performance-reviewer for resource or timing defects. mobile-code-reviewer is final.

## Ordered workflow

1. Restate observed versus expected behavior, affected scope, reproduction, severity, and evidence quality.
2. Inspect instructions, repository status, relevant code and configuration, recent in-scope changes when available, and existing tests without modification.
3. Reproduce the defect using the smallest safe target, or create a deterministic failing test that demonstrates it. If neither is possible, define the evidence gap and obtain approval before diagnostic edits.
4. Trace data, state, lifecycle, concurrency, navigation, platform, bridge, or configuration paths to identify the root cause.
5. Separate root cause from secondary symptoms and list alternative hypotheses with disconfirming evidence.
6. Select the owning technology responsibility and define the minimal correction, compatibility impact, and regression test.
7. Obtain approval for any dependency, public contract, persistence, permission, privacy, lockfile, build, or architecture change.
8. Implement the smallest correction without broad refactoring.
9. Run the failing reproduction or regression test and confirm it now passes for the intended reason.
10. Run adjacent tests and applicable platform checks to detect regressions.
11. Verify error, cancellation, recovery, offline, lifecycle, concurrency, localization, accessibility, and resource behavior when implicated.
12. Obtain specialist and final code reviews; return findings to the implementation owner and rerun evidence.
13. Complete triple validation and final verification.

## Conditional steps

- Crash or security issue: redact evidence, involve mobile-security-reviewer, and avoid live exploitation.
- Flaky or timing issue: mobile-test-engineer defines repeated runs and synchronization evidence; do not add arbitrary delays or retries.
- Platform-specific failure in shared code: kmp-engineer owns common logic; native owner validates platform integration.
- React Native or Flutter bridge failure: partition cross-platform contract from host implementation.
- Data migration issue: require rollback, recovery, backward-compatibility, and human approval before any persistent change.

## Validation gates

- Gate 1: expected behavior and defect evidence are credible.
- Gate 2: a failing reproduction, test, or explicitly accepted evidence boundary exists.
- Gate 3: root cause is supported and ownership is unique.
- Gate 4: the regression evidence passes after the minimal correction and would detect recurrence.
- Gate 5: adjacent checks and required reviews pass without new warning or behavior change.
- Gate 6: triple review confirms no symptom masking, scope expansion, or fabricated success.

## Failures

If reproduction is inconsistent, record conditions and stop before guessing. If the proposed fix does not make the original evidence pass, revert only Codex-created diagnostic reasoning in the plan, not user files, and reassess the root cause. Never hide the defect with broad exception handling, silent defaults, retries, timeouts, test weakening, or feature removal.

## Stop conditions

Stop for undefined expected behavior, sensitive logs, inability to inspect the failing path, destructive reproduction, production access, unavailable required environment, unapproved public or persistent change, conflicting user edits, credential or signing need, or evidence that the issue is out of scope.

## Evidence

Record original failure, environment, reproduction rate, root-cause path, changed files, regression test, before-and-after results, adjacent checks, warnings, reviewer findings, and unavailable conditions.

## Outputs

- evidence-backed root-cause explanation;
- minimal fix and regression test when authorized tools exist;
- verification and regression evidence;
- criterion ledger, review history, residual risks, and safe next actions.

## Acceptance criteria

The original defect is demonstrated and no longer occurs under the same conditions, the correction addresses root cause, regression coverage is deterministic, adjacent behavior remains valid, and required reviews pass.

## Human approvals

Require approval for production diagnostics, personal data, dependencies, architecture, public or persistent contracts, permissions, privacy, telemetry, destructive reproduction, device state changes, and external tools.

## Prohibited actions

Do not fabricate reproduction, expose sensitive evidence, alter production behavior only to satisfy a test, add arbitrary retries or delays, suppress failures, perform destructive diagnostics, use production credentials, self-review, sign, publish, upload, deploy, or run Git write commands.
