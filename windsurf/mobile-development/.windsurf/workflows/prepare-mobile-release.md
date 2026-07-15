# prepare-mobile-release

Description: Manually prepare a mobile release readiness report without publishing, uploading, submitting, deploying, distributing, spending money, or using real signing credentials.

## Trigger

Invoke manually with `/prepare-mobile-release`.

## Inputs

- Target platform: Android, iOS, KMP, Flutter, React Native, or mixed.
- Release type and version intent.
- Human-approved scope and repository path.
- Existing release documentation, build configuration, changelog, signing prerequisites, and store metadata when present.

## Preconditions

- Human explicitly requested release preparation.
- Current changes inspected and preserved.
- No real signing credentials, private keys, provisioning profiles, keystores, service accounts, or store credentials are imported or used.
- Publishing, upload, submission, deployment, distribution, financial, and destructive actions are out of scope.

## Primary Owner

`mobile-release-engineer`

## Reviewers

`mobile-security-reviewer`, `mobile-test-engineer`, and `mobile-code-reviewer`

## Steps

1. Confirm platform, release target, version intent, and prohibited actions.
2. Inspect project structure and discover release-related commands without running publishing, signing, uploading, deployment, or destructive operations.
3. Review versioning, variants, flavors, schemes, bundle IDs/application IDs, package names, changelog, store metadata, privacy declarations, permissions, entitlements, dependencies, lockfiles, and reproducibility controls.
4. Conditionally run only non-publishing validation commands that are available and safe: build validation, tests, lint, static analysis, type checking, manifest/entitlement inspection, and package dry-run style checks when officially supported.
5. Stop for human approval before any dependency, lockfile, signing, credential, privacy, analytics, telemetry, network security, manifest, entitlement, external write, or store-facing change.
6. Produce a release readiness report with passed checks, failed checks, unavailable infrastructure, required human actions, risks, and explicit non-actions.

## Validation Gates

- No real signing credentials used.
- No external upload, submit, publish, deploy, distribute, or paid action executed.
- Android: Gradle tasks, variants, manifests, permissions, Android lint, unit/instrumented checks when available.
- iOS: workspace/project, schemes, build-for-testing or non-publishing build checks, warnings, tests, entitlements, privacy files when available.
- KMP: targets, source sets, shared/platform tests, `expect`/`actual`, interoperability when available.
- Flutter: `flutter analyze`, tests, non-publishing build validation, flavors, packages, permissions when available.
- React Native: type checking, lint, tests, Metro/package manager, native host checks, bridge review when available.

## Failures And Stop Conditions

Stop on missing scope, missing required approval, secret/signing material exposure, destructive command requirement, validation failure requiring product decision, unavailable critical release infrastructure, or any request to publish/upload/submit/deploy/distribute/spend money.

## Evidence And Outputs

- Commands discovered and commands run.
- Validation outputs summarized without secrets.
- Files inspected or changed.
- Release readiness report.
- Human approval checklist.

## Acceptance Criteria

- Release readiness is documented with concrete evidence.
- Required, conditionally required, and not-applicable checks are classified with reasons.
- No prohibited release action occurred.
