# Plan Web Change

Description: Cascade-only manual workflow for `/plan-web-change`.

Use only in Cascade. Devin Local does not support workflows; use `stack-discovery` or `architecture-decision` skills there.

Discover the stack and requirements, define ownership, compare material approaches, identify risks, and produce an implementation plan with explicit verification gates. Do not modify files during planning.

## Inputs
Goal, constraints, affected product surfaces, known risks, prohibited changes, and required approvals.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Completion
End with PASS, FAIL, or BLOCKED. Include confirmed facts, assumptions, decision points, role ownership, phased plan, validation gates, required reviews, unresolved risks, and human-review requirements.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
