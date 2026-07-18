---
name: testing-browser-compatibility
description: Define and assess risk-based tests and browser compatibility.
---

# Testing Browser Compatibility

## Mission
Define and assess risk-based tests and browser compatibility.

## Invocation and surface
- Cascade: Invoke with `@testing-browser-compatibility` or allow Cascade to select it to map or review test and browser-compatibility evidence.
- Devin Local: Compatible as a project skill; invoke with `/testing-browser-compatibility` when using Devin Local.
- Not a test runner, browser preview, App Deploy, hook, MCP server, or external automation.

## Inputs and preconditions
Acceptance criteria, changed files, supported browsers, risk areas, available validation evidence, known exclusions, and prohibited operations.

## Expected output and evidence
Risk-based test matrix, browser compatibility expectations, evidence status, gaps, residual risk, and NOT EXECUTED checks.

## Stop conditions
Stop with BLOCKED when required tests or browser evidence are missing for a PASS claim.

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

## Prohibited actions
- Do not run commands, install packages, mutate Git state, deploy, publish, authenticate, handle secrets, spend money, sign artifacts, or perform destructive operations without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
