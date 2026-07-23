---
name: audit-mobile-security
description: Perform an authorized, read-only security and privacy audit of Android, iOS, KMP, Flutter, or React Native code and configuration. Do not use for exploitation, production scanning, compliance certification, or automatic remediation.
---

# Audit Mobile Security

## Objective

Produce an evidence-based mobile security/privacy assessment covering the authorized scope without changing code, accessing secrets, testing production, or overstating compliance.

## Required inputs

- Explicit audit scope, repository/revision, target platforms, and authorization boundary.
- Data classification and known trust boundaries.
- Relevant threat model, regulatory/product requirements, and excluded systems.
- Whether dependency advisory lookup or external official documentation is authorized; never upload project data.

If authorization or scope is unclear, stop before inspecting sensitive or external systems.

## Preconditions

1. Confirm read-only operation and exact authorized files/systems.
2. Read instructions, security documentation, and available threat model.
3. Inspect status/diff so user changes and review base are explicit.
4. Do not open credential stores, private keys, token files, production telemetry, or personal data. If a filename suggests a secret, report its presence without exposing content.
5. Define severity/confidence criteria and platform-specific review checklist.
6. Classify every completion criterion as required, conditionally required, or not applicable with a documented reason.

## Agent ownership

`mobile-security-reviewer` is the primary auditor. The coordinator may obtain read-only platform feasibility evidence from `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer`. Use `mobile-architect` for trust-boundary clarification. No implementation agent may edit during the audit, and the security reviewer never remediates its own findings.

## Execution

1. **Threat map.** Identify assets, actors, entry points, trust boundaries, data flows, storage, external SDKs/services, and relevant attacker capabilities from repository evidence.
2. **Platform configuration.** Review Android permissions/exported components/network security/backups and Apple entitlements/privacy/ATS/background capabilities as applicable.
3. **Identity and session.** Review authentication, authorization assumptions, token lifecycle, logout/revocation, deep links, intents/URL schemes, and account transitions.
4. **Data protection.** Review local files/databases/preferences, keychain/keystore use, backups, screenshots/clipboard, logs, telemetry, crash data, retention, and deletion.
5. **Transport and parsing.** Review TLS configuration, redirects, WebViews, certificates, request signing if present, input validation, serialization, unsafe deserialization, and error disclosure.
6. **Code risks.** Review cryptography, random generation, concurrency races affecting security, native bridges/platform channels, dynamic loading/evaluation, file/path handling, and injection surfaces.
7. **Dependencies/build/release.** Review manifests/lockfiles, repository sources, build scripts, secret references, signing configuration references without opening secret material, debug flags, and release hardening.
8. **Test coverage.** Identify security invariants lacking deterministic tests; do not create them during this audit.
9. **Finding validation.** For each candidate, prove the code/config path, preconditions, impact, affected versions, and false-positive conditions. Do not actively exploit.
10. **Independent consistency gate.** Check severity, duplicates, remediation feasibility, and whether any claim relies on unavailable external configuration.
11. **Final read-only gate.** Confirm no repository or external state changed.

## Error handling and stop conditions

Stop on missing authorization, need for credentials/production data, out-of-scope live testing, a critical exposed secret requiring immediate containment, or unverifiable external configuration. Do not print secret values. Route urgent containment and credential rotation to the human owner; do not perform them.

## Outputs

- Scope, exclusions, method, and threat map.
- Findings ordered by severity and confidence, each with file/line evidence, preconditions, impact, minimal remediation, verification, and residual risk.
- Security test gaps and platform-specific human checks.
- Completion matrix with required/conditional/not-applicable status, reasons, and exact results.
- Limitations and areas with no findings.

## Acceptance criteria

- Every finding is reproducible from authorized repository evidence and avoids secret disclosure.
- Permission, auth, storage, transport, privacy, logging, WebView/deep-link, bridge, dependency, and release surfaces are covered when applicable.
- False positives, external assumptions, and residual risk are explicit.
- No code, credential, repository state, production system, or external service was modified.

## Prohibited actions

Do not exploit live systems, read/copy secrets, use production data, upload code/logs, install scanners, enable MCP, change files, rotate credentials, weaken controls, claim certification/compliance, sign, publish, deploy, or automatically remediate.
