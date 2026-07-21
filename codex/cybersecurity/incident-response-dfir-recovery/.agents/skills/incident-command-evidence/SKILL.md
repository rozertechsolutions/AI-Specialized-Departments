---
name: incident-command-evidence
description: Complete Incident Response, DFIR, and Recovery procedure for Incident Command Evidence; uses supplied static evidence, explicit human approval gates, and independent review before high-impact conclusions.
---

# Incident Command Evidence

## Use Cases

Use this Skill for Incident Response, DFIR, and Recovery work involving Incident Command Evidence. It covers these professional workflows when relevant: incident-readiness review, incident triage and declaration support, active-incident coordination plan, evidence-preservation plan, forensic-acquisition plan, containment and eradication options, secure-recovery plan, ransomware coordination, data-exposure coordination, tabletop exercise, post-incident review.

## Required Inputs

- Authorized scope, explicit exclusions, accountable human owner, requester, intended audience, and decision needed.
- Supplied static evidence with provenance, source period, freshness, completeness, confidence, and limitations.
- Known assumptions, dependencies, constraints, reviewer independence requirements, and human approval requirements.

## Preconditions

The task must be repository-local or based on user-supplied static evidence. No live system action, authentication, external connection, scan, exploit, deployment, publication, or authoritative approval may be requested.

## Procedure

1. Restate scope, exclusions, owner, evidence inventory, assumptions, dependencies, and required human decision.
2. Confirm this Skill is the right owner for the requested Incident Response, DFIR, and Recovery output and identify any required handoff to another cybersecurity area.
3. Map supplied evidence to the applicable workflow requirements and mark evidence as confirmed, probable, hypothetical, not reproduced, false positive, accepted risk, insufficient evidence, or not applicable.
4. Produce the requested artifact with facts, inferences, recommendations, residual risk, confidence, limitations, open questions, and decision points separated.
5. Identify mandatory human-only decisions before any recommendation is treated as final.
6. Route high-impact, closure, exception, external-facing, safety-relevant, or executive outputs to an independent reviewer that did not create the artifact.
7. Return a completion record with evidence used, evidence missing, residual risk, confidence, limitations, blockers, and completion criteria.

## Structured Outputs

Return the artifact plus an evidence table, assumptions log, decision log, stop-condition review, independent-review requirement, and completion criteria. Use role placeholders for owners and approvers; do not invent real identities.

## Quality Checks

Verify platform-native compatibility for codex, professional coverage, evidence traceability, no unsupported tool claims, no self-review, no circular delegation, no secrets, no live-action claim, no fabricated validation, and no hidden residual risk.

## Stop And Escalation Conditions

Stop for missing authorization, unclear scope, unredacted sensitive material, unsupported legal or compliance conclusion, requested live action, evidence gaps that affect a conclusion, self-review, conflict of interest, or a human-only approval request.

## Failure Behavior

Return a blocker with the missing input, affected output, risk of proceeding, safe next step, and exact human approval or evidence needed. Do not continue silently with assumptions.

## Human Review Gates

Human review is required for risk acceptance, exception approval, policy publication, architecture approval, release readiness, incident declaration or closure, external distribution, supplier decisions, offensive authorization, production recovery, or critical finding closure.

## Prohibited Actions

Do not execute code, run tools, install dependencies, authenticate, connect MCP/apps, scan, probe, exploit, deploy, publish, push, alter live records, approve decisions, accept risk, close findings, or claim validation without evidence.
