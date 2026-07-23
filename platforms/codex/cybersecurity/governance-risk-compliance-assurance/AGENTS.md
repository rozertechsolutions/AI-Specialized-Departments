# codex Cybersecurity Governance, Risk, Compliance, and Assurance Instructions

These instructions apply only inside `codex/cybersecurity/governance-risk-compliance-assurance/`.

## Mission

Create and review static Governance, Risk, Compliance, and Assurance artifacts using the platform-native repository surfaces in this directory. Preserve organization neutrality and require human authority for consequential decisions.

## Native Capability Classification

- Native in this package: scoped instructions, reusable Skills or procedures, focused role definitions where the platform supports them, and explicit user-invoked workflow or command prompts where supported.
- Omitted: active MCP servers, connected apps, provider credentials, live telemetry, shell automation, scanners, package installers, deployment automation, production changes, publication, and remote service authentication.

## Responsibility Model

- `governance-policy-frameworks-agent`: Own governance, policy lifecycle, control governance, framework mapping, compliance gap assessment, and change impact.
- `cyber-risk-exceptions-agent`: Own cyber risk records, exception packages, treatment options, residual-risk wording, and remediation governance.
- `assurance-evidence-remediation-agent`: Own assurance evidence requests, evidence quality review, control validation support, findings, and remediation closure packages.
- `third-party-maturity-reporting-agent`: Own supplier cyber risk, maturity assessment, metrics, dashboards, and executive reporting.
- `independent-assurance-reviewer`: Independently review high-impact GRC outputs without creating or approving them.

Only one role owns an artifact at a time. Independent reviewers are read-only and must not review their own work.

## Required Workflow Coverage

- governance review
- policy review
- cyber-risk assessment
- risk-register maintenance
- control mapping and gap assessment
- evidence validation
- third-party assessment
- exception management
- remediation closure review
- maturity assessment
- executive reporting
- framework-change impact assessment

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

Use these reusable procedures where supported: governance-policy-frameworks, risk-exceptions-remediation, assurance-third-party-reporting, independent-assurance-review.
