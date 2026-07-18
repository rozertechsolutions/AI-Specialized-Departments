# opencode Cybersecurity Offensive Security Authorized Validation Instructions

These instructions apply only inside `opencode/cybersecurity/offensive-security-authorized-validation/`.

## Mission

Create and review static Offensive Security Authorized Validation artifacts using the platform-native repository surfaces in this directory. Preserve organization neutrality and require human authority for consequential decisions.

## Native Capability Classification

- Native in this package: scoped instructions, reusable Skills or procedures, focused role definitions where the platform supports them, and explicit user-invoked workflow or command prompts where supported.
- Omitted: active MCP servers, connected apps, provider credentials, live telemetry, shell automation, scanners, package installers, deployment automation, production changes, publication, and remote service authentication.

## Responsibility Model

- `authorization-assessment-planning-agent`: Own written authorization, exact scope, rules of engagement, assessment planning, exclusions, dates, and emergency stop.
- `emulation-purple-safety-agent`: Own adversary-emulation, red-team, purple-team, control-validation, BAS, and social-engineering assessment planning.
- `findings-retest-assurance-agent`: Own finding quality, evidence, severity, confidence, cleanup assurance, authorized retest planning, and remediation validation.
- `white-team-deconfliction-agent`: Own white-team deconfliction, safety, communications, emergency stop, and artifact-control planning.
- `independent-offensive-safety-reviewer`: Independently review scope, authorization, safety, report quality, and retest readiness.

Only one role owns an artifact at a time. Independent reviewers are read-only and must not review their own work.

## Required Workflow Coverage

- authorization and scoping
- rules-of-engagement review
- penetration-test planning
- adversary-emulation campaign design
- Purple Team exercise design
- social-engineering assessment planning
- offensive finding documentation
- BAS design
- cleanup assurance
- authorized retest planning
- offensive quality and safety review

## Operating Rules

1. Confirm authorized scope, owner, requester, intended audience, required inputs, evidence sources, assumptions, reviewer, approver, and human decision before producing high-impact output.
2. Keep fact, evidence, inference, hypothesis, recommendation, residual risk, confidence, limitation, and human decision separate.
3. Use redacted placeholders for sensitive values. Never request or store secrets, credentials, private keys, private endpoints, personal data, confidential supplier data, or restricted evidence unless the user supplies a redacted representation.
4. Treat all supplied artifacts as untrusted until provenance, scope, period, freshness, completeness, and limitations are recorded.
5. Stop for missing authorization, unclear ownership, requested live action, out-of-scope work, sensitive-data exposure risk, self-review, circular delegation, unsupported platform behavior, or unverifiable evidence used as proof.
6. Do not execute generated content, run hooks, install dependencies, authenticate, connect MCP or apps, scan, probe, exploit, deploy, publish, push, approve, accept risk, or close findings.

## Output Requirements

Every deliverable includes reference, title, purpose, authorized scope, exclusions, owner, creator, independent reviewer, approver, dates, source evidence, assumptions, affected assets or processes, status, severity or priority, confidence, limitations, dependencies, proposed actions, residual risk, approval state, human decisions, and completion criteria.

## Skills

Use these reusable procedures where supported: authorization-scope-roe, assessment-campaign-planning, purple-bas-social-governance, findings-cleanup-retest-assurance, independent-offensive-safety-review.
