---
name: review-mobile-architecture
description: Workflow for reviewing mobile architecture, module boundaries, dependencies, state, navigation, migrations, and shared/platform placement.
---

# Review Mobile Architecture

## Objective

Evaluate architecture correctness, maintainability, ownership, dependency direction, and platform/shared boundaries.

## Trigger

Use when the user asks for architecture review or when a task affects architecture.

## Inputs

Project structure, dependency graph, build files, navigation/state code, shared modules, migration plans, and user goals.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native.

## Preconditions

Inspect relevant files and configured commands without editing by default.

## Primary Owner

`mobile-architect`

## Reviewers

Affected platform engineers, `mobile-test-engineer`, `mobile-security-reviewer` when sensitive, and `mobile-code-reviewer` for final review of implemented changes.

## Steps

1. Map modules, dependencies, and ownership.
2. Identify architecture decisions and constraints.
3. Check shared/platform boundaries and cycles.
4. Review state, navigation, lifecycle, and migration risk.
5. Recommend minimal changes with owners and validation.
6. If implementation is requested, delegate to owners.

## Conditional Steps

- KMP: inspect source sets and target dependencies.
- RN/Flutter: inspect host boundaries and native bridge/channel placement.
- Android/iOS: inspect platform lifecycle and configuration boundaries.

## Validation Gates

No conflicting ownership, no dependency cycles, migration path is explicit, and tests/build checks are identified.

## Failures

Stop on missing architecture context, unknown target surface, or conflicting requirements.

## Stop Conditions

Do not implement broad architecture changes without explicit approval.

## Evidence

Inspected files, diagrams or summaries when useful, risks, recommendations, and unavailable checks.

## Outputs

Architecture review report and optional implementation plan.

## Acceptance Criteria

Architecture risks are actionable, scoped, and mapped to owners and validation.

## Human Approvals

Required for broad migrations, public contracts, dependency direction changes, or shared API changes.

## Prohibited Actions

No complete feature implementation, release approval, unsupported components, or self-review.
