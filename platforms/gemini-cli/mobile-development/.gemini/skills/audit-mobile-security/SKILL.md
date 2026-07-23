---
name: audit-mobile-security
description: Performs a read-only threat-oriented mobile security audit covering data, authentication, authorization, storage, networking, permissions, WebViews, deep links, cryptography, logging, dependencies, and platform controls. Use when the user asks for a security or privacy audit.
---

# Audit Mobile Security

## Objective and trigger

Produce an evidence-based, read-only mobile security/privacy audit with threat
scope, severity, remediation ownership, and escalation. Activate only for an
explicit security/privacy audit or as the security gate of another Skill. Do not
silently implement fixes under this workflow.

Activation is read-only and grants no tools. Use only project-allowed read tools;
do not use shell, write, replace, MCP, scanners, or external services.

## Inputs

- Audit objective, in-scope apps/modules/platforms/environments, and exclusions.
- Assets, data classes, actors, trust boundaries, threat assumptions, and policy/
  compliance requirements supplied by the user or project.
- Exact change set or current-state files and available test/scan evidence.
- Known accepted risks with owner, expiry, and rationale.

## Preconditions and ownership

Inspect instructions and repository state. Work only from local non-sensitive
files and supplied sanitized evidence. Do not open secret stores, credentials,
production systems, crash analytics, or external scanners/services.

`mobile-security-reviewer` is primary owner. Platform engineers clarify native
controls and later own remediation; `mobile-architect` supports trust/boundary
analysis; test/performance/UI reviewers support only distinct findings. No final
code review is required for a no-change audit, but any subsequent remediation
must use the appropriate implementation Skill and independent review.

## Workflow and gates

1. **Scope gate:** define assets, data classification, actors, entry points, trust
   boundaries, platforms, environments, exclusions, and severity rubric.
2. **Evidence gate:** inspect manifests/entitlements/permissions/privacy files,
   auth/session/authorization, storage/keychain/keystore, backups, networking/TLS,
   certificates, APIs, WebViews, deep/app links, IPC, cryptography, logging/
   telemetry, clipboard/screenshots, dependencies/locks, and relevant tests.
3. **Threat gate:** enumerate misuse/abuse cases and attacker prerequisites for
   local device, network, malicious app/content/link, compromised account, and
   supply chain as applicable. Separate evidence, inference, and unknown.
4. **Control gate:** evaluate least privilege, validation, secure defaults,
   lifecycle/revocation, denial/recovery paths, redaction, consent, dependency
   provenance, and platform controls. Never equate absence of evidence with safety.
5. **Finding gate:** for each issue record ID, severity, confidence, scenario,
   preconditions, exact evidence, impact, smallest remediation, primary platform
   owner, validation, and release impact. Avoid filename-only findings.
6. **Escalation gate:** unresolved critical/high issues are blockers. Accepted risk
   requires explicit human owner/rationale/expiry; the reviewer cannot accept it.
7. **Report gate:** prioritize remediation and propose a safe validation plan.
   Start no fix, dependency update, credential rotation, or external action.

## Completion classification

Classify scope/threat model; configuration; code/build/test evidence; dependency
review; secret scanning evidence; authentication/authorization; storage/network/
permissions/WebViews/deep links/crypto/logging/privacy; accessibility/performance
interactions; offline/recovery; documentation; warnings; regressions; platform
controls; remediation validation; and independent security status as `required`,
`conditionally-required`, or `not-applicable` with concrete reasons.

## Errors and stop conditions

Stop for unknown scope/data classification, required secret/production/personal
data access, unsanitized evidence, unclear authorization, external tooling/cost,
or inability to inspect a material control. Escalate uncertainty; do not exploit,
probe live services, or weaken controls to test a theory.

## Outputs, evidence, and acceptance

Return scope/exclusions, asset/data/threat maps, evidence index, findings with
severity/confidence/owner/validation, positive controls, unknowns, completion
ledger, accepted risks with human owner/expiry, blockers, and remediation order.

Acceptance requires coverage of every applicable threat area, traceable and
reproducible findings, no secret exposure, explicit unknowns, named owners, and
escalation of all unresolved high risk. A clean report requires affirmative
evidence, not merely no discovered findings.

## Human review and prohibited actions

Humans authorize sensitive access and accept residual risk. Never edit files,
access/copy/log secrets or PII, exploit systems, contact production, upload code/
data, install scanners, rotate credentials, change dependencies/controls, enable
MCP, sign/publish/deploy, destroy data, or perform Git writes.
