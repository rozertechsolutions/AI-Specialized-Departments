---
name: "integrate-mobile-api"
description: "Integrate mobile API access with secure networking, error handling, offline behavior, tests, dependency review, and no real secrets or private endpoints."
---
# Integrate Mobile API

Use this skill when adding or changing network/API integration, clients, DTOs, platform channels, GraphQL/REST calls, authentication flows, or data synchronization.

## Workflow Definition

Objective: integrate APIs securely and testably without embedding secrets or activating private services by default.

Trigger: request to connect to an API, add endpoint usage, change networking, or update data sync.

Inputs: API contract or public docs, endpoint classification, auth requirements, data model, error semantics, caching/offline expectations, privacy constraints, and affected platforms.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, and React Native.

Preconditions:

- Confirm whether endpoints/config values are public client configuration or sensitive.
- Inspect existing networking, serialization, storage, retry, and dependency patterns.
- Ask approval for auth, credentials, private endpoints, dependencies, lockfiles, telemetry, privacy, or external writes.

Primary owner: matching platform engineer or `kmp-engineer` for shared networking.

Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, `mobile-performance-reviewer` for sync/heavy traffic, and `mobile-code-reviewer`.

## Steps

1. Classify API data, secrets, endpoint visibility, auth, privacy, and storage requirements.
2. Reuse existing client, serialization, dependency injection, and error handling conventions.
3. Implement request/response handling, validation, timeouts, cancellation, retries, and recovery states.
4. Add secure storage only through platform-native secure APIs and only when required.
5. Add tests with deterministic fixtures/mocks; do not call production services in tests.
6. Review logging and telemetry for sensitive data exposure.
7. Run relevant typecheck/lint/analyze/build/test commands.
8. Request security and final code review.

## Validation Gates

- No real secrets, tokens, certificates, keys, service accounts, or private URLs are committed.
- Auth/privacy/storage/network security changes have approval.
- Error, retry, cancellation, offline, and recovery behavior is handled where applicable.
- Dependency and lockfile changes have approval.

## Failures And Stop Conditions

Stop for missing API contract, private credentials, unclear endpoint sensitivity, unapproved dependencies, production external calls, destructive commands, signing, upload, publication, or cost.

## Evidence And Outputs

Output changed files, API/config classification, security review notes, tests, commands run, validation results, unavailable checks, and residual risk.

Acceptance criteria: API behavior is scoped, secure, tested with deterministic data, validated, and independently reviewed.

Human approvals: required for auth, credentials, privacy, telemetry, analytics, dependencies, lockfiles, network security, secure storage, and external writes.

Prohibited actions: committing secrets, using production services in tests, silent broad exception handling, disabling TLS/validation, release actions, and self-review.
