---
name: accessibility-performance-seo
description: Assess accessibility, performance, responsive behavior, resilience, and SEO. Use for user-facing web review before acceptance or release.
---

# Accessibility, Performance, And SEO

## Mission
Assess accessibility, performance, responsive behavior, and SEO as one user-facing quality review.

## Use when
- The user asks for accessibility, responsive, performance, resilience, metadata, or SEO review.
- A frontend or full-stack change is ready for independent user-impact review.

## Do not use when
- The task is backend-only and has no user-facing behavior.
- The user has not provided enough UI, route, screenshot, browser, or measurement evidence.

## Inputs
Requested scope, affected routes/components, target users, supported browsers, UI files, screenshots, measurements, test output, SEO expectations, and known constraints.

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

## Stop and failure behavior
Return BLOCKED when required UI evidence, target browsers, measurements, accessibility criteria, SEO policy, or approval for external tooling is missing.

## Review requirements
Remain independent from the implementation under review. Findings need severity, affected users, evidence, remediation criteria, and residual risk.

## Prohibited actions
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
