---
name: backend-api-auth
description: Plan or implement backend, API, authentication, session, and persistence work.
---

# Backend Api Auth

## Mission
Plan or implement backend, API, authentication, session, and persistence work.

## Trigger boundary
Use when work changes server behavior, API contracts, authentication, authorization, sessions, cookies, CORS, persistence, integrations, or backend error handling. Do not use for browser-only presentation work.

## Required procedure
1. Define inputs, validation, authorization, side effects, idempotency, errors, observability, and data retention.
2. Enforce authorization server-side; never trust client claims.
3. Use secure cookie, token, CORS, CSRF, rate-limit, and secret-handling practices appropriate to the stack.
4. Do not expose credentials or real endpoints in generated files.
5. Return contract changes, migration impact, tests required, and security-review items.

## Output contract
- State confirmed scope and evidence.
- Separate facts, assumptions, risks, and unresolved decisions.
- List files or components affected or reviewed.
- State which quality gates are PASS, FAIL, BLOCKED, or NOT APPLICABLE.
- Do not claim execution or success without direct evidence.

## Prohibited actions
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
