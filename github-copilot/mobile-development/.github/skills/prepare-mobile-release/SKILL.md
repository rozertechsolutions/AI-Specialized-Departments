---
name: prepare-mobile-release
description: Manually prepares mobile release readiness by validating versioning, build configuration, changelog, tests, static analysis, security, accessibility, performance, signing prerequisites, store-package readiness, and final human approval without signing or publishing.
---

# Prepare a mobile release

## Objective

Produce a complete release-readiness decision and, when explicitly requested, safe repository-local version/configuration updates, while stopping before real credentials, signing, archives for distribution, uploads, submissions, deployments, or publication.

## Trigger

This Skill is manual-only. Use only when the user explicitly requests release preparation or a release-readiness assessment. Never infer it from a release branch, version file, or build failure.

## Inputs

- candidate version/build numbers, target platforms, variants/flavors/schemes, package identifiers, and release scope;
- changelog/release-note requirements and approved issue/change list;
- supported OS/devices, rollout/rollback expectations, and store metadata requirements;
- required build/test/static/security/accessibility/performance evidence;
- documented signing and store prerequisites without secret values;
- human approvers and acceptable residual risks.

## Preconditions

- Invoke `mobile-release-engineer` explicitly.
- Read applicable instructions, release documentation, versions, build configuration, dependency locks, CI definitions, changelog, permissions/entitlements/privacy declarations, store metadata files, tests, and current changes.
- Confirm that every planned command is local, non-publishing, non-distributing, and cannot use real signing credentials. Prefer explicit no-signing/unsigned options.
- Do not access signing assets, credentials, private store data, or production services.

## Ownership

Primary owner: `mobile-release-engineer`. Technology owners fix platform code/configuration; test, security, UI/accessibility, performance, and code reviewers supply independent gates. Final approval belongs to an authorized human.

## Sequence and intermediate gates

1. **Initiation gate:** record the user's explicit request, scope, candidate identifiers, target platforms, release exclusions, approvers, and stop-before-publication boundary.
2. Verify version/build-number consistency, variant/flavor/scheme mapping, package/bundle IDs, deployment targets, environment separation, dependency locks, generated-code state, and reproducibility prerequisites.
3. Trace the candidate change list to changelog/release notes, migrations, compatibility statements, known issues, rollback, support, and user/privacy disclosures.
4. Review permissions, entitlements, privacy manifests/declarations, network policy, debug flags, logging, telemetry, symbols/mappings, and store metadata readiness.
5. Apply only explicitly requested non-secret repository-local version or release-configuration edits. Do not enable publication or signing.
6. **Quality gate:** run discovered compile/type/static checks and required tests in safe modes. Build only unsigned/non-publishing artifacts when the toolchain makes that guarantee. Record exact configurations and output.
7. **Review gate:** obtain current security, accessibility, performance, test, and independent code-review results. Failed, unavailable, stale, or out-of-scope evidence is not a pass.
8. Verify signing prerequisites as documentation only: required certificate/profile/keystore type, responsible human/team, secure system, and future manual step. Never inspect or create the material.
9. Verify store-package readiness as a checklist only: metadata, privacy, assets, identifiers, symbols, notices, and human-owned submission steps. Do not create or upload a signed distributable.
10. **Readiness gate:** classify every criterion as passed, failed, unavailable, or not applicable with evidence. Any failed/unavailable required item produces `not ready`.
11. Stop and request final human approval. Do not proceed into signing, upload, submission, distribution, deployment, promotion, or publication even after approval within this Skill.

## Errors and stop conditions

- Abort a command if it can archive for distribution, sign, notarize, upload symbols/artifacts, submit, publish, promote, deploy, or change remote state.
- Stop if a required build mode cannot be guaranteed unsigned or if credentials/signing materials are present in the intended path.
- Do not bypass failed quality gates, change store records, or mark unavailable evidence passed.
- An unresolved high-risk security finding, accessibility blocker, failed test/build, version inconsistency, or missing human approver blocks readiness.

## Completion classification

Classify every coordinator criterion. Scope, configuration, applicable unsigned compilation, required tests, static checks, dependency resolution/locks, security/secret review, accessibility/localization, performance evidence, documentation/changelog, warnings, regression status, and independent review are normally required. UI test levels, adaptive/offline/recovery behavior, storage/network/battery domains, and artifacts are conditionally required according to the candidate's supported behavior; state concrete reasons.

## Outputs and evidence

Return changed files, candidate version/configuration, change trace, exact safe commands/results, complete gate matrix, reproducibility and unsigned-artifact status, signing/store prerequisites as documentation only, blockers, reviewer status, completion-classification table, and the required final human decision.

## Acceptance criteria

- Every required readiness item has current, candidate-specific evidence.
- Versioning/configuration/changelog are consistent and contain no secrets or active publication setup.
- Any produced artifact is explicitly unsigned and non-publishing; otherwise no artifact is produced.
- The result is `ready for human-controlled signing/submission` or `not ready`, never `released`.

## Human review requirements

An authorized human confirms scope, version, changelog, permissions/privacy, all risk gates, secure signing environment, store metadata, and final readiness. Signing and submission are separate human-controlled processes outside this Skill.

## Prohibited actions

Never access/create/import credentials or signing material; archive/export for distribution; sign, notarize, upload, submit, publish, deploy, distribute, promote, create remote releases/tags, configure active external integrations, bypass gates, or claim release completion.
