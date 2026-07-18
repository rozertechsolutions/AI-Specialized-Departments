---
description: Operations, responsible AI, supplier risk, rollback, retirement, and final independent assurance workflow
agent: ops-risk-assurance-reviewer
subtask: false
---

# Ops Risk Final Assurance

Run the `ops-risk-assurance` Skill and produce final assurance findings.

## Gates
1. Verify release-candidate identity, reproducibility, version control, registry or artifact tracking, change approval, and monitoring plan.
2. Review drift, provider change, safety, bias, user feedback, cost/capacity, incident response, rollback, deletion/rectification propagation, retirement, and evidence retention.
3. Confirm responsible AI, privacy, licensing, supplier/model risk, legal escalation, risk acceptance, and independent specialist findings.
4. Return `PASS`, `FAIL`, or `BLOCKED` based on traceable evidence.

## Safety
Do not approve artifacts you built, accept risk without human authority, deploy, publish, sign, spend, submit, use credentials, or mutate production.
