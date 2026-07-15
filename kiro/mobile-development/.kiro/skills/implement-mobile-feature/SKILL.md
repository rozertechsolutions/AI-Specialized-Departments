---
name: implement-mobile-feature
description: Implement a requested mobile feature in an existing Android, iOS, KMP, Flutter, or React Native project.
---

# implement-mobile-feature

Objective: implement the smallest complete feature change within the detected mobile technology and existing architecture.

Trigger: request to add or change user-facing or domain behavior.

Inputs: feature requirements, acceptance criteria, affected platforms, design/API contracts, current files, and validation expectations.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: inspect relevant files and user changes; detect technology from manifests and source layout; identify primary owner; confirm approvals for public API, dependency, privacy/security, telemetry, permissions, or persistent format changes.

Primary owner: selected by deterministic routing in `AGENTS.md`.

Reviewers: `mobile-test-engineer`, `mobile-security-reviewer` when behavior touches security/privacy, `mobile-ui-accessibility-reviewer` for UI, `mobile-performance-reviewer` when performance-sensitive, and `mobile-code-reviewer`.

Ordered steps:

1. Trace requirements to files and owners.
2. Classify completion criteria.
3. Inspect existing conventions for state, navigation, networking, storage, UI, error handling, and tests.
4. Implement only the requested behavior.
5. Add or update focused tests where warranted.
6. Discover and run relevant checks.
7. Correct failures caused by the change.
8. Perform independent review and record gaps.

Conditional steps: request architecture review for cross-module changes; request security review for auth/privacy/network/permissions; request UI review for visual or accessibility changes; request performance review for startup/rendering/background/network/storage effects.

Validation gates: compile/build, targeted tests, static analysis/lint/typecheck/format where configured, security and secret review, accessibility/localization/adaptive review for UI, performance evidence for performance claims, and independent code review.

Failures: ambiguous acceptance criteria, unsupported technology, ownership conflict, missing tooling, validation failure, or out-of-scope requirement.

Stop conditions: dependency/lockfile change without approval, credentials, real endpoints, signing, publishing, production writes, destructive commands, or privacy/security change needing human review.

Evidence: requirement traceability, changed files, commands run, results, unavailable infrastructure, reviewer findings, and criteria classification.

Outputs: implementation, tests or test-gap explanation, validation report, and remaining human actions.

Acceptance criteria: feature meets stated behavior, validation evidence is honest, and no required criterion fails.

Human approvals: dependencies, lockfiles, permissions, entitlements, privacy, auth, telemetry, external writes, signing, release, destructive, or financial actions.

Prohibited actions: unrelated refactors, invented data, broad suppressions, simulated unsupported capabilities, publication, signing, uploading, deployment, or self-review as final review.
