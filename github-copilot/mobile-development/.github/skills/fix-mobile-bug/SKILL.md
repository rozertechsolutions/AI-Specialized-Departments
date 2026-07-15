---
name: fix-mobile-bug
description: Diagnoses and fixes a mobile bug from evidence, reproduces it when possible, applies the smallest root-cause correction, adds regression coverage, validates affected platforms, and obtains independent review. Use for explicit defect correction.
---

# Fix a mobile bug

## Objective

Correct the demonstrated root cause with the smallest safe change, preserve unrelated behavior, add regression evidence, validate the affected platform, and complete independent review.

## Trigger

Use for an explicit bug, crash, test regression, incorrect state, or platform defect. Do not use for speculative cleanup or a feature request framed as a bug.

## Inputs

- expected and actual behavior;
- reproduction steps, frequency, affected versions/devices/configurations, and last known good state;
- logs, stack traces, screenshots, failing tests, traces, or crash evidence with sensitive data removed;
- scope, severity, user impact, workaround, and acceptance criteria.

## Preconditions

- Read applicable instructions, current changes, relevant history when useful, surrounding code, configuration, tests, and analogous paths.
- Validate evidence provenance and redact or avoid sensitive data.
- Select the technology owner from the actual fault boundary, not the visible symptom.
- Define a falsifiable reproduction or, if reproduction is unavailable, state the evidence threshold required before editing.

## Ownership

Primary owner: the technology engineer owning the root-cause boundary. `mobile-test-engineer` owns regression-test design when separately partitioned. Domain reviewers and `mobile-code-reviewer` remain read-only and independent.

## Sequence and intermediate gates

1. **Evidence gate:** normalize expected/actual behavior, environment, timing, logs, and scope. Stop if the report cannot distinguish a defect from intended behavior.
2. Reproduce with the smallest existing command or test when possible. Record exact attempts and results; do not fabricate reproduction.
3. Trace the failing state through lifecycle, concurrency, data, navigation, platform, and configuration boundaries. Generate hypotheses and eliminate them with evidence.
4. **Root-cause gate:** identify the causal defect and explain why it produces the observed behavior. If only a symptom workaround is possible, obtain explicit approval and document residual risk.
5. Add a focused failing regression test when the project supports a deterministic test at an effective level.
6. Apply the smallest compatible correction. Avoid opportunistic refactoring, unrelated formatting, broad fallback behavior, or swallowed errors.
7. Run the regression test, adjacent tests, relevant compile/type/static checks, and reasonable affected platform suite.
8. Check edge, failure, cancellation, lifecycle, state restoration, offline, locale, accessibility, and performance regressions that are plausible for this fault.
9. Invoke applicable domain reviewers and `mobile-code-reviewer`. The primary owner resolves findings and repeats affected validation.

## Errors and stop conditions

- If reproduction depends on unavailable devices, accounts, credentials, production data, or paid services, stop that path and report it; do not connect or fabricate data.
- If evidence points outside approved scope or requires a contract, migration, dependency, permission, or security change, explain and obtain approval.
- Do not change production behavior merely to satisfy an incorrect test.
- A failed required check, unexplained warning, or unresolved high-risk finding blocks completion.

## Completion classification

Classify every coordinator criterion. Requirements/root-cause traceability, affected compilation/type checks, regression tests, static checks, security/secret review, warning review, regression assessment, and independent review are normally required. Other test levels, configuration, dependencies, UI/accessibility, localization, adaptive/offline/recovery behavior, performance, and documentation depend on the fault boundary and must receive concrete reasons.

## Outputs and evidence

Return evidence and reproduction status, root-cause explanation, rejected hypotheses, changed files, regression test, exact commands/results, affected-platform coverage, domain and independent reviews, unavailable checks, residual risk, and completion-classification table.

## Acceptance criteria

- The root cause is supported by evidence and corrected by a minimal change.
- A deterministic regression test fails before and passes after when feasible; otherwise the alternative evidence and limitation are explicit.
- Required affected-platform checks pass without unexplained warnings or regressions.
- Independent review has no unresolved blocking finding.

## Human review requirements

Humans approve non-reproducible or workaround-only fixes, broadened scope, dependency/contract/migration/security changes, unavailable required validation, and accepted residual risk.

## Prohibited actions

Do not use production credentials/data, hide errors, weaken tests, disable validation, perform unrelated cleanup, publish/sign/deploy, destructively reset state, or claim reproduction or review that did not occur.
