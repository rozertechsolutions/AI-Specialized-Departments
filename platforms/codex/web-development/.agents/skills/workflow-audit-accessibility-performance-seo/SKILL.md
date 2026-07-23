---
name: workflow-audit-accessibility-performance-seo
description: Run the audit-accessibility-performance-seo Web Development workflow with explicit safety and verification gates.
---

# Audit Accessibility Performance Seo

Perform an evidence-based accessibility, responsive, performance, and SEO review. Separate blocking defects from recommendations and identify missing measurements.

## Trigger boundary
Use for an end-to-end quality audit of user-facing web surfaces. Do not use for implementation or release signoff.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
