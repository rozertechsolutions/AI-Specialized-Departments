---
name: coverage-quality-assurance
description: Reusable Defensive Security Operations, Detection, and Intelligence procedure for coverage quality assurance using static evidence, human approval gates, and independent review.
---

# Coverage Quality Assurance

## Use Cases

Use this Skill for Defensive Security Operations, Detection, and Intelligence work related to coverage quality assurance, including the applicable workflows: SOC operating-model review, telemetry-source onboarding design, detection design and review, supplied-alert triage, threat-hunt planning, threat-intelligence assessment, defensive malware-analysis planning, SOAR playbook design, detection-coverage assessment, SOC quality review, incident escalation.

## Required Inputs

- Authorized scope, explicit exclusions, accountable human owner, requester, intended audience, and decision needed.
- Supplied static evidence with provenance, source period, freshness, completeness, and limitations.
- Relevant constraints, assumptions, dependencies, approval requirements, and reviewer independence.

## Preconditions

The task is repository-local or based on supplied static evidence. No live system action, authentication, external connection, scan, exploit, deployment, publication, or authoritative approval is requested.

## Procedure

1. Restate scope, exclusions, owner, evidence inventory, assumptions, and required human decision.
2. Select one primary role from: soc-governance-telemetry-agent, detection-triage-hunting-agent, intelligence-malware-automation-agent, coverage-quality-assurance-agent, incident-escalation-reviewer.
3. Map evidence to each relevant workflow requirement and mark missing, stale, partial, contradictory, or unverifiable evidence.
4. Produce the requested artifact with confirmed facts, probable findings, hypotheses, not reproduced items, false positives, accepted risks, insufficient evidence, and not-applicable criteria separated.
5. Identify human-only decisions and approval gates before any recommendation can be treated as final.
6. Route high-impact, closure, exception, external-facing, or executive outputs to an independent reviewer that did not create the artifact.
7. Return a completion record with residual risk, confidence, limitations, open questions, and blocked validations.

## Structured Outputs

Return the artifact plus an evidence table, decision log, stop-condition review, independent-review requirement, and completion criteria. Include owners and approvers as role placeholders, not real identities.

## Quality Checks

Verify native-surface compatibility, professional coverage, evidence traceability, least-privilege behavior, no unsupported tool claims, no self-review, no circular delegation, no real secrets, no live-action claim, and no fabricated validation.

## Stop And Escalation Conditions

Stop for missing authorization, unredacted sensitive material, unsupported legal or compliance conclusion, requested live action, evidence gaps that affect a conclusion, self-review, conflict of interest, or a human-only approval request.

## Failure Behavior

Return a blocker with the missing input, affected output, risk of proceeding, safe next step, and exact human approval or evidence needed. Do not silently continue with assumptions.

## Human Review Gates

Human review is required for risk acceptance, exception approval, policy publication, architecture approval, release readiness, incident declaration or closure, external distribution, supplier decisions, offensive authorization, production recovery, or critical finding closure.

## Prohibited Actions

Do not execute code, run tools, install dependencies, authenticate, connect MCP/apps, scan, probe, exploit, deploy, publish, push, alter live records, approve decisions, accept risk, close findings, or claim validation without evidence.
