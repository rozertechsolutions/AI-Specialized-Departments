---
name: fix-mobile-bug
description: Diagnose and fix a mobile bug with reproduction, root cause, regression coverage, and safe validation.
---

# Fix Mobile Bug

## Objective

Fix a confirmed or plausibly reproducible mobile defect without changing unrelated behavior.

## Trigger

Use when the user reports a bug, failing test, crash, regression, or incorrect mobile behavior.

## Inputs

Bug description, logs, stack traces, screenshots, affected platform, reproduction steps, expected behavior, observed behavior, and affected version if known.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native.

## Preconditions

Inspect current changes, related code, tests, configuration, logs, crash context, and issue history when available. Reproduce locally when feasible before editing.

## Primary Owner

The platform engineer for the failing runtime. Use `kmp-engineer` for shared KMP root causes and `mobile-test-engineer` for regression coverage.

## Reviewers

`mobile-code-reviewer` and `mobile-test-engineer`; add security, UI/accessibility, or performance reviewers when the defect touches those surfaces.

## Steps

1. Establish the smallest known reproduction or exact unavailable reason.
2. Identify root cause and affected ownership boundary.
3. Implement the smallest fix using existing conventions.
4. Add a regression test or explain why no reliable test can be added.
5. Run the failing check, targeted tests, and relevant configured checks.
6. Review for side effects, error handling, and regression risk.

## Conditional Steps

- If the bug cannot be reproduced, document the attempted reproduction and inspect the most likely code path.
- If the root cause is shared KMP logic, route the fix to `kmp-engineer`.
- If the fix affects security, UI/accessibility, performance, or release behavior, invoke the matching reviewer.
- If the failing validation depends on unavailable infrastructure, report the exact blocker instead of fabricating evidence.

## Validation Gates

Required: reproduction evidence or blocker, regression test or justified exception, affected tests, compile/build where relevant, configured lint/type/static analysis, formatting, secret review, and code review.

## Failures and Stop Conditions

Stop when reproduction requires credentials, paid services, production data, destructive device actions, signing, publication, or missing tools that cannot be safely substituted.

## Evidence

Record reproduction, root cause, files changed, regression coverage, commands, outputs, and any unavailable infrastructure.

## Outputs

Scoped bug fix, regression evidence, validation results, and residual risk.

## Acceptance Criteria

The defect is fixed or blocked with evidence, no unrelated behavior changes are introduced, and required checks pass.

## Human Approvals

Required for security-sensitive behavior, dependencies, permissions, entitlements, production services, credential use, destructive commands, or external writes.

## Prohibited Actions

Do not mask the bug with broad catches, arbitrary defaults, disabled tests, blanket suppressions, fabricated data, signing, publishing, uploads, or out-of-scope rewrites.
