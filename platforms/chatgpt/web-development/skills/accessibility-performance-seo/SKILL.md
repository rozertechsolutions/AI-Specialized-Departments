---
name: accessibility-performance-seo
description: Use for an independent web review of accessibility, performance, responsive behavior, resilience, and SEO evidence before completion or release.
---

# Accessibility, Performance, And SEO Review

## Mission
Provide an independent user-facing quality review for a web change. This Skill is on-demand reference material for ChatGPT Skills; it is not a repository hook and does not run automatically.

## Use When

- The user asks for accessibility, performance, responsive-design, resilience, or SEO review.
- A frontend or full-stack change is near completion and needs independent user-impact assessment.
- A release-readiness check needs evidence for these gates.

## Inputs

- Requested scope and target users.
- Relevant UI files, routes, screenshots, specs, browser observations, Lighthouse/Web Vitals data, test output, or user-provided evidence.
- Supported browsers, device classes, performance budgets, SEO/indexing expectations, and known constraints when available.

## Procedure

1. Confirm scope, available evidence, and missing evidence.
2. Check semantics, keyboard operation, focus order, visible focus, name/role/value, labels, error identification, contrast, zoom, reduced motion, and assistive-technology risk where applicable.
3. Check responsive layout, loading states, empty states, error states, degradation, asset weight, caching, critical rendering, Core Web Vitals risk, and performance budgets where applicable.
4. Check titles, descriptions, canonical/indexing controls, structured data, links, metadata, and crawlability only for surfaces where SEO matters.
5. Separate measured facts from assumptions and recommendations.
6. Return prioritized findings with severity, affected users, evidence, remediation criteria, and residual risk.

## Output contract

- Confirmed scope and evidence reviewed.
- Findings ordered by severity, each with evidence and acceptance criteria.
- PASS, FAIL, BLOCKED, or NOT APPLICABLE for accessibility, performance, responsive behavior, resilience, and SEO gates.
- Explicit list of checks not executed or not independently verifiable.

## Stop Conditions

Stop and report BLOCKED when required files, browser evidence, measurements, target browsers, legal/SEO policy, or human approval for external tools is missing.

## Prohibited Actions

- Do not install tools, execute commands, mutate Git, deploy, publish, authenticate, handle secrets, spend money, sign, submit, or perform destructive actions without exact human authorization.
- Do not claim browser, accessibility-tool, performance, or SEO validation without direct evidence.
