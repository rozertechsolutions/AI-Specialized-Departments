---
name: ops-risk-assurance
description: Use for MLOps and LLMOps readiness, monitoring, drift, incidents, rollback, retirement, responsible AI, model risk, supplier risk, and independent Data and AI assurance.
---

# Operations Risk Assurance

Use this skill for release-readiness review, operational monitoring design, incident/near-miss response, provider/model change review, responsible AI/model risk review, retirement, and final independent assurance. Do not build the artifact being approved.

## Procedure

1. Confirm independence, reviewed artifact, builder, owner, risk owner, human approvers, evidence available, and evidence missing.
2. Review reproducibility, configuration/version control, registry or inventory entries, release candidate criteria, monitoring signals, drift thresholds, safety/bias feedback, cost/capacity signals, rollback path, incident process, and retirement criteria.
3. Review responsible AI/model risk: impact, fairness, explainability, privacy, misuse, licensing, external model/data/provider risk, supplier risk, legal escalation, and risk acceptance authority.
4. Verify deletion/rectification propagation, retention, documentation, model/system/data cards, waivers, unresolved findings, and re-review triggers.
5. For incidents or near misses, classify severity, affected data/model/users, containment, corrective action, regression tests, communication needs, and rollback or suspension criteria.
6. Return final status with findings, evidence references, owners, closure criteria, approved waivers, and next monitoring or assurance action.

## Quality Gates

- Independent assurance did not create the artifact it reviews.
- Release readiness includes monitoring, rollback, incident response, change control, and retirement requirements.
- Responsible AI and supplier/model risks have owners, controls, evidence, and explicit acceptance or escalation.
- Critical findings block `PASS` unless a human risk owner grants a documented waiver.
- Status is exactly `PASS`, `FAIL`, or `BLOCKED`.
