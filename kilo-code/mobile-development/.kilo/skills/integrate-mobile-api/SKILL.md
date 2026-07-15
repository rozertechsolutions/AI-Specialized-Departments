---
name: integrate-mobile-api
description: Use when integrating a mobile app with an API while preserving security, error handling, cancellation, offline behavior, and existing networking conventions.
---

# integrate-mobile-api

- Objective: Integrate mobile API access using existing networking, serialization, authentication, cancellation, retry, offline, and error-handling conventions.
- Trigger: User asks to connect a screen or feature to an API, service, client, endpoint, or data source.
- Inputs: API contract, endpoint class or interface, auth requirements, request/response models, error states, caching/offline needs, and test expectations.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: Inspect existing networking stack, do not embed real endpoints or secrets, and ask before auth/privacy/dependency changes.
- Primary owner: Platform engineer for the affected code; `kmp-engineer` owns shared KMP clients when present.
- Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, and `mobile-code-reviewer`.
- Steps: Locate existing API patterns; model success/error/cancellation/retry/offline behavior; implement scoped integration; add tests with fixtures/mocks where appropriate; avoid real secret values; run targeted checks; request security review.
- Validation gates: Type/compile checks, tests for success and failure paths, no secrets, auth/privacy approval where applicable, and secure logging.
- Failures: Stop on missing API contract, real credential requirement, production endpoint ambiguity, unsupported networking stack, or validation failure.
- Stop conditions: External service activation, credential import, dependency/lockfile change without approval, telemetry/privacy change without approval, publishing, signing, or destructive command.
- Evidence: Files changed, contract assumptions, commands run, tests, secret-scan reasoning, and unavailable infrastructure.
- Outputs: API integration, fixtures/tests, security notes, validation report, and unresolved contract questions.
- Acceptance criteria: Integration follows existing conventions, handles failure paths, avoids secrets, and passes or reports applicable checks.
- Human approvals: Required for auth, privacy, production endpoints, dependencies, lockfiles, telemetry, analytics, external writes, and credential handling.
- Prohibited actions: Hardcoding secrets or private endpoints, logging sensitive data, activating integrations, publishing, signing, deployment, destructive commands, and fabricated validation.

