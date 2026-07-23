---
name: review-mobile-architecture
description: Review existing mobile architecture, dependencies, state/navigation ownership, platform/shared boundaries, testability, security boundaries, and maintainability without rewriting it.
when_to_use: Use for an evidence-based architecture assessment, migration readiness analysis, or prioritization of structural risks across Android, iOS, KMP, Flutter, React Native, or hybrid code.
argument-hint: "[scope and architecture concern]"
model: inherit
---

# Objective

Map and assess the current architecture described in `$ARGUMENTS`, producing prioritized evidence-backed findings without implementing an architecture rewrite.

# Required input and supported scope

Require review goals, affected products/modules/platforms, known constraints, quality attributes, and desired decision horizon. Support every configured mobile technology and explicitly map hybrid boundaries.

# Preconditions and inspection

Read all instructions; inspect status, repository/module structure, build and dependency configuration, source sets/targets, entry points, state and navigation flows, data/domain/UI layers, persistence/network boundaries, dependency injection, tests, and existing ADRs. Treat diagrams/docs as claims to verify against code.

# Ownership

`mobile-architect` is the read-only primary owner. Technology engineers clarify platform conventions; `mobile-test-engineer` reviews testability; `mobile-security-reviewer` reviews trust boundaries; `mobile-performance-reviewer` reviews structural performance risks; `mobile-code-reviewer` independently checks precision and evidence. No reviewer implements a redesign.

# Procedure and gates

1. Define in-scope quality attributes and non-goals. Gate: review criteria are explicit.
2. Build a current-state map of modules, dependency direction, state owners, navigation, data flow, platform/shared boundaries, and external interfaces, citing files.
3. Compare actual dependencies and responsibilities with stated architecture; identify cycles, boundary leaks, duplicated ownership, hidden coupling, and change/test seams.
4. Assess testability, security/privacy trust boundaries, failure isolation, scalability, maintainability, and relevant runtime constraints.
5. Rank findings by demonstrated impact, likelihood, and change urgency. Separate confirmed defects from trade-offs and hypotheses.
6. For each finding, offer a minimal option, prerequisites, migration/rollback considerations, owner, and validation—not a silent rewrite.
7. Have relevant specialists challenge findings independently; correct unsupported or overlapping conclusions and produce the final prioritized report.

# Failure and stop handling

Stop or narrow the conclusion when key configuration/code is missing, docs conflict with implementation, requirements are unknown, or a recommendation would alter public contracts/persistence without user direction. State evidence gaps rather than filling them with assumptions.

# Evidence and acceptance

Return the current-state map, responsibility/dependency findings, file citations, priority/rationale, alternatives and trade-offs, migration prerequisites, validation plan, applicability classification, and unresolved questions. `not-applicable` criteria require concrete reasons.

Report every considered universal and technology-specific completion criterion as `required`, `conditionally-required`, or `not-applicable`; give a concrete reason for every `not-applicable`, and label unavailable infrastructure `unavailable` rather than passed.

Accept when every conclusion is traceable to inspected evidence, ownership is unambiguous, all five technology areas present in scope are considered, and no rewrite or runtime claim is presented as completed.

# Human review and prohibited actions

Human approval is required before any architecture migration, public API/persistence change, target/module removal, or foundational dependency. Never modify production code, invent constraints, prescribe a fashionable framework without need, conflate preference with defect, or claim scalability/security/performance without evidence.
