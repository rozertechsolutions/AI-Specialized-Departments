---
name: prepare-mobile-release
description: Prepare a mobile release checklist and unsigned validation without signing, publishing, uploading, submitting, or distributing.
---

# Prepare Mobile Release

## Objective

Prepare release readiness evidence without using real signing credentials or publishing channels.

## Trigger

Use only when the user manually asks to prepare a mobile release.

## Inputs

Target platform, release version, variant/flavor/scheme, changelog requirements, store readiness criteria, signing prerequisites, and validation scope.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native.

## Preconditions

Inspect versioning, variants/flavors/schemes, build scripts, changelog conventions, release docs, permissions, privacy files, signing configuration, and current changes. Never import or use real credentials.

## Primary Owner

`mobile-release-engineer`.

## Reviewers

`mobile-security-reviewer`, `mobile-test-engineer`, `mobile-ui-accessibility-reviewer` when UI changed, `mobile-performance-reviewer` when performance-sensitive, and `mobile-code-reviewer`.

## Steps

1. Confirm manual release-preparation request and target.
2. Identify release configuration, versioning, variants, schemes, flavors, and unsigned validation commands.
3. Check signing prerequisites without accessing secrets.
4. Run non-publishing, unsigned, simulator-safe, or build-for-testing validation where available.
5. Verify tests, lint, static analysis, privacy, permissions, localization, accessibility, and release notes as applicable.
6. Produce a release readiness report with blockers and human-only actions.

## Conditional Steps

- If signing credentials are required, stop and list the human-owned prerequisite without accessing them.
- If store metadata, screenshots, symbols, or source maps are requested, prepare checks only and do not upload.
- If release validation needs a long, paid, production-connected, or destructive action, ask before running it.
- If versioning or changelog conventions are missing, report the decision required.

## Validation Gates

Required: project config, versioning, unsigned build/build-for-testing where available, relevant tests, lint/static analysis/formatting, dependency consistency, secret review, security review, and code review. Conditional: store metadata, screenshots, accessibility, localization, performance, crash reporting, symbol/source map preparation checks without upload.

## Failures and Stop Conditions

Stop before signing, publishing, uploading, submitting, distributing, spending money, importing credentials, modifying credentials, production service writes, destructive commands, or unavailable required tools.

## Evidence

Record versions, variants, commands, outputs, blockers, omitted publishing/signing steps, and required human actions.

## Outputs

Release readiness report, unsigned artifacts only if produced by safe local commands, validation evidence, and blocker list.

## Acceptance Criteria

Release preparation is complete only when required non-publishing validation passes or blockers are explicit, and all signing/publication actions remain human-owned.

## Human Approvals

Required for any signing, credential use, publishing, upload, submission, deployment, distribution, paid service, release tag, branch, commit, or external write.

## Prohibited Actions

Do not sign, publish, upload, submit, distribute, deploy, spend money, use real signing credentials, erase devices/simulators, or claim store readiness without evidence.
