---
name: integrate-mobile-api
description: Workflow for integrating a mobile API with networking, serialization, auth, cancellation, retry, offline behavior, tests, and security review.
---

# Integrate Mobile API

## Objective

Integrate an API using existing networking conventions while protecting auth, privacy, error handling, cancellation, retry, and offline behavior.

## Trigger

Use when the user asks to connect a mobile app to an API, endpoint, SDK, service, or backend.

## Inputs

API contract, base URL policy, auth requirements, request/response schemas, error model, caching/offline expectations, and target platforms.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native.

## Preconditions

Inspect existing networking stack and configuration. Do not invent real endpoints, tokens, or credentials.

## Primary Owner

The platform or shared engineer owning the networking layer.

## Reviewers

`mobile-security-reviewer`, `mobile-test-engineer`, `mobile-architect` for shared boundaries, and `mobile-code-reviewer`.

## Steps

1. Verify API contract and configuration source.
2. Locate existing network/client patterns.
3. Implement typed request/response handling.
4. Handle auth, errors, retries, cancellation, timeouts, loading, and offline states as applicable.
5. Add tests with fixtures or mocks according to project conventions.
6. Run validation and security review.
7. Perform final review.

## Conditional Steps

- Authenticated API: require explicit approval for auth changes and credential handling.
- KMP: place shared networking only where dependencies support all targets.
- WebView/deep link integration: require security review.

## Validation Gates

No secrets embedded, schema handling tested, errors handled, cancellation considered, and configured checks pass or are unavailable.

## Failures

Stop on missing API contract, real credential requirement, unsupported dependency, approval denial, or external service uncertainty.

## Stop Conditions

Do not call production services or store credentials without explicit approval.

## Evidence

Contract source, files changed, tests, commands run, security review notes, and unavailable checks.

## Outputs

API integration, tests, configuration notes, and validation report.

## Acceptance Criteria

Integration follows existing patterns, handles failure states, avoids secrets, and is tested.

## Human Approvals

Required for auth, privacy, dependencies, lockfiles, external calls, telemetry, analytics, and real endpoints.

## Prohibited Actions

No hardcoded secrets, fabricated real endpoints, external writes, production calls, self-review, publishing, signing, or deployment.
