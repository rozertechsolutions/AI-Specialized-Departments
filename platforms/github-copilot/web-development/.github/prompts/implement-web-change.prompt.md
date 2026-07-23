---
description: Web Development implement web change workflow
---

# Implement Web Change

Validate scope, use the relevant specialist role, make only requested repository changes, preserve native conventions, record evidence, and stop before deployment, publication, Git mutation, or external side effects.

## Expected input
Requested behavior, acceptance criteria, affected files or surfaces, prohibited changes, and verification expectations.

## Recommended agent
Use `web-development-lead` for multi-surface work, `frontend-specialist` for browser-facing changes, or `backend-api-specialist` for server/API changes.

## Output and evidence
Return changed files, behavior, direct verification evidence, unresolved risks, required reviews, and checks marked PASS, FAIL, BLOCKED, NOT APPLICABLE, or NOT EXECUTED.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
