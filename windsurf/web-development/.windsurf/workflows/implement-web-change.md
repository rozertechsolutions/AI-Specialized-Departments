# Implement Web Change

Description: Cascade-only manual workflow for `/implement-web-change`.

Use only in Cascade. Devin Local does not support workflows; use `frontend-delivery`, `backend-api-auth`, or another relevant skill there.

Validate scope, use the relevant specialist responsibility, make only requested repository changes, preserve native conventions, record evidence, and stop before deployment, publication, Git mutation, or external side effects.

## Inputs
Requested behavior, acceptance criteria, affected files or surfaces, prohibited changes, and verification expectations.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Completion
End with PASS, FAIL, or BLOCKED. Include changed files or proposed changes, behavior, direct verification evidence, required reviews, unresolved risks, and human-review requirements for sensitive changes.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
