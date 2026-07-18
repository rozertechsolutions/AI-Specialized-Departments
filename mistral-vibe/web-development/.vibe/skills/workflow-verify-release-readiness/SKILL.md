---
name: workflow-verify-release-readiness
description: "Guide release-readiness verification without deploying or publishing."
user-invocable: true
allowed-tools:
  - read
  - read_file
  - grep
  - ask_user_question
---

# Verify Release Readiness

Use this slash-command Skill to guide release-readiness verification. Trace requirements to repository evidence, verify all required reviews, list unresolved risks, and issue PASS, FAIL, BLOCKED, or NOT APPLICABLE. Never deploy or publish.

## Expected input
Acceptance criteria, changed files, role handoffs, review outcomes, validation evidence, known exclusions, and release constraints.

## Expected output
Final PASS, FAIL, or BLOCKED verdict with gate-by-gate evidence, unresolved risks, required human approvals, and NOT EXECUTED checks.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
