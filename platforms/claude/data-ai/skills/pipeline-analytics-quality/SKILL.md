---
name: pipeline-analytics-quality
description: Design and review data products, pipelines, quality rules, lineage, observability, governed metrics, BI assets, and reproducible analytics.
---

# Pipeline Analytics Quality

Use this skill for data products, analytical models, dashboards, governed metrics, lineage reviews, observability design, and data-quality incidents. Do not claim runtime state without supplied evidence.

## Steps

1. Define asset purpose, consumers, owner, source contracts, transformation logic, refresh cadence, storage expectations, SLOs, and recoverability.
2. Specify quality checks for freshness, completeness, validity, uniqueness, reconciliation, schema drift, anomalies, and lineage.
3. For metrics and BI, define grain, filters, exclusions, semantic-layer ownership, certification criteria, reproducibility, and change control.
4. Review operational readiness: monitoring, alert routing, incident severity, backfill, rollback, dependency failure, and rectification/deletion propagation.
5. Return certification status, unresolved findings, evidence needed, owners, risks, and re-review trigger.

## Acceptance Gates

- Asset ownership, consumers, contracts, SLOs, lineage, quality thresholds, and change process are explicit.
- Metrics are governed and reproducible.
- Observability and incident response are defined before certification.
- Final status is `PASS`, `FAIL`, or `BLOCKED`.
