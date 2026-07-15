---
name: fix-mobile-bug
description: Diagnose a mobile defect from evidence, reproduce it when possible, identify the root cause, apply the smallest safe correction, add regression coverage, and obtain independent review.
user-invocable: true
---

# Fix Mobile Bug

## Objective

Correct the proven root cause of a mobile defect with the smallest safe change, preserve unrelated behavior, and prevent regression with deterministic evidence.

## Trigger

Use for an explicit request to diagnose and fix incorrect existing mobile behavior. If the user asks only for diagnosis, stop after the root-cause report and do not edit.

## Inputs

- Expected versus observed behavior, affected versions/platforms/devices, frequency, and first-known occurrence.
- Reproduction steps, logs, crash/trace data, screenshots, failing tests, or support evidence when available.
- Approved behavior/file scope and compatibility constraints.

## Preconditions

- Read instructions, status/diff, relevant history when useful, affected code/tests/configuration, and existing user changes.
- Treat supplied logs and data as potentially sensitive; do not expose or transmit them.
- Establish whether reproduction infrastructure is safe and available.

## Ownership

- Primary owner: the single specialist owning the root-cause area under the `QWEN.md` matrix.
- `mobile-test-engineer` owns regression strategy.
- Security/accessibility/performance reviewers participate when the defect or fix affects their domains; `mobile-code-reviewer` reviews last.

## Tool and permission boundary

Use read/search and safe local reproduction first. Edit only after root-cause evidence and scope are established. Run targeted, project-defined commands under normal approval. No production access, credentials, external writes, dependency changes, destructive resets, signing, or publishing.

## Sequence and gates

1. **Evidence gate:** Normalize expected/actual behavior, environment, frequency, and evidence. Separate facts, hypotheses, and missing data.
2. **Reproduction gate:** Reproduce with the smallest deterministic local case or a failing test when possible. Record exact steps and environment. If reproduction is impossible, require a strong static causal chain and label confidence.
3. **Localization gate:** Trace from symptom through state/data/lifecycle/concurrency/native boundaries to the earliest incorrect invariant. Test competing hypotheses; do not patch the symptom.
4. **Root-cause gate:** State the violated invariant, triggering condition, exact path/line, why existing tests missed it, and affected surface. Stop if evidence is insufficient for a safe fix.
5. **Ownership/scope gate:** Assign the root-cause area to one primary owner and define the smallest changed paths. Obtain approval for any contract, schema, dependency, permission, or migration change.
6. **Correction gate:** Implement the minimal fix, explicitly handling the triggering condition and relevant error/cancellation/recovery behavior without broad fallback or suppression.
7. **Regression-test gate:** Add a deterministic test that fails for the original cause and passes for the fix. Cover adjacent boundary/failure cases proportionately.
8. **Validation gate:** Run the new test before/after when feasible, affected suite, compilation/non-publishing build, configured analysis, and platform checks. Confirm no unexplained warning or unrelated diff.
9. **Independent review gate:** Obtain applicable specialist reviews and final code review. A correction invalidates prior results and requires revalidation and rereview.
10. **Completion gate:** Classify all `QWEN.md` criteria, document confidence and any unverified environment-specific risk.

## Errors and stop conditions

Stop when evidence cannot distinguish causes, reproduction requires production or sensitive access, the fix needs an unapproved contract/dependency/migration, the affected owner is unclear, required infrastructure is unavailable and static evidence is insufficient, validation fails, or a high/critical finding remains.

## Outputs and evidence

- Reproduction or static causal evidence, exact environment, and confidence.
- Root cause and violated invariant with exact paths/lines.
- Minimal changed paths and regression cases.
- Exact commands, exit codes, targets, and observed results.
- Completion ledger, reviews/corrections, residual risks, and human actions.

## Acceptance criteria

- The root cause, not only the symptom, is corrected.
- A meaningful regression test demonstrates the triggering condition where feasible.
- Affected builds/checks/tests pass and no existing validated behavior regresses.
- Scope is minimal and required independent review has no unresolved blocker.

## Human review requirements

Humans approve changed expected behavior, compatibility trade-offs, migrations, dependencies, permissions, production/sensitive investigation, and unavailable-risk acceptance.

## Prohibited actions

Do not guess a root cause, suppress the error broadly, add arbitrary delays/retries/defaults, weaken assertions, modify production behavior only for tests, access production, expose logs/secrets, reset user changes, or self-approve.
