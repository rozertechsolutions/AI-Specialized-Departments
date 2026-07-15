---
name: integrate-mobile-api
description: Use when integrating a verified API contract into an existing mobile project with secure transport, explicit errors, cancellation, retry/cache/offline behavior, and local tests.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - todo
  - ask_user_question
  - task
  - write_file
  - edit
  - bash
---

# Integrate Mobile API

## Objective and trigger

Integrate a defined API through the project's existing networking/data boundaries without exposing credentials or relying on live production access.

## Inputs

- Authoritative request/response/error contract, base-environment selection mechanism, authentication lifecycle, transport requirements, pagination/streaming/idempotency/rate-limit behavior, cache/offline policy, data classification/retention, and acceptance criteria.
- Existing client/repository/model conventions and approved local fixtures/mock mechanism.

## Preconditions and ownership

Inspect instructions, status/diff, networking/auth/storage/logging architecture, models, dependencies, platform security configuration, and tests. Stop if the contract, auth/storage/retention behavior, endpoint ownership, or safe local test method is missing.

Partition shared client/repository, framework runtime, and native host/security configuration into non-overlapping units, then assign the matrix owner to each. Each platform owner owns contract tests in its unit unless the coordinator explicitly separates a bounded test-only unit for `mobile-test-engineer`; use `mobile-architect` only for a new shared networking/persistence boundary. `mobile-security-reviewer` and mobile test-strategy review are required. Performance review is conditional for high-volume, streaming, latency, or battery-sensitive work; final code review is mandatory.

## Sequence and gates

1. Contract gate: map methods/paths, request/response types, optionality, unknown/malformed fields, status/error mapping, auth expiry, pagination/stream lifecycle, cancellation, timeouts, rate limits, idempotency, and compatibility. Do not infer missing server behavior.
2. Data/threat gate: trace data through transport, memory, logs, telemetry, storage, UI, backup, and deletion. Security review identifies controls before implementation; unresolved high risk blocks work.
3. Boundary gate: reuse the established client/repository/service pattern. Obtain architecture and human approval for a new boundary, dependency, public API, or persistent format.
4. Implement transport models and mapping with explicit validation and errors; do not silently default invalid required data.
5. Implement auth injection/refresh, TLS/redirect handling, timeout, cancellation, safe idempotent retry/backoff, cache/offline behavior, and redacted logging according to verified policy.
6. Integrate state for loading, success, empty, stale/offline, auth expiry, recoverable and terminal errors; prevent duplicate requests and stale-response races.
7. Intermediate security review covers credentials, secure storage, transport, redirects, deep links/WebViews, logs, analytics, caching, and retention. Sensitive configuration changes require human review.
8. The assigned test owner adds deterministic local mapping, malformed response, error, timeout, cancellation, retry, auth-expiry, cache/offline, and redaction tests; `mobile-test-engineer` validates level selection, fixtures, determinism, and coverage. Never call live services.
9. Run discovered static/type/lint/compile/tests. Performance evidence is required when classified.
10. Independent code review; correct findings, rerun affected gates, and inspect final diff.

## Errors and stop conditions

Stop on contradictory/missing contracts, real credentials/data, production or paid access, unapproved code generation/dependency, unclear auth/storage/retention, TLS weakening, pinning changes without operations plan, unavailable local fixture mechanism, signing/deployment, conflicting user work, or unrelated failures.

## Outputs and evidence

Provide contract/data-flow map, changed files, security controls/findings, state/error/offline behavior, local fixtures/tests, exact commands/results, performance evidence when required, criterion matrix, unverified server assumptions, and blockers.

## Acceptance and human review

The verified contract and defined evolution/errors are handled; auth/secrets/logs/storage/transport/retention pass security review; timeout/cancellation/retry/cache/offline/auth-expiry paths are tested as applicable; required checks pass without live production calls; and independent review is clear. Humans approve auth, secure storage, TLS/pinning, endpoint, retention, telemetry, permission, dependency, and persistent/public-contract changes.

## Prohibited actions

Do not deploy/change a backend, call production writes, use real credentials/user data, disable TLS validation, add casual certificate pinning, log sensitive payloads, install dependencies, enable MCP/connectors, sign/publish/deploy, or fabricate API behavior.
