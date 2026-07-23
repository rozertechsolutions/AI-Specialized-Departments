---
name: fix-mobile-bug
description: Diagnose and minimally fix an evidence-backed mobile defect, add a regression test, and validate the affected Android, iOS, KMP, Flutter, or React Native path.
when_to_use: Use when existing behavior is incorrect, crashes, regresses, or violates an established contract and reproduction or equivalent evidence can be gathered.
argument-hint: "[bug evidence or reproduction]"
model: inherit
---

# Objective

Reproduce or substantiate the defect in `$ARGUMENTS`, identify its root cause, apply the smallest correct fix, and prove the regression is covered.

# Required input and supported scope

Require expected versus actual behavior, affected versions/platforms, reproduction steps or logs/tests, frequency, environment, and acceptance criteria. Support all five mobile technologies and hybrid ownership after inspection.

# Preconditions and inspection

Read project instructions and inspect status/diff, affected technology and call path, recent relevant history when useful, configuration, logs supplied by the user, existing tests, and project commands. Sanitize sensitive logs and never request credentials or private production data.

# Ownership

Assign the affected implementation surface to its technology owner. `mobile-test-engineer` owns reproduction and regression-test strategy; use `mobile-security-reviewer` for security/privacy impact, `mobile-performance-reviewer` for measured performance defects, and `mobile-code-reviewer` for final independent review. Cross-platform symptoms do not change shared/platform ownership.

# Procedure and gates

1. Reproduce with an existing test or minimal controlled case. If direct reproduction is unavailable, gather equivalent deterministic evidence and label its limits. Gate: no code fix without credible failure evidence.
2. Trace state/data/control flow and test competing hypotheses. Identify the causal condition, not merely the failing line. Gate: root cause explains the evidence and affected scope.
3. Define the minimal correction, compatibility impact, and regression-test level. Stop for unapproved architectural/public/persistence changes.
4. Add a regression test that fails for the original cause, then implement the fix without broad cleanup or arbitrary fallback behavior.
5. Run the regression test, adjacent tests, target compilation/build, lint/static analysis, and relevant platform checks discovered in the repository.
6. Review error handling, lifecycle/concurrency, offline/network, security, accessibility, and performance effects as applicable.
7. Obtain final independent review. If any fix changes after review, rerun affected evidence and review.

# Failure and stop handling

If reproduction remains impossible, return the evidence gap and a safe diagnostic plan instead of a speculative patch. Stop on secrets, production-connected diagnostics without approval, failed required checks, broader root cause requiring authorization, or inability to add a meaningful regression test; state the precise blocker.

# Evidence and acceptance

Return reproduction/equivalent evidence, root-cause chain, minimal diff, regression test, exact commands/results, applicability classification, reviews, and residual risk. Classify each considered criterion as `required`, `conditionally-required`, or `not-applicable` with reasons.

Accept only when the original failure is demonstrably prevented, the regression test would catch recurrence, adjacent behavior remains valid, required checks pass, and independent review has no blocker. Unavailable device/infrastructure remains `unavailable`.

# Human review and prohibited actions

Require human review for behavior-contract changes, migrations, dependencies, sensitive logs/configuration, and production diagnostics. Never guess a fix, hide the symptom with broad exception handling/defaults, delete or weaken tests, access private data, publish/sign/deploy, or claim an unreproduced issue is resolved.
