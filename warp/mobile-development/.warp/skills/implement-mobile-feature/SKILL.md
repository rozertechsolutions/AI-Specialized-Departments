---
name: implement-mobile-feature
description: Implement a mobile feature with deterministic platform ownership, tests, and independent review.
---

# Implement Mobile Feature

## Objective

Deliver a requested feature within the detected mobile platform and existing architecture.

## Trigger

Use when the user asks to add or change user-visible or developer-facing mobile behavior.

## Inputs

Feature requirements, target platform, affected screens or modules, API contracts, state/navigation expectations, and acceptance criteria.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native.

## Preconditions

Inspect relevant files, current changes, manifests, commands, dependencies, state management, navigation, tests, and docs. Ask when behavior or API contracts cannot be derived safely.

## Primary Owner

The platform engineer matching the affected runtime. Use `mobile-architect` first for cross-module, navigation, persistence, or shared-boundary changes.

## Reviewers

`mobile-test-engineer`, `mobile-security-reviewer` when data/auth/privacy/network is touched, `mobile-ui-accessibility-reviewer` for UI, `mobile-performance-reviewer` for performance-sensitive paths, and `mobile-code-reviewer`.

## Steps

1. Map requirements to files and platform owner.
2. Define testable behavior and failure states.
3. Implement the smallest complete change using existing patterns.
4. Add or update tests for changed behavior and regressions.
5. Preserve loading, empty, error, retry, cancellation, offline, and recovery states when applicable.
6. Run targeted checks and relevant broader checks.
7. Perform independent reviews and correct in-scope findings.

## Conditional Steps

- If the change crosses module or runtime boundaries, invoke `mobile-architect` before implementation.
- If UI changes are present, run UI/accessibility review.
- If auth, privacy, network, storage, permissions, or telemetry are touched, stop for security review and required human approvals.
- If performance-sensitive paths are touched, capture baseline and post-change evidence when feasible.

## Validation Gates

Required: compile/build or exact blocker, affected tests, lint/type/static analysis when configured, formatting, secret scan by inspection, and code review. Conditional: UI/accessibility, localization, network failure, performance, memory, battery, and release checks.

## Failures and Stop Conditions

Stop for ambiguous requirements, public API changes, persistent format changes, dependency changes, security-sensitive changes requiring human review, unavailable required tools, or unrelated validation failures.

## Evidence

Record files changed, behavior implemented, tests added, commands run, results, skipped checks with reasons, and reviewer findings.

## Outputs

Feature implementation, tests, validation evidence, and limitations.

## Acceptance Criteria

Behavior meets the request, ownership boundaries are preserved, required checks pass or blockers are explicit, and no unsupported capability is introduced.

## Human Approvals

Required for dependencies, permissions, entitlements, privacy, auth, crypto, telemetry, external services, lockfiles, signing, publishing, destructive commands, or spending.

## Prohibited Actions

Do not self-review, bypass validation, invent APIs, use production data, sign, publish, upload, deploy, or modify out-of-scope files.
