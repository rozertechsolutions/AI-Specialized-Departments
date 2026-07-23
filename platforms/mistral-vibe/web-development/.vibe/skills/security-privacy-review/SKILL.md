---
name: security-privacy-review
description: "Perform an independent web security and privacy review."
user-invocable: true
allowed-tools:
  - read
  - read_file
  - grep
  - ask_user_question
---

# Security Privacy Review

## Mission
Perform an independent web security and privacy review.

## Vibe invocation
Invoke with `/security-privacy-review` for independent security, privacy, auth, browser-policy, trust-boundary, secret, logging, tracker, or sensitive-data review. Do not edit the implementation under review.

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
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
