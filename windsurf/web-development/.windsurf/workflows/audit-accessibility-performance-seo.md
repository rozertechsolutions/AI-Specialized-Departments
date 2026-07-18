# Audit Accessibility Performance Seo

Description: Cascade-only manual workflow for `/audit-accessibility-performance-seo`.

Use only in Cascade. Devin Local does not support workflows; use the `accessibility-performance-seo` skill there.

Perform an evidence-based accessibility, responsive, performance, and SEO review. Separate blocking defects from recommendations and identify missing measurements.

## Inputs
Files, feature area, URL or component names, acceptance criteria, supported browsers, and any measurements already available.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Completion
End with PASS, FAIL, or BLOCKED. Include direct evidence, missing measurements, unresolved risks, and human-review requirements for sensitive changes.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
