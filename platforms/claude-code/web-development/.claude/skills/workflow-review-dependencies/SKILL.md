---
name: workflow-review-dependencies
description: Run the review-dependencies workflow safely and consistently.
---

# Review Dependencies

Evaluate every proposed dependency or third-party script for necessity, provenance, maintenance, license, security, transitive impact, and runtime or bundle cost. Do not install anything.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
