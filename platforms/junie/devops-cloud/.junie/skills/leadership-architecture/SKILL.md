---
name: leadership-architecture
description: Use for DevOps and Cloud request triage, target architecture, ADRs, technology tradeoff analysis, exception review, dependency routing, and static Well-Architected assessment.
---
# Leadership Architecture Skill

Use this skill only for section 01 leadership and architecture work. Keep the work provider-neutral until requirements justify a provider or product.

## Procedure
1. Classify the request with `devops-cloud-request-triage`: objective, urgency, environment class, affected owners, constraints, dependencies, required approvals, and evidence.
2. Route to one primary owner: Orchestrator for coordination or Cloud and Platform Architect for architecture decisions.
3. For architecture work, perform `cloud-architecture-assessment`: current assumptions, target state, ownership model, guardrails, risks, and handoffs.
4. For decisions, produce an `architecture-decision-record` with context, alternatives, tradeoffs, risks, selected direction, owner, status, review trigger, and human approval need.
5. For technology choices, use `technology-selection-and-tradeoff-analysis`: requirements first, vendor/product second. Do not select a provider from preference alone.
6. For reviews, run a static `well-architected-review` across operations, security, reliability, performance, cost, and sustainability.

## Stop criteria
Stop on missing requirements, secret exposure, requested runtime execution, real cloud identifiers, unsupported platform mechanisms, duplicated ownership, circular delegation, or unresolved human approval.

Reference: `docs/leadership-architecture-workflows.md`.

## Evidence
Return only static evidence: assumptions, files inspected, decisions produced, risks, handoffs, approvals needed, and checks not run.
