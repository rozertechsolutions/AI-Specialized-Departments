---
description: Review data contract, semantic/model design, collection, annotation, and dataset acceptance.
---

# Data Contract Dataset Acceptance

## Workflow
1. Run `data-contract-dataset-readiness`.
2. Review schemas, semantic definitions, identifiers, lineage, versioning, quality rules, labeling, annotation, synthetic controls, representativeness, splits, leakage, and contamination.
3. Require dataset card or equivalent evidence before analytics, ML, RAG, or AI application use.
4. Route governance/privacy exceptions to `data-ai-solution-governance-reviewer`.
5. Stop on missing acceptance thresholds, unresolved leakage, missing consent, or missing permitted-use evidence.

## Output
Dataset readiness decision, contract gaps, downstream obligations, acceptance thresholds, blockers, and exactly `PASS`, `FAIL`, or `BLOCKED`.
