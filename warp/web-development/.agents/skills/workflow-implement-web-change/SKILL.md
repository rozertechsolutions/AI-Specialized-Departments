---
name: workflow-implement-web-change
description: Guide scoped web implementation for local Warp agents.
---

# Implement Web Change

Guide scoped web implementation after approval boundaries are clear. Preserve native conventions, make only requested repository changes, record evidence, and stop before deployment, publication, Git mutation, terminal command execution, or external side effects.

## Expected input
Requested behavior, acceptance criteria, affected files or surfaces, prohibited changes, and verification expectations.

## Required output
Changed files or proposed changes, behavior, direct verification evidence, required reviews, unresolved risks, required human approvals, and NOT EXECUTED checks.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
