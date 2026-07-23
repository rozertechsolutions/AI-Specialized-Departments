---
name: workflow-verify-release-readiness
description: Run the verify-release-readiness workflow with Web Development safety and evidence gates.
---

# Verify Release Readiness

Trace requirements to repository evidence, verify all required reviews, list unresolved risks, and issue PASS, FAIL, BLOCKED, or NOT APPLICABLE. Never deploy or publish.

## Trigger boundary
Use as the final static release-readiness workflow after implementation and applicable reviews. Do not use to perform release actions.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
