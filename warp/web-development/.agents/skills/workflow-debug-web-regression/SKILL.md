---
name: workflow-debug-web-regression
description: Guide web regression debugging for local Warp agents.
---

# Debug Web Regression

Guide regression debugging from available evidence. Map the execution path, form competing hypotheses, isolate the root cause, propose the smallest fix, define regression checks, and avoid speculative broad rewrites. This Skill does not execute reproduction steps by itself.

## Expected input
Observed behavior, expected behavior, changed files or commits, environment, reproduction steps, and relevant logs or screenshots.

## Required output
Confirmed facts, hypotheses rejected, root cause evidence, minimal fix plan, regression checks, unresolved risks, and NOT EXECUTED checks.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
