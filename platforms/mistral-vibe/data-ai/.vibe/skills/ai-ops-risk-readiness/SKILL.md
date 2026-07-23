---
name: ai-ops-risk-readiness
description: Review MLOps, LLMOps, monitoring, drift, provider changes, incidents, rollback, retirement, supplier risk, and operational readiness.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - task
---

# AI Ops Risk Readiness

## Use When
An ML, GenAI, RAG, agent, or AI application release candidate needs operational readiness, monitoring, supplier risk, change, incident, rollback, or retirement review.

## Procedure
1. Verify release-candidate identity, artifact lineage, configuration/version control, owner model, change approval, reproducibility, and evidence retention.
2. Review monitoring for data quality, drift, provider/model changes, performance, cost/capacity, safety, bias, feedback, incidents, and near misses.
3. Check rollback, graceful degradation, corrective action, deletion/rectification propagation, retirement, and human escalation paths.
4. Assess supplier/provider risk, licensing, privacy, misuse, legal escalation, and risk acceptance authority.
5. Return status as exactly `PASS`, `FAIL`, or `BLOCKED`.

## Output
Operational readiness decision, residual risks, monitoring gaps, rollback/retirement gaps, approvals needed, blockers, and status.
