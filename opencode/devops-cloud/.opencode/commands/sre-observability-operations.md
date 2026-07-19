---
description: Static SRE, observability, SLO, alert, incident, postmortem, and toil workflows.
agent: site-reliability-engineer
subtask: true
---

# SRE, Observability and Operations Workflows

## service-operational-readiness
1. Review ownership, SLOs, telemetry, alerts, runbooks, escalation, on-call, dependencies, and known risks.
2. Identify missing readiness evidence without querying production systems.
3. Return blockers and handoffs.

## slo-definition
1. Define user or service outcome, SLI, SLO target, measurement window, error budget, owner, and review cadence.
2. Confirm measurability and evidence limitations.
3. Require human approval for SLO/error-budget adoption.

## observability-design
1. Define logs, metrics, traces, profiles, correlation, retention, dashboards, and data quality.
2. Map OpenTelemetry and monitoring stack choices only from requirements.
3. Keep integrations disabled and static.

## alert-review
1. Check objective linkage, owner, actionability, severity, paging criteria, runbook, suppression, and escalation.
2. Reject noisy or ownerless alerts.
3. Do not change alerting systems.

## operational-incident-response
1. Define command structure, roles, severity, communications, timeline, evidence capture, and escalation.
2. Route security incident command to Cybersecurity.
3. Do not mutate real incidents or page responders.

## postmortem-and-follow-up
1. Build an evidence-based, blameless timeline and impact summary.
2. Identify contributing factors, corrective actions, owners, and due dates.
3. Avoid blame and unverifiable claims.

## toil-reduction
1. Identify repetitive manual work, frequency, owner, risk, and automation or process options.
2. Prioritize by reliability impact and effort.
3. Hand off implementation to the appropriate owner.
