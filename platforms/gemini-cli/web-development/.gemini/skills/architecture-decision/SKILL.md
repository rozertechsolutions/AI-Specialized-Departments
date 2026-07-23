---
name: architecture-decision
description: Create a proportionate architecture decision for a web change.
---

# Architecture Decision

## Mission
Create a proportionate architecture decision for a web change.

## Trigger boundary
Use when a material design choice affects boundaries, contracts, rendering strategy, data flow, migration, or rollback. Do not use for routine implementation details that already follow existing patterns.

## Procedure
1. Start from verified requirements and the discovered stack.
2. Compare at least two viable approaches when the decision is material.
3. Evaluate correctness, security, accessibility, performance, maintainability, migration cost, operability, and reversibility.
4. Prefer the smallest change that fits existing architecture.
5. Record decision, rejected alternatives, consequences, interfaces, and rollback considerations.

## Output
State scope, evidence, decision, alternatives rejected, affected files or interfaces, risks, unresolved questions, and PASS, FAIL, BLOCKED, or NOT APPLICABLE gates.
