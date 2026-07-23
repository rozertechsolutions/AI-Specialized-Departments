---
name: prepare-mobile-release
description: Manually prepare a mobile release readiness report and unsigned validation for Android, iOS, KMP, Flutter, or React Native without publishing, uploading, submitting, deploying, spending money, or using real signing credentials.
disable-model-invocation: true
---

# prepare-mobile-release

Objective: prepare a release readiness report and safe unsigned validation only.

Trigger: manual user invocation for release preparation. Do not run automatically.

Inputs: target platform, version, changelog, build variant/flavor/scheme, release checklist, store requirements, and validation expectations.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: confirm manual initiation; inspect version/config files and current changes; verify commands are non-publishing and non-signing or use debug/unsigned/simulator-safe paths; stop if real credentials or external uploads are required.

Primary owner: `mobile-release-engineer`.

Reviewers: `mobile-security-reviewer`, `mobile-ui-accessibility-reviewer` for user-facing release changes, `mobile-performance-reviewer` for performance claims, `mobile-test-engineer`, and `mobile-code-reviewer`.

Steps:

1. Inventory release configuration, variants, flavors, schemes, package metadata, signing references, and store-readiness files.
2. Classify criteria including build, tests, lint/static analysis, privacy, accessibility, localization, performance, dependency consistency, and documentation.
3. Discover safe validation commands.
4. Run only non-publishing, unsigned, local checks.
5. Record blockers, warnings, manual actions, and approvals.
6. Hand off independent reviews.

Validation gates: no real credentials, no signing, no publish/upload/submit/deploy/distribute, build/test/static checks when safe, secret scan, release configuration review, and independent review.

Failures: signing required, credentials needed, store submission requested, external upload, paid service, destructive action, missing version policy, validation failure, or unresolved required review.

Stop conditions: real signing material, publication, upload, submission, deployment, distribution, production write, payment, destructive command, or credential import.

Evidence: files inspected, commands discovered/run, unsigned validation output, criteria classification, reviewer findings, and limitations.

Outputs: release-readiness report, blockers, prerequisites, manual approval checklist, and safe command evidence.

Acceptance criteria: release readiness is assessed without irreversible or external action and all required blockers are reported.

Human approvals: signing, store metadata, privacy declarations, distribution, release notes, external uploads, production systems, paid services, and final release decision.

Prohibited actions: publishing, uploading, submitting, deploying, distributing, spending money, importing/using real signing credentials, destructive operations, or final release approval.
