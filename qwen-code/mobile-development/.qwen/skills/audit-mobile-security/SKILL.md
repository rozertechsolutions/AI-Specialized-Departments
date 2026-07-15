---
name: audit-mobile-security
description: Perform a read-only mobile threat and privacy audit covering data, authentication, authorization, storage, networking, permissions, WebViews, deep links, cryptography, logging, dependencies, and platform controls.
user-invocable: true
---

# Audit Mobile Security

## Objective

Produce an evidence-based, read-only mobile security and privacy audit with explicit threats, severity, affected paths, remediation, residual risk, and human escalation.

## Trigger

Use when the user explicitly requests a security/privacy audit, threat review, or security readiness assessment. Do not implement findings unless a separate change request authorizes it.

## Inputs

- Audit scope, platforms/targets, application environments, data classes, threat assumptions, and compliance constraints.
- Known architecture, trust boundaries, authentication providers, backend contracts, and prior findings when available.
- Explicit exclusions and permitted evidence sources.

## Preconditions

- Read instructions, project documentation, relevant source/configuration/tests/dependencies, and current changes.
- Do not request, open, copy, or transmit real credentials or personal/production data.
- Establish the audit boundary and limitations; authenticated or production testing requires separate explicit approval and is outside this default workflow.

## Ownership

- Primary owner: `mobile-security-reviewer`.
- Platform engineers clarify implementation behavior but do not co-own findings.
- `mobile-code-reviewer` may independently audit report traceability. Remediation is assigned later to the relevant implementation owner.

## Tool and permission boundary

Use read/list/search and public official documentation fetch only. No edits, shell execution, scanners requiring installation, MCP, authenticated endpoints, active exploitation, external uploads, production access, signing, or deployment.

## Sequence and gates

1. **Scope gate:** Define platforms, builds/environments, assets, data classifications, actors, entry points, trust boundaries, threat capabilities, exclusions, and evidence limitations.
2. **Inventory gate:** Map manifests/entitlements/permissions, components/routes/deep links, WebViews, auth/session, networking, storage/cache/database, IPC/native bridges, logs/telemetry, cryptography, backups, dependencies, and security tests with exact paths.
3. **Data-flow gate:** Trace each sensitive data class from collection/input through validation, authorization, transit, storage, display/share, logging/telemetry, backup, and deletion. Mark unknown flows.
4. **Identity gate:** Review authentication and authorization separately, token/session lifecycle, account/device binding, logout/revocation, reauthentication, least privilege, and denial paths.
5. **Platform gate:** Review Android exported components/intents/permissions/backups/network security/secure storage and iOS entitlements/URL handling/ATS/Keychain/data protection/privacy declarations as applicable.
6. **Attack-surface gate:** Review untrusted input, injection, WebView configuration/bridges, deep links/universal/app links, file/content providers, deserialization, path traversal, native bridges, screenshots/clipboard, TLS/certificate behavior, crypto APIs, dependency/supply-chain exposure, sensitive logs, and telemetry consent.
7. **Control/test gate:** Identify observed preventive/detective controls and test evidence. Recommend exact safe static/runtime/manual checks without claiming they ran.
8. **Severity gate:** For each finding record preconditions, exploit path, likelihood, impact, scope, evidence/confidence, severity, smallest remediation, verification, and owner. Escalate unresolved high/critical risks immediately.
9. **Independent precision gate:** Verify references resolve, threats are credible, severities are consistent, no secret is exposed, findings do not duplicate ownership, and absence of evidence is not reported as safety.
10. **Completion gate:** Classify every `QWEN.md` criterion, marking execution checks unavailable/not applicable with reasons.

## Errors and stop conditions

Stop on discovered live secrets/personal data (report location without content), required production/authenticated access, unclear authorization to inspect sensitive files, need for active exploitation, conflicting scope, or a critical issue requiring immediate human containment.

## Outputs and evidence

- Scope/threat model, asset/data-flow and trust-boundary maps.
- Exact files and controls inspected.
- Findings ordered by severity with evidence, scenario, impact, confidence, remediation, verification, and owner.
- Positive controls, unknowns, test recommendations, residual risk, completion ledger, and release-security decision.

## Acceptance criteria

- All in-scope trust boundaries and required control categories are assessed or explicitly unavailable.
- Every finding is actionable, evidence-based, severity-justified, and assigned to one remediation owner.
- No secret or personal data is reproduced and no unsupported safety claim is made.
- High/critical findings and evidence gaps are visibly escalated.

## Human review requirements

Humans decide scope, sensitive access, threat assumptions, risk acceptance, remediation priority, production testing, credential use, compliance interpretation, and release blocking.

## Prohibited actions

Do not edit, exploit, brute-force, scan production, access accounts, copy secrets/data, weaken controls, upload code/findings to external services, install tools, assign `no risk` from missing evidence, or treat the audit as legal/compliance certification.
