---
name: implement-mobile-feature
description: Workflow for implementing a mobile feature with clear ownership, tests, security, accessibility, and independent review.
---

# Implement Mobile Feature

## Objective

Implement requested mobile behavior in the correct platform or shared layer with evidence-backed validation.

## Trigger

Use when the user asks to add or change product behavior.

## Inputs

Feature requirements, target platforms, existing project files, UX details, API contracts, state/navigation impact, and acceptance criteria.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native when present in the project.

## Preconditions

Inspect project conventions, detect target technology, identify primary owner, and clarify ambiguous requirements before editing.

## Primary Owner

The platform or shared engineer matching the affected implementation surface.

## Reviewers

`mobile-architect` when boundaries change, `mobile-test-engineer`, `mobile-security-reviewer` for sensitive surfaces, `mobile-ui-accessibility-reviewer` for UI, and `mobile-code-reviewer`.

## Steps

1. Trace requirements to files and owners.
2. Identify architecture, security, accessibility, and test impacts.
3. Implement the smallest complete change.
4. Add or update tests proportional to risk.
5. Run discovered formatting, lint, typecheck, build, and tests.
6. Correct failures caused by the change.
7. Complete independent final review.

## Conditional Steps

- UI feature: include loading, empty, error, retry, cancel, recovery, localization, and accessibility states as applicable.
- API feature: validate networking, serialization, auth, retries, cancellation, and offline behavior as applicable.
- Shared feature: validate source-set placement and platform actuals.

## Validation Gates

Requirements traceability, relevant tests, static checks, security review, accessibility review for UI, and final review.

## Failures

Stop on unsupported platform, unclear ownership, missing approval, failing caused checks, or unverifiable core behavior.

## Stop Conditions

Do not proceed if requirements or platform targets are materially ambiguous.

## Evidence

Changed files, commands run, test results, review findings, unavailable infrastructure, and residual risk.

## Outputs

Implemented feature, tests, and validation report.

## Acceptance Criteria

Feature meets requested behavior, preserves conventions, handles relevant errors/states, and passes available checks.

## Human Approvals

Required for sensitive changes, dependencies, lockfiles, external services, signing, publishing, or destructive actions.

## Prohibited Actions

No broad refactors, unsupported integrations, fabricated data, self-review, publishing, signing, upload, deployment, or spending.
