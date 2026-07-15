---
name: audit-mobile-security
description: Audit mobile security and privacy across authentication, secure storage, networking, permissions, cryptography, WebViews, deep links, telemetry, and dependencies.
---

# audit-mobile-security

Objective: perform a read-only mobile security/privacy audit and report actionable findings.

Trigger: request for security audit, privacy review, dependency risk review, release security check, or sensitive feature review.

Inputs: audit scope, changed files, manifests, entitlements, network security config, dependency files, auth/storage/crypto/WebView/deep-link/telemetry code, validation evidence.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: remain read-only by default; inspect relevant files; protect secrets; do not connect external scanners or services without approval.

Primary owner: `mobile-security-reviewer`.

Reviewers: `mobile-code-reviewer`; implementation owners remediate through separate workflow.

Ordered steps:

1. Define audit scope and affected platforms.
2. Classify criteria.
3. Inspect secrets, permissions, entitlements, network security, secure storage, auth, crypto, WebViews, deep links, logging, telemetry, and dependencies.
4. Run safe local secret/config checks where available.
5. Report findings with severity, evidence, impact, and remediation.
6. Identify human approvals and blockers.

Conditional steps: stop immediately on discovered real secret or credential; request approval before any external scanning or remediation edits.

Validation gates: secret scan, configuration review, dependency risk review where local metadata exists, privacy/permission review, final code review of audit report.

Failures: inaccessible scope, real secret, missing evidence, external service requirement, or unsupported technology.

Stop conditions: credential exposure, production data, auth/privacy/security change requiring approval, external writes, signing/publishing/upload/deployment, destructive commands.

Evidence: files inspected, checks run, findings, unavailable infrastructure, criteria classification.

Outputs: audit report, prioritized findings, approval requirements, remediation owners.

Acceptance criteria: findings are evidence-backed, no source is modified by default, and no secret is exposed in the report.

Human approvals: remediation edits, external scanners, dependencies, permissions, entitlements, privacy, auth, telemetry, credentials, release.

Prohibited actions: source edits by default, exposing secrets, enabling MCP/external services, publication, signing, uploading, deployment.
