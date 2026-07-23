---
name: audit-mobile-security
description: Perform an evidence-based mobile security and privacy audit covering data, auth, storage, transport, permissions, WebViews, deep links, cryptography, logging, dependencies, and platform controls.
when_to_use: Use for a scoped threat-oriented review of Android, iOS, KMP, Flutter, React Native, or hybrid code; do not treat it as penetration testing or compliance certification.
argument-hint: "[scope and threat concerns]"
model: inherit
---

# Objective

Audit the scope in `$ARGUMENTS`, identify evidence-backed risks, prioritize them by demonstrated likelihood/impact, and require human escalation for unresolved high risk.

# Required input and supported scope

Require target technologies/releases, in-scope modules/flows, data classification, trust assumptions, authentication model, environments, known threats, and desired depth. Do not request secrets, real tokens, private keys, personal production data, or unauthorized system access.

# Preconditions and inspection

Read instructions; inspect status/diff, manifests/entitlements/privacy declarations, entry points, auth/authorization/session flows, secure storage, network configuration, API clients, local data/cache, logging/analytics, WebViews, deep/universal links, IPC/bridges, permissions, cryptography, dependencies/lockfiles, build configuration, and security tests. Confirm platform/shared ownership.

# Ownership

`mobile-security-reviewer` is the read-only primary owner. Technology engineers clarify implementation and own remediation; `mobile-architect` reviews trust-boundary architecture; `mobile-test-engineer` owns security regression tests; UI/performance/release reviewers participate when findings affect them; `mobile-code-reviewer` independently checks remediation. Reviewers do not self-approve fixes.

# Procedure and gates

1. Define assets, actors, entry points, trust boundaries, attacker capabilities, data lifecycle, and out-of-scope areas. Gate: threat assumptions and data classification are explicit.
2. Review authentication, authorization, session/token lifecycle, account transitions, and failure/recovery behavior.
3. Review storage, backups, caches, clipboard/screenshots, logs/analytics/crash reports, and deletion/retention for sensitive data.
4. Review TLS/cleartext, certificate policy, endpoint validation, request/response redaction, WebSockets, downloads, and unsafe retries.
5. Review least permissions/entitlements, exported components, URL/deep-link validation, WebViews/JavaScript bridges, intent/IPC/native bridges, and platform privacy controls.
6. Review cryptography/key handling for standard primitives, randomness, nonce/IV use, key lifecycle, and absence of hard-coded secrets; do not access key material.
7. Review dependency provenance, versions/locks, known project-supplied advisories, build scripts, and supply-chain exposure using local evidence or approved official public sources.
8. Record each finding with severity, evidence, exploit/failure condition, impact, remediation owner, and verification. Separate hypotheses and unavailable dynamic checks.
9. Escalate unresolved high risk to the user. After owner remediation, rerun the affected review and regression tests, then obtain independent code review.

# Failure and stop handling

Stop for required credential/private-data access, unauthorized active testing, unclear authorization boundary, insufficient data classification, production impact, or paid/external scanning without approval. Report limitations; never convert missing evidence into a pass.

# Evidence and acceptance

Return threat model, reviewed surfaces, severity-ranked findings with file citations, remediation/verification, applicability classification, unresolved assumptions, unavailable dynamic tests, and human decisions. A no-finding result states what was actually inspected.

Report every considered universal and technology-specific completion criterion as `required`, `conditionally-required`, or `not-applicable`; give a concrete reason for every `not-applicable`, and label unavailable infrastructure `unavailable` rather than passed.

Accept the audit only when all in-scope categories are addressed and high-risk findings are escalated; this does not certify the application. Remediation is complete only after tests and independent re-review.

# Human review and prohibited actions

Human review is mandatory for high-risk acceptance, auth/permission/entitlement/crypto/privacy changes, active security testing, and production data. Never access secrets, exploit systems, weaken controls, transmit code/data externally without approval, claim compliance/certification, publish/sign/deploy, or let an implementer approve its own remediation.
