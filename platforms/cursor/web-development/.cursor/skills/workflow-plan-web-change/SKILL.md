---
name: workflow-plan-web-change
description: Run the plan-web-change workflow with Web Development safety and evidence gates.
---

# Plan Web Change

Discover the stack and requirements, define ownership, compare material approaches, identify risks, and produce an implementation plan with explicit verification gates. Do not modify files during planning.

## Trigger boundary
Use when scope, approach, ownership, or verification strategy must be settled before edits. Do not use after implementation has started except to re-plan a blocked change.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
