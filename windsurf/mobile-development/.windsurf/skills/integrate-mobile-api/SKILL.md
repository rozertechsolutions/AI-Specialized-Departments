---
name: integrate-mobile-api
description: Integrate a mobile API client or endpoint using existing networking, error handling, security, offline, and test conventions.
---

# integrate-mobile-api

## Objective

Integrate an API safely into a mobile client without leaking secrets or weakening authentication, privacy, or network security.

## Inputs

API contract, endpoint type, authentication model, data models, caching/offline expectations, affected platforms, and approved scope.

## Supported Technologies

Android, iOS, KMP shared networking, Flutter, React Native, and native bridge integrations.

## Preconditions

- Inspect existing networking stack, serialization, dependency injection, error model, retry/cancellation, offline/cache strategy, logging, telemetry, and tests.
- Confirm public client configuration versus protected secrets.
- Get human approval for auth changes, privacy changes, endpoints, certificates, network security config, ATS, deep links, WebViews, analytics, telemetry, dependencies, and lockfiles.

## Primary Owner

Technology owner for the networking layer, with `kmp-engineer` primary for shared KMP clients.

## Reviewers

`mobile-security-reviewer`, `mobile-test-engineer`, and `mobile-code-reviewer`; add performance reviewer for high-volume or startup-critical calls.

## Steps

1. Trace API requirements and data flow.
2. Add or update models, client calls, mappers, repositories, and UI state integration using existing patterns.
3. Implement explicit error, cancellation, retry, timeout, offline, loading, and recovery behavior where applicable.
4. Add deterministic tests with fixtures/mocks approved by project conventions.
5. Validate logs do not expose sensitive data.
6. Run discovered checks and independent final review.

## Validation Gates

Compilation/type checks, unit/integration tests, lint/static analysis/formatting, security review, dependency review, network security review, offline/error-state coverage, and secret detection.

## Failures And Stop Conditions

Stop on missing API contract, unclear auth/privacy requirements, request to embed secrets, unapproved dependency, certificate/signing change, or validation failure.

## Evidence And Outputs

Changed files, API traceability, tests/fixtures, command results, security review, unavailable checks, and residual risks.

## Acceptance Criteria

API behavior is implemented with safe error handling, no secret leakage, deterministic tests, and independent review.

## Prohibited Actions

No real endpoints requiring secrets unless approved, no credential import, no insecure TLS bypass, no sensitive logging, and no fabricated API success.
