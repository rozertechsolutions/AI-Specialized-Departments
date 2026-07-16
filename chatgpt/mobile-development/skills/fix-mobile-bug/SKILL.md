---
name: fix-mobile-bug
description: Diagnose and correct a mobile defect using evidence, regression tests, and independent final review.
---

# Fix Mobile Bug

## Inputs

- Bug report, reproduction details, affected platform, expected behavior, actual behavior, logs or supplied files, and acceptance criteria.

## Preconditions

- Separate confirmed evidence from assumptions.
- Select the platform owner from detected files and bug surface.
- ChatGPT cannot run repository builds, tests, devices, simulators, signing, or release actions unless a separately enabled native tool supplies verifiable evidence.

## Owner And Reviewers

- Owner: coordinator-selected platform engineer.
- Reviewers: `mobile-test-engineer` and `mobile-code-reviewer`; add security, UI, or performance reviewers when the fix touches their domain.

## Steps

1. Reconstruct the failure path from supplied evidence.
2. Identify the minimal code or configuration change.
3. Define or add the regression test that would fail before the fix.
4. Check edge cases, nullability, lifecycle, concurrency, offline/error states, and platform-specific constraints.
5. Require independent review before completion.

## Validation Gates

- Evidence: root cause, fix scope, regression coverage, manual checks still needed, and residual risk.
- Completion: defect path is addressed without unrelated behavior changes.

## Prohibited Actions

- Do not weaken validation, hide errors, broaden the fix without cause, self-review, claim unrun tests passed, sign, publish, upload, deploy, or use credentials.
