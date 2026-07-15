---
name: prepare-mobile-release
description: Prepare and assess an unsigned, unuploaded mobile release through version, configuration, evidence, signing-prerequisite, package-readiness, and human-approval checks.
when_to_use: Use only when the user explicitly invokes this Skill to assess Android, iOS, KMP, Flutter, React Native, or hybrid release readiness; never invoke automatically.
argument-hint: "[version and target platforms]"
disable-model-invocation: true
model: inherit
---

# Objective

Prepare and report release readiness for `$ARGUMENTS` while leaving every signing, upload, submission, publication, distribution, deployment, credential, and final approval action to a human outside this workflow.

# Required input and supported scope

Require intended version/build number, target apps/platforms, release channel, included changes, supported variants/flavors/schemes/configurations, changelog/store-metadata expectations, and approval to modify version metadata if requested. Confirm this Skill was manually invoked.

# Preconditions and inspection

Read instructions; inspect status/diff, release conventions, version sources, target/variant/scheme/flavor configuration, dependency lockfiles, changelog, CI/release scripts, store metadata, privacy declarations, permissions/entitlements, test/static-analysis reports, specialist reviews, and references to signing prerequisites without opening protected material.

Stop immediately if manual invocation is absent, scope/version is ambiguous, user changes are unexplained, credentials/signing material would be accessed, or any actual release action is requested.

# Ownership

`mobile-release-engineer` is primary. Technology owners validate their targets; `mobile-test-engineer`, `mobile-security-reviewer`, `mobile-ui-accessibility-reviewer`, and `mobile-performance-reviewer` supply applicable evidence; `mobile-code-reviewer` supplies final code review. Only the human user can approve or execute a release.

# Procedure and gates

1. Map version/build sources and confirm requested values are monotonic and consistent across targets. Gate: obtain human approval before edits.
2. Discover variants/flavors/schemes/configurations and intended package identifiers. Verify release configuration without reading credentials.
3. Verify changelog and store/package metadata readiness, privacy declarations, permission/entitlement rationale, dependency locks, and documentation.
4. Build an evidence matrix for compilation/non-signing builds, unit/integration/UI/end-to-end tests, lint, formatting, static analysis, dependency resolution, security, secret scanning, accessibility/localization/adaptive layout, performance/memory/network/offline, and independent review.
5. Mark every criterion `required`, `conditionally-required`, or `not-applicable`; give a concrete reason for each `not-applicable`. Mark unavailable infrastructure `unavailable`, never passed.
6. Run only discovered local non-publishing and non-signing checks necessary to fill missing safe evidence. For Apple builds, disable signing explicitly; for other platforms, stop if release configuration would use a real signing identity/store.
7. Document required certificates, profiles, keys, accounts, and store access by name/purpose only. Never inspect, import, generate, export, or validate real credential contents.
8. Prepare unsigned local package output only when explicitly requested, safe, and supported without credentials; do not upload it.
9. Obtain specialist and independent reviews. Any required failure or unresolved high-risk finding blocks readiness.
10. Produce the checklist and stop for final human decision. Do not execute the decision.

# Failure and stop handling

Required failures, unresolved high-risk findings, inconsistent versions, missing release scope, unavailable mandatory evidence, credential prompts, signing, external writes, uploads, release automation, or store actions are blockers. Report exact remediation and owner; never bypass the gate.

# Evidence and acceptance

Return version/configuration map, changed metadata, checklist with evidence links/commands/results, unsigned artifact paths if any, signing prerequisites, required/conditional/not-applicable/unavailable classifications, review status, blockers, and residual risks.

Preparation is complete only when all required non-release checks pass, evidence is reproducible, artifacts remain unsigned/unuploaded, no secret was accessed, and final human approval is still pending. Readiness is not release execution.

# Human review and prohibited actions

Human approval is mandatory for version changes, release configuration, metadata, signing prerequisites, artifact handling, and the eventual release. Never auto-approve, sign, notarize, publish, upload, submit, distribute, deploy, import credentials, reveal secrets, trigger Fastlane/store/vendor release automation, create a public release/tag, or call external write tools.
