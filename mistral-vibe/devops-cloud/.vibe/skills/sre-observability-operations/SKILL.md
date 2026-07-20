---
name: sre-observability-operations
description: Use for SLI/SLO/error-budget design, observability architecture, actionable alerts, dashboards, runbooks, incidents, postmortems, and toil assessment.
---
# SRE, Observability and Operations Skill

Use this skill for section 05 static reliability and observability design only. Do not query production systems, run monitoring stacks, page responders, mutate incidents, or claim achieved availability.

## Procedure
1. Classify the request as sli-slo-error-budget-design, observability-architecture, actionable-alert-design, dashboard-review, runbook-generation, incident-command, blameless-postmortem, toil-assessment.
2. Identify service owner, user outcome, SLI/SLO/error budget, telemetry sources, alert ownership, runbook prerequisites, escalation, incident structure, and toil-reduction path.
3. Use OpenTelemetry, Prometheus, Alertmanager, Grafana, Loki, Tempo, Jaeger, Elastic Stack, OpenSearch, cloud-native monitoring services, and optional disabled incident/on-call integrations only when justified by requirements.
4. Verify SLOs are measurable, alerts actionable and owned, runbooks safe and escalating, and postmortems evidence-based/blameless/action-oriented.
5. Return static evidence, risks, approvals needed, and checks not run.

Reference: `docs/sre-observability-operations.md`.
