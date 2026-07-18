---
name: data-platform-analytics-quality
description: Review data products, pipelines, quality, reliability, lineage, observability, governed metrics, semantic layers, BI, and decision intelligence.
---

# Data Platform and Analytics Quality

## When to use

Use for ingestion, batch/stream processing, transformation, storage design, data products, quality rules, observability, marts, dashboards, governed metrics, and analytical reporting.

## Instructions

1. Confirm data product owner, upstream/downstream contracts, processing mode, storage boundary, recoverability target, freshness SLO, and consumer impact.
2. Review transformation logic, orchestration dependencies, reconciliation, idempotency, schema evolution, backfill behavior, lineage, observability, alert ownership, incident diagnosis, and rollback criteria.
3. Validate metrics definitions, semantic layer mappings, dashboard logic, filters, cohorts, aggregation grains, decision use, reproducibility, and change-control path.
4. Separate implementation evidence from independent metric or quality certification.
5. Return `PASS`, `FAIL`, or `BLOCKED` with unverified claims, failed checks, monitoring needs, and human-review gates.
