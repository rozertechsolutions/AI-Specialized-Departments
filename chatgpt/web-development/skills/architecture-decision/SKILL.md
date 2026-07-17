---
name: architecture-decision
description: Use to make or review a proportionate architecture decision for a web change, including tradeoffs, contracts, risks, and rollback.
---

# Architecture Decision

## Mission
Create or review a proportionate architecture decision for a web change. This Skill is on-demand guidance for ChatGPT Skills; it does not create an automatic repository workflow.

## Use When

- The user asks for an architecture recommendation, ADR-style decision, or tradeoff analysis.
- A change affects rendering strategy, API contracts, state ownership, storage, auth/session flow, integration boundaries, deployment readiness, or long-term maintainability.
- Competing approaches need evidence-based comparison.

## Inputs

- Requirement, constraints, affected surfaces, current architecture evidence, non-goals, deadlines, risk tolerance, and any required platform or framework decisions.

## Procedure

1. Start from verified requirements and the discovered stack.
2. Compare at least two viable approaches when the decision is material.
3. Evaluate correctness, security, accessibility, performance, maintainability, migration cost, operability, and reversibility.
4. Prefer the smallest change that fits existing architecture.
5. Record decision, rejected alternatives, consequences, interfaces, and rollback considerations.

## Output Contract

- Context, decision, status, and evidence.
- Options considered, including rejected alternatives.
- Security, privacy, accessibility, performance, testing, migration, observability, and rollback implications.
- Open questions, required approvals, and quality-gate status.

## Stop Conditions

Stop and report BLOCKED when the current architecture, requirements, security constraints, data ownership, or required human decision is unknown and would materially change the recommendation.

## Prohibited Actions

- Do not invent unavailable platform features or claim runtime verification without evidence.
- Do not install dependencies, mutate code, run commands, change architecture contracts, deploy, publish, or configure external systems unless the user explicitly approves that exact action.
