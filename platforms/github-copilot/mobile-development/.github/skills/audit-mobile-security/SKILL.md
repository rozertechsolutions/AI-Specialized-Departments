---
name: audit-mobile-security
description: Performs a read-only, threat-oriented mobile security audit covering data, authentication, authorization, storage, networking, permissions, WebViews, deep links, cryptography, logging, dependencies, and platform controls with severity and escalation. Use for explicit security audits.
---

# Audit mobile security

## Objective

Produce an evidence-based, read-only security and privacy assessment with scoped threats, data classification, prioritized findings, remediation ownership, verification requirements, and explicit escalation.

## Trigger

Use for an explicit mobile security/privacy audit or threat review. Do not silently expand a general code review into a full audit.

## Inputs

- systems, platforms, versions, modules, environments, and exclusions;
- assets, data classifications, actors, trust boundaries, entry points, and threat concerns;
- authentication/authorization design and server assumptions;
- available security documentation, tests, scanner reports, manifests, entitlements, privacy declarations, and dependency inventories;
- severity policy and required human contacts.

## Preconditions

- Invoke `mobile-security-reviewer` explicitly and keep it read-only.
- Read applicable instructions and only the code/configuration/evidence needed for the agreed scope.
- Do not access credentials, private production data, or sensitive files. Ask for redacted evidence when necessary.
- Record audit limitations, tool availability, and whether dependency/vulnerability data is current before drawing conclusions.

## Ownership

Primary owner: `mobile-security-reviewer`. Technology owners clarify behavior and later implement approved remediation. `mobile-code-reviewer` independently reviews remediation; the security reviewer rechecks findings.

## Sequence and intermediate gates

1. **Scope gate:** define assets, actors, data classes, trust boundaries, entry points, platforms, exclusions, and severity model. Stop if the audit target or authority is unclear.
2. Map data flows and lifecycle: collection, transmission, processing, storage, backup, logging, analytics, sharing, deletion, and user control.
3. Review authentication/session lifecycle and verify that authorization is enforced at trusted server/resource boundaries rather than assumed from client UI.
4. Review storage, backups, keychain/keystore use, file protection, caches, databases, screenshots, clipboard, notifications, logs, crash reports, and test fixtures.
5. Review transport/TLS, certificate policy, hostname validation, cleartext exceptions, timeouts/retries, request validation, WebSockets, and sensitive logging.
6. Review permissions, entitlements, exported components, intents/URL schemes/universal or app links, IPC, WebViews/JavaScript bridges, file/content providers, pasteboard, and platform privacy controls.
7. Review cryptography for standard primitives, key generation/storage/rotation, randomness, nonce/IV use, and absence of custom cryptographic design.
8. Review dependencies, build/release hardening, debug flags, obfuscation assumptions, supply chain, and scanner evidence. Never invent CVEs or claim a scan ran when it did not.
9. **Finding gate:** give each finding evidence, attack path, preconditions, impact, severity, confidence, affected platforms, remediation owner, and verification method. Separate defense-in-depth recommendations from exploitable defects.
10. Escalate unresolved critical/high findings immediately. Technology owners implement only separately approved fixes; rerun affected tests and independent review, then security re-review.

## Errors and stop conditions

- Stop if evidence requires unauthorized access to credentials, accounts, production systems/data, paid scanners, or external services.
- If runtime testing, vulnerability data, or backend authorization evidence is unavailable, report the limitation and narrow confidence.
- Do not exploit systems, exfiltrate data, weaken controls, or make out-of-scope security changes.
- An unresolved critical/high finding or unknown material trust boundary blocks a clean audit conclusion.

## Completion classification

Classify every coordinator criterion for the audit. Scope traceability, configuration/security-boundary inspection, secret-scanning status, dependency evidence, relevant error/offline/logging behavior, documentation of findings, and independent validation of remediations are normally required. Compilation, tests, lint, UI/accessibility, adaptive layout, performance, warnings, and regression execution are conditionally required only to verify a finding or remediation; give concrete reasons.

## Outputs and evidence

Return scope/threat model, data-flow summary, findings by severity, evidence and confidence, cleanly reviewed areas, scanner/runtime status, remediation owners, verification steps, limitations, escalation decision, and completion-classification table. Never include secret values.

## Acceptance criteria

- Scope, assets, threats, data classes, and trust boundaries are explicit.
- Every finding has a defensible evidence-to-impact path and severity.
- Limitations and unrun checks are visible; no unsupported assurance is given.
- Critical/high findings are escalated and cannot be silently accepted by the reviewer.

## Human review requirements

Humans confirm scope, data classification, severity policy, backend assumptions, access to security tools, remediation priority, and acceptance of residual risk. Only an authorized human can accept unresolved high-risk findings.

## Prohibited actions

Do not edit during the audit, access or expose secrets/production data, run intrusive tests without authorization, invent vulnerabilities or scans, weaken controls, configure external services, publish/sign/deploy, or let the reviewer approve its own remediation.
