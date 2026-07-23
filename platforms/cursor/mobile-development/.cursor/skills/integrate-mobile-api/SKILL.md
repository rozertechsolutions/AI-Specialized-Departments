---
name: integrate-mobile-api
description: Integrate a mobile app with an API using existing networking, models, error handling, caching, and security conventions.
---

# integrate-mobile-api

Objective: integrate an API without embedding secrets or inventing contracts, using existing networking and state patterns.

Trigger: request to connect mobile code to an API, endpoint, SDK, backend, or service.

Inputs: API contract, schemas, authentication behavior, error model, caching/offline needs, privacy requirements, and affected platforms.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: inspect existing network layer, models, serialization, storage, auth, tests, and environment config; verify contract from provided docs or repository files; obtain approval for auth/privacy, endpoints, dependencies, lockfiles, telemetry, or external writes.

Primary owner: runtime boundary owner; `kmp-engineer` owns shared KMP network logic when present.

Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, `mobile-performance-reviewer` for network/storage efficiency, and `mobile-code-reviewer`.

Steps:

1. Verify API contract and data sensitivity.
2. Classify criteria for network, offline, loading, empty, error, retry, cancellation, and recovery.
3. Implement models/client/state integration using existing patterns.
4. Avoid real secrets and production writes; use existing public config only when already present.
5. Add tests with fixtures/mocks where the project supports them.
6. Run relevant build, tests, static analysis, and security checks.
7. Hand off security and code review.

Validation gates: contract traceability, serialization/parsing tests when feasible, network error handling, offline/cache behavior when applicable, secret scan, auth/privacy review, and independent code review.

Failures: missing API contract, real credential required, endpoint ambiguity, unapproved dependency, production write, or validation failure.

Stop conditions: credentials, private URLs, auth changes, privacy changes, telemetry, external service activation, destructive operations, signing, publishing, or spending.

Evidence: contract source, changed files, test fixtures, commands and results, security findings, unavailable infrastructure, and criteria classification.

Outputs: API integration, tests or test-gap explanation, validation report, and human approval list.

Acceptance criteria: API behavior is traceable to a contract, handles failure states, contains no secrets, and required checks pass or blockers are explicit.

Human approvals: auth, endpoints, dependencies, lockfiles, privacy, telemetry, production systems, external writes, credentials, and release/signing changes.

Prohibited actions: fabricated endpoints, embedded secrets, live production writes, unapproved SDKs, silent parsing failures, signing, publishing, uploading, deployment, or final self-review.
