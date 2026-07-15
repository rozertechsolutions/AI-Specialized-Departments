---
name: prepare-mobile-release
description: Manually prepare a mobile release readiness report and unsigned validation without publishing, uploading, submitting, deploying, spending, or using real signing credentials.
---

# prepare-mobile-release

Objective: prepare mobile release readiness with unsigned/local validation and explicit human next steps.

Trigger: manual user request to prepare a release.

Inputs: target platform, version/build number, release notes, variants/flavors/schemes, store checklist, validation expectations, signing prerequisites.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: manual invocation only; inspect release/build files and user changes; verify no real signing credentials are used; obtain approval for version/build config, dependencies, lockfiles, privacy declarations, signing config, or external services.

Primary owner: `mobile-release-engineer`.

Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, `mobile-performance-reviewer` when applicable, and `mobile-code-reviewer`.

Ordered steps:

1. Confirm manual release-prep intent and target platform.
2. Classify criteria and release blockers.
3. Discover variants, flavors, schemes, versions, and safe validation commands.
4. Verify signing/publishing/upload/deployment commands are not run.
5. Run non-publishing build/build-for-testing or dry validation where available.
6. Review privacy, permissions, dependencies, changelog, tests, performance, and security evidence.
7. Produce release readiness report and human action list.

Conditional steps: stop if real signing credentials are required; ask before version/build config edits; do not use store credentials or external release services.

Validation gates: non-publishing build or build-for-testing, tests/static analysis where configured, secret scan, signing credential absence, privacy/security review, performance evidence when relevant, final code review.

Failures: request to publish/upload/submit/deploy/sign, missing required validation, discovered secret/signing material, validation failure, unapproved external service.

Stop conditions: real credentials, signing, publishing, uploading, submitting, distributing, deployment, spending, destructive commands, production external writes.

Evidence: release files inspected, variants/schemes/flavors discovered, commands run, results, blockers, criteria classification.

Outputs: release readiness report, unsigned validation evidence, required human actions, no-publish confirmation.

Acceptance criteria: readiness is honestly classified, blockers are explicit, and no prohibited release action occurred.

Human approvals: version changes, dependencies, lockfiles, privacy declarations, signing config, store metadata, credentials, external services.

Prohibited actions: publishing, uploading, submitting, distributing, deploying, spending money, signing with real credentials, importing credentials, destructive commands.
