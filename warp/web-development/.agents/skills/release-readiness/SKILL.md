---
name: release-readiness
description: Produce a human-reviewable release-readiness assessment without deploying.
---

# Release Readiness

## Mission
Produce a human-reviewable release-readiness assessment without deploying.

## Warp invocation
Invoke manually as `/release-readiness` or let the local Warp agent load it only after implementation and required reviews have evidence. This Skill never deploys, publishes, tags, merges, or submits.

## Inputs
Acceptance criteria, changed files, review outcomes, validation evidence, browser support evidence, known exclusions, operational constraints, and release risks.

## Expected output
Final PASS, FAIL, or BLOCKED verdict with gate-by-gate evidence, unresolved risks, required human approvals, and NOT EXECUTED checks.

## Stop conditions
Stop with BLOCKED for missing acceptance traceability, missing required review, unresolved material findings, secret exposure, or absent human approval.

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

## Prohibited actions
- Do not run commands, install packages, mutate Git state, deploy, publish, authenticate, handle secrets, spend money, sign artifacts, or perform destructive operations without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
