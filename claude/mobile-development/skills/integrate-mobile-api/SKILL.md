---
name: integrate-mobile-api
description: Integrates an approved remote API into a mobile project with secure failure handling. Use for Android, iOS, KMP, Flutter, or React Native clients.
---

# Integrate Mobile API

## Objective

Integrate an authoritative remote API contract into an existing mobile project with correct transport, models, authentication boundaries, validation, cancellation, retries, caching, offline behavior, privacy, and tests.

## Trigger

Use when the primary task is adding or changing a mobile client's remote API integration. Do not use for backend implementation or for a feature whose API work is only incidental.

## Inputs

- authoritative API specification, sample schemas, versioning, and error model;
- approved environments and public base-address policy without credentials;
- authentication and authorization design, token lifecycle, and ownership boundaries;
- data classification, privacy, retention, logging, and telemetry requirements;
- timeout, retry, idempotency, pagination, caching, offline, cancellation, and rate-limit requirements;
- existing networking, serialization, dependency-injection, storage, and test conventions;
- acceptance criteria and safe non-production test evidence.

Do not invent fields, status handling, authentication, endpoints, sample personal data, or server behavior.

## Supported technologies

Android, iOS, KMP, Flutter, and React Native. Shared KMP clients remain with kmp-engineer; native secure storage and platform transport remain with native owners.

## Preconditions

- The contract source, revision, and environment are known.
- Relevant project code, generated-code policy, and networking conventions are inspected.
- No real secret, production credential, or private endpoint must be embedded or exposed.
- Human approval covers authentication, privacy, dependency, storage, and network-security changes.
- One technology owner is selected for the client integration.

## Primary owner and reviewers

Select the owner of the client layer: android-engineer, ios-engineer, kmp-engineer, flutter-engineer, or react-native-engineer. mobile-security-reviewer is mandatory. mobile-test-engineer reviews contract and failure coverage. mobile-architect reviews new service boundaries or shared placement. mobile-performance-reviewer reviews payload, paging, cache, or streaming impacts. mobile-code-reviewer is final. Native owners review secure storage and host configuration.

## Ordered workflow

1. Restate contract revision, use cases, data classification, environments, auth boundary, failure behavior, and non-goals.
2. Inspect repository status, networking abstractions, serialization, model mapping, dependency injection, secure storage, caching, logging, tests, and dependency declarations.
3. Trace the data flow from request initiation through transport, validation, mapping, persistence or cache, state, UI, cancellation, and error presentation.
4. Produce a contract matrix for request fields, response fields, errors, pagination, optionality, nullability, versioning, and unknown values.
5. Define transport and security policy: TLS, certificate behavior, headers, token handling, redaction, timeout, retry, idempotency, rate limits, and server trust.
6. Define loading, partial, empty, error, retry, cancellation, offline, stale-cache, and recovery behavior.
7. Reuse the project's existing client and dependencies. Obtain approval before adding or updating any package, generator, plugin, certificate policy, permission, storage, or lockfile.
8. Implement the smallest client, model mapping, repository or service integration, and state exposure using the selected owner. Keep server secrets and privileged logic off the client.
9. Add deterministic tests for request construction, parsing, missing and unknown fields, server errors, transport failures, timeout, cancellation, retry limits, pagination, cache behavior, and redaction as applicable.
10. Validate against contract fixtures or an explicitly approved non-production endpoint. Never write to production or use live-user data.
11. Run targeted type, analysis, formatting, compilation, and tests, then broader relevant checks.
12. Obtain security, performance, test, architecture, native-host, and final code reviews as applicable.
13. Resolve findings through the implementation owner, rerun checks, then complete triple review and final verification.

## Conditional steps

- Authentication: require human-approved token lifecycle, secure storage, refresh serialization, logout and revocation, clock skew, and error handling.
- Generated client: verify generator source, version, license, reproducibility, generated-file policy, and diff; network download needs approval.
- Upload or download: validate size, MIME type, filenames, paths, cancellation, progress, storage, and malicious content.
- Streaming or sockets: validate lifecycle, reconnect bounds, background behavior, ordering, backpressure, and battery use.
- Offline cache: define freshness, invalidation, encryption needs, migration, eviction, and conflict behavior.
- KMP: place shared transport only in appropriate source sets and validate platform engines and actual implementations.

## Validation gates

- Gate 1: contract, revision, environment, auth, and data classification are authoritative.
- Gate 2: field, error, lifecycle, and offline matrices are complete.
- Gate 3: security review approves the proposed boundaries and no client secret is present.
- Gate 4: contract and failure tests pass using safe fixtures or approved non-production evidence.
- Gate 5: applicable target builds and broader checks pass without unexplained warning.
- Gate 6: final review and triple validation pass.

## Failures

On schema conflict or undocumented server behavior, stop and request contract clarification. On network or test failure, preserve status and sanitized diagnostics; do not log payloads, tokens, headers, or personal data. Do not add unlimited retry, silent fallback, permissive parsing, disabled certificate validation, or hardcoded production values.

## Stop conditions

Stop for missing or contradictory contract, real credential need, private data exposure, production-only validation, unapproved dependency, auth or storage change, certificate or network-security weakening, destructive server operation, unavailable required environment, or conflicting user changes.

## Evidence

Record contract source and revision, data-flow and field matrices, changed files, dependency decision, sanitized fixtures, exact commands, tests by failure mode, target builds, security findings, warnings, and unavailable integration infrastructure.

## Outputs

- scoped client integration and mappings;
- explicit failure, cancellation, retry, caching, and offline behavior;
- deterministic contract and error tests;
- security and privacy review record;
- criterion ledger, validation evidence, and human actions.

## Acceptance criteria

The client follows the authoritative contract, handles all applicable failure and lifecycle states, protects credentials and private data, uses existing approved architecture and dependencies, passes relevant tests and target checks, and has no unresolved security or final-review finding.

## Human approvals

Require approval for authentication, authorization, privacy, secure storage, network security, certificates, dependencies, generators, lockfiles, analytics, non-production external access, uploads, downloads, and persistent caching.

## Prohibited actions

Do not invent a contract, embed credentials or privileged secrets, disable TLS validation, use production writes or live-user data, log sensitive payloads, add unbounded retries, install unapproved dependencies, sign, publish, deploy, or run Git write commands.
