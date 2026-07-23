---
description: Guide independent security and privacy review through the primary web lead.
agent: web-development-lead
subtask: false
---

# Review Security And Privacy

Coordinate independent threat, security, privacy, CSP, cookie, CORS, tracker, and dependency review. The lead must invoke `security-privacy-reviewer` and must not close its own findings.

## Expected input
Changed files, trust boundaries, data types, auth/session behavior, third-party services, browser policies, and logging/storage behavior.

## Required output
Return findings ordered by severity, exploit conditions, evidence, remediation criteria, residual risk, blocking status, and NOT EXECUTED checks.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
