---
description: Deliver governed pipeline, data product, lineage, quality, observability, metric, BI, and reporting review.
---

# Pipeline Analytics Quality

1. Run `pipeline-analytics-quality`.
2. `data-platform-analytics-reviewer` reviews owners, inputs, outputs, dependencies, orchestration design, recoverability, quality rules, lineage, observability, SLOs, dashboards, semantic layers, and metric certification.
3. Route source/contract concerns to `data-architecture-dataset-reviewer`.
4. Route operational monitoring and rollback concerns to `ops-risk-assurance-reviewer`.
5. Stop on missing owners, unverifiable lineage, ungoverned metric definitions, or fabricated validation results.

Return quality findings, lineage/observability gaps, metric concerns, operational risks, blockers, and exactly `PASS`, `FAIL`, or `BLOCKED`.
