---
name: data-contract-dataset-readiness
description: Review data contracts, semantic/model design, sourcing, provenance, annotation, synthetic-data controls, lineage, and dataset acceptance.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - task
---

# Data Contract Dataset Readiness

## Use When
A source, dataset, third-party data asset, semantic model, label set, synthetic dataset, RAG corpus, feature dataset, or analytics dataset needs onboarding or acceptance.

## Procedure
1. Verify ownership, provenance, lawful/permitted use, consent, retention, classification, access policy, and downstream obligations.
2. Review schemas, data contracts, identifiers, glossary terms, semantic definitions, lineage, versioning, and change control.
3. Assess collection, labeling, annotation quality, deduplication, synthetic controls, representativeness, splits, and acceptance thresholds.
4. Check leakage, contamination, missingness, freshness, completeness, consistency, bias-sensitive slices, and deletion/rectification propagation.
5. Return status as exactly `PASS`, `FAIL`, or `BLOCKED`.

## Output
Contract gaps, semantic/model risks, dataset readiness decision, downstream constraints, human approvals, blockers, and status.
