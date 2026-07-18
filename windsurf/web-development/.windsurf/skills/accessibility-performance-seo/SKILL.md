---
name: accessibility-performance-seo
description: Assess accessibility, performance, responsive behavior, and SEO as one user-facing quality review.
---

# Accessibility Performance Seo

## Mission
Assess accessibility, performance, responsive behavior, and SEO as one user-facing quality review.

## Invocation and surface
- Cascade: Invoke with `@accessibility-performance-seo` or allow Cascade to select it when accessibility, responsive behavior, performance, SEO, metadata, or user-impact evidence is relevant.
- Devin Local: Compatible as a project skill; invoke with `/accessibility-performance-seo` when using Devin Local.
- Not a workflow, hook, MCP server, external scanner, browser automation, or independent agent.

## Inputs and preconditions
Reviewed files or components, target user flows, acceptance criteria, supported browsers or viewport constraints, available measurements, and any prohibited changes.

## Expected output and evidence
Prioritized findings with severity, affected users, evidence, acceptance criteria, measurement gaps, unresolved risks, and gates marked PASS, FAIL, BLOCKED, NOT APPLICABLE, or NOT EXECUTED.

## Stop conditions
Stop with BLOCKED when required browser, measurement, accessibility, responsive, or SEO evidence is missing for a completion claim.

## Required procedure
1. Apply WCAG-oriented semantic, keyboard, focus, name/role/value, contrast, zoom, motion, and error-identification checks where applicable.
2. Review critical rendering, asset weight, caching, loading strategy, Core Web Vitals risks, and performance budgets.
3. Review titles, metadata, canonical/indexing controls, structured data, and crawlability only where relevant.
4. Separate measured evidence from recommendations.
5. Return prioritized findings with severity, evidence, affected users, and acceptance criteria.

## Output contract
- State confirmed scope and evidence.
- Separate facts, assumptions, risks, and unresolved decisions.
- List files or components affected or reviewed.
- State which quality gates are PASS, FAIL, BLOCKED, or NOT APPLICABLE.
- Do not claim execution or success without direct evidence.

## Prohibited actions
- Do not run commands, install packages, mutate Git state, deploy, publish, authenticate, handle secrets, spend money, sign artifacts, or perform destructive operations without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
