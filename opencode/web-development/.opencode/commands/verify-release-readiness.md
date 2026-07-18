---
description: Guide release-readiness verification through the primary web lead.
agent: web-development-lead
subtask: false
---

# Verify Release Readiness

Coordinate release-readiness verification. The lead must invoke `quality-release-reviewer` after required implementation and independent review evidence exists. Never deploy or publish.

## Expected input
Acceptance criteria, changed files, role handoffs, review outcomes, validation evidence, known exclusions, and release constraints.

## Required output
Return final PASS, FAIL, or BLOCKED verdict with gate-by-gate evidence, unresolved risks, required human approvals, and NOT EXECUTED checks.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
