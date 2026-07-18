# Review Api And Auth

Description: Cascade-only manual workflow for `/review-api-and-auth`.

Use only in Cascade. Devin Local does not support workflows; use `backend-api-auth` or `security-privacy-review` skills there.

Review API contracts, validation, authentication, authorization, session and token handling, data access, rate limits, error leakage, and negative tests. Return findings without self-approval.

## Inputs
API routes, auth/session behavior, data flows, contracts, relevant files, and expected negative paths.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Completion
End with PASS, FAIL, or BLOCKED. Include findings with severity, affected files or flows, evidence, remediation criteria, residual risk, required reviews, and human-review requirements for sensitive changes.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
