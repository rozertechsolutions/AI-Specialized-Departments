---
name: audit-mobile-security
description: Workflow for mobile security audit covering secrets, auth, storage, network, privacy, permissions, crypto, WebViews, deep links, logging, telemetry, dependencies, and release risk.
---

# Audit Mobile Security

## Objective

Audit mobile security and privacy risks without exposing secrets or making unapproved sensitive changes.

## Trigger

Use when the user requests a security audit, privacy review, secret scan, permission review, or release security check.

## Inputs

Target project, changed files, manifests/entitlements, network config, storage/auth code, dependency files, logging/telemetry code, and release config.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native.

## Preconditions

Define audit scope. Avoid protected files unless explicitly approved.

## Primary Owner

`mobile-security-reviewer`

## Reviewers

Affected platform engineer, `mobile-test-engineer` for validation, and `mobile-code-reviewer` for final review if changes are made.

## Steps

1. Inventory security-sensitive surfaces.
2. Check protected files and `.clineignore` coverage without exposing secrets.
3. Review auth, authorization, storage, network, WebViews, deep links, permissions, crypto, logging, telemetry, dependencies, and signing prerequisites.
4. Classify findings by severity.
5. Recommend minimal remediation.
6. If fixes are requested and approved, delegate implementation to owners.
7. Re-review after fixes.

## Conditional Steps

- Dependency risk: inspect lockfiles only with approval for changes.
- Release readiness: confirm no real signing or publishing.
- Public config: distinguish public client IDs from secrets.

## Validation Gates

No secrets exposed, sensitive findings documented, approvals captured, and remediation validated when performed.

## Failures

Stop on discovered secret exposure, approval denial, protected file uncertainty, or external service requirement.

## Stop Conditions

Do not proceed with credential use, external upload, or security-control changes without explicit approval.

## Evidence

Files inspected, findings, commands run, unavailable checks, approvals required, and residual risk.

## Outputs

Security audit report and optional fix plan.

## Acceptance Criteria

Security posture is accurately reported and no secrets or unsupported controls are introduced.

## Human Approvals

Required for sensitive edits, credential access, dependency changes, telemetry/privacy changes, and external services.

## Prohibited Actions

No credential import, publishing, signing, upload, deployment, destructive commands, or simulated security tooling.
