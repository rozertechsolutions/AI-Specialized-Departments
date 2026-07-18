---
name: workflow-review-api-and-auth
description: Run the review-api-and-auth Gemini CLI workflow with Web Development safety and evidence gates.
---

# Review API And Auth

## Trigger boundary
Use for independent review of backend contracts, auth, sessions, cookies, CORS, validation, or data access. Do not use for frontend-only changes with no server trust boundary.

Review API contracts, validation, authentication, authorization, session and token handling, data access, rate limits, error leakage, and negative tests. Return findings without self-approval.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.
