---
name: backend-api-auth
description: Plan or review backend, API, authentication, authorization, sessions, persistence, integrations, validation, and server failure handling.
---

# Backend, API, And Auth

## Mission
Plan or implement backend, API, authentication, session, and persistence work.

## Use when
- A task changes server behavior, API contracts, auth, authorization, sessions, cookies, CORS, persistence, integrations, validation, or errors.
- A frontend change depends on backend contract decisions.

## Do not use when
- The change is purely presentational and has no server or API contract.

## Inputs
Routes, schemas, auth/session model, roles, storage model, trust boundaries, integration requirements, existing errors/logs, and relevant files.

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

## Stop and failure behavior
Return BLOCKED when auth rules, data sensitivity, migration requirements, production context, external scopes, or credential handling are unclear.

## Review requirements
Include validation, authorization, session/cookie/CORS/CSRF, persistence, error, observability, migration, rollback, and security-review handoff evidence.

## Prohibited actions
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
