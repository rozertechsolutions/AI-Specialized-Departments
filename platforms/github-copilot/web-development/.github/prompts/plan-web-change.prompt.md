---
description: Web Development plan web change workflow
---

# Plan Web Change

Discover the stack and requirements, define ownership, compare material approaches, identify risks, and produce an implementation plan with explicit verification gates. Do not modify files during planning.

## Expected input
Goal, constraints, affected product surfaces, known risks, deadline or sequencing needs, and any prohibited changes.

## Recommended agent
Use `web-development-lead` for coordination or `web-architecture-specialist` when material architecture decisions are expected.

## Output and evidence
Return confirmed facts, assumptions, decision points, phased plan, required reviews, validation gates, and checks marked PASS, FAIL, BLOCKED, NOT APPLICABLE, or NOT EXECUTED.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
