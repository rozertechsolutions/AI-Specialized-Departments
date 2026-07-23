---
name: use-case-risk-triage
description: Triage a Data and AI use case for value, feasibility, alternatives to AI, impact, ownership, required evidence, and risk class.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - task
---

# Use-Case Risk Triage

## Use When
A Data or AI request needs intake, feasibility review, value framing, prioritization, alternatives-to-AI analysis, impact assessment, or initial risk classification.

## Procedure
1. Identify outcome, users, decision impact, lifecycle owner, risk owner, value hypothesis, adoption objective, and success metrics.
2. Compare non-AI, rules-based, analytics, workflow, human-process, and AI alternatives.
3. Classify data sensitivity, privacy, allowed use, external exposure, model/provider dependency, user impact, production blast radius, and required human oversight.
4. Define evidence needed for data, model, analytics, operations, responsible AI, monitoring, rollback, retirement, and assurance gates.
5. Return status as exactly `PASS`, `FAIL`, or `BLOCKED`.

## Output
Risk class, owner map, alternatives considered, evidence checklist, required specialist reviews, human-review gates, blockers, and status.
