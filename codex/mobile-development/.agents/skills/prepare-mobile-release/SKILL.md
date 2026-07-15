---
name: prepare-mobile-release
description: Prepare Android, iOS, KMP, Flutter, or React Native release metadata and readiness evidence without signing, archiving for distribution, publishing, deploying, tagging, committing, or uploading artifacts.
---

# Prepare Mobile Release

## Objective

Produce a reviewable release-ready state and checklist using approved version metadata and verified quality gates, while leaving all signing, publication, deployment, authenticated Git, and distribution actions to humans outside this workflow.

## Required inputs

- Target platform(s), product/flavor/scheme, release scope, and base revision.
- Explicitly approved marketing version and build/version code for every target.
- Release-note/changelog format and audience.
- Required quality gates and supported OS/device matrix.
- Existing documented release process and known issues.

Never infer version numbers, signing identity, store account, release channel, or submission metadata.

## Preconditions

1. Read instructions and release documentation; inspect status/diff, version sources, manifests, lockfiles, CI/release files, and recent read-only history.
2. Confirm feature work is complete and the release scope contains no unexplained/unrelated changes.
3. Confirm no command under consideration can sign, archive/export for distribution, publish, deploy, upload symbols/source maps/artifacts, create releases/tags, or use credentials.
4. Classify every release gate as required, conditional, or not applicable with a reason.
5. Stop if approved version values or the safe unsigned validation path are missing.

## Agent ownership

`mobile-release-engineer` owns approved version metadata, release documentation, and readiness synthesis. Platform owners provide implementation/build evidence but do not publish. `mobile-test-engineer` supplies test results. `mobile-security-reviewer`, `mobile-ui-accessibility-reviewer`, and `mobile-performance-reviewer` provide required risk-based reviews. `mobile-code-reviewer` performs final diff review. The coordinator controls sequence and human decisions.

## Execution

1. **Freeze scope.** Record included changes, excluded work, known issues, target matrix, version values, and required gates. Do not mutate Git state.
2. **Version consistency.** `mobile-release-engineer` updates only explicitly approved version/build metadata and synchronized documentation. Do not touch signing/provisioning/store credentials.
3. **Release notes.** Generate notes only from verified scoped changes and project convention. Separate user-visible changes, fixes, migrations, and known issues; do not invent claims.
4. **Configuration gate.** Validate manifests, lockfiles, environment selection, debug flags, permissions/entitlements/privacy files, and release configuration references. Sensitive changes require human review.
5. **Static/build gates.** Run configuration, formatting, lint, type, static analysis, and compilation only through commands proven not to sign or publish. Use simulator-safe/unsigned paths. If the project cannot produce relevant evidence without signing, mark that gate blocked for human execution.
6. **Test gates.** Collect required unit, integration, UI, and platform test results from `mobile-test-engineer`; run reasonable safe local suites. Do not use production services or credentials.
7. **Specialist gates.** Require security for sensitive/network/storage/auth/release changes, UI/accessibility for user-interface changes, and performance for material performance-sensitive changes. Failed required findings block readiness.
8. **Code review.** `mobile-code-reviewer` reviews the release diff and unresolved warnings/test gaps.
9. **Reproducibility and documentation.** Record tool versions, exact safe commands, expected human-only signing/submission inputs without values, rollback notes, and remaining manual checks.
10. **Final release gate.** Review the complete diff/status. Mark `ready for human signing/submission` only when all non-signing required gates pass and no unresolved high-impact issue remains. This is not approval to sign or publish.

## Error handling and stop conditions

Stop on unapproved/mismatched versions, dirty or ambiguous scope, failed required checks, unavailable safe unsigned validation, signing/provisioning access, credentials, store/production access, dependency changes, destructive commands, or any publication/upload action. Report the exact blocked gate and human action; never bypass it.

## Outputs

- Version and release-documentation files changed.
- Release scope and notes.
- Required/conditional/not-applicable gate matrix with exact results.
- Specialist/code-review findings and known issues.
- Reproducible safe commands and explicit human-only remaining steps.
- Confirmation that no signing, upload, publication, deployment, tag, commit, push, or release creation occurred.

## Acceptance criteria

- Approved versions are consistent across all relevant sources.
- Release notes accurately reflect verified scope.
- Every non-signing required configuration/static/build/test/review gate passes.
- No secret/signing material or unrelated file changed and no unexplained warning remains.
- Signing and distribution remain unperformed and clearly human-only.

## Prohibited actions

Do not sign, archive/export for distribution, build release artifacts that may sign, notarize, upload symbols/source maps/binaries, publish/deploy/submit, create Git tags/commits/pushes/GitHub releases, access credentials/store accounts, change dependencies, or declare readiness with a failed required gate.
