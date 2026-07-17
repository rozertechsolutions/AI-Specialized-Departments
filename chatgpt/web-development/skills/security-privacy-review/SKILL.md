---
name: security-privacy-review
description: Use for an independent web security and privacy review covering threats, data flows, auth, cookies, CORS, CSP, secrets, trackers, and sensitive flows.
---

# Security Privacy Review

## Mission
Perform an independent security and privacy review. Reviewers cite evidence and do not self-approve their own implementation.

## Use When

- The task touches authentication, authorization, sessions, cookies, CSP, CORS, CSRF, input handling, file handling, redirects, secrets, sensitive data, logging, trackers, third-party scripts, payments, or external integrations.
- The user asks for a security or privacy review.
- Release readiness requires independent security evidence.

## Inputs

- Relevant files, routes, data flow, trust boundaries, roles, auth/session model, storage, logs, third-party integrations, privacy requirements, and known threat assumptions.

## Procedure

1. Model trust boundaries, actors, assets, entry points, abuse cases, and data flows.
2. Review authentication, authorization, sessions, input/output handling, injection, XSS, CSRF, SSRF, file handling, redirects, CSP, CORS, cookies, caching, logging, and error leakage as applicable.
3. Check privacy purpose, minimization, retention, consent, trackers, and sensitive-data exposure.
4. Do not edit the implementation under review unless a human explicitly reassigns the task.
5. Return evidence-based findings, severity, exploit conditions, remediation criteria, and residual risk.

## Output Contract

- Threat model summary and evidence reviewed.
- Findings ordered by severity with exploit condition, impact, affected files or flows, and remediation criteria.
- Privacy risks, data-minimization notes, and human-review requirements.
- PASS, FAIL, BLOCKED, or NOT APPLICABLE for security and privacy gates.

## Stop Conditions

Stop and report BLOCKED when sensitive data handling, auth rules, production context, third-party scopes, legal/privacy requirements, or required files are unavailable.

## Prohibited Actions

- Do not weaken security or privacy controls to satisfy feature requirements.
- Do not expose secrets, authenticate external systems, mutate production, install tools, execute commands, or edit reviewed code without exact human authorization and role reassignment.
