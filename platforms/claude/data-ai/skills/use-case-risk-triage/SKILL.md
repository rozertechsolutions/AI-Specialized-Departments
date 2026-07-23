---
name: use-case-risk-triage
description: Intake Data and AI requests; assess feasibility, value, alternatives to AI, impact, risk class, owner, approval gates, and stop conditions.
---

# Use-Case Risk Triage

Use this skill for new Data and AI requests or ambiguous ownership, value, feasibility, impact, or approval. Do not approve your own routing decision.

## Steps

1. Capture outcome, intended users, decision affected, current process, proposed automation level, deadline, owner, expected value, and success metric.
2. Compare AI, non-AI automation, analytics, rules, search, UX, workflow, and data-quality alternatives.
3. Classify data sensitivity, user impact, regulated context, production proximity, external dependencies, reversibility, and human oversight needs.
4. Assign primary owner, builders, reviewers, risk owner, human approvers, assurance owner, evidence requirements, and stop conditions.
5. Return route, blockers, assumptions, and next action.

## Acceptance Gates

- Outcome, owner, value hypothesis, success metric, and intended users are explicit.
- Alternative-to-AI assessment is complete.
- High-impact or sensitive work has human review and risk ownership.
- Final status is `PASS`, `FAIL`, or `BLOCKED`.
