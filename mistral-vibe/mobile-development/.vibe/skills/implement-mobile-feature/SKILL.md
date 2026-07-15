---
name: implement-mobile-feature
description: Use when implementing a defined mobile feature in an existing Android, iOS, Kotlin Multiplatform, Flutter, React Native, or mixed project.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - todo
  - ask_user_question
  - task
  - write_file
  - edit
  - bash
---

# Implement Mobile Feature

## Objective and trigger

Implement one defined feature completely within the existing architecture, with data/domain/UI/navigation/error/offline behavior as applicable, targeted tests, specialist review, and evidence. Do not use when behavior or acceptance criteria are still speculative.

## Inputs

- User-visible behavior, non-goals, acceptance criteria, supported platforms/versions, entry/navigation points, and data/API contracts.
- Existing architecture and ownership boundaries, compatibility constraints, analytics/privacy requirements, and validation commands.
- Required loading, empty, error, retry, cancellation, offline, recovery, localization, accessibility, and performance states.

## Preconditions and ownership

Inspect instructions, status/diff, related implementation/tests, callers, manifests/build files, dependencies, and conventions. Create a requirement-to-file/test trace. Stop if product behavior, API contracts, platform routing, or conflicting user edits cannot be resolved.

Identify every affected runtime and file boundary, partition mixed work into non-overlapping units, and assign one platform owner to each unit. KMP shared code stays with `kmp-engineer`; Android/iOS UI or host code stays with its native owner; Flutter/React Native runtime code stays with its framework owner while substantial native host/module code receives the matching native owner. Each platform owner also owns the platform-specific tests in its unit. `mobile-test-engineer` owns strategy/fixtures and only an explicitly separated test-only unit. Use `mobile-architect` only for a new or consequential boundary. Security, UI/accessibility, and performance reviewers support when their domains are affected; final `mobile-code-reviewer` is mandatory.

## Sequence and gates

1. Scope gate: record requirements, non-goals, non-overlapping units and one primary owner per unit, affected contracts, reviewers, and criterion classifications.
2. Design gate: map data flow, state ownership, navigation, lifecycle/concurrency, platform/shared boundaries, failure/recovery states, and test seams. Obtain approval for any architecture/public/persistent/dependency change.
3. Implement the smallest vertical slice using existing patterns; validate untrusted input and preserve backward compatibility.
4. Complete domain/data mapping, UI states, navigation, cancellation, retry/offline behavior, and error propagation only where required by the feature.
5. Intermediate reviews: security for auth/data/network/storage/permissions; UI/accessibility for UI; performance for material resource impact. Sensitive findings block further work.
6. The assigned test owner adds deterministic regression coverage at appropriate levels; `mobile-test-engineer` validates level selection, fixtures, determinism, and coverage without changing production behavior.
7. Run targeted format/type/static/lint/compile/tests, then the broader reasonable affected suite. Record exact output and new warnings.
8. Independent code review: inspect every changed file and affected caller/contract. Correct in-scope findings, rerun affected checks, and re-review.
9. Review final status/diff against the requirement trace and update required documentation.

## Errors and stop conditions

Stop on ambiguous requirements/contracts, unapproved dependencies or architecture changes, credentials/production access, permission/entitlement/privacy changes awaiting human review, signing/release actions, destructive commands, unavailable required tooling, conflicting user edits, or unrelated failing checks.

## Outputs and evidence

Provide requirement trace, ownership, behavior/state changes, complete file list, tests and review findings, commands/results, criterion matrix, compatibility/security/accessibility/performance notes, warnings, and blockers.

## Acceptance and human review

Every accepted requirement and applicable state is implemented and tested; required safe build/static/test gates pass; independent review has no unresolved required finding; no unexplained warning, secret, unapproved dependency, unrelated change, or contract regression remains. Human approval is required for sensitive and contract-changing work described in `AGENTS.md`.

## Prohibited actions

Do not expand scope, add dependencies without approval, hide errors, weaken tests/lint/security/accessibility, access real credentials/data, enable integrations, sign/publish/deploy, mutate Git, or fabricate validation.
