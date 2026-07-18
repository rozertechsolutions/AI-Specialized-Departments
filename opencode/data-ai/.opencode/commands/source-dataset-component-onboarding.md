---
description: Onboard a data source, dataset, third-party model, provider, or component with provenance and permitted-use evidence.
---

# Source Dataset Component Onboarding

## Workflow
1. `data-ai-orchestrator` classifies the source, dataset, model, provider, or component and routes ownership.
2. `data-architecture-dataset-reviewer` verifies provenance, permitted use, contracts, sensitivity, lineage, and acceptance obligations.
3. `data-ai-solution-governance-reviewer` reviews privacy, governance, supplier/legal escalation, and policy exceptions.
4. `ops-risk-assurance-reviewer` reviews supplier/model risk, lifecycle obligations, monitoring, rollback, deletion propagation, and evidence retention.
5. Stop on missing provenance, missing permitted use, private endpoint exposure, credential requirement, or unsupported integration.

## Output
Onboarding decision, ownership, constraints, required controls, residual risk, human approvals, blockers, and exactly `PASS`, `FAIL`, or `BLOCKED`.
