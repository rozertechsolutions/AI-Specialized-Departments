---
description: Web Development debug web regression workflow
---

# Debug Web Regression

Reproduce from available evidence, map the execution path, form competing hypotheses, isolate the root cause, propose the smallest fix, define regression checks, and avoid speculative broad rewrites.

## Expected input
Observed behavior, expected behavior, changed files or commits, environment, reproduction steps, and relevant logs or screenshots.

## Recommended agent
Start with `web-development-lead` for coordination or select the relevant implementation specialist directly if the failing surface is known.

## Output and evidence
Return confirmed facts, hypotheses rejected, root cause evidence, minimal fix plan, regression checks, and checks marked PASS, FAIL, BLOCKED, NOT APPLICABLE, or NOT EXECUTED.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
