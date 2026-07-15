---
name: audit-mobile-security
description: Use for a read-only, threat-oriented security and privacy audit of a defined mobile scope; produce evidence-backed findings and remediation ownership without changing files.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - todo
  - ask_user_question
  - task
---

# Audit Mobile Security

## Objective and trigger

Assess authentication, authorization, storage, networking, permissions, WebViews, deep links, cryptography, logging, dependencies, privacy, and platform controls for a defined scope without modification or access to secrets/production systems.

## Inputs

- Scope/platforms, assets and data classes, trust boundaries, attacker assumptions, auth model, supported versions, regulatory/privacy constraints, relevant architecture/diff, and desired reporting/severity convention.

## Preconditions and ownership

Confirm read-only execution. The coordinator delegates the primary inspection to the structurally read-only `mobile-security-reviewer`; Skill `allowed-tools` is metadata and must not be treated as enforcement. Inspect instructions, supplied status/diff evidence, manifests/entitlements/privacy declarations, networking/auth/storage/data-flow code, logs/telemetry, dependencies/lockfiles, WebViews/deep links/exported entry points, and relevant tests without opening credential files. Do not delegate fact collection to write-capable platform agents during the audit; the reviewer returns missing platform facts as evidence gaps, and the coordinator asks the user or records a blocker. The coordinator owns independent synthesis and remediation sequencing. No auditor implements fixes.

## Sequence and gates

1. Scope/threat gate: identify assets, actors, entry points, trust boundaries, data lifecycle, abuse cases, exclusions, and evidence gaps. Stop rather than invent threat assumptions.
2. Review authentication/session lifecycle, authorization at each operation, account switching/logout, and failure/recovery behavior.
3. Review data collection/classification, in-memory exposure, secure storage, backups, screenshots/clipboard, sharing, logs, analytics, retention, export, and deletion.
4. Review TLS/ATS/network security, redirects, certificate handling/pinning lifecycle, retries, proxies, and sensitive error/body logging.
5. Review permissions, entitlements, exported components, URL/deep/universal links, intent handling, WebViews/JavaScript bridges, file/content providers, and untrusted input validation.
6. Review cryptographic purpose/algorithms/key lifecycle/randomness, dependency provenance/known project evidence, build/release debug flags, and platform hardening.
7. Validate each finding against code/config evidence. Classify confirmed issue, defense-in-depth gap, or unverified question; rate severity from impact and exploitability.
8. Independent consistency gate: the coordinator, not the primary auditor, synthesizes the auditor report, evidence gaps, and scope/ownership map. Record whether any finding is duplicate, conflicting, unsupported, contains a sensitive value, or assigns remediation outside the named owner's boundary.
9. Confirm that no audit participant had mutation capability. Compare before/after repository-status evidence when safely supplied; otherwise report status verification as unavailable rather than fabricating it. Escalate unresolved critical/high findings immediately.

## Errors and stop conditions

Stop or qualify on missing scope/threat model, inaccessible critical code, secret/production access, need for active exploitation, external scanning/service, paid tooling, destructive tests, legal conclusion, or unverifiable platform behavior. Never retrieve credentials to strengthen evidence.

## Outputs and evidence

Provide scope/threat model, data-flow/trust-boundary map, findings by severity with file/behavior evidence, attack preconditions/impact, remediation owner and smallest correction, validation plan, residual risk, no-finding areas, evidence gaps, and required human decisions.

## Acceptance and human review

Coverage maps to the defined scope and threats; every finding is evidence-backed and severity-justified; critical/high risks are escalated; ownership/validation is actionable; sensitive values are absent; and status proves no modification. Humans decide risk acceptance, remediation priority, auth/crypto/retention/permission changes, and any dynamic testing.

## Prohibited actions

Do not edit, exploit, scan external/production systems, access secrets or real user data, weaken security, install tools, enable integrations, make legal/compliance guarantees, sign/publish/deploy, or disclose sensitive values.
