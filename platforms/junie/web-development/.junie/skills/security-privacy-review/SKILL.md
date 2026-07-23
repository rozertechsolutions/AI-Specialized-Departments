---
name: security-privacy-review
description: Perform an independent web security and privacy review.
---

# Security Privacy Review

Use this skill for changes involving trust boundaries, auth, sensitive data, browser security policy, third-party code, trackers, logging, storage, or privacy obligations. Do not use it as an implementation role unless explicitly reassigned by a human.

1. Model trust boundaries, actors, assets, entry points, abuse cases, and data flows.
2. Review authentication, authorization, sessions, input/output handling, injection, XSS, CSRF, SSRF, file handling, redirects, CSP, CORS, cookies, caching, logging, and error leakage as applicable.
3. Check privacy purpose, minimization, retention, consent, trackers, and sensitive-data exposure.
4. Do not edit the implementation under review unless a human explicitly reassigns the task.
5. Return findings ordered by severity with exploit condition, impact, affected files or flows, remediation criteria, residual risk, and blocked-state criteria.
