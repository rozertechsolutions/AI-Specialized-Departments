---
name: implement-mobile-feature
description: Implement a scoped mobile feature in an existing Android, iOS, KMP, Flutter, React Native, or hybrid repository with tests and independent review.
when_to_use: Use when requested behavior adds or changes a coherent user or system capability; use add-mobile-screen or integrate-mobile-api when that narrower workflow fully covers the task.
argument-hint: "[feature request and acceptance criteria]"
model: inherit
---

# Objective

Implement the feature in `$ARGUMENTS` with traceable requirements, controlled scope, relevant UI/data/domain/navigation states, validation, and independent review.

# Required input and supported scope

Require observable behavior, acceptance criteria, affected users/platforms, data and API expectations, error/offline behavior, compatibility constraints, and explicit non-goals. Support Android, iOS, KMP, Flutter, React Native, and inspected hybrid combinations.

# Preconditions and inspection

Read project instructions; inspect status/diff, technology configuration, architecture, affected call paths, models, navigation, persistence/network layers, UI patterns, dependency conventions, tests, and executable scripts. Stop if requirements conflict, ownership is unclear, or the feature needs an unapproved public API, persistence, architecture, dependency, permission, or backend-contract change.

# Ownership

Choose the dominant technology engineer as primary owner. Use `kmp-engineer` only for shared KMP ownership and relevant native owners for hosts. Add `mobile-architect` only for material boundary decisions; `mobile-test-engineer` owns test strategy; security and UI/accessibility reviews are required when relevant; `mobile-performance-reviewer` is required for performance-sensitive paths; `mobile-code-reviewer` is always final and independent.

# Procedure and gates

1. Trace each acceptance criterion to existing entry points and define data, domain, UI, navigation, analytics/privacy, and failure effects. Gate: no unresolved material behavior.
2. Map implementation ownership and the minimal file set. Gate: architecture is preserved or an explicit decision is approved.
3. Design success, loading, empty, error, retry/recovery, cancellation, and offline states where applicable; identify accessibility/localization/adaptive needs.
4. Implement the smallest vertical slice using existing conventions. Validate inputs and untrusted data, preserve backward compatibility, and avoid unrelated refactoring.
5. Add or update deterministic tests at the lowest sufficient levels, including failure and edge paths. Do not change production semantics solely for tests.
6. Run targeted compile/type checks, tests, lint/static analysis, and formatting checks, then broader affected suites when reasonable. Use only commands discovered in the repository.
7. Obtain required security, UI/accessibility, performance, and test reviews. Have the primary owner fix findings, rerun affected checks, then obtain final `mobile-code-reviewer` review.

# Failure and stop handling

Stop on failed required checks, unavailable required contracts, unsafe credential/signing needs, unexplained behavior regression, or changes beyond approved scope. Report the exact failure, evidence, affected behavior, and user decision needed. Never substitute a speculative implementation.

# Evidence and acceptance

Return a requirement-to-file/test trace, changed files, decisions, exact commands/results, specialist findings and resolutions, unavailable checks, and residual risks. Classify each considered build/test/lint/format/security/accessibility/localization/adaptive/performance/network/offline criterion as `required`, `conditionally-required`, or `not-applicable`, with reasons.

Accept only when all requested behavior and relevant states are implemented, required tests/checks pass, required reviews have no unresolved blocker, scope is contained, documentation is updated where conventions require, and no result is fabricated.

# Human review and prohibited actions

Require human review for sensitive configuration, permissions/entitlements, auth/privacy, dependencies, public contracts, persistence, and architecture changes. Never publish, sign, upload, deploy, access secrets, silently alter architecture, weaken controls/tests, or let an implementer provide the independent final approval.
