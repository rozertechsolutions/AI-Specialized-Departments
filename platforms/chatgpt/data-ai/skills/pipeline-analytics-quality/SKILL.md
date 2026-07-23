---
name: pipeline-analytics-quality
description: Use for data products, pipeline design, quality rules, lineage, observability, governed metrics, BI, analytics engineering, decision intelligence, and reproducible reporting.
---

# Pipeline Analytics Quality

Use this skill for governed data product delivery, analytics assets, metric changes, dashboard/report logic, quality incidents, lineage review, and data observability design. Infrastructure provisioning and production deployment belong outside this specialization.

## Procedure

1. Define the data product or analytics asset, consumers, owner, SLA/SLO, source contracts, transformations, storage expectations, refresh cadence, and recoverability requirements.
2. Specify quality rules for freshness, completeness, validity, uniqueness, reconciliation, anomaly detection, schema drift, lineage, and incident severity.
3. For metrics and BI, define the business definition, grain, filters, exclusions, semantic layer ownership, certification criteria, reproducibility, and change-control process.
4. Assess operational readiness: monitoring, alert routing, runbook expectations, backfill strategy, rollback criteria, dependency failures, and data rectification/deletion propagation.
5. Identify evidence required from tests, profile results, lineage checks, metric reconciliation, user acceptance, and independent review.
6. Return certification status, unresolved findings, risks, owner actions, and next review trigger.

## Quality Gates

- Each asset has an owner, consumers, contract, quality thresholds, lineage expectations, and change process.
- Metrics are governed, reproducible, and traceable to source logic.
- Observability covers freshness, completeness, validity, anomaly detection, lineage, and incident handling.
- Runtime claims are made only when evidence is provided.
- Status is exactly `PASS`, `FAIL`, or `BLOCKED`.
