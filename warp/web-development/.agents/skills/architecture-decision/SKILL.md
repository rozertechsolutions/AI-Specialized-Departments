---
name: architecture-decision
description: Create a proportionate architecture decision for a web change.
---

# Architecture Decision

## Mission
Create a proportionate architecture decision for a web change.

## Warp invocation
Invoke manually as `/architecture-decision` or let the local Warp agent load it for material web architecture, rendering, interface, data-flow, integration, migration, or rollback decisions.

## Inputs
Confirmed requirements, discovered stack, affected files or interfaces, constraints, alternatives, and operational or migration concerns.

## Expected output
Decision, alternatives considered, rationale, consequences, affected interfaces, migration and rollback notes, evidence, unresolved risks, and NOT EXECUTED checks.

## Stop conditions
Stop with BLOCKED when requirements, interface ownership, migration authority, or required human approvals are missing.

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

## Prohibited actions
- Do not run commands, install packages, mutate Git state, deploy, publish, authenticate, handle secrets, spend money, sign artifacts, or perform destructive operations without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
