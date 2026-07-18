---
name: security-privacy-review
description: Perform an independent web security and privacy review.
---

# Security Privacy Review

## Mission
Perform an independent web security and privacy review.

## Warp invocation
Invoke manually as `/security-privacy-review` or let the local Warp agent load it for independent security, privacy, trust-boundary, auth, browser-policy, tracker, logging, dependency, or sensitive-data review.

## Inputs
Changed files, trust boundaries, data types, auth/session behavior, third-party services, browser policies, logging, storage, and expected abuse cases.

## Expected output
Findings ordered by severity with exploit conditions, impact, affected files or flows, remediation criteria, residual risk, evidence, and NOT EXECUTED checks.

## Stop conditions
Stop with BLOCKED for missing security evidence, unclear trust boundary, unapproved sensitive-data change, or unresolved material finding.

## Required procedure
1. Model trust boundaries, actors, assets, entry points, abuse cases, and data flows.
2. Review authentication, authorization, sessions, input/output handling, injection, XSS, CSRF, SSRF, file handling, redirects, CSP, CORS, cookies, caching, logging, and error leakage as applicable.
3. Check privacy purpose, minimization, retention, consent, trackers, and sensitive-data exposure.
4. Do not edit the implementation under review unless a human explicitly reassigns the task.
5. Return evidence-based findings, severity, exploit conditions, remediation criteria, and residual risk.

## Output contract
- State confirmed scope and evidence.
- Separate facts, assumptions, risks, and unresolved decisions.
- List files or components affected or reviewed.
- State which quality gates are PASS, FAIL, BLOCKED, or NOT APPLICABLE.
- Do not claim execution or success without direct evidence.

## Prohibited actions
- Do not run commands, install packages, mutate Git state, deploy, publish, authenticate, handle secrets, spend money, sign artifacts, or perform destructive operations without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
