---
name: create-mobile-project
description: Create or scaffold a mobile project for Android, iOS, KMP, Flutter, or React Native using only current stable native capabilities and explicit approvals.
---

# create-mobile-project

Objective: create the smallest valid mobile project structure requested by the user.

Trigger: an explicit request to create or scaffold a new mobile project.

Inputs: target technology, app name, package or bundle identifier, supported platforms, minimum OS versions, UI approach, required integrations, and acceptance criteria.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: verify target technology and installed tooling; inspect destination; require user-provided identifiers; obtain approval for dependencies, SDK downloads, templates that execute network access, signing, external services, or generated files outside scope.

Primary owner: `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer` by requested technology; `mobile-architect` when multiple runtimes or module boundaries are involved.

Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, `mobile-ui-accessibility-reviewer` for UI, and `mobile-code-reviewer`.

Ordered steps:

1. Confirm target technology and missing identifiers.
2. Classify criteria as `required`, `conditionally-required`, or `not-applicable`.
3. Detect installed tools and official scaffold mechanism without installing anything.
4. Inspect destination for conflicts or user changes.
5. Create only approved native project files.
6. Configure no secrets, real endpoints, signing credentials, active MCP, publishing, or deployment.
7. Discover validation commands from generated files.
8. Run safe local validation where available.
9. Collect independent review.

Conditional steps: if tooling is missing, stop with exact blocker; if identifiers are missing, ask; if network/dependency installation is required, obtain approval first.

Validation gates: project configuration, dependency resolution when local and safe, non-publishing compile/build, tests created by the scaffold, lint/analyze/typecheck where configured, secret scan, security review, accessibility baseline, and final code review.

Failures: missing required identifiers, unavailable tooling, conflicting destination, generated signing material, external integration activation, validation failure, or unapproved dependency/network action.

Stop conditions: real credentials, signing, publishing, upload, deployment, production external writes, destructive commands, paid services, or out-of-scope files.

Evidence: detected tools, official scaffold path, files created, commands run, outputs, unavailable checks, and criteria classification.

Outputs: project files, validation report, review findings, and required human next actions.

Acceptance criteria: scaffold matches request, uses stable native project format, validates where available, and contains no fabricated data or prohibited activation.

Human approvals: dependencies, lockfiles, SDK installs, identifiers when not provided, permissions, privacy, signing, external writes, publishing, deployment, financial actions.

Prohibited actions: invented identifiers, secrets, signing, publishing, uploading, deployment, paid actions, destructive commands, unsupported simulated project formats.
