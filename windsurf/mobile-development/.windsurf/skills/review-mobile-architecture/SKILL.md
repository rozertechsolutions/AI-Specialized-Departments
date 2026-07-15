---
name: review-mobile-architecture
description: Review mobile architecture, module boundaries, state, navigation, dependency direction, and shared/platform boundaries without implementing features.
---

# review-mobile-architecture

## Objective

Evaluate architecture quality, risks, and migration paths for mobile repositories without taking implementation ownership.

## Inputs

Architecture question, target platforms/modules, relevant files, diagrams/docs if present, constraints, and requested depth.

## Supported Technologies

Android, iOS, Kotlin Multiplatform, Flutter, React Native, and mixed mobile repositories.

## Preconditions

- Inspect source layout, module graph, dependency configuration, navigation/state patterns, shared/platform boundaries, and tests.
- Keep review read-only unless the user explicitly requests documentation edits.

## Primary Owner

`mobile-architect`

## Reviewers

`mobile-code-reviewer`; add technology owners and security/performance/accessibility reviewers where the architecture affects their scope.

## Steps

1. Map modules, dependencies, entry points, state ownership, navigation, data flow, and platform boundaries.
2. Identify coupling, cycles, ownership conflicts, migration risks, and testability gaps.
3. Check technology-specific constraints such as KMP source sets, Android Gradle modules, iOS targets/schemes, Flutter packages, and React Native native bridges.
4. Prioritize findings by severity and evidence.
5. Provide concrete remediation options without unapproved implementation.

## Validation Gates

Native project configuration review, dependency direction review, test strategy review, security/privacy boundary review, performance-sensitive path review, and unsupported-infrastructure reporting.

## Failures And Stop Conditions

Stop on insufficient repository access, ambiguous scope, request to approve release, or request to implement complete features under architecture ownership.

## Evidence And Outputs

Findings with file references, risk level, rationale, affected platforms, recommended next steps, and open questions.

## Acceptance Criteria

The review identifies actionable architectural risks and respects non-implementation boundaries.

## Prohibited Actions

No feature implementation, release approval, fabricated diagrams, dependency changes, or broad refactors without explicit approval.
