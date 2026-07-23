---
name: responsible-ai-assurance
description: Perform independent responsible AI, model risk, evidence, separation-of-duties, and final assurance review.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - task
---

# Responsible AI Assurance

## Use When
A Data or AI deliverable needs final independent assurance, responsible AI review, model risk review, evidence validation, risk acceptance packet, or completion decision.

## Procedure
1. Confirm independence, reviewed artifact, builders, reviewers, owners, risk owner, human approval gates, and scope boundaries.
2. Trace every applicable requirement to evidence, validation result, owner, threshold, unresolved risk, monitoring, rollback, documentation, and closure decision.
3. Verify fairness, explainability, privacy, licensing, misuse, supplier/model risk, legal escalation, contestability, appeals, override, accessibility, training, and automation-bias controls where applicable.
4. Block completion for missing provenance, missing permitted-use evidence, fabricated metrics, unresolved critical findings, unsupported simulated capabilities, or separation-of-duties conflicts.
5. Return status as exactly `PASS`, `FAIL`, or `BLOCKED`.

## Output
Assurance decision, findings, residual risk, required human decisions, evidence gaps, waiver requirements, blockers, and status.
