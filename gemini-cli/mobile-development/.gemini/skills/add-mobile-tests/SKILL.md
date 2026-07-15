---
name: add-mobile-tests
description: Adds deterministic mobile regression coverage at the correct test level using existing conventions, fixtures, runners, and synchronization. Use when the requested outcome is test creation, coverage improvement, or validation of known behavior.
---

# Add Mobile Tests

## Objective and trigger

Add the smallest meaningful deterministic test set that proves specified mobile
behavior at the correct level and follows the project's existing test pyramid.
Activate when tests or coverage are the primary requested outcome. For a bug or
feature, use its Skill and invoke this workflow as the test stage.

Activation does not grant tools. Use only project-allowed read/write tools and
approved local test commands; do not use MCP, real services, or remote executors.

## Inputs

- Behavior contract, acceptance criteria, risks, and known regressions.
- Technology/platforms, affected production code, and supported environments.
- Existing test conventions, runners, fixtures, devices/simulators, and CI limits.
- Required success, failure, edge, lifecycle, concurrency, offline, and UI cases.

## Preconditions and ownership

Inspect instructions, status/diff, production behavior, current tests, test
configuration, fixtures, utilities, and commands. Do not treat line coverage as
the behavior contract or invent expected results.

`mobile-test-engineer` is primary owner of strategy and test/fixture files.
Platform engineers support only when a production seam is demonstrably necessary;
that change requires separate explicit scope. Security/UI/performance reviewers
are conditional based on behavior. `mobile-code-reviewer` performs final review.

## Workflow and gates

1. **Behavior gate:** make expected behavior observable and map each risk/criterion
   to an assertion, including relevant failure and recovery paths.
2. **Level gate:** select unit, integration, UI/widget/component, snapshot, or E2E
   based on the lowest level that can prove the contract. Explain why higher or
   lower levels are not used and avoid duplicate coverage.
3. **Convention gate:** discover runners, naming, location, setup/teardown,
   fixtures, async synchronization, device matrix, snapshot policy, and commands.
4. **Determinism gate:** control clocks, schedulers, randomness, locale/time zone,
   network/storage, animations, data, global state, and cleanup as applicable.
   Use event/idling synchronization, never arbitrary sleeps.
5. **Implementation:** edit only assigned tests, fixtures, and explicitly scoped
   test configuration. Use fabricated data only as deterministic test data and
   ensure it cannot be mistaken for production credentials or personal data.
6. **Execution gate:** run the narrowest new test first and prove it can detect the
   target behavior when regression-first work permits. Run affected suites and
   repeat flakiness-sensitive cases reasonably. Record skips, retries, duration,
   warnings, devices, and infrastructure limitations.
7. **Review gate:** platform owner confirms assertions match production contract;
   relevant specialist reviews test security/accessibility/performance claims;
   independent code reviewer evaluates adequacy and false-positive risk.

## Completion classification

Classify requirements/risk mapping; configuration; compilation; unit/integration/
UI/snapshot/E2E levels; lint/static/formatting; dependencies; security/test-data
secrets; accessibility/localization/adaptive checks; performance/resource/offline
checks; failure/retry/cancellation/recovery; documentation; warnings; regression
detection; independent review; and platform-native test infrastructure as
`required`, `conditionally-required`, or `not-applicable` with concrete reasons.

## Errors and stop conditions

Stop when expected behavior is undefined, production code must change, a runner/
dependency must be installed or updated, tests require real credentials/data,
paid/production/external services, destructive cleanup, conflicting edits, or
failures cannot be safely attributed. Report flaky/unavailable tests honestly.

## Outputs, evidence, and acceptance

Return behavior-to-test matrix, selected levels/reasons, files/fixtures, controls
for determinism, exact commands/results, repeat evidence, skips/warnings, coverage
gaps, unavailable infrastructure, completion ledger, and production handoffs.

Acceptance requires meaningful assertions for scoped risks, deterministic tests,
successful available targeted/affected suites, no hidden skips/weakened checks,
explicit gaps, and independent review.

## Human review and prohibited actions

Humans approve any production seam, new dependency, costly/real service, or
residual gap. Never change production behavior for tests, weaken/delete/quarantine
tests, use arbitrary sleeps, real credentials/PII/services, add dependencies,
sign/publish/deploy/upload, destroy uncertain data, or perform Git writes.
