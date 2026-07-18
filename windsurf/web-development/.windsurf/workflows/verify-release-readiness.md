# Verify Release Readiness

Description: Cascade-only manual workflow for `/verify-release-readiness`.

Use only in Cascade. Devin Local does not support workflows; use `release-readiness` there.

Trace requirements to repository evidence, verify all required reviews, list unresolved risks, and issue PASS, FAIL, or BLOCKED. Never deploy or publish.

## Inputs
Acceptance criteria, changed files, role handoffs, review outcomes, validation evidence, known exclusions, and release constraints.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Completion
End with PASS, FAIL, or BLOCKED. Include gate-by-gate evidence, unresolved risks, required human approvals, human-review requirements, and NOT EXECUTED checks.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
