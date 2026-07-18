# Review Security And Privacy

Description: Cascade-only manual workflow for `/review-security-and-privacy`.

Use only in Cascade. Devin Local does not support workflows; use `security-privacy-review` there.

Perform an independent threat, security, privacy, CSP, cookie, CORS, tracker, and dependency review. Block completion for unresolved material findings.

## Inputs
Changed files, trust boundaries, data types, auth/session behavior, third-party services, browser policies, and logging/storage behavior.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Completion
End with PASS, FAIL, or BLOCKED. Include findings ordered by severity, exploit conditions, evidence, remediation criteria, residual risk, blocking status, and human-review requirements for sensitive changes.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
