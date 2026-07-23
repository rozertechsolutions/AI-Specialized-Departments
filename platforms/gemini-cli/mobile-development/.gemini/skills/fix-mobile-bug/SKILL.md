---
name: fix-mobile-bug
description: Reproduces and fixes a mobile defect with evidence, root-cause analysis, the smallest safe correction, regression coverage, platform validation, and independent review. Use when existing Android, iOS, KMP, Flutter, or React Native behavior is incorrect.
---

# Fix Mobile Bug

## Objective and trigger

Prove and correct the root cause of an existing defect with the smallest safe
change and regression evidence. Activate for incorrect existing behavior,
crashes, regressions, or flaky behavior; do not use for new feature scope.

Use project-allowed tools only. Do not access production telemetry, crash systems,
user data, or authenticated services unless the user separately authorizes the
exact read; no MCP server is configured.

## Inputs

- Observed versus expected behavior and acceptance criteria.
- Reproduction steps, platform/device/OS/build, frequency, logs/stack traces, and
  first known version when available.
- Affected modules/targets and any user data, security, or compatibility risk.
- Existing tests, recent relevant changes, and available local environments.

## Preconditions and ownership

Sanitize logs and never request real secrets or personal data. Inspect
instructions, status/diff, history where useful, relevant source/config/tests,
and all files before editing. Distinguish confirmed facts from hypotheses.

Select one owner based on the proven root cause: `android-engineer` for Android,
`ios-engineer` for iOS, `kmp-engineer` for established shared KMP logic,
`flutter-engineer` for Flutter, or `react-native-engineer` for React Native.
`mobile-test-engineer` owns regression-test design.
Require security/UI/performance review if the root cause or correction touches
those domains, and final `mobile-code-reviewer` review in all cases.

## Workflow and gates

1. **Evidence gate:** normalize expected/actual behavior, environment, steps,
   logs, frequency, impact, and scope. Reject unsanitized sensitive data.
2. **Reproduction gate:** reproduce locally when safe and available, or establish
   a deterministic failing test/minimal evidence. Record exact command and result.
   If not reproducible, keep status explicit and avoid speculative changes.
3. **Root-cause gate:** trace control/data/state/lifecycle/concurrency flow to the
   earliest incorrect assumption. List hypotheses and falsifying evidence. Do not
   patch a downstream symptom without explaining causality.
4. **Ownership/risk gate:** assign one primary owner and disjoint files. Obtain
   architecture approval if the smallest correction changes contracts/boundaries.
5. **Regression-first gate:** where feasible, `mobile-test-engineer` adds a test
   that fails for the demonstrated defect for the correct reason.
6. **Correction:** primary owner applies the smallest complete change, preserving
   behavior outside the acceptance criteria and handling relevant failure paths.
7. **Validation:** prove the regression test now passes; run affected compile,
   unit/integration/UI and lint/static/format checks plus reasonable broader tests.
8. **Specialist and independent review:** review changed sensitive/UI/performance
   surfaces, then final code review. Fix findings and rerun from the affected gate.

## Completion classification

Classify requirements/scope; reproduction; root cause; configuration;
compilation; unit/integration/UI/snapshot/E2E tests; lint/static/formatting;
dependencies; security/secrets; accessibility/localization/adaptive UI;
performance/resources/offline/recovery; documentation; warnings; regressions;
independent review; and platform-native checks as `required`,
`conditionally-required`, or `not-applicable` with concrete reasons. A test or
reproduction is passed only with recorded successful evidence.

## Errors and stop conditions

Stop for ambiguous expected behavior, unsafe/production-only reproduction,
personal data or credentials, no causal evidence, required architecture/
dependency/API changes without approval, destructive actions, conflicting edits,
or validation failures outside scope. Report `not_reproduced` honestly.

## Outputs, evidence, and acceptance

Return sanitized evidence, reproduction status, hypotheses, proven root cause,
owner/files, correction, regression tests, commands/results, specialist review,
completion ledger, warnings, unavailable checks, and residual risk.

Acceptance requires a causal explanation, smallest safe correction, regression
coverage where feasible, successful available affected-platform validation, no
unresolved blockers, and independent review. If reproduction was impossible,
state the reduced confidence and obtain explicit human acceptance.

## Human review and prohibited actions

Humans approve behavior changes, production access, dependency/public-contract
changes, and residual risk. Never hide failures, weaken assertions, delete data,
use production telemetry without authorization, add dependencies, use secrets,
sign/publish/deploy/upload, or perform Git writes/destructive commands.
