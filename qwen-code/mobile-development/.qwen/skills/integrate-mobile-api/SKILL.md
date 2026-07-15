---
name: integrate-mobile-api
description: Integrate a mobile API from a verified contract with explicit authentication, transport security, models, error mapping, timeouts, safe retries, caching, offline behavior, sensitive-log prevention, and tests.
user-invocable: true
---

# Integrate Mobile API

## Objective

Integrate a verified remote API contract into the existing mobile architecture with secure transport, typed boundaries, deterministic failures, justified retry/cache/offline behavior, and complete tests without exposing credentials or using production data.

## Trigger

Use when the primary request is to add or change a mobile client's remote API integration. Do not use for an architecture-only review or an unrelated UI feature.

## Inputs

- Authoritative endpoint contract/version, environments, authentication scheme, and data classification.
- Request/response/error models, pagination, idempotency, rate limits, timeouts, cache/freshness, offline, cancellation, and compatibility requirements.
- Approved test endpoints or fixtures, with no real secrets.

## Preconditions

- Read instructions, status/diff, existing network stack, model/domain mapping, auth/session flow, storage/cache, connectivity handling, logging/telemetry, dependency configuration, and tests.
- Verify the contract against an in-repository specification or current official documentation. Stop if the contract is unavailable or ambiguous.
- Confirm no new dependency, permission, credential, or production connection is implicitly required.

## Ownership

- Primary owner: the technology engineer owning the consuming application area.
- Native bridge/host changes are separately owned by Android/iOS specialists; KMP shared networking is owned by `kmp-engineer` when it is in a shared source set.
- `mobile-test-engineer` supports test strategy; `mobile-security-reviewer` review is required; performance review is conditional; `mobile-code-reviewer` reviews last.

## Tool and permission boundary

Use read/search for discovery and contract review. Edit only assigned network/model/domain/cache/test paths under normal approval. Use local mocks/fixtures and project commands. Do not use MCP, production credentials/data, authenticated live calls, external writes, package installation, certificate bypasses, signing, or deployment.

## Sequence and gates

1. **Contract gate:** Record source/version, base-path strategy, operations, methods, headers, query/body schema, success/error schema, pagination, limits, idempotency, and compatibility. Stop on unresolved mismatch.
2. **Trust/security gate:** Classify data; define authentication/token ownership, TLS/ATS/network-security requirements, certificate behavior, authorization boundaries, redaction, storage, telemetry, and privacy. Human approval is required for credentials and new permissions.
3. **Architecture/ownership gate:** Place transport DTOs, client, repository/data source, domain models, cache, state/UI mapping, and platform-specific code according to the existing dependency direction. Assign one owner per area.
4. **Failure-policy gate:** Define connect/read/write timeouts, cancellation, offline detection, status and transport error mapping, rate-limit handling, and retry rules. Retry only safe/idempotent operations with bounded backoff/jitter and cancellation; never retry authentication or semantic failures blindly.
5. **Cache/offline gate:** Define cache key, freshness, invalidation, consistency, storage protection, stale-data presentation, mutation queue/conflict policy, and recovery only when requirements need them. Do not add a cache by default.
6. **Implementation gate:** Add typed models and explicit mapping, client/data boundary, auth injection without embedded values, error handling, cancellation, cache/offline behavior, and sensitive-log redaction as applicable.
7. **Test gate:** Add deterministic request/response, serialization, mapping, auth-header redaction, timeout/cancellation, retry/idempotency, status/error, malformed data, cache/offline, and recovery tests as applicable using controlled fakes/fixtures.
8. **Validation gate:** Run targeted format/lint/type/static checks, compilation/non-publishing build, tests, dependency resolution, and manifest/permission/transport configuration review. Scan changed content for secrets and unredacted data.
9. **Independent review gate:** Obtain security and test review, conditional performance review, then final code review. Correct and fully repeat after any finding.
10. **Completion gate:** Classify every `QWEN.md` criterion and report contract/runtime checks not performed.

## Errors and stop conditions

Stop on unverified contract, required real credential or production access, unclear auth/authorization, insecure transport request, non-idempotent automatic retry, unapproved dependency/permission/storage/schema change, sensitive logging, failed validation, or unresolved high/critical risk.

## Outputs and evidence

- Contract source/version and operation/error matrix.
- Data/auth/trust boundaries and area-to-owner map.
- Exact changed model/client/domain/cache/state/test/config paths.
- Retry/cache/offline policy and sensitive-data handling.
- Exact commands, exit codes, targets, observed results, completion ledger, reviews, and limitations.

## Acceptance criteria

- Models and errors map explicitly and safely; cancellation/timeouts and applicable retry/offline/recovery behavior are deterministic.
- Authentication and sensitive data are injected/stored/logged according to existing secure boundaries with no embedded value.
- Tests cover relevant success and failure contracts; required build/analysis/tests and security review pass without unresolved blocker.
- No live production call or external write is required to claim local integration correctness.

## Human review requirements

Humans approve contracts, environments, credentials, scopes, permissions, certificate/security policy, dependencies, production tests, privacy/telemetry, and external service actions.

## Prohibited actions

Do not invent a contract, embed secrets, disable TLS validation, log tokens/personal data, retry unsafe mutations automatically, use production data, install clients/packages without approval, contact authenticated services, deploy, sign, or self-approve.
