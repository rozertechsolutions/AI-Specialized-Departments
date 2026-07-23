---
name: "audit-mobile-security"
description: "Audit mobile authentication, authorization, storage, network security, privacy, permissions, crypto, WebViews, deep links, logging, telemetry, dependencies, and secrets."
---
# Audit Mobile Security

Use this skill for security review, privacy review, secret detection, permission review, dependency risk, secure storage review, WebView/deep link review, or pre-release security checks.

## Workflow Definition

Objective: identify security and privacy risks without making unauthorized changes.

Trigger: explicit audit request, sensitive feature change, release readiness, dependency change, network/API integration, permissions/entitlements change, or suspected secret exposure.

Inputs: changed files, manifests, entitlements, dependency files, network/storage/auth code, logs, telemetry, privacy declarations, build config, and validation evidence.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, and React Native.

Preconditions:

- Remain read-only unless the user explicitly authorizes edits.
- Distinguish genuine secrets from public mobile client configuration.
- Ask approval before changing auth, privacy, dependencies, lockfiles, signing, manifests, entitlements, network security, deep links, WebViews, analytics, telemetry, or credentials.

Primary owner: `mobile-security-reviewer`.

Reviewers: matching platform engineer for remediation, `mobile-test-engineer` for security tests, and `mobile-code-reviewer` for final review.

## Steps

1. Identify affected platform(s), sensitive data, trust boundaries, and entry points.
2. Inspect credentials, config, storage, network, auth, permissions, entitlements, WebViews, deep links, logging, telemetry, and dependencies.
3. Check for path traversal, command injection, unsafe deserialization, insecure transport, sensitive logging, weak crypto, overbroad permissions, and privacy gaps where applicable.
4. Classify findings by severity with file references and exploit/misuse scenario.
5. Recommend minimal remediation and required human approvals.
6. Request implementation only through the owning engineer.
7. Verify fixes and tests when remediation is performed.

## Validation Gates

- Findings are evidence-backed.
- No secrets are exposed in reports.
- Required human approvals are explicit.
- Read-only review is preserved unless scope changes.

## Failures And Stop Conditions

Stop for credential handling, private data exposure risk, missing approval, production external services, destructive commands, request to weaken security, signing/upload/publishing, or cost.

## Evidence And Outputs

Output findings, severity, affected files, evidence summary, recommended fixes, required approvals, unavailable checks, and residual risk.

Acceptance criteria: risk is clearly classified, no secrets are revealed, and remediation path is scoped.

Human approvals: required for all security/privacy/auth/dependency/lockfile/permission/entitlement/network/deep-link/WebView/telemetry/signing changes.

Prohibited actions: exposing secrets, editing by default, weakening controls, importing credentials, publishing, signing, deployment, destructive commands, and self-review.
