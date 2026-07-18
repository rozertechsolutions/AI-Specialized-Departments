---
name: testing-browser-compatibility
description: Define or review risk-based web tests, acceptance coverage, regression checks, and browser/device compatibility evidence.
---

# Testing Browser Compatibility

## Mission
Define and assess risk-based tests and browser compatibility.

## Use when
- The user asks what to test, whether coverage is enough, or which browsers/devices matter.
- A change affects UI behavior, API contracts, auth, persistence, errors, responsive layout, or release readiness.

## Do not use when
- There are no acceptance criteria or behavior changes to test.

## Inputs
Requirements, changed behavior, current tests or output, supported browsers/devices, risk areas, affected routes/APIs/components, and known regressions.

## Required procedure
1. Map acceptance criteria to unit, integration, contract, component, end-to-end, accessibility, security, and regression checks as applicable.
2. Use the repository’s existing tools and supported browser policy; do not invent coverage thresholds.
3. Include negative paths, authorization boundaries, race conditions, retries, time zones, localization, and responsive states where relevant.
4. Do not claim tests passed unless direct evidence is available.
5. Return the test matrix, evidence status, gaps, and residual risk.

## Output contract
- State confirmed scope and evidence.
- Separate facts, assumptions, risks, and unresolved decisions.
- List files or components affected or reviewed.
- State which quality gates are PASS, FAIL, BLOCKED, or NOT APPLICABLE.
- Do not claim execution or success without direct evidence.

## Stop and failure behavior
Return BLOCKED when acceptance criteria, supported browser policy, test evidence, or required environment details are missing.

## Review requirements
Return a risk-based test matrix, browser/device matrix, evidence status, gaps, recommended next checks, and residual risk.

## Prohibited actions
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
