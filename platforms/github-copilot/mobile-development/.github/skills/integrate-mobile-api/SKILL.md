---
name: integrate-mobile-api
description: Integrates a mobile API from a verified contract with authentication boundaries, transport security, models, error mapping, timeouts, safe retries, caching, offline behavior, sensitive logging prevention, tests, and independent review. Use for explicit network-service integration.
---

# Integrate a mobile API

## Objective

Integrate a verified API contract through the project's existing networking and architecture layers with safe authentication, transport, parsing, error, timeout, retry, caching, offline, privacy, and test behavior.

## Trigger

Use when the user explicitly requests a new or changed remote API integration. Do not use for configuring Firebase, Sentry, GitHub, or another external service unless the user separately authorizes that exact integration and supplies an approved contract.

## Inputs

- authoritative endpoint contract, methods, paths, models, status/errors, pagination, idempotency, and versioning;
- environment/base-URL strategy with no private or real credential values;
- authentication mechanism and token lifecycle, with server-side authorization assumptions;
- timeout, retry, rate-limit, caching, freshness, offline, cancellation, and data-classification requirements;
- affected platforms, existing client stack, acceptance criteria, and test environment.

## Preconditions

- Read applicable instructions, existing network client, dependency injection, models, domain repositories, storage/cache, logging, configuration, tests, and current changes.
- Verify the contract from project-provided material or approved official documentation. Stop rather than invent fields, endpoints, or error semantics.
- Confirm that existing dependencies can implement the contract. Obtain approval before any dependency change.
- Define trust boundaries and classify request/response data before editing.

## Ownership

Primary owner: the engineer owning the network/domain boundary; `kmp-engineer` is primary for shared KMP clients. Platform owners handle only native networking/security configuration. `mobile-security-reviewer`, test, performance, and code reviewers support independently.

## Sequence and intermediate gates

1. **Contract gate:** record operations, schemas, validation, errors, pagination, idempotency, version compatibility, and unresolved questions. Stop on material ambiguity.
2. **Security gate:** define authentication/session ownership, authorization expectations, TLS/platform policy, certificate behavior, sensitive fields, storage, redaction, and least-privilege permissions. Never embed credentials or disable certificate validation.
3. **Behavior gate:** define timeouts, cancellation, safe retries with backoff/jitter and idempotency, rate limits, caching/freshness, offline/stale behavior, and user-visible error/recovery mapping.
4. Implement transport DTOs and strict parsing/validation at the untrusted boundary. Keep transport, domain, and UI models separated according to existing architecture.
5. Implement the client/repository operation with existing abstractions, structured error mapping, cancellation, observability without sensitive content, and safe cache/storage behavior.
6. Connect domain and UI callers without leaking raw transport errors or secrets. Implement applicable loading, empty, error, retry, offline, cancellation, and recovery states.
7. Add deterministic tests for encoding/decoding, success, malformed data, status errors, auth expiry, timeout, cancellation, retry eligibility and limits, rate limiting, cache freshness, offline behavior, and log redaction as applicable. Use local fakes/fixtures, not live services.
8. **Validation gate:** run targeted compile/type/static checks and tests, then the reasonable affected suite. Do not make live external calls unless separately authorized.
9. **Review gate:** invoke security review for every authentication/sensitive-data integration, performance review for network/cache impact, UI/accessibility for user-visible states, and independent code review. Resolve findings and rerun affected checks.

## Errors and stop conditions

- Stop if the contract, auth model, data classification, environment strategy, or server authorization behavior is unknown and material.
- Do not fall back to insecure transport, infinite/default retries, silent parsing defaults, broad exception swallowing, or sensitive logs.
- Report unavailable integration infrastructure without substituting live production access or fabricated success.
- An unresolved high-risk security finding, failed required test, or unverified data migration blocks completion.

## Completion classification

Classify every coordinator criterion. Contract traceability, configuration, compilation/type checks, unit/integration tests using local controlled endpoints, static checks, dependency justification, security/secret scanning, network/offline and recovery behavior, warnings, regression evidence, and independent review are normally required. UI/accessibility/localization/adaptive behavior, performance/storage, end-to-end tests, and documentation become required when the integration exposes or changes those concerns.

## Outputs and evidence

Return the verified contract source, trust/data classification, auth and transport decisions, timeout/retry/cache/offline policy, changed files, fixture coverage, exact commands/results, log-redaction evidence, reviews, unavailable checks, residual risks, and completion-classification table.

## Acceptance criteria

- Implementation matches the verified contract and existing architecture.
- Authentication, transport, validation, error, timeout, retry, cancellation, cache, offline, and logging behavior is explicit and tested where applicable.
- No credential, private endpoint, sensitive fixture, insecure override, or unapproved dependency is introduced.
- Required checks and security/independent reviews have no unresolved blocker.

## Human review requirements

Humans approve contracts, environments, authentication and sensitive-data design, dependency changes, certificate pinning policy, live service access, unavailable required validation, and accepted residual risk.

## Prohibited actions

Do not invent contracts; embed secrets/private URLs; disable TLS validation; log sensitive data; call live services without authorization; configure external MCP/services; publish/sign/deploy; or self-approve.
