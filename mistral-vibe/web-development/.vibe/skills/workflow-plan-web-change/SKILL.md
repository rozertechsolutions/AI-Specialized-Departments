---
name: workflow-plan-web-change
description: "Guide web change planning with stack discovery, ownership, risks, and verification gates."
user-invocable: true
allowed-tools:
  - read
  - read_file
  - grep
  - ask_user_question
  - task
---

# Plan Web Change

Use this slash-command Skill to guide planning. Discover the stack and requirements, define ownership, compare material approaches, identify risks, and produce an implementation plan with explicit verification gates. Do not modify files during planning.

## Expected input
Goal, constraints, affected product surfaces, known risks, selected Vibe agent, and prohibited changes.

## Expected output
Confirmed facts, assumptions, decision points, role ownership, phased plan, required reviews, validation gates, and NOT EXECUTED checks.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
