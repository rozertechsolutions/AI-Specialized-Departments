# Pipeline, Data Product, Analytics, and Observability Delivery

1. Confirm product owner, consumers, data contracts, processing mode, SLOs, dependencies, lineage, and rollback criteria.
2. Use `data-platform-analytics-quality` to review ingestion, transformations, orchestration, reconciliation, quality rules, lineage, alerts, dashboards, semantic layers, governed metrics, and decision use.
3. Use `analytics-experiment-review` when statistical claims, experiments, metric certification, or causal interpretation are involved.
4. Require separate evidence review for quality certification and metric approval.
5. Return `PASS`, `FAIL`, or `BLOCKED` with unrun checks and unresolved risks.
