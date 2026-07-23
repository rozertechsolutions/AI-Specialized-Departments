---
name: pipeline-analytics-quality
description: Review governed pipeline, data product, lineage, quality, observability, metric, BI, and reporting delivery.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - task
---

# Pipeline Analytics Quality

## Use When
A data pipeline, data product, governed metric, BI asset, semantic layer, dashboard, reporting workflow, or data-quality design needs review.

## Procedure
1. Identify inputs, outputs, consumers, owners, contracts, dependencies, orchestration design, recoverability, and change controls.
2. Review freshness, completeness, reconciliation, validity, duplication, anomaly detection, lineage, observability, SLOs, and incident diagnosis.
3. Verify metric ownership, semantic definitions, dashboard intent, reproducible queries, access controls, consumer impact, and certification/change process.
4. Distinguish observed validation from design review; do not invent runtime evidence.
5. Return status as exactly `PASS`, `FAIL`, or `BLOCKED`.

## Output
Quality gaps, lineage concerns, metric certification issues, operational risks, required evidence, blockers, and status.
