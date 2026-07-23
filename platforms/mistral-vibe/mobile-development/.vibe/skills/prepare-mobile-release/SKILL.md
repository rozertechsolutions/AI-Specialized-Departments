---
name: prepare-mobile-release
description: Use only when the user explicitly invokes or requests mobile release preparation with approved version values; never activate automatically and never sign, archive/export, upload, submit, publish, deploy, or mutate Git.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - todo
  - ask_user_question
  - task
  - write_file
  - edit
  - bash
---

# Prepare Mobile Release

## Objective and trigger

Prepare approved version metadata, release documentation, and reproducible non-signing readiness evidence. This Skill must be manually initiated by an explicit user request. If it was inferred without that request, stop without reading release secrets or changing anything.

## Inputs

- Target platform/products, flavor/variant/scheme, base revision and included scope, explicitly approved marketing/build versions, release-note format/audience, supported OS/device matrix, known issues, documented release process, and required gates.

Never infer version numbers, signing identity, store account, channel, credentials, or submission metadata.

## Preconditions and ownership

Inspect instructions, status/diff, release docs, version sources, manifests, lockfiles, build/release configuration, and existing safe unsigned validation. Confirm scope has no unexplained changes and no contemplated command can sign, archive/export for distribution, publish, deploy, upload artifacts/symbols/source maps, authenticate, tag, commit, or push.

`mobile-release-engineer` owns approved metadata/docs and readiness synthesis. The coordinator records each release-metadata file as a non-overlapping release unit; platform owners supply safe build evidence but do not edit the same file concurrently. `mobile-test-engineer` supplies tests; risk reviewers supply required findings; `mobile-code-reviewer` is final. The coordinator owns all human decisions.

## Sequence and gates

1. Manual/scope gate: record explicit request, included/excluded changes, base, products, target matrix, approved version values, known issues, and gate classifications.
2. Version gate: update only approved version/build sources and synchronized docs. Do not touch signing, provisioning, store credentials, dependencies, or unrelated configuration.
3. Release notes: derive user-visible changes, fixes, migrations, and known issues only from verified scope and project convention.
4. Configuration gate: validate manifests, lockfiles, environment selection, debug flags, permissions/entitlements/privacy declarations, and release references. Sensitive changes require human/security review.
5. Static/build gates: run only commands proven unsigned/non-publishing; collect formatting/lint/type/static/compile evidence. Mark signing-dependent gates blocked for human execution.
6. Test gates: collect required unit/integration/UI/platform results without production services or credentials.
7. Specialist gates: security for sensitive/network/storage/auth/release changes; UI/accessibility for UI; performance for performance-sensitive changes; all required findings must be resolved.
8. Independent code review covers the release diff, warnings, test gaps, version/docs consistency, and prohibited side effects.
9. Reproducibility gate: record tool versions, exact safe commands, expected human-only prerequisites without values, rollback, and remaining manual checks.
10. Final human gate: state `ready for human signing/submission` only if every non-signing required gate passed. This is not authority to perform either action.

## Errors and stop conditions

Stop on no explicit request, unapproved/mismatched version, dirty/ambiguous scope, failed required check, missing safe unsigned path, dependencies, credentials, signing/provisioning/store/production access, any upload/publication/deployment/Git command, or unrelated failure.

## Outputs and evidence

Provide files changed, release scope/notes, version consistency, complete required/conditional/not-applicable gate matrix with exact results, specialist/code-review findings, known issues, reproducible safe commands, rollback, human-only steps, blockers, and confirmation no signing/upload/publication/deployment/tag/commit/push occurred.

## Acceptance and human review

Approved versions are consistent; notes match verified scope; every non-signing required configuration/static/build/test/review gate passes; no secret/signing material, unapproved dependency, unrelated file, or unexplained warning remains; and final signing/distribution is explicitly human-only.

## Prohibited actions

Do not sign, archive/export for distribution, build a potentially signed release artifact, notarize, upload symbols/source maps/binaries, publish/deploy/submit, create tags/commits/pushes/releases/PRs, access credentials/store accounts, install dependencies/tools, or declare readiness with a failed required gate.
