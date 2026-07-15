---
name: audit-mobile-security
description: Perform a read-only mobile security and privacy audit with evidence, severity, and safe remediation guidance.
---

# Audit Mobile Security

## Objective

Assess mobile security and privacy risks without modifying code unless the user separately approves remediation.

## Trigger

Use when the user asks for a security audit or when changes touch auth, authorization, secure storage, network security, privacy, permissions, crypto, WebViews, deep links, logs, telemetry, or dependencies.

## Inputs

Audit scope, platform, threat model if available, changed files, manifests, dependency files, storage/network/auth code, and privacy requirements.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native.

## Preconditions

Inspect relevant files read-only. Do not access secrets unless explicitly authorized and necessary. Do not run external scanners that upload code or data.

## Primary Owner

`mobile-security-reviewer`.

## Reviewers

`mobile-code-reviewer`; platform owner for implementation feasibility.

## Steps

1. Define audit boundary and assets.
2. Inspect permissions, entitlements, manifests, exported components, deep links, WebViews, auth, storage, crypto, transport security, logging, telemetry, and dependencies.
3. Distinguish genuine secrets from public mobile client configuration.
4. Classify findings by severity, exploitability, evidence, and affected files.
5. Recommend scoped remediation and validation.
6. Identify required human approvals.

## Conditional Steps

- If dependency advisory tooling is configured and safe, run it without uploading source.
- If suspected secrets are found, stop and avoid printing sensitive values.
- If a finding depends on platform policy, verify it against official platform documentation.
- If remediation is requested later, route implementation to the relevant platform owner and keep this role as reviewer.

## Validation Gates

Required: read-only inspection, file references, secret-risk assessment, no credential exposure, no external upload, and severity ordering. Conditional: dependency advisory checks, manifest lint, privacy declaration checks, and platform-specific static analysis when configured and safe.

## Failures and Stop Conditions

Stop for unclear authorization, sensitive files outside scope, production credentials, required external uploads, or destructive commands.

## Evidence

Record inspected files, commands if any, findings, false positives, official docs consulted, and remediation validation plan.

## Outputs

Security findings, required approvals, remediation plan, and residual risks.

## Acceptance Criteria

Findings are evidence-based, no secrets are exposed, and recommendations are scoped and actionable.

## Human Approvals

Required before changing auth, authorization, cryptography, secure storage, permissions, entitlements, privacy manifests, telemetry, dependencies, lockfiles, network security, WebViews, deep links, or exported components.

## Prohibited Actions

Do not modify code in audit mode, reveal secrets, upload source, use production credentials, weaken controls, sign, publish, upload artifacts, deploy, or spend money.
