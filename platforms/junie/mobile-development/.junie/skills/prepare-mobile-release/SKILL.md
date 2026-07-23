---
name: "prepare-mobile-release"
description: "Manually prepare mobile release readiness for versions, variants, flavors, schemes, reproducibility, package validation, signing prerequisites, and store readiness without publishing or signing."
---
# Prepare Mobile Release

Use this skill only when the user explicitly asks to prepare a mobile release, release checklist, version bump, package readiness review, or store readiness review.

## Workflow Definition

Objective: prepare release readiness while preserving human control over signing, uploads, submissions, publishing, deployment, distribution, credentials, and cost.

Trigger: manual user request. Do not run automatically.

Inputs: target platform(s), version/build number policy, variants/flavors/schemes, changelog/release notes, test evidence, store readiness requirements, signing prerequisites, and release blockers.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, and React Native.

Preconditions:

- Confirm release preparation scope and target platform(s).
- Inspect version/build/signing-related files without exposing secrets.
- Discover non-publishing validation commands.
- Require human approval for any real signing, credential import, upload, submission, publication, deployment, distribution, or cost.

Primary owner: `mobile-release-engineer`.

Reviewers: `mobile-test-engineer`, `mobile-security-reviewer`, `mobile-ui-accessibility-reviewer` when UI changed, `mobile-performance-reviewer` when performance risk exists, and `mobile-code-reviewer`.

## Steps

1. Verify release is manually initiated.
2. Inspect versioning, variants, flavors, schemes, package identifiers, entitlements/manifests, privacy declarations, dependency state, and changelog/release notes.
3. Classify release criteria as required, conditionally-required, or not-applicable with reasons.
4. Confirm no real signing credentials, keystores, provisioning profiles, certificates, service accounts, or tokens are imported or exposed.
5. Run non-publishing build/test/analyze validation when available and safe.
6. Collect security, test, accessibility, performance, and code-review evidence.
7. Produce blockers and human action list for real signing/submission outside the agent.

## Validation Gates

- No publishing, upload, submission, deployment, distribution, or spending occurs.
- No real credentials are used or imported.
- Signing prerequisites are documented without secret values.
- Non-publishing validations are evidenced or unavailable.

## Failures And Stop Conditions

Stop immediately for real signing credentials, upload/submission/publish/deploy/distribute/spend requests, production external writes, destructive commands, missing human approval, or exposed secrets.

## Evidence And Outputs

Output release readiness checklist, changed files if any, validations run, results, blockers, human action list, unsupported omissions, and residual risk.

Acceptance criteria: release readiness is accurately documented, validations are evidenced, blockers are explicit, and all real release actions remain human-controlled.

Human approvals: required for version changes, signing prerequisites, credentials, store metadata, uploads, submissions, publication, deployment, distribution, and financial actions.

Prohibited actions: publishing, uploading, submitting, distributing, deploying, signing with real credentials, importing credentials, spending money, destructive commands, and self-review.
