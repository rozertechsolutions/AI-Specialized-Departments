---
name: architecture-decision
description: Create or review web architecture decisions. Use for rendering strategy, API boundaries, data flow, storage, integration, or rollback tradeoffs.
---

# Architecture Decision

## Mission
Create a proportionate architecture decision for a web change.

## Use when
- A change affects architecture, API contracts, rendering strategy, state ownership, storage, auth/session flow, integrations, or rollback.
- The user asks for tradeoffs, ADR-style output, or approach selection.

## Do not use when
- The request is a narrow implementation detail with no material architecture impact.

## Inputs
Requirement, current stack evidence, affected surfaces, constraints, non-goals, data ownership, risk tolerance, and required human decisions.

## Required procedure
1. Start from verified requirements and the discovered stack.
2. Compare at least two viable approaches when the decision is material.
3. Evaluate correctness, security, accessibility, performance, maintainability, migration cost, operability, and reversibility.
4. Prefer the smallest change that fits existing architecture.
5. Record decision, rejected alternatives, consequences, interfaces, and rollback considerations.

## Output contract
- State confirmed scope and evidence.
- Separate facts, assumptions, risks, and unresolved decisions.
- List files or components affected or reviewed.
- State which quality gates are PASS, FAIL, BLOCKED, or NOT APPLICABLE.
- Do not claim execution or success without direct evidence.

## Stop and failure behavior
Return BLOCKED when requirements, current architecture, data ownership, security constraints, or approval authority are unclear.

## Review requirements
Record decision, rejected alternatives, consequences, security/privacy/accessibility/performance impact, test expectations, migration risk, and rollback path.

## Prohibited actions
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
