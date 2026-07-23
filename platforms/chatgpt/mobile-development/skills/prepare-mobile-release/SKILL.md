---
name: prepare-mobile-release
description: Prepare mobile release readiness evidence without signing, publishing, uploading, submitting, deploying, or distributing.
---

# Prepare Mobile Release

## Inputs

- Release target, versioning requirements, supported platforms, changelog inputs, validation evidence, known risks, and human approval state.

## Preconditions

- This workflow must be manually requested.
- Treat release as readiness-only.
- ChatGPT cannot run repository builds, tests, devices, simulators, signing, or release actions unless a separately enabled native tool supplies verifiable evidence.

## Owner And Reviewers

- Owner: `mobile-release-engineer`.
- Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, and `mobile-code-reviewer`.

## Steps

1. Inventory release prerequisites, versioning, changelog, artifacts expected, validation commands, and signing/publication blockers.
2. Confirm no real signing credential, store submission, upload, deploy, or distribution action is requested.
3. Classify required checks and unavailable infrastructure.
4. Prepare readiness report and human action checklist.
5. Stop before any publishing, signing, upload, submission, deployment, spending, or production mutation.

## Validation Gates

- Evidence: release checklist, validation status, unresolved risks, approval requirements, and manual actions.
- Completion: readiness is reported without performing release actions.

## Prohibited Actions

- Never sign, publish, upload, submit, deploy, distribute, spend money, import credentials, create store releases, or claim human-only steps are complete.
