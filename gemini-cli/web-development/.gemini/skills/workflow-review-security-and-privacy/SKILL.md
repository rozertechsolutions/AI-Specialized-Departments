---
name: workflow-review-security-and-privacy
description: Run the review-security-and-privacy Gemini CLI workflow with Web Development safety and evidence gates.
---

# Review Security And Privacy

## Trigger boundary
Use for an independent security or privacy gate after relevant design or implementation work. Do not use as a substitute for human risk acceptance.

Perform an independent threat, security, privacy, CSP, cookie, CORS, tracker, and dependency review. Block completion for unresolved material findings.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.
