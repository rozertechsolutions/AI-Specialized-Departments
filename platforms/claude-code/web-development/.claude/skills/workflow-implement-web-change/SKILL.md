---
name: workflow-implement-web-change
description: Run the implement-web-change workflow safely and consistently.
---

# Implement Web Change

Validate scope, use the relevant specialist role, make only requested repository changes, preserve native conventions, record evidence, and stop before deployment, publication, Git mutation, or external side effects.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
