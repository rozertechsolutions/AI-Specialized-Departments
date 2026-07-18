---
name: workflow-review-api-and-auth
description: Guide API and auth review for local Warp agents.
---

# Review Api And Auth

Guide API, authentication, authorization, session, token, data-access, rate-limit, error-leakage, and negative-path review. Return findings without self-approval. This Skill does not run tests by itself.

## Expected input
API routes, auth/session behavior, data flows, contracts, relevant files, and expected negative paths.

## Required output
Findings with severity, affected files or flows, evidence, remediation criteria, residual risk, required reviews, and NOT EXECUTED checks.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
