---
name: workflow-audit-accessibility-performance-seo
description: "Guide the accessibility, performance, responsive, and SEO audit workflow with evidence and safety gates."
user-invocable: true
allowed-tools:
  - read
  - read_file
  - grep
  - ask_user_question
---

# Audit Accessibility Performance Seo

Use this slash-command Skill to guide an evidence-based accessibility, responsive, performance, and SEO review. Separate blocking defects from recommendations and identify missing measurements. This Skill coordinates review steps; it is not a deterministic command and does not execute measurements by itself.

## Expected input
Files, feature area, URL or component names, acceptance criteria, supported browsers, and any measurements already available.

## Expected output
Prioritized findings with severity, evidence, affected users, acceptance criteria, measurement gaps, and NOT EXECUTED checks.

## Gates
1. Verify inputs, scope, stack, and applicable risks.
2. Produce or inspect only the approved artifacts.
3. Request independent review for security-sensitive or release-sensitive work.
4. Record evidence for every completion claim.
5. Stop with BLOCKED if a required decision or approval is missing.

## Safety
Do not execute commands, install dependencies, mutate Git, deploy, publish, authenticate, expose secrets, or perform destructive actions automatically.
