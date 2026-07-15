---
name: prepare-mobile-release
description: Workflow for manually initiated mobile release preparation without publishing, uploading, submitting, deploying, distributing, spending money, or signing with real credentials.
---

# Prepare Mobile Release

## Objective

Prepare release readiness evidence while preserving human control over signing, publishing, upload, submission, distribution, deployment, and spending.

## Trigger

Use only when the user explicitly asks to prepare a mobile release.

## Inputs

Target platforms, version, variant/flavor/scheme, release notes source, build commands, signing prerequisites, store requirements, and validation expectations.

## Supported Technologies

Android, iOS, KMP artifacts, Flutter, and React Native host builds.

## Preconditions

Confirm manual initiation, target platform, non-publishing scope, and no real signing credentials are required.

## Primary Owner

`mobile-release-engineer`

## Reviewers

Platform engineers, `mobile-test-engineer`, `mobile-security-reviewer`, `mobile-ui-accessibility-reviewer` for user-facing release risk, `mobile-performance-reviewer` when required, and `mobile-code-reviewer`.

## Steps

1. Discover versioning, variants/flavors/schemes, and release commands.
2. Verify signing prerequisites without reading or using real credentials.
3. Run non-publishing build/build-for-testing validation when available.
4. Run relevant tests, lint, static analysis, and release checks.
5. Review permissions, privacy, entitlements, manifests, telemetry, and dependencies.
6. Compile readiness report with gaps and required human approvals.
7. Complete independent final review.

## Conditional Steps

- Android: validate Gradle assemble/bundle tasks without signing real release credentials.
- iOS: use non-publishing build or build-for-testing and avoid real signing.
- Flutter/RN: validate host builds and package manager checks when configured.
- KMP: validate target compilation and artifact prerequisites without publication.

## Validation Gates

Release checks are local and non-publishing, security review is complete, unavailable infrastructure is reported, and no real credentials are used.

## Failures

Stop on request to publish, upload, submit, distribute, deploy, spend money, import credentials, or sign with real credentials.

## Stop Conditions

Do not continue if release scope is ambiguous or would require prohibited actions.

## Evidence

Commands run, outputs, version/scheme/flavor discovery, security review, signing prerequisite gaps, and unavailable checks.

## Outputs

Release readiness report, validation evidence, and human approval checklist.

## Acceptance Criteria

The release is prepared for human decision-making without any prohibited external or credential action.

## Human Approvals

Always required for any real signing, store, distribution, deployment, publication, upload, submission, or paid action.

## Prohibited Actions

No publishing, uploading, submitting, deploying, distributing, spending money, importing credentials, or signing with real credentials.
