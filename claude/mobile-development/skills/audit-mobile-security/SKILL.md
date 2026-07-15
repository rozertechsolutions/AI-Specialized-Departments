---
name: audit-mobile-security
description: Performs a read-only mobile security and privacy audit with evidence-backed findings. Use for Android, iOS, KMP, Flutter, or React Native reviews.
---

# Audit Mobile Security

## Objective

Perform a scoped, threat-oriented, read-only assessment of mobile authentication, authorization, data, storage, transport, permissions, WebViews, deep links, logging, telemetry, dependencies, and platform boundaries.

## Trigger

Use when the user explicitly requests a security, privacy, threat, or dependency-risk audit. Do not use this Skill to implement remediation.

## Inputs

- audit scope, assets, threat actors, trust boundaries, environments, and risk model;
- data classification, privacy obligations, authentication and authorization design;
- repository snapshot, configuration, manifests, entitlements, privacy declarations, dependency files, and relevant tests;
- platform targets and supported versions;
- safe redacted findings from scanners or runtime tools when available.

## Supported technologies

Android, iOS, KMP, Flutter, and React Native, including platform channels, bridges, shared source sets, and native hosts.

## Preconditions

- Scope and repository snapshot are explicit.
- Review can remain read-only and non-destructive.
- Protected material is excluded or safely redacted.
- Any scanner, network, external source, or runtime test is trusted, reviewed, and approved.
- Production access, live exploitation, credential use, and external upload are unnecessary.

## Primary owner and reviewers

mobile-security-reviewer is primary and read-only. Relevant technology owners explain implementation context but do not influence severity or acceptance. mobile-architect reviews trust and dependency boundaries. mobile-test-engineer reviews security-test evidence. mobile-code-reviewer reviews the report for evidence, false positives, and coverage. A human security or privacy owner accepts risk.

## Ordered workflow

1. Define assets, data classes, actors, entry points, trust boundaries, abuse cases, environments, exclusions, and severity model.
2. Inspect repository instructions, status, application configuration, dependencies, manifests, entitlements, privacy files, networking, storage, auth, crypto, deep links, WebViews, logging, telemetry, bridges, and tests.
3. Map sensitive data from collection through transport, processing, storage, logging, sharing, retention, deletion, backup, and recovery.
4. Review authentication, authorization, session lifecycle, account recovery, replay, enumeration, and server-enforced controls.
5. Review secure storage, backups, screenshots, clipboard, memory, local databases, files, caches, and migration behavior.
6. Review TLS and cleartext policy, certificate and hostname validation, request validation, retries, error leakage, and API trust assumptions.
7. Review permissions, exported components, URL schemes, universal or app links, intents, WebViews, JavaScript bridges, file access, and navigation authorization.
8. Review input validation, serialization, injection, path traversal, unsafe deserialization, attachment handling, platform channels, and native bridges.
9. Review logging, analytics, crash reporting, identifiers, consent, retention, data minimization, and deletion.
10. Review dependency provenance, versions, lockfiles, install scripts, maintenance, licensing, and known official advisories using approved sources.
11. Validate each potential finding against actual reachability and controls; document false positives and missing evidence.
12. Rate findings with affected asset, prerequisite, evidence, impact, likelihood, remediation guidance, validation recommendation, and residual risk.
13. Obtain report review, correct analysis errors without editing production, then complete triple validation and final verification.

## Conditional steps

- KMP: compare expect and actual security behavior and verify no target receives weaker storage, crypto, or transport.
- Flutter or React Native: review platform-channel or bridge validation and host permission parity.
- WebView: review origin and navigation controls, JavaScript, bridges, file or content access, cookies, downloads, mixed content, and external intents.
- Deep link: review parsing, origin or association, authorization after navigation, replay, fallback, and sensitive parameter handling.
- Dependency advisory lookup: use only current official vendor, registry, or advisory sources and do not upload project data.

## Validation gates

- Gate 1: threat, data, and coverage scope are explicit.
- Gate 2: each finding is tied to exact source or configuration and a credible failure condition.
- Gate 3: secrets and personal data are not reproduced.
- Gate 4: false positives and compensating controls are considered.
- Gate 5: report review has no unresolved evidence or severity error.
- Gate 6: no production edit, exploitation, connector activation, or prohibited action occurred.

## Failures

If a scanner fails or coverage is incomplete, report the limitation and do not infer safety. If an actual secret is discovered, stop, do not reproduce it, identify only its location and category, and direct rotation or revocation to the responsible human. Do not remediate silently.

## Stop conditions

Stop for real credential exposure, production access, live exploitation, destructive test, external code or data upload, unclear legal or privacy authority, unapproved scanner or network use, missing critical configuration, or user request to implement within this read-only audit.

## Evidence

Record scope, inspected paths, data flows, exact finding locations, official advisory sources, tool versions and sanitized output, false-positive analysis, coverage gaps, reviewer findings, and source freshness.

## Outputs

- threat and data-flow summary;
- prioritized evidence-backed findings and affected assets;
- remediation and validation guidance without edits;
- false positives, compensating controls, residual risks, and human owners;
- criterion ledger and audit limitations.

## Acceptance criteria

The audit is read-only, scoped, reproducible, free of secret reproduction, covers applicable attack surfaces, distinguishes findings from hypotheses, considers false positives, and assigns unresolved risk to a human owner.

## Human approvals

Humans authorize scanners, network lookups, runtime testing, access to sensitive configuration, risk acceptance, remediation, privacy decisions, dependency changes, and any later production change.

## Prohibited actions

Do not edit production, expose secrets, exploit live systems, use credentials, upload code or data externally, auto-update dependencies, weaken security, accept risk, approve release, sign, publish, deploy, destroy data, or run Git write commands.
