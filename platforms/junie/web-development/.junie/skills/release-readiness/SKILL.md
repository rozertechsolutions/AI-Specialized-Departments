---
name: release-readiness
description: Produce a human-reviewable release-readiness assessment without deploying.
---

# Release Readiness

Use this skill after implementation and required reviews when deciding whether the web change is ready for human release action. Do not use it to deploy, publish, tag, merge, or approve unresolved risk.

1. Trace requirements to implementation and verification evidence.
2. Confirm security, privacy, accessibility, performance, SEO, tests, browser support, observability, migration, rollback, and documentation status as applicable.
3. Block readiness for unresolved critical findings, missing required evidence, secret exposure, or unauthorized scope changes.
4. Never publish, merge, deploy, tag, spend, sign, or submit automatically.
5. Return PASS, FAIL, BLOCKED, or NOT APPLICABLE with evidence, required human decisions, and NOT EXECUTED checks.
