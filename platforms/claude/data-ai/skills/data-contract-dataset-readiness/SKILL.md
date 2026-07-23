---
name: data-contract-dataset-readiness
description: Review data governance, contracts, schemas, semantics, sourcing, labeling, synthetic-data controls, leakage, provenance, versioning, and dataset acceptance.
---

# Data Contract Dataset Readiness

Use this skill for any dataset, source, semantic asset, feature source, prompt corpus, embedding corpus, label set, or evaluation set proposed for Data and AI work. Avoid copying sensitive records; summarize evidence at the minimum useful level.

## Steps

1. Confirm data owner, steward, permitted use, classification, retention, consent/restriction, access policy, exception path, and privacy basis where applicable.
2. Define contract fields: producer, consumer, schema, constraints, units, freshness, completeness, allowed values, nullability, semantics, lineage, version, and change process.
3. Assess provenance, collection method, representativeness, coverage gaps, deduplication, synthetic-data controls, leakage/contamination risk, splits, and versioning.
4. For labels, define instructions, reviewer qualification, adjudication, gold set, defect taxonomy, inter-annotator target, and acceptance threshold.
5. Return acceptance status, required fixes, evidence gaps, owners, monitoring, and refresh triggers.

## Acceptance Gates

- Provenance and permitted use are available for every source.
- Contract, semantic meaning, owner, lineage, quality thresholds, and version are explicit.
- Leakage, contamination, representativeness, and synthetic-data risks are reviewed.
- Final status is `PASS`, `FAIL`, or `BLOCKED`.
