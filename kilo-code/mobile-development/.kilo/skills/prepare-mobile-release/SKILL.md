---
name: prepare-mobile-release
description: Use only when the user manually asks to prepare a mobile release readiness checklist or non-publishing validation; never publish, upload, submit, deploy, distribute, spend money, or sign with real credentials.
---

# prepare-mobile-release

- Objective: Prepare release readiness through versioning, variants/flavors/schemes, reproducibility, package-readiness checks, signing prerequisites, store-readiness, and non-publishing validation.
- Trigger: Manual user request to prepare a mobile release. Do not auto-trigger.
- Inputs: Target platform, release version/build number, flavor/variant/scheme, changelog inputs, test evidence, signing prerequisites, and store-readiness requirements.
- Supported technologies: Android, iOS, KMP libraries only for package readiness, Flutter, React Native.
- Preconditions: Confirm manual initiation, inspect release configuration, verify no real signing credentials or publishing actions are needed, and ask before version/build config edits.
- Primary owner: `mobile-release-engineer`.
- Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, platform owner, and `mobile-code-reviewer`.
- Steps: Inspect release files; confirm versioning and target variants; check signing prerequisites without using credentials; run non-publishing validation if available; compile release checklist; record blockers; request security/test/final review.
- Validation gates: No publishing/upload/submission/deployment/distribution/signing/spending, no credential import, non-publishing build/test/lint evidence, and explicit human approval gates.
- Failures: Stop on credential requirement, publishing/signing request, paid action, validation failure, or unavailable release infrastructure.
- Stop conditions: Any request to publish, upload, submit, deploy, distribute, sign with real credentials, spend money, or run destructive commands.
- Evidence: Files reviewed/changed, commands discovered/run, release checklist, signing absence confirmation, and unavailable infrastructure.
- Outputs: Release-readiness report, approved version/config edits if any, non-publishing validation evidence, blockers, and manual next steps.
- Acceptance criteria: Release is prepared but not distributed, all gates are explicit, and independent reviews are complete.
- Human approvals: Required for every release decision, signing prerequisite, credential action, store action, dependency/lockfile change, privacy decision, and external write.
- Prohibited actions: Publishing, uploading, submitting, deploying, distributing, spending money, signing with real credentials, importing credentials, destructive commands, and fabricated release readiness.

