---
trigger: model_decision
description: Apply for SLI/SLO/error-budget design, observability architecture, alerts, dashboards, runbooks, incidents, postmortems, and toil.
---

# SRE, Observability, and Operations Rule

Use for Section 05 reliability and operations design. Primary owners:

- Site Reliability Engineer: SLIs, SLOs, error budgets, operational readiness, incident command design, postmortems, toil reduction, on-call design, and reliability backlog.
- Observability Engineer: OpenTelemetry, Prometheus, Grafana, Loki, Tempo, Jaeger, Elastic, OpenSearch, metrics, logs, traces, profiles, dashboards, alerts, correlation, retention, and data quality.

SLOs must be measurable, alerts actionable and owned, runbooks safe and escalating, postmortems blameless and evidence-based, and toil work tied to operational value.

Do not query production systems, page responders, mutate incidents, run observability stacks, trigger integrations, or claim achieved availability.

Use `@sre-observability-operations` for detailed procedures.
