---
name: workflow-debug-web-regression
description: Run the debug-web-regression workflow safely and consistently.
---

# Debug Web Regression

Reproduce from available evidence, map the execution path, form competing hypotheses, isolate the root cause, propose the smallest fix, define regression checks, and avoid speculative broad rewrites.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
