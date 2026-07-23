---
name: implement-mobile-feature
description: Implements a scoped mobile feature in the existing architecture, including applicable data, domain, UI, navigation, failure, offline, tests, domain reviews, and independent code review. Use when the user asks to add behavior to an existing mobile project.
---

# Implement a mobile feature

## Objective

Deliver the requested feature completely within the existing architecture and approved scope, with one primary owner, appropriate user and failure states, deterministic tests, validation evidence, domain reviews, and independent code review.

## Trigger

Use for explicit feature implementation in an existing Android, iOS, KMP, Flutter, or React Native project. Use `add-mobile-screen` for a screen-focused request and `integrate-mobile-api` when the primary change is an API integration.

## Inputs

- functional requirements and acceptance criteria;
- affected users, platforms, versions, modules, and public contracts;
- UI/navigation/state and data/domain behavior;
- loading, empty, error, retry, cancellation, offline, recovery, and analytics/privacy expectations;
- compatibility, rollout, migration, dependency, and performance constraints;
- available test environments and required evidence.

## Preconditions

- Read applicable instructions, current changes, architecture, analogous features, configuration, dependencies, and tests.
- Trace each requirement to an observable outcome and identify unresolved ambiguity before editing.
- Confirm ownership from actual changed boundaries and record explicitly partitioned supporting work.
- Obtain approval before a dependency, public API, persistent format, permission, entitlement, or architecture change.

## Ownership

Primary owner: the technology engineer that owns the feature's central code boundary. `kmp-engineer` owns shared KMP behavior; host specialists own only platform partitions. Test, security, UI/accessibility, performance, and code reviewers remain independent.

## Sequence and intermediate gates

1. **Requirement gate:** create a requirement-to-behavior-and-test map, including failures and exclusions. Stop if expected behavior is contradictory or materially incomplete.
2. **Architecture gate:** map data flow, state ownership, navigation, persistence, networking, shared/platform boundaries, concurrency, and existing extension points. Reject unrelated refactoring.
3. **Ownership gate:** name one primary owner and non-overlapping supporting partitions. Confirm that no reviewer is also the implementer.
4. Design the smallest compatible change, including validation, error mapping, cancellation, lifecycle, offline/cache behavior, migration, and rollback when applicable.
5. Implement data/domain behavior before dependent presentation behavior, following existing abstractions and conventions.
6. Implement UI/navigation with complete applicable states, accessibility semantics, localization readiness, adaptive behavior, and platform conventions.
7. Add deterministic tests at the lowest effective levels for success, failure, edge, lifecycle/concurrency, offline, and regression paths in scope.
8. **Validation gate:** run targeted compile/type/static checks and tests, then the reasonable affected suite. Record exact commands, configurations, and results.
9. **Domain-review gate:** explicitly invoke security for sensitive boundaries, UI/accessibility for user-facing behavior, and performance for material runtime impact. The primary owner fixes accepted findings and reruns affected checks.
10. **Independent-review gate:** invoke `mobile-code-reviewer`, resolve accepted findings, rerun validation, and obtain a clean re-review or document a human-accepted residual risk.

## Errors and stop conditions

- Reproduce and isolate build/test failures; do not mask them with defaults, broad exception handling, disabled checks, or weakened assertions.
- Stop for approval when implementation requires architecture, dependency, contract, schema, permission, security, privacy, or release changes outside confirmed scope.
- Report unavailable infrastructure without substituting a claim of success.
- Do not continue if an unresolved high-risk security finding or failed required check remains.

## Completion classification

Classify every coordinator criterion with a feature-specific reason. Requirements, affected configuration, compilation/type checks, closest tests, static checks, security/secret review, applicable UI/accessibility and state handling, warnings, regression evidence, and independent review are normally required. Other test levels, dependencies, localization, adaptive UI, offline behavior, performance domains, and documentation become required when the feature intersects them.

## Outputs and evidence

Return the requirement trace, ownership record, changed files, architecture impact, state/error/offline behavior, tests, exact validation results, domain and independent review findings, fixes, unavailable checks, residual risks, and completion-classification table.

## Acceptance criteria

- Every confirmed requirement maps to implemented behavior and evidence.
- The feature follows existing architecture and public contracts, with no unrelated change.
- Applicable failure, recovery, accessibility, localization, adaptive, security, and performance behavior is addressed.
- Required checks pass with no unexplained warning and independent review has no unresolved blocking finding.

## Human review requirements

Humans approve requirement ambiguity, scope expansion, dependencies, public/persistent contracts, sensitive permissions or data behavior, unavailable required validation, and accepted residual risk.

## Prohibited actions

Do not invent behavior, change architecture or dependencies without approval, weaken validation, use credentials, enable external integrations, publish/sign/deploy, perform destructive operations, or self-approve.
