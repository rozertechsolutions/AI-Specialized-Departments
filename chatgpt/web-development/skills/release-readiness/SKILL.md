---
name: release-readiness
description: Use to produce a human-reviewable web release-readiness verdict without deploying, publishing, merging, or signing.
---

# Release Readiness

## Mission
Produce a final, evidence-based release-readiness assessment. This Skill never deploys, publishes, merges, tags, signs, spends, or submits.

## Use When

- The user asks whether a web change is ready to release.
- A task needs final gate status, residual risk, or a human approval package.
- Multiple specialist reviews need a single verdict.

## Inputs

- Requirements, implementation summary, changed files, test/build/browser/security/accessibility/performance evidence, deployment plan, rollback plan, monitoring plan, and unresolved findings.

## Procedure
1. Trace requirements to implementation and verification evidence.
2. Confirm security, privacy, accessibility, performance, SEO, tests, browser support, observability, migration, rollback, and documentation status as applicable.
3. Block readiness for unresolved critical findings, missing required evidence, secret exposure, or unauthorized scope changes.
4. Never publish, merge, deploy, tag, spend, sign, or submit automatically.
5. Return a final verdict: PASS, FAIL, BLOCKED, or NOT APPLICABLE, with evidence and required human decisions.

## Output Contract

- Final verdict: PASS, FAIL, or BLOCKED.
- Gate-by-gate status and evidence.
- Required human approvals before release.
- Unexecuted checks, residual risks, rollback notes, and owner decisions.

## Stop Conditions

Stop and report BLOCKED when required evidence, independent review, approval, rollback, monitoring, migration, or risk acceptance is missing.

## Prohibited Actions

- Do not deploy, publish, merge, tag, sign, submit, spend, mutate Git, authenticate, or perform destructive actions.
- Do not convert missing evidence into PASS.
