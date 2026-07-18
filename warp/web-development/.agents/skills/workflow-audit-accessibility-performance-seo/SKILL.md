---
name: workflow-audit-accessibility-performance-seo
description: Guide the accessibility, performance, responsive, and SEO audit workflow for local Warp agents.
---

# Audit Accessibility Performance Seo

Guide an evidence-based accessibility, responsive, performance, and SEO review in the active local Warp conversation. Separate blocking defects from recommendations and identify missing measurements. This Skill does not run measurements, start terminals, or create Oz cloud runs.

## Expected input
Files, feature area, URL or component names, acceptance criteria, supported browsers, and any measurements already available.

## Required output
Prioritized findings with severity, affected users, evidence, acceptance criteria, measurement gaps, unresolved risks, and NOT EXECUTED checks.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
