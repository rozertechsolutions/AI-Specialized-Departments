---
name: data-contract-dataset-readiness
description: Use for data governance, contracts, schemas, semantic modeling, sourcing, labeling, synthetic-data controls, provenance, leakage checks, and dataset acceptance.
---

# Data Contract And Dataset Readiness

Use this skill when a source, dataset, semantic asset, label set, prompt corpus, embedding corpus, feature source, or evaluation set is proposed or changed. Do not copy sensitive records into the response; summarize only the minimum necessary evidence.

## Procedure

1. Confirm data owner, steward, permitted use, lawful basis where applicable, classification, retention, consent or restriction, access policy, and exception path.
2. Define the data contract: producer, consumer, schema, units, constraints, freshness, completeness, nullability, allowed values, semantics, lineage, versioning, and change notice.
3. Review source provenance, collection method, deduplication, representativeness, coverage gaps, bias risks, leakage/contamination risk, synthetic-data controls, and split strategy.
4. For labeling or annotation, define instructions, reviewer qualification, inter-annotator agreement target, adjudication, gold set, defect taxonomy, and acceptance threshold.
5. For semantic systems, define entities, relationships, taxonomy/ontology terms, master/reference data, identifiers, interoperability assumptions, and stewardship.
6. Return an acceptance decision, required fixes, evidence gaps, owners, and monitoring or refresh requirements.

## Quality Gates

- Provenance and permitted use are present for every source.
- Contract fields, semantics, lineage, version, ownership, quality thresholds, and change process are explicit.
- Leakage, contamination, representativeness, and synthetic-data risks are assessed before use.
- Dataset acceptance is independent of the builder when used for model or evaluation release.
- Status is exactly `PASS`, `FAIL`, or `BLOCKED`.
