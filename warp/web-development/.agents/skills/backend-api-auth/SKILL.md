---
name: backend-api-auth
description: Plan or implement backend, API, authentication, session, and persistence work.
---

# Backend Api Auth

## Mission
Plan or implement backend, API, authentication, session, and persistence work.

## Warp invocation
Invoke manually as `/backend-api-auth` or let the local Warp agent load it for scoped backend, API, authentication, session, validation, authorization, persistence, or server-side behavior work.

## Inputs
API routes, contracts, auth/session expectations, data flows, persistence constraints, affected files, prohibited changes, and required human-review points.

## Expected output
Contract impact, validation and authorization behavior, data integrity notes, migration or rollback impact, changed or proposed files, required reviews, evidence, risks, and NOT EXECUTED checks.

## Stop conditions
Stop with BLOCKED for unclear contracts, missing authorization decisions, unsafe persistence assumptions, migration risk without approval, or sensitive-data uncertainty.

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
- Do not run commands, install packages, mutate Git state, deploy, publish, authenticate, handle secrets, spend money, sign artifacts, or perform destructive operations without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
