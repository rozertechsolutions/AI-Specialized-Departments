---
name: workflow-review-security-and-privacy
description: "Guide independent security, privacy, CSP, cookie, CORS, tracker, and dependency review."
user-invocable: true
allowed-tools:
  - read
  - read_file
  - grep
  - ask_user_question
---

# Review Security And Privacy

Use this slash-command Skill to guide independent threat, security, privacy, CSP, cookie, CORS, tracker, and dependency review. Block completion for unresolved material findings. Do not edit the implementation under review.

## Expected input
Changed files, trust boundaries, data types, auth/session behavior, third-party services, browser policies, and logging/storage behavior.

## Expected output
Findings ordered by severity, exploit conditions, evidence, remediation criteria, residual risk, and NOT EXECUTED checks.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
