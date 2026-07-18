---
name: testing-browser-compatibility
description: Use to define or review risk-based web tests and browser compatibility evidence for frontend, backend, and full-stack changes.
---

# Testing Browser Compatibility

## Mission
Define or review risk-based tests and browser compatibility evidence. This Skill may recommend checks; it does not claim they ran unless evidence is provided.

## Use When

- The user asks what to test, whether test coverage is sufficient, or which browsers/devices matter.
- A change affects UI behavior, API contracts, auth, persistence, error handling, responsive layout, or release readiness.
- Existing test or browser evidence needs independent review.

## Inputs

- Requirements, changed behavior, current test files or output, supported browsers/devices, risk areas, affected routes/APIs/components, and known incidents or regressions.

## Procedure
1. Map acceptance criteria to unit, integration, contract, component, end-to-end, accessibility, security, and regression checks as applicable.
2. Use the repository’s existing tools and supported browser policy; do not invent coverage thresholds.
3. Include negative paths, authorization boundaries, race conditions, retries, time zones, localization, and responsive states where relevant.
4. Do not claim tests passed unless direct evidence is available.
5. Return the test matrix, evidence status, gaps, and residual risk.

## Output Contract

- Risk-based test matrix mapped to acceptance criteria.
- Browser and device compatibility matrix grounded in project policy or user requirements.
- PASS, FAIL, BLOCKED, or NOT APPLICABLE for each evidence category.
- Gaps, recommended next checks, and residual risk.

## Stop Conditions

Stop and report BLOCKED when acceptance criteria, supported browser policy, test evidence, or required environment details are missing.

## Prohibited Actions

- Do not run tests, install browsers, execute package managers, mutate Git, deploy, publish, authenticate, or perform destructive actions without exact human authorization.
- Do not invent coverage thresholds, browser support, or passing test results.
