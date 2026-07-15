---
name: integrate-mobile-api
description: Integrate a mobile API or network/data contract with secure configuration, error handling, offline behavior, and tests.
---

# integrate-mobile-api

Objective: integrate an API or data contract safely using existing networking, storage, and error-handling patterns.

Trigger: request to connect a mobile app to an API, backend, SDK, data source, or platform channel service.

Inputs: API contract, authentication requirements, data models, environments, error states, caching/offline expectations, privacy constraints.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: inspect existing networking/storage conventions; verify contract source; never invent real endpoints or credentials; obtain approval for auth, privacy, dependencies, lockfiles, telemetry, permissions, or external writes.

Primary owner: selected by deterministic routing; `kmp-engineer` when shared networking/data logic is in KMP.

Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, `mobile-performance-reviewer` for network/storage efficiency, and `mobile-code-reviewer`.

Ordered steps:

1. Trace API requirements and data ownership.
2. Classify criteria including security, privacy, network, storage, offline, retry, cancellation, and recovery.
3. Inspect existing clients, serialization, errors, caching, dependency injection, and tests.
4. Implement models/client/use-case/UI integration only as requested.
5. Handle loading, empty, error, retry, cancellation, recovery, and offline states when applicable.
6. Add tests using approved mocks/fixtures only.
7. Run validation and security review.
8. Record external integration status and human actions.

Conditional steps: stop if the API contract is missing or requires credentials; ask before adding SDKs or lockfile changes; request performance review for caching/background/network impact.

Validation gates: compile/build, unit/integration tests with safe fixtures, static analysis/lint/typecheck, secret scan, security/privacy review, network/offline behavior evidence, performance review when relevant, final code review.

Failures: missing contract, real credential need, unapproved endpoint/environment, validation failure, insecure storage/transport, or unsupported integration.

Stop conditions: production writes, secrets, auth/privacy change without approval, dependency/lockfile change without approval, signing/publishing/upload/deployment, destructive commands.

Evidence: contract source, files changed, mocks/fixtures used, commands run, results, unavailable infrastructure, criteria classification.

Outputs: integration, tests or test-gap explanation, security/performance review findings, validation report.

Acceptance criteria: integration follows existing patterns, protects credentials/data, handles failures, and has honest validation evidence.

Human approvals: auth, privacy, telemetry, dependencies, lockfiles, permissions, external writes, real endpoints, credentials.

Prohibited actions: hardcoded secrets, fabricated production endpoints, live writes, unsupported SDK simulation, publication, signing, uploading, deployment.
