# Review Dependencies

Description: Cascade-only manual workflow for `/review-dependencies`.

Use only in Cascade. Devin Local does not support workflows; use `dependency-supply-chain-review` there.

Evaluate every proposed dependency or third-party script for necessity, provenance, maintenance, license, security, transitive impact, and runtime or bundle cost. Do not install anything.

## Inputs
Package names, version changes, lockfile or manifest changes, external scripts, SDKs, plugins, CDN assets, and intended use.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Completion
End with PASS, FAIL, or BLOCKED. Include approve, reject, or human-review-required status with evidence, affected files, runtime impact, unresolved risk, and human-review requirements for dependency or third-party changes.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
