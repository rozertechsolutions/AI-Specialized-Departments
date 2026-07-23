---
name: integrate-mobile-api
description: Integrate a verified remote API into a mobile project with authentication, secure transport, typed models, error mapping, safe retries, caching/offline behavior, secret exclusion, and tests.
when_to_use: Use when Android, iOS, KMP, Flutter, React Native, or hybrid code must consume or change a remote HTTP, GraphQL, WebSocket, or project-defined service contract.
argument-hint: "[endpoint or contract and feature]"
model: inherit
---

# Objective

Integrate the API in `$ARGUMENTS` through existing project boundaries while preserving security, correctness, offline behavior, and testability.

# Required input and supported scope

Require an authoritative contract or supplied schema, environments/base-URL strategy, authentication method, request/response examples without secrets, error semantics, timeout/SLA expectations, caching/offline requirements, data sensitivity, and acceptance criteria. Never infer a production contract from a name alone.

# Preconditions and inspection

Read instructions; inspect status, existing network client and serialization, auth/session ownership, dependency injection, data/domain boundaries, cache/persistence, connectivity handling, logging/telemetry, certificate/network-security configuration, generated clients, and tests. Verify whether credentials are runtime/user-provided and absent from source.

# Ownership

The dominant technology owner implements platform code; `kmp-engineer` owns shared KMP networking/data logic. `mobile-architect` resolves boundary changes, `mobile-security-reviewer` reviews authentication/transport/data/logging, `mobile-test-engineer` owns test strategy, `mobile-performance-reviewer` reviews significant network/cache cost, and `mobile-code-reviewer` is final.

# Procedure and gates

1. Verify method/operation, URL/path, headers, auth, request/response schema, status/application errors, pagination/streaming, and versioning. Gate: no implementation against an unverified material contract.
2. Classify data and trust boundaries. Define token ownership/refresh, secure storage references, redaction, and transport requirements without reading or embedding a secret.
3. Reuse the existing client/serialization stack. Add dependencies only when necessary and approved.
4. Implement validated request and response models, explicit error mapping, cancellation, timeouts, and lifecycle/threading behavior.
5. Retry only idempotent or explicitly safe operations with bounded backoff and cancellation; never retry authentication or non-idempotent writes blindly.
6. Define caching freshness/invalidation, offline reads/writes/queueing, conflict handling, and recovery only where required. Avoid sensitive plaintext persistence.
7. Prevent sensitive request/response/token logging and validate untrusted fields, URLs, deep links, and downloaded file paths.
8. Add contract/model, client, error, timeout, retry, cache/offline, auth-expiry, cancellation, and edge tests at appropriate levels using deterministic fakes/fixtures.
9. Run discovered compile/type checks, tests, lint/static analysis, and affected integration checks without production access. Obtain security, test, performance when relevant, and final independent review.

# Failure and stop handling

Stop for missing/contradictory contract details, real credential requirements, production-only verification without approval, unsafe transport, unbounded retry, unapproved dependency/architecture/persistence changes, or failed required checks. Return the exact contract or authorization needed.

# Evidence and acceptance

Return contract source/version, data/auth model, changed files, dependency rationale, error/retry/cache/offline decisions, redaction controls, exact commands/results, applicability classification, review results, and untested external conditions.

Report every considered universal and technology-specific completion criterion as `required`, `conditionally-required`, or `not-applicable`; give a concrete reason for every `not-applicable`, and label unavailable infrastructure `unavailable` rather than passed.

Accept only when contract mapping is traceable, secrets are excluded, auth/transport/error/cancellation behavior is explicit, safe offline/retry requirements are met, required tests/checks pass, and security/final review has no blocker.

# Human review and prohibited actions

Require human review for auth scopes, production endpoints/access, certificate pinning, sensitive persistence, retrying writes, dependencies, and backend-contract changes. Never embed or access credentials, call production to test, disable TLS validation, log sensitive data, invent schemas, publish/sign/deploy, or claim external integration success without evidence.
