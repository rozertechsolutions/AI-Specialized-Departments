---
name: data-contract-dataset-readiness
description: Review data contracts, semantic models, sourcing, annotation, synthetic data controls, lineage, and dataset acceptance.
---

# Data Contract and Dataset Readiness

Use this Skill before relying on data for analytics, ML, GenAI, RAG, evaluation, or production decisions.

## Procedure
1. Verify source ownership, provenance, permitted use, retention, consent, classification, access policy, and policy exceptions.
2. Review schemas, data contracts, semantic definitions, identifiers, joins, lineage, master/reference data, and versioning.
3. Assess collection, labeling, annotation guidance, annotation quality, deduplication, synthetic data controls, representativeness, and split strategy.
4. Check leakage, contamination, missingness, freshness, completeness, consistency, outliers, bias-sensitive slices, and known exclusions.
5. Confirm acceptance thresholds, validation evidence, documentation, unresolved risks, and downstream consumers.
6. Return `PASS`, `FAIL`, or `BLOCKED` with contract changes, dataset gaps, and approval needs.

Do not invent profiling results or treat sample inspection as full dataset validation.
