---
name: workflow-review-api-and-auth
description: "Guide API, authentication, authorization, session, and negative-path review."
user-invocable: true
allowed-tools:
  - read
  - read_file
  - grep
  - ask_user_question
---

# Review Api And Auth

Use this slash-command Skill to guide API, authentication, authorization, session, token, data-access, rate-limit, error-leakage, and negative-test review. Return findings without self-approval. This Skill does not run tests by itself.

## Expected input
API routes, auth/session behavior, data flows, contracts, relevant files, and expected negative paths.

## Expected output
Findings with severity, affected files or flows, evidence, remediation criteria, residual risk, and NOT EXECUTED checks.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
