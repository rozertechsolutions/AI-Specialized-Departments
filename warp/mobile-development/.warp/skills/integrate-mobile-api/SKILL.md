---
name: integrate-mobile-api
description: Integrate a mobile API using existing networking, models, error handling, privacy, and test conventions.
---

# Integrate Mobile API

## Objective

Connect mobile code to an API contract safely, with validation for errors, privacy, security, and offline or retry behavior where applicable.

## Trigger

Use when the user asks to add or modify network, service, GraphQL, REST, SDK, platform channel, or bridge integration behavior.

## Inputs

API contract, endpoint policy, auth requirements, request/response schemas, error cases, caching/offline requirements, privacy implications, and acceptance criteria.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native.

## Preconditions

Inspect existing networking stack, model serialization, error handling, dependency declarations, tests, secure storage, logging, privacy rules, and public config conventions. Do not invent endpoints or credentials.

## Primary Owner

Runtime platform owner. Use `kmp-engineer` when the API client belongs in shared KMP logic.

## Reviewers

`mobile-security-reviewer`, `mobile-test-engineer`, `mobile-code-reviewer`, and `mobile-performance-reviewer` when caching, polling, streaming, or background work is involved.

## Steps

1. Verify API contract and whether values are public configuration or secrets.
2. Locate existing client, models, dependency injection, and error conventions.
3. Implement request, parsing, cancellation, timeout, retry, offline, cache, and error behavior as applicable.
4. Prevent sensitive data from logs, analytics, screenshots, and persisted storage.
5. Add unit and integration tests with deterministic fixtures or mocks.
6. Run configured checks and security review.

## Conditional Steps

- If the API contract is missing or ambiguous, stop and request it.
- If credentials, private endpoints, OAuth, production writes, or paid services are required, stop for human approval.
- If the integration belongs in shared KMP logic, route ownership to `kmp-engineer`.
- If caching, polling, streaming, or background work is introduced, run performance review.

## Validation Gates

Required: contract traceability, tests for success and failure paths, static analysis/type checks, compile/build where relevant, secret review, logging review, and code review. Conditional: integration tests, offline/cache tests, performance/network efficiency, and privacy manifest review.

## Failures and Stop Conditions

Stop for missing API contract, credential requirements, production writes, auth changes without approval, dependency additions, unclear privacy impact, or unavailable required test infrastructure.

## Evidence

Record contract source, files changed, test fixtures, commands, outputs, security review, and any skipped checks with reasons.

## Outputs

API integration, deterministic tests, security notes, and validation evidence.

## Acceptance Criteria

API behavior matches the contract, handles failures safely, protects sensitive data, and does not activate real external writes unless explicitly approved.

## Human Approvals

Required for auth, credentials, private endpoints, telemetry, privacy changes, dependency or lockfile changes, external writes, production services, and paid services.

## Prohibited Actions

Do not commit secrets, use live-user data, hit production writes by default, log sensitive values, ignore cancellation, fabricate contracts, sign, publish, upload, or deploy.
