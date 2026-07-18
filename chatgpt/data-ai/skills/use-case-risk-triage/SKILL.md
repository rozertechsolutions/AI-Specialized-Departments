---
name: use-case-risk-triage
description: Use for Data and AI intake, feasibility, value, alternatives-to-AI, impact classification, ownership, routing, and stop-condition decisions.
---

# Use-Case Risk Triage

Use this skill before starting a new Data and AI effort or when ownership, feasibility, value, approval, or risk class is unclear. Do not approve your own route or fabricate missing business, data, privacy, or risk evidence.

## Procedure

1. Capture the requested outcome, users, decisions affected, delivery deadline, operating environment, expected value, and success metrics.
2. Identify whether non-AI automation, analytics, rules, search, UX, process change, or data cleanup would meet the outcome with less risk.
3. Classify data sensitivity, decision impact, automation level, user population, regulated context, external dependencies, and production proximity.
4. Assign the primary owner, required specialists, independent reviewers, human approvers, evidence expected, and completion status rule.
5. State stop conditions for missing authority, sensitive data exposure, unclear lawful/allowed use, high-impact decisions without human review, unsupported platform capability, or absent evidence.
6. Return the route, assumptions, blockers, and next owner.

## Quality Gates

- Outcome, value hypothesis, success metric, intended users, owner, and decision rights are explicit.
- Alternatives to AI are considered before model work begins.
- Risk class drives the required reviews and approvals.
- Coordinator work is separate from builder, risk, and final assurance work.
- Status is exactly `PASS`, `FAIL`, or `BLOCKED`.
