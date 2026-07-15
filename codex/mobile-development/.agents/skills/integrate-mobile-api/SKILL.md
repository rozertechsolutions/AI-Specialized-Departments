---
name: integrate-mobile-api
description: Integrate an HTTP, GraphQL, WebSocket, or existing backend API into a mobile project with secure authentication, typed boundaries, failure/offline behavior, and tests. Do not use for deploying or changing the backend.
---

# Integrate Mobile API

## Objective

Add a secure, testable mobile API integration using the project's existing networking stack while preventing secret leakage, unsafe production access, contract ambiguity, and silent failure.

## Required inputs

- Authoritative API contract: endpoint class, methods/operations, schemas, status/error model, authentication, pagination, rate limits, and versioning.
- Environment-selection mechanism and approved non-secret base URLs.
- Required caching, retry, timeout, cancellation, offline, idempotency, and freshness behavior.
- Data classification, storage/retention rules, and telemetry/redaction requirements.
- Target platforms/modules and acceptance criteria.

Do not infer undocumented server behavior. Ask for missing contract or security decisions.

## Preconditions

1. Read instructions and inspect status/diff, networking abstractions, models, auth/session handling, secure storage, environment configuration, error mapping, caches, tests, and dependencies.
2. Confirm the integration can use the existing client and dependencies. Obtain approval before SDK/client-generator/dependency changes.
3. Confirm no real credential, production write, live-user data, private endpoint, or authenticated external call is required for implementation/tests.
4. Define contract fixtures with fabricated, non-sensitive test data.
5. Classify every completion criterion as required, conditionally required, or not applicable with a documented reason.

## Agent ownership

The coordinator chooses the primary platform owner: `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer`. `mobile-architect` is required only for a new shared networking boundary or persistent contract. `mobile-security-reviewer` is mandatory. `mobile-test-engineer` owns contract/network tests. Use `mobile-performance-reviewer` for high-volume, streaming, battery, or latency-sensitive work and `mobile-code-reviewer` for final review.

## Execution

1. **Contract map.** Record request/response types, optionality, error/status mapping, auth lifecycle, pagination/stream lifecycle, cancellation, timeouts, rate limits, idempotency, and compatibility behavior.
2. **Data-flow and threat gate.** Trace data from input through transport, logs, storage, UI, telemetry, and deletion. `mobile-security-reviewer` identifies required controls before implementation. Stop on unresolved credential or sensitive-data handling.
3. **Boundary design.** Reuse the established client/repository/service pattern. If no boundary exists, obtain `mobile-architect` guidance. Keep transport models from leaking into domain/UI where project conventions separate them.
4. **Implement models and mapping.** Handle missing/unknown fields, schema evolution, malformed responses, date/number precision, and explicit error types. Do not silently default invalid required data.
5. **Implement transport.** Apply existing TLS, auth injection, timeout, cancellation, retry/backoff, cache, and offline conventions. Retry only safe/idempotent operations and honor server guidance. Never log tokens or sensitive bodies.
6. **Implement state integration.** Represent loading, success, empty, stale/offline, auth expiry, recoverable error, and terminal error as applicable. Prevent duplicate requests and stale-response races.
7. **Intermediate security gate.** Re-review auth refresh, secure storage, certificate/transport settings, redirects, deep links, WebViews, logs, analytics, and cache persistence. Sensitive configuration changes require human review.
8. **Tests.** `mobile-test-engineer` adds deterministic request/response, mapping, error, timeout, cancellation, retry, auth-expiry, caching/offline, and redaction tests using local fakes/fixtures. Do not call live services.
9. **Targeted verification.** Run compile/type/static checks and relevant tests. Use an existing approved local mock server only when already part of the project.
10. **Conditional performance review.** Measure payload, memory, rendering/backpressure, network, and battery behavior for high-volume or streaming paths.
11. **Code review and final gate.** `mobile-code-reviewer` inspects the full diff. Fix scoped findings, rerun affected checks, and confirm no secret/private data or unauthorized endpoint appears.

## Error handling and stop conditions

Stop on missing or contradictory API contracts, required production access, real credentials/data, unapproved dependency or code generation, unclear auth/storage/retention policy, TLS weakening, certificate pinning changes without an operational plan, or a required external/paid test. Report the missing decision and safe local test alternative.

## Outputs

- API/data-flow contract and files changed.
- Security controls and review findings.
- State/error/offline behavior implemented.
- Tests/fixtures and command results.
- Completion matrix with required/conditional/not-applicable status, reasons, and exact results.
- Performance evidence when required.
- Unverified server assumptions or human configuration steps.

## Acceptance criteria

- Contract mapping is explicit and resilient to defined errors/evolution.
- Auth, secrets, logs, storage, transport, retention, and user-data handling pass security review.
- Failure, timeout, cancellation, retry, cache/offline, and auth-expiry behavior is tested as applicable.
- Required compile/static/test checks pass without live production calls.
- No real secret, private data, TLS weakening, unapproved dependency, signing, deployment, or unrelated change exists.

## Prohibited actions

Do not deploy/change the backend, call production writes, use real credentials or user data, disable TLS validation, add certificate pinning casually, log sensitive payloads, add dependencies without approval, enable MCP without explicit request, sign, publish, or fabricate API behavior.
