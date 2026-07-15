---
name: integrate-mobile-api
description: Integrate a mobile API with explicit contracts, safe networking, error states, tests, and human approval for auth, privacy, telemetry, or real endpoints.
compatibility: opencode
metadata:
  owner: coordinator
---

# integrate-mobile-api

- Objective: integrate an API using explicit contracts and existing networking patterns.
- Trigger: user asks to connect mobile code to an API or data service.
- Inputs: API contract, base URL policy, auth model, request/response schema, error handling, caching/offline needs.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: contract is provided or discoverable locally; no real secrets are required.
- Primary owner: route by networking layer ownership.
- Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, `mobile-ui-accessibility-reviewer` for user-visible states, `mobile-code-reviewer`.
- Steps: inspect existing clients; validate contract; implement models/client/use case; add loading/empty/error/retry/cancel/offline behavior as applicable; add tests with approved fixtures; run checks.
- Conditional steps: stop for approval before auth, privacy, telemetry, dependency, lockfile, or real endpoint changes.
- Validation gates: compile/type check; unit/integration tests with local fixtures or approved mocks; security review.
- Failures: report missing contract, unavailable test server, real credential requirement, network flakiness.
- Stop conditions: private endpoint or secret needed, production writes, schema ambiguity, dependency change without approval.
- Evidence: contract source, changed files, test fixtures, commands.
- Outputs: API integration, tests, validation report, remaining operational needs.
- Acceptance criteria: integration follows existing patterns and handles documented failure states.
- Human approvals: auth, privacy, telemetry, real endpoints, dependencies, external writes.
- Prohibited actions: embedding secrets, using real credentials, fabricating production data, publishing, destructive commands.
