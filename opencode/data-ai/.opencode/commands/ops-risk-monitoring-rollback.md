---
description: Review monitoring, drift, provider/model changes, incidents, near misses, corrective action, rollback, retirement, and risk readiness.
---

# Ops Risk Monitoring Rollback

## Workflow
1. Run `ops-risk-assurance`.
2. `ops-risk-assurance-reviewer` reviews release-candidate identity, reproducibility, configuration/version control, monitoring, drift, provider changes, safety, bias, feedback, incidents, near misses, corrective actions, rollback, deletion propagation, retirement, supplier/model risk, and risk acceptance.
3. Route missing evaluation evidence to `ml-genai-evaluation-reviewer`.
4. Route governance/legal/privacy concerns to `data-ai-solution-governance-reviewer`.
5. Stop on missing monitoring thresholds, missing rollback criteria, unresolved critical risk, or absent human risk owner.

## Output
Operational readiness decision, monitoring gaps, rollback/retirement gaps, residual risk, approvals needed, blockers, and exactly `PASS`, `FAIL`, or `BLOCKED`.
