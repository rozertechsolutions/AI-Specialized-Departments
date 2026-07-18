---
name: security-privacy-review
description: Perform independent web security and privacy review. Use for auth, data flows, CSP, CORS, cookies, secrets, trackers, or sensitive flows.
---

# Security Privacy Review

## Mission
Perform an independent web security and privacy review.

## Use when
- A task touches auth, authorization, sessions, cookies, CSP, CORS, CSRF, input handling, file handling, redirects, secrets, sensitive data, logs, trackers, payments, or integrations.

## Do not use when
- There is no security, privacy, dependency, data, auth, or external-system impact.

## Inputs
Relevant files, routes, data flows, trust boundaries, roles, auth/session model, storage, logs, integrations, privacy requirements, and threat assumptions.

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

## Stop and failure behavior
Return BLOCKED when sensitive data handling, auth rules, production context, third-party scopes, legal/privacy requirements, or required files are unavailable.

## Review requirements
Remain independent. Findings need severity, exploit condition, impact, affected files or flows, remediation criteria, privacy notes, and human-review requirements.

## Prohibited actions
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
