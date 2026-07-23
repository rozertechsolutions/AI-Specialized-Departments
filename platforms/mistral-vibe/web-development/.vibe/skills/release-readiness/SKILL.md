---
name: release-readiness
description: "Produce a human-reviewable release-readiness assessment without deploying."
user-invocable: true
allowed-tools:
  - read
  - read_file
  - grep
  - ask_user_question
---

# Release Readiness

## Mission
Produce a human-reviewable release-readiness assessment without deploying.

## Vibe invocation
Invoke with `/release-readiness` only after implementation and required reviews have evidence. This Skill never deploys, publishes, tags, merges, or submits.

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
