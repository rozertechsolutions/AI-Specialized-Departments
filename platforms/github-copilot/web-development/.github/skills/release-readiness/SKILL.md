---
name: release-readiness
description: Produce a human-reviewable release-readiness assessment without deploying.
---

# Release Readiness

## Mission
Produce a human-reviewable release-readiness assessment without deploying.

## Trigger boundary
Use after implementation and required reviews when deciding whether the web change is ready for human release action. Do not use to deploy, publish, tag, merge, or approve unresolved risk.

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
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
