---
name: integrate-mobile-api
description: Integrates a mobile API with verified contracts, authentication boundaries, transport security, models, error mapping, timeouts, safe retries, caching, offline behavior, log redaction, deterministic tests, and specialist review. Use for a new or changed remote API integration.
---

# Integrate Mobile API

## Objective and trigger

Integrate a verified remote API contract into an existing mobile project with
safe authentication, transport, data mapping, errors, timeouts, retries, caching,
offline behavior, redaction, tests, and review. Activate when network/API work is
the primary outcome, including a material contract change.

Activation does not grant tools. Use only project-allowed read/write tools and
approved local validation commands; do not use MCP, production, or live APIs.

## Inputs

- Authoritative API contract/version, environments, ownership, and compatibility.
- Endpoint methods/paths, request/response/error models, idempotency, pagination,
  rate limits, timeouts, cache semantics, and deprecation policy.
- Authentication/session flow without real tokens, data classification, privacy,
  offline requirements, and logging/telemetry policy.
- Target platforms, architecture, existing client stack, and test infrastructure.

## Preconditions and ownership

Do not infer a contract from examples alone. Inspect project instructions, status,
network/auth/data layers, models, storage/cache, dependencies/locks, call sites,
tests, and platform security configuration before editing. Stop if the contract
or authentication boundary is not authoritative.

Select one primary owner: `android-engineer` for Android, `ios-engineer` for iOS,
`kmp-engineer` when the established KMP shared layer owns networking,
`flutter-engineer` for Flutter, or `react-native-engineer` for React Native.
Native TLS/credential/host changes belong to Android/iOS owners.
`mobile-security-reviewer` and `mobile-test-engineer` are
required; UI/accessibility is required when user states change; performance is
required for material latency/payload/cache impact; final code review is required.

## Workflow and gates

1. **Contract gate:** record source/version, environments, every endpoint/model/
   status/error, nullability, pagination, rate limits, idempotency, cache headers,
   and compatibility. Resolve contradictions before coding.
2. **Threat/data gate:** classify each field and map trust boundaries, auth/token
   lifecycle, authorization expectations, TLS requirements, pinning policy if
   already used, storage, backups, logs/telemetry, and privacy/consent. Never put
   secrets in mobile client code or treat client configuration as server secrets.
3. **Architecture gate:** identify existing client, serialization, repository,
   domain error, cache/offline, cancellation, and threading patterns. Architecture
   approval is required for new boundaries or a new client framework.
4. **Behavior gate:** define validated models, unknown/forward-compatible fields,
   error mapping, cancellation, explicit timeouts, retry eligibility/backoff/
   jitter, idempotency safeguards, caching/staleness, offline queue/conflicts,
   redaction, and user-visible recovery.
5. **Implementation:** primary owner makes the smallest change using existing
   dependencies. Keep transport models separate from domain models where the
   project does. Validate untrusted data and avoid logging bodies/tokens/PII.
6. **Test gate:** use deterministic fake/local contract fixtures only. Cover
   success, malformed/null data, mapped status errors, auth expiry, timeout,
   cancellation, retry eligibility/exhaustion, pagination, cache/offline and
   recovery as applicable. Never call production in tests.
7. **Review gate:** security reviewer evaluates auth, TLS, storage, permissions,
   logs, deep links/WebViews if relevant; UI reviewer checks states; performance
   reviewer checks payload/cache/network patterns when material.
8. **Validation gate:** run discovered compile, lint/static/format, affected tests,
   and broader reasonable platform checks. Finish with independent code review.

## Completion classification

Classify contract/scope; configuration; compilation; unit/integration/UI/snapshot/
E2E tests; lint/static/formatting; dependencies; security/secrets/auth/transport;
accessibility/localization/adaptive states; performance/network/storage/offline;
loading/empty/error/retry/cancellation/recovery; documentation; warnings;
regressions; independent review; and platform-native network/security checks as
`required`, `conditionally-required`, or `not-applicable` with concrete reasons.

## Errors and stop conditions

Stop for unverified contracts, real credentials, unclear auth/authorization,
insecure transport, unknown data classification, unsafe retry semantics,
unapproved dependency/architecture/persistence changes, production calls,
external writes, conflicting edits, destructive actions, or failing checks.

## Outputs, evidence, and acceptance

Return contract traceability, data/threat map, owner/files, models/errors/timeouts/
retries/cache/offline behavior, redaction rules, tests/fixtures, commands/results,
specialist findings, completion ledger, warnings, unavailable checks, and risks.

Acceptance requires every used contract field/status traced, no embedded secret,
secure transport/auth boundaries, deterministic failure/recovery tests, successful
available validation, resolved security blockers, and independent review.

## Human review and prohibited actions

Humans approve contracts, auth, data retention, dependency/public API/persistence
changes, and live environments. Never use real credentials/production data,
weaken TLS/auth, add dependencies without approval, contact production, enable
MCP, deploy/upload/publish/sign/submit, destroy data, or perform Git writes.
