---
name: release-readiness
description: Produce a human-reviewable release-readiness assessment without deploying.
---

# Release Readiness

## Mission
Produce a human-reviewable release-readiness assessment without deploying.

## Trigger boundary
Use after implementation and required reviews when deciding whether the web change is ready for human release action. Do not use to deploy, publish, tag, merge, or approve unresolved risk.

## Procedure
1. Trace requirements to implementation and verification evidence.
2. Confirm security, privacy, accessibility, performance, SEO, tests, browser support, observability, migration, rollback, and documentation status as applicable.
3. Block readiness for unresolved critical findings, missing required evidence, secret exposure, or unauthorized scope changes.
4. Never publish, merge, deploy, tag, spend, sign, or submit automatically.
5. Return a final verdict: PASS, FAIL, BLOCKED, or NOT APPLICABLE, with evidence and required human decisions.

## Output
State verdict, gate evidence, unresolved risk, required human approvals, and NOT EXECUTED checks.
