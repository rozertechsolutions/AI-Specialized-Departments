# Debug Web Regression

Description: Cascade-only manual workflow for `/debug-web-regression`.

Use only in Cascade. Devin Local does not support workflows; use a relevant skill there.

Reproduce from available evidence, map the execution path, form competing hypotheses, isolate the root cause, propose the smallest fix, define regression checks, and avoid speculative broad rewrites.

## Inputs
Observed behavior, expected behavior, changed files or commits, environment, reproduction steps, and relevant logs or screenshots.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Completion
End with PASS, FAIL, or BLOCKED. Include confirmed facts, hypotheses rejected, root cause evidence, minimal fix plan, regression checks, and human-review requirements for sensitive changes.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
