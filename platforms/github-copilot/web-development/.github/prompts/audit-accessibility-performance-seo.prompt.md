---
description: Web Development audit accessibility performance seo workflow
---

# Audit Accessibility Performance Seo

Perform an evidence-based accessibility, responsive, performance, and SEO review. Separate blocking defects from recommendations and identify missing measurements.

## Expected input
Files, feature area, URL or component names, acceptance criteria, and any measurements already available.

## Recommended agent
Use `accessibility-performance-seo-reviewer` directly on IDE surfaces that support prompt files and custom agents. Otherwise run this prompt in the active Copilot chat and keep the result read-only.

## Output and evidence
Return prioritized findings with severity, evidence, affected users, acceptance criteria, and checks marked PASS, FAIL, BLOCKED, NOT APPLICABLE, or NOT EXECUTED.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
