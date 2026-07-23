---
name: "review-mobile-architecture"
description: "Review mobile architecture, module boundaries, dependency direction, state, navigation, shared/platform boundaries, migrations, and validation evidence."
---
# Review Mobile Architecture

Use this skill for architecture review, design review, module planning, dependency direction checks, navigation/state review, migration planning, or cross-platform boundary decisions.

## Workflow Definition

Objective: evaluate architecture and produce actionable findings without implementing a complete feature.

Trigger: request for architecture review, broad design change, module refactor, migration, shared logic decision, or dependency boundary question.

Inputs: target concern, repository structure, diagrams/docs if present, build files, modules, navigation/state code, shared/platform interfaces, and validation evidence.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, and React Native.

Preconditions:

- Inspect actual files and project structure.
- Identify platform technologies and ownership boundaries.
- Avoid speculative architecture not grounded in the codebase.

Primary owner: `mobile-architect`.

Reviewers: matching platform engineers for feasibility, `mobile-security-reviewer` for sensitive flows, `mobile-performance-reviewer` for performance-sensitive architecture, and `mobile-code-reviewer` for final review of recommendations.

## Steps

1. Define the review question and affected platform(s).
2. Map modules, dependencies, state ownership, navigation, shared/platform boundaries, and migrations.
3. Identify cycles, duplicated responsibilities, hidden platform coupling, unstable contracts, and validation gaps.
4. Classify findings by severity and evidence.
5. Recommend minimal changes with owners and validation gates.
6. Mark unsupported or unavailable checks explicitly.

## Validation Gates

- Findings cite actual files or documented absence.
- Ownership is unique and non-conflicting.
- No implementation role is asked to final-review itself.
- Security, release, and migration risks have human approval gates.

## Failures And Stop Conditions

Stop for missing repository context, ambiguous goals, unsupported capabilities, hidden credentials/private docs, destructive operations, or requests to perform unapproved broad refactors.

## Evidence And Outputs

Output architecture findings, responsibility boundaries, owner map, validation plan, not-applicable criteria with reasons, unsupported omissions, and residual risk.

Acceptance criteria: findings are evidence-backed, scoped, actionable, and independent from implementation.

Human approvals: required for public API changes, persistent format changes, migrations, dependency direction changes, auth/privacy architecture, and release-impacting structure.

Prohibited actions: complete feature implementation, speculative rewrites, fake diagrams as evidence, release approval, and self-review.
