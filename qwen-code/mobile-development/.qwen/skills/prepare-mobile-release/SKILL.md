---
name: prepare-mobile-release
description: Manually prepare mobile release readiness by validating versioning, build configuration, changelog, tests, analysis, security, accessibility, performance, signing prerequisites, and store-package requirements without signing or publishing.
user-invocable: true
disable-model-invocation: true
---

# Prepare Mobile Release

## Objective

Produce reproducible evidence that explicitly selected mobile builds are ready for human-controlled signing and submission, or report precise blockers. Never perform a release action.

## Trigger

Manual invocation only. The user must explicitly request release preparation and identify the intended version/build and platforms. Never infer this workflow from ordinary feature or build work.

## Inputs

- Approved release version/build identifiers, platforms, targets, variants/schemes/flavors, stores/channels, and release scope.
- Changelog/release-note source, compatibility and migration requirements, and required quality evidence.
- Human-owned signing and store prerequisites by type only; never values or file contents.

## Preconditions

- Read instructions, status/diff, version sources, build/release configuration, dependency locks, manifests/entitlements/privacy declarations, changelog, CI, signing references, and existing release documentation.
- Confirm implementation is complete and the working scope is understood. Do not discard or include unrelated changes.
- Confirm every external, signing, upload, store, tag, and publication action remains human-owned.

## Ownership

- Primary owner: `mobile-release-engineer`.
- Platform owners supply build evidence; test, security, accessibility, performance, and code reviewers supply independent decisions.
- No role may substitute for missing human signing/submission approval.

## Tool and permission boundary

Use read/search and existing local non-publishing commands under normal approval. Edit only explicitly approved version/changelog/release-configuration paths. No MCP, credentials, signing asset reads, archive export, notarization, upload, submission, release/tag creation, deployment, or external write.

## Sequence and gates

1. **Authorization gate:** Confirm manual user request, version/build identifiers, platforms/variants/schemes/flavors, stores/channels, approved file scope, and explicit prohibition on external release actions.
2. **Version/configuration gate:** Verify every version source, identifier, OS baseline, build setting, environment/endpoint selection, feature flag, manifest/entitlement/permission/privacy declaration, and release note is consistent. Do not infer a missing version.
3. **Dependency/reproducibility gate:** Verify lockfiles, checksums where present, generated artifacts, toolchain requirements, and dependency changes. No unapproved floating/new dependency or secret/machine-specific path may remain.
4. **Quality-evidence gate:** Collect exact required compilation/build-for-testing, unit/integration/UI/snapshot/E2E, static analysis/lint/type/format, warning, and regression evidence for the real platforms. Unavailable infrastructure remains a blocker or explicit human decision, never a pass.
5. **Security/privacy gate:** Require secret scan, permission/entitlement/network/storage/logging/privacy review, dependency risk review, and no unresolved high/critical security finding.
6. **Accessibility/localization gate:** Require applicable adaptive layout, complete state, text scale, focus/traversal, screen-reader, locale/RTL, resource, and manual-device evidence or explicit blocker.
7. **Performance gate:** Require project-defined startup/rendering/memory/battery/network/storage/size evidence when release criteria or changes make it applicable. Do not invent thresholds.
8. **Non-publishing build gate:** Run only discovered safe compilation, build-for-testing, unsigned, or signing-disabled validation. Stop before archive export or any command that signs, notarizes, uploads, submits, distributes, deploys, tags, or publishes.
9. **Independent review gate:** Require final test, security, accessibility, performance (when applicable), and code-review decisions. Any correction invalidates prior conclusions; repeat all gates and reviews.
10. **Human handoff gate:** Classify every `QWEN.md` criterion, list blockers and exact human-owned signing/store steps, and decide only `blocked` or `ready for human-controlled signing/submission`.

## Errors and stop conditions

Stop on missing manual authorization/version, dirty ambiguous scope, version mismatch, unapproved dependency, secret/signing material, real signing requirement, external connection/write, failed or missing required check, unexplained warning, privacy/permission inconsistency, non-reproducible build, or unresolved review blocker.

## Outputs and evidence

- Release scope/version/platform matrix and exact files changed.
- Readiness matrix covering configuration, dependencies, builds, all test levels, analysis, warnings, security, accessibility/localization, performance, documentation, signing prerequisites, and independent review.
- Exact safe commands, exit codes, configurations/targets, and observed results.
- Completion ledger, blockers, unavailable evidence, residual risks, and human steps.

## Acceptance criteria

- Version/configuration/changelog and required package prerequisites are consistent and reviewed.
- All locally available required non-publishing checks pass without unexplained warning; unavailable required evidence is not hidden.
- No secret, real signing asset, production write, or unresolved high/critical finding exists in scope.
- The only possible positive decision is `ready for human-controlled signing/submission`; it is not proof of release.

## Human review requirements

Humans approve version, release notes, risk acceptance, credentials/signing assets, store metadata, legal/privacy declarations, final real-device acceptance, signing, notarization, tags/releases, upload, submission, distribution, deployment, and publication.

## Prohibited actions

Never generate/read/use real signing credentials, archive/export for distribution, sign, notarize, upload, submit, publish, deploy, distribute, create a tag/release, change production services, contact stores, bypass checks, or report `released`.
