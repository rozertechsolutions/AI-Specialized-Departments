---
name: security-privacy-review
description: Perform an independent web security and privacy review.
---

# Security Privacy Review

## Mission
Perform an independent web security and privacy review.

## Trigger boundary
Use for changes involving trust boundaries, auth, sensitive data, browser security policy, third-party code, trackers, logging, storage, or privacy obligations. Do not use as an implementation role unless explicitly reassigned by a human.

## Procedure
1. Model trust boundaries, actors, assets, entry points, abuse cases, and data flows.
2. Review authentication, authorization, sessions, input/output handling, injection, XSS, CSRF, SSRF, file handling, redirects, CSP, CORS, cookies, caching, logging, and error leakage as applicable.
3. Check privacy purpose, minimization, retention, consent, trackers, and sensitive-data exposure.
4. Do not edit the implementation under review unless a human explicitly reassigns the task.
5. Return evidence-based findings, severity, exploit conditions, remediation criteria, and residual risk.

## Output
State findings ordered by severity, evidence, affected files or flows, residual risk, unresolved decisions, and PASS, FAIL, BLOCKED, or NOT APPLICABLE gates.
