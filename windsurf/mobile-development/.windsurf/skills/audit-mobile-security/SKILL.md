---
name: audit-mobile-security
description: Audit mobile authentication, authorization, storage, network, privacy, permissions, cryptography, WebViews, deep links, logs, telemetry, and dependencies.
---

# audit-mobile-security

## Objective

Perform a read-only security and privacy audit with actionable findings and evidence.

## Inputs

Audit scope, target platforms, threat concerns, relevant files, dependency manifests, and requested output format.

## Supported Technologies

Android, iOS, KMP, Flutter, React Native, and mixed mobile repositories.

## Preconditions

- Inspect only approved files and configuration.
- Do not modify production code unless the user explicitly requests a follow-up implementation.
- Protect secrets and do not print sensitive values in reports.

## Primary Owner

`mobile-security-reviewer`

## Reviewers

`mobile-code-reviewer`; add technology owners for platform-specific verification.

## Steps

1. Map auth, authorization, secure storage, networking, privacy, permissions, cryptography, WebViews, deep links, logging, telemetry, and dependency surfaces.
2. Check manifests, entitlements, ATS/network security config, permission prompts, exported components, URL schemes, dependency files, and local environment references.
3. Distinguish genuine secrets from public mobile client config.
4. Prioritize findings by severity, exploitability, and evidence.
5. Recommend scoped remediations and required human approvals.

## Validation Gates

Secret detection, dependency risk review, privacy/permission review, secure storage review, TLS/network review, deep-link/WebView review, logging/telemetry review, and unsupported-infrastructure reporting.

## Failures And Stop Conditions

Stop on suspected secret exposure, request to use credentials, unsupported external scan requiring upload, missing scope, or requested security weakening.

## Evidence And Outputs

Findings with file references, severity, rationale, affected platforms, remediation, approvals required, and limitations.

## Acceptance Criteria

Audit is evidence-based, avoids leaking sensitive values, and clearly separates confirmed issues from assumptions.

## Prohibited Actions

No source mutation by default, no credential use, no external upload of code or logs, no disabling controls, and no fabricated scan results.
