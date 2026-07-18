---
name: backend-api-auth
description: Use for backend, API, authentication, authorization, session, persistence, validation, and server-side failure-handling work.
---

# Backend, API, And Auth

## Mission
Plan or review backend, API, authentication, authorization, session, and persistence work using the project's actual stack and contracts.

## Use When

- The task changes server behavior, API contracts, authentication, authorization, sessions, cookies, CORS, validation, persistence, integrations, or error handling.
- A frontend change depends on backend contract decisions.
- A security or release review needs server-side evidence.

## Inputs

- Current API routes or schemas, auth/session model, storage model, user roles, trust boundaries, error contract, integration requirements, and relevant files or logs.

## Procedure
1. Define inputs, validation, authorization, side effects, idempotency, errors, observability, and data retention.
2. Enforce authorization server-side; never trust client claims.
3. Use secure cookie, token, CORS, CSRF, rate-limit, and secret-handling practices appropriate to the stack.
4. Do not expose credentials or real endpoints in generated files.
5. Return contract changes, migration impact, tests required, and security-review items.

## Output Contract

- Confirmed backend scope and affected contracts.
- Validation, authorization, session, persistence, error, and observability plan or review findings.
- Migration and rollback considerations where applicable.
- Required tests, security-review handoff, and PASS/FAIL/BLOCKED/NOT APPLICABLE gate status.

## Stop Conditions

Stop and report BLOCKED when auth rules, data sensitivity, migration requirements, production access, external integration scopes, or credential handling are unclear.

## Prohibited Actions

- Do not weaken authentication, authorization, validation, cookies, CORS, CSRF, transport security, or logging safeguards for convenience.
- Do not install, execute commands, mutate Git, deploy, publish, authenticate, use secrets, or perform destructive actions without exact human authorization.
