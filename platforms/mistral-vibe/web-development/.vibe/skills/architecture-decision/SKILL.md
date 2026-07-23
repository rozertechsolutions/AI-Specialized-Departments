---
name: architecture-decision
description: "Create a proportionate architecture decision for a web change."
user-invocable: true
allowed-tools:
  - read
  - read_file
  - grep
  - ask_user_question
---

# Architecture Decision

## Mission
Create a proportionate architecture decision for a web change.

## Vibe invocation
Invoke with `/architecture-decision` for material interface, rendering, data-flow, integration, migration, rollback, or full-stack trade-off decisions. This Skill produces a decision record in the conversation only.

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
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
