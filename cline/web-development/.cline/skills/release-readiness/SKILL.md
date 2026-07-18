---
name: release-readiness
description: Produce a final web release-readiness verdict. Use when requirements, evidence, reviews, rollback, approvals, and risks must be checked.
---

# Release Readiness

## Mission
Produce a human-reviewable release-readiness assessment without deploying.

## Use when
- The user asks whether a web change is ready to release, merge, publish, or hand off.
- Multiple quality gates need one final evidence-based verdict.

## Do not use when
- Implementation or required independent reviews are still intentionally in progress.

## Inputs
Requirements, changed files, implementation summary, test/build/browser/security/accessibility/performance evidence, deployment plan, rollback plan, and unresolved findings.

## Required procedure
1. Trace requirements to implementation and verification evidence.
2. Confirm security, privacy, accessibility, performance, SEO, tests, browser support, observability, migration, rollback, and documentation status as applicable.
3. Block readiness for unresolved critical findings, missing required evidence, secret exposure, or unauthorized scope changes.
4. Never publish, merge, deploy, tag, spend, sign, or submit automatically.
5. Return a final verdict: PASS, FAIL, BLOCKED, or NOT APPLICABLE, with evidence and required human decisions.

## Output contract
- State confirmed scope and evidence.
- Separate facts, assumptions, risks, and unresolved decisions.
- List files or components affected or reviewed.
- State which quality gates are PASS, FAIL, BLOCKED, or NOT APPLICABLE.
- Do not claim execution or success without direct evidence.

## Stop and failure behavior
Return BLOCKED when required evidence, independent review, approval, rollback, monitoring, migration, or risk acceptance is missing.

## Review requirements
Return PASS, FAIL, or BLOCKED with gate-by-gate evidence, unexecuted checks, residual risks, and required human approvals.

## Prohibited actions
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
