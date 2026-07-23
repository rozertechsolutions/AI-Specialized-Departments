---
name: audit-mobile-security
description: Run a read-only mobile security and privacy audit covering credentials, auth, secure storage, network security, permissions, WebViews, deep links, telemetry, and dependency risk.
---

# audit-mobile-security

Objective: produce an evidence-based read-only security audit without modifying source or activating integrations.

Trigger: request for security audit, privacy review, secret scan, dependency risk review, or permission review.

Inputs: audit scope, target platforms, compliance concerns, diff or full project scope, and available validation commands.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: inspect files read-only; avoid sensitive file access unless necessary and authorized; do not authenticate services; distinguish public client config from secrets.

Primary owner: `mobile-security-reviewer`.

Reviewers: `mobile-code-reviewer` for final audit consistency when requested.

Steps:

1. Inventory manifests, entitlements, privacy files, network config, auth paths, storage, WebViews, deep links, logs, telemetry, and dependencies.
2. Classify criteria and unsupported areas.
3. Run local secret/security checks if available and safe.
4. Identify findings with severity, evidence, and remediation options.
5. List approval-required changes separately.

Validation gates: file/path evidence, secret detection, dependency/security tooling when configured, no source edits, no external services, and no fabricated pass.

Failures: sensitive access uncertainty, unavailable audit tooling, external service required, credentials encountered, or unclear scope.

Stop conditions: real credentials, production systems, external writes, dependency modification, signing, publishing, deployment, destructive commands, or source edit request.

Evidence: inspected files, checks run, findings, unavailable infrastructure, and criteria classification.

Outputs: audit report, findings, recommended remediations, and human approval list.

Acceptance criteria: audit is read-only, scoped, evidence-based, and explicit about limitations.

Human approvals: required before any remediation that changes auth, privacy, permissions, cryptography, secure storage, dependencies, lockfiles, telemetry, network security, WebViews, or deep links.

Prohibited actions: editing source, importing credentials, authenticating services, external uploads, signing, publishing, deployment, destructive operations, or approving fixes as implemented.
