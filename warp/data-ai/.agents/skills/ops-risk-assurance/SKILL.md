---
name: ops-risk-assurance
description: Perform Data and AI operations readiness, model/provider risk review, monitoring, incident, rollback, retirement, and independent assurance checks.
---

# Operations, Risk, and Assurance

## When to use

Use for MLOps/LLMOps readiness, model/provider change, monitoring, drift, incidents, near misses, rollback, retirement, deletion/rectification propagation, responsible AI risk review, third-party risk, and final assurance.

## Instructions

1. Confirm release candidate, owners, evidence set, environments, data/model/provider versions, registry or inventory status, monitoring plan, alert owners, incident path, rollback criteria, retirement path, and evidence retention.
2. Review responsible AI, privacy, fairness, explainability, licensing, misuse, supplier/model risk, legal escalation, and risk acceptance evidence.
3. Validate readiness for drift, provider changes, cost/capacity issues, quality regressions, safety regressions, user feedback, deletion/rectification propagation, and rollback or graceful degradation.
4. Check separation of duties: final assurance cannot be performed by the builder, coordinator, or risk-control author alone.
5. Return `PASS`, `FAIL`, or `BLOCKED` with traceability, unresolved risks, waiver needs, and human decision points.
