---
name: workflow-review-security-and-privacy
description: Run the review-security-and-privacy workflow safely and consistently.
---

# Review Security And Privacy

Perform an independent threat, security, privacy, CSP, cookie, CORS, tracker, and dependency review. Block completion for unresolved material findings.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
