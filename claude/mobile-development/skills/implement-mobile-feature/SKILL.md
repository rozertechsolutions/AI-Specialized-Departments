---
name: implement-mobile-feature
description: Implements a scoped mobile feature using existing project conventions. Use for feature work in Android, iOS, KMP, Flutter, or React Native.
---

# Implement Mobile Feature

## Objective

Implement one approved feature end to end within an existing mobile project while preserving architecture, contracts, dependencies, security, accessibility, performance, and user changes.

## Trigger

Use when the user requests new behavior that is broader than a single screen and is not primarily a defect, test-only change, performance optimization, security audit, or release task.

## Inputs

- functional requirements, user journeys, and measurable acceptance criteria;
- current repository snapshot, applicable instructions, and relevant source;
- target technologies, modules, variants, schemes, flavors, devices, locales, and supported versions;
- design, navigation, state, API, storage, analytics, permission, and error-state requirements;
- existing architecture and testing conventions;
- allowed dependencies and human approvals.

## Supported technologies

Android, iOS, KMP, Flutter, and React Native, including explicitly evidenced hybrid boundaries.

## Preconditions

- The current behavior and requested outcome are understood.
- All affected files and configuration have been inspected.
- Existing user changes and ownership boundaries are known.
- Commands, toolchains, and test infrastructure are discovered from the project.
- API contracts, designs, identifiers, and sensitive behavior are supplied rather than invented.
- One primary owner is selected before editing.

## Primary owner and reviewers

Choose the technology owner for the dominant production surface. Partition hybrid work before editing; each partition has one owner and returns to the coordinator. Use mobile-architect only if boundaries or public contracts change. mobile-test-engineer reviews cross-cutting coverage. mobile-security-reviewer and mobile-ui-accessibility-reviewer are required when their domains apply. mobile-performance-reviewer is required for performance-sensitive paths. mobile-code-reviewer is always final and read-only.

## Ordered workflow

1. Translate the request into traceable acceptance criteria, non-goals, edge cases, and prohibited changes.
2. Inspect repository status, instructions, architecture, configuration, dependencies, current behavior, tests, and related history if a safe read tool provides it.
3. Identify the dominant technology owner and partition any host, shared, UI, data, and test slices without overlap.
4. Reproduce or characterize the existing behavior with the smallest safe evidence.
5. Produce a minimal implementation plan listing affected files, contracts, state transitions, UI states, error handling, tests, and validation commands.
6. Obtain approval for any architecture, dependency, API, persistence, permission, privacy, telemetry, lockfile, or build change.
7. Implement one slice at a time, following current naming, state, navigation, dependency-injection, concurrency, storage, and error-handling patterns.
8. Add tests inseparable from each production slice. Return cross-cutting or test-only work to mobile-test-engineer.
9. Validate each slice with the narrowest discovered formatter, analyzer, compiler, and tests before continuing.
10. Verify complete loading, empty, error, retry, cancellation, recovery, offline, accessibility, localization, and adaptive states where applicable.
11. Run broader relevant checks without signing, publication, destructive device action, or external write.
12. Obtain specialist reviews, return findings to the owning implementer, correct only in-scope issues, and rerun affected checks.
13. Obtain mobile-code-reviewer review from a reviewer that did not implement the feature.
14. Complete the criterion ledger, triple review, and final verification.

## Conditional steps

- Architecture boundary changes: mobile-architect produces a human-approved decision before implementation.
- KMP shared behavior: kmp-engineer owns shared code; native owners validate target hosts.
- Flutter or React Native bridge: cross-platform owner defines the contract; native owner implements non-trivial host code.
- Remote data: apply integrate-mobile-api only if the task is primarily an API integration; otherwise keep API work as a scoped feature slice with mandatory security review.
- UI: mobile-ui-accessibility-reviewer checks semantics, focus, dynamic text, localization, sizes, orientations, and all data states.
- Sensitive behavior: mobile-security-reviewer checks threats, permissions, privacy, auth, storage, transport, logs, and dependencies.

## Validation gates

- Gate 1: requirements, non-goals, affected platforms, and ownership are explicit.
- Gate 2: baseline or existing behavior is evidenced.
- Gate 3: every sensitive or contract-changing decision has approval.
- Gate 4: each implementation slice and its targeted tests pass.
- Gate 5: broader applicable checks and specialist reviews pass with no unexplained warning.
- Gate 6: independent final review and triple validation pass.

## Failures

Stop on a required failure, preserve exact evidence, and determine whether it is caused by the feature, pre-existing, or environmental. Fix only caused in-scope failures. Never weaken a test, suppress a warning, add a fallback, broaden a catch, change architecture, or alter production semantics merely to pass.

## Stop conditions

Stop for ambiguous behavior, missing contract or design, conflicting user changes, unknown ownership, inaccessible affected files, unapproved dependency or sensitive change, missing required toolchain, production credential need, signing, external write, publication, destructive action, or expanding scope.

## Evidence

Record requirements-to-file mapping, baseline, changed files, tool and SDK versions, commands and results, tests by acceptance criterion, UI and security review, performance evidence when applicable, warnings, corrections, and unavailable infrastructure.

## Outputs

- minimal completed feature changes;
- tests and documentation required by project convention;
- ownership and reviewer record;
- criterion ledger and exact validation evidence;
- residual risks and human actions.

## Acceptance criteria

Every approved behavior and edge state is implemented on the intended targets, existing contracts and conventions are preserved unless approved, relevant checks pass, required reviewers find no unresolved blocker, and no prohibited action occurs.

## Human approvals

Require approval for architecture, public or persistent contracts, dependencies, permissions, entitlements, auth, privacy, telemetry, lockfiles, build configuration, external writes, and any behavior not explicitly covered by requirements.

## Prohibited actions

Do not implement unrequested behavior, invent API or product rules, expose secrets, add unapproved dependencies, let an implementation owner perform final review, sign, publish, upload, submit, deploy, distribute, spend money, destroy data, or run Git write commands.
