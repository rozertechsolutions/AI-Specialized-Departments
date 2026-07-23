---
name: "implement-mobile-feature"
description: "Implement a scoped mobile feature across Android, iOS, KMP, Flutter, or React Native with owner selection, tests, validation, and independent review."
---
# Implement Mobile Feature

Use this skill when the user asks to add or change mobile product behavior.

## Workflow Definition

Objective: implement the requested feature within existing architecture and platform conventions.

Trigger: explicit request for new or changed mobile behavior.

Inputs: feature requirements, affected platform(s), UX states, data/API needs, acceptance criteria, existing files, and constraints.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, and React Native.

Preconditions:

- Inspect existing structure, dependencies, commands, and conventions.
- Identify primary owner by affected technology.
- Ask for approval before auth, privacy, permissions, dependencies, lockfiles, signing/build config, external writes, or destructive commands.

Primary owner: matching platform engineer; `kmp-engineer` owns shared KMP logic; `mobile-architect` owns broad architectural decisions.

Reviewers: `mobile-test-engineer`, relevant read-only reviewers, and `mobile-code-reviewer`.

## Steps

1. Trace requirements to files and classify completion criteria.
2. Select one primary owner and list reviewers.
3. Inspect current architecture, UI patterns, state management, navigation, tests, and commands.
4. Implement the smallest scoped change that satisfies the feature.
5. Cover loading, empty, error, retry, cancellation, recovery, offline, accessibility, localization, and adaptive layout states when applicable.
6. Add or update tests at the lowest reliable level and broader levels when justified.
7. Run discovered format/lint/typecheck/build/test commands that are relevant and safe.
8. Request independent reviews for test, security, UI/accessibility, performance, and final code review as applicable.
9. Record evidence and limitations.

## Validation Gates

- Requirements are mapped to implementation and tests.
- No ownership overlap or self-review.
- Public APIs, persistent formats, dependencies, permissions, and privacy-sensitive behavior are changed only with approval.
- Relevant platform checks are run or reported unavailable.

## Failures And Stop Conditions

Stop for unclear requirements, architecture conflict, unsupported technology, missing approval for sensitive changes, failing validation caused by the change, credentials, publication/signing/upload requests, or destructive operations.

## Evidence And Outputs

Output changed files, behavior summary, tests added or not-applicable reasons, commands run, validation results, reviewers used, unsupported omissions, and remaining risk.

Acceptance criteria: feature works within scope, validations pass or are clearly unavailable, required reviews are complete, and no fabricated evidence exists.

Human approvals: required for security/privacy/auth, dependencies, lockfiles, permissions, manifests, entitlements, signing/build config, external services, release actions, and destructive commands.

Prohibited actions: broad refactors, unsupported abstractions, fake data in production, weakening validation, release actions, and self-review.
