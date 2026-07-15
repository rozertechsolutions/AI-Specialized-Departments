---
name: prepare-mobile-release
description: Manually prepares Android, iOS, KMP, Flutter, or React Native release readiness by validating versioning, build configuration, evidence, reviews, signing prerequisites, and store-package requirements without signing, publishing, uploading, distributing, or submitting.
---

# Prepare Mobile Release

## Objective and trigger

Assess and prepare a mobile release package for final human review without
performing any real signing, credential use, publication, upload, deployment,
distribution, or store submission. This Skill is manual-only: activate only when
the user explicitly requests release preparation. Never trigger automatically.

Activation does not grant tools. Use only project-allowed read/write tools and
approved local non-signing validation commands; do not use MCP or vendor APIs.

## Inputs

- Intended platforms/channel, release scope, version/build identifiers, variants,
  flavors/schemes, supported OS/device matrix, and target date.
- Approved changelog/release notes source and compatibility/migration statements.
- Compilation, test, lint/static, security, accessibility, performance, and final
  code-review evidence for the exact candidate.
- Documented signing/store prerequisites without credentials, keys, profiles,
  certificates, service accounts, or private values.

## Preconditions and ownership

Inspect instructions, repository status/diff, version sources, build configuration,
manifests/entitlements/privacy declarations, dependencies/locks, changelog, and
all supplied evidence. Confirm candidate scope is stable and no unrelated changes
are included.

`mobile-release-engineer` is primary owner. Platform engineers own their build
configuration and explain native constraints. Test/security/UI/performance/code
reviewers provide independent evidence; none may be substituted by release review.
The human user is the sole release approver and operator of sensitive actions.

## Workflow and gates

1. **Manual scope gate:** confirm explicit user initiation, exact candidate,
   platforms/channel, versions/builds, variants/schemes/flavors, and exclusions.
2. **Version/config gate:** verify authoritative version sources, monotonic build
   numbers, application IDs/bundle IDs, deployment targets, build modes, feature
   flags, endpoints, manifests, entitlements, permissions, privacy declarations,
   dependencies/locks, and reproducibility. Never invent a missing version.
3. **Evidence gate:** require candidate-specific compile, configured unit/
   integration/UI/snapshot/E2E, lint/static/format, dependency, secret/security,
   accessibility/localization/adaptive, performance/resource, offline/recovery,
   warnings/regression, and independent-review evidence as classified.
4. **Readiness-edit gate:** make only explicitly requested, assigned version/build/
   changelog documentation changes. No credential, team, profile, certificate,
   signing, publishing, or external-service configuration.
5. **Non-sensitive validation gate:** run only approved local non-publishing and
   non-signing checks. Use unsigned/debug/build-for-testing validation where the
   project supports it. Hook guards may deny archive/release/sign/upload actions;
   do not bypass them.
6. **Store/package gate:** verify metadata and package prerequisites from local
   configuration and documented policies. Do not create a signed/distributable
   artifact or contact any vendor/store API.
7. **Review gate:** obtain final candidate-specific security, accessibility,
   performance where required, test, platform, and independent code-review status.
   Any unresolved blocker yields `not_ready`.
8. **Human handoff gate:** provide reproducible steps, signing prerequisites,
   blockers/risks, rollback, artifact expectations, and a clearly separated list
   of human-only signing/upload/submission actions. Do not execute them.

## Completion classification

Classify requirements/scope; version/build configuration; compilation; unit/
integration/UI/snapshot/E2E tests; lint/static/formatting; dependencies/locks;
security/secrets/privacy; accessibility/localization/adaptive UI; performance/
memory/battery/network/storage/offline; all UI/recovery states; documentation/
changelog; warnings; regressions; independent review; signing prerequisites;
store metadata; and platform-native release checks as `required`,
`conditionally-required`, or `not-applicable`, each with exact evidence/reason.

## Errors and stop conditions

Stop for non-manual invocation, ambiguous candidate/version, unrelated changes,
missing required evidence, unresolved findings/warnings, credentials or signing
material, dependency changes, authentication, external writes/costs, archive/
export/upload/publish/deploy/submit commands, destructive actions, or failures.

## Outputs, evidence, and acceptance

Return `ready_for_human_release_review`, `not_ready`, or `blocked`; exact candidate
scope; versions/configuration; files changed; full evidence/completion ledger;
commands/results; warnings/findings/accepted risks; signing/store prerequisites;
reproducibility/rollback; and human-only actions.

Acceptance means only that all applicable non-sensitive preparation and evidence
gates passed for human review. It never means signed, distributed, published, or
submitted. Final approval and sensitive execution remain human.

## Human review and prohibited actions

Never authenticate, import/generate/use credentials, keys, certificates, profiles,
or service accounts; invoke Fastlane release lanes, Gradle publishing/release,
Xcode archive/export/signing, Flutter release upload, npm/pub publication, vendor
CLIs, store APIs, artifact uploads, deployment, distribution, submission, or Git
writes. Never bypass hooks or label unavailable checks as passed.
