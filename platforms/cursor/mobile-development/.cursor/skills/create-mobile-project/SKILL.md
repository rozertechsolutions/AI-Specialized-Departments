---
name: create-mobile-project
description: Create or scaffold a mobile project when the user explicitly asks for a new Android, iOS, KMP, Flutter, or React Native project.
---

# create-mobile-project

Objective: create a mobile project only with stable native tooling already available in the workspace and only after required identifiers and product decisions are known.

Trigger: explicit request to create, scaffold, initialize, or add a new mobile project.

Inputs: target technology, app name, package name or bundle identifier, minimum OS targets, license expectations, target directory, UI requirements, and approved tooling.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: inspect existing directories; detect installed SDK/tool versions; confirm identifiers are user-provided; verify scaffold command is local and stable; obtain approval for dependency downloads, generated lockfiles, signing config, external services, or non-repository writes.

Primary owner: `mobile-architect` for structure, then `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer` for implementation.

Reviewers: `mobile-security-reviewer`, `mobile-ui-accessibility-reviewer`, `mobile-release-engineer`, and `mobile-code-reviewer` when project creation completes.

Steps:

1. Inspect scope, existing files, and current changes.
2. Classify requested criteria as `required`, `conditionally-required`, or `not-applicable`.
3. Verify the native scaffold mechanism and installed toolchain.
4. Stop for missing identifiers or approvals.
5. Generate only necessary files in the target project path.
6. Remove empty placeholders generated only to preserve a generic tree when safe and approved.
7. Discover validation commands from generated files.
8. Run safe local validation that does not sign, publish, upload, deploy, or use real credentials.
9. Hand off independent review.

Validation gates: project configuration parse, dependency resolution when approved, unsigned compile/build if available, initial tests if generated, lint/analyze when configured, secret scan, and review.

Failures: unsupported scaffold, missing identifiers, dependency download not approved, signing requirement, external integration, validation failure, or out-of-scope file changes.

Stop conditions: credential, production endpoint, publication, signing, deployment, destructive command, payment, or unclear ownership.

Evidence: installed versions, files created, commands discovered/run, unavailable infrastructure, criteria classification, and reviewer findings.

Outputs: project files, validation report, limitations, and human action list.

Acceptance criteria: project is created within scope, uses stable native tooling, contains no secrets, and has evidence for all required criteria.

Human approvals: identifiers, dependencies, lockfiles, external tooling, permissions, entitlements, signing prerequisites, and any non-repository or external action.

Prohibited actions: inventing identifiers, adding active integrations, real signing, publishing, uploading, submitting, deploying, distributing, spending money, or destructive operations.
