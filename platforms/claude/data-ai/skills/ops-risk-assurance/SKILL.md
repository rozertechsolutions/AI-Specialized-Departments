---
name: ops-risk-assurance
description: Review MLOps/LLMOps readiness, monitoring, drift, incidents, provider/model changes, rollback, retirement, responsible AI, model risk, supplier risk, and final assurance.
---

# Operations Risk Assurance

Use this skill for operational readiness, responsible AI/model risk review, incident or near-miss analysis, model/provider change review, retirement, and final independent assurance. Do not build the artifact under approval.

## Steps

1. Confirm reviewed artifact, builder, owner, risk owner, human approvers, assurance independence, evidence available, and evidence missing.
2. Review reproducibility, version control, registry/inventory entries, release candidate criteria, monitoring signals, drift thresholds, performance, cost/capacity, safety/bias feedback, rollback, incidents, and retirement.
3. Assess responsible AI and model risk: impact, fairness, explainability, privacy, misuse, licensing, third-party provider/model/data risk, legal escalation, and risk acceptance authority.
4. Verify data/model/system cards, deletion/rectification propagation, evidence retention, waivers, unresolved findings, and re-review triggers.
5. Return findings with severity, owner, closure criteria, waiver status, monitoring obligations, and final status.

## Acceptance Gates

- Assurance independence is explicit.
- Monitoring, rollback, incident response, change control, and retirement are covered.
- Risk controls have owners, evidence, and human acceptance or escalation.
- Critical unresolved findings block `PASS`.
