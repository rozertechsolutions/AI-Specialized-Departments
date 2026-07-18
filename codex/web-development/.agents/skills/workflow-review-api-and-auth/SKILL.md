---
name: workflow-review-api-and-auth
description: Run the review-api-and-auth Web Development workflow with explicit safety and verification gates.
---

# Review Api And Auth

Review API contracts, validation, authentication, authorization, session and token handling, data access, rate limits, error leakage, and negative tests. Return findings without self-approval.

## Trigger boundary
Use for independent review of backend contracts, auth, sessions, cookies, CORS, validation, or data access. Do not use for frontend-only changes with no server trust boundary.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
