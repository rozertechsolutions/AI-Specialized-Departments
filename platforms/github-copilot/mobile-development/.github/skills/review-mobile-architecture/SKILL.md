---
name: review-mobile-architecture
description: Performs a read-only mobile architecture review covering modules, dependencies, state, navigation, shared/platform boundaries, testability, security boundaries, maintainability, and prioritized findings. Use for explicit architecture assessment, not automatic rewriting.
---

# Review mobile architecture

## Objective

Produce an evidence-based, read-only map and prioritized assessment of the current architecture without automatically rewriting it or treating preferences as defects.

## Trigger

Use for explicit architecture review, dependency/module assessment, shared-versus-platform evaluation, migration planning, or maintainability analysis.

## Inputs

- review question and business/technical constraints;
- technologies, platforms, supported versions, and relevant modules;
- known pain points, quality attributes, change horizon, and excluded scope;
- available diagrams, decision records, tests, metrics, and ownership information.

## Preconditions

- Read applicable instructions, architecture and build documentation, manifests, dependency definitions, entry points, representative vertical slices, navigation/state code, persistence/network boundaries, tests, and current changes.
- Confirm review scope and distinguish current-state assessment from a requested future design.
- Do not edit source or configuration during this workflow.

## Ownership

Primary owner: `mobile-architect`. Technology specialists clarify platform details. `mobile-test-engineer` and read-only security/performance reviewers support applicable findings. `mobile-code-reviewer` reviews only any separately approved documentation change.

## Sequence and intermediate gates

1. **Scope gate:** define systems, modules, platforms, quality attributes, constraints, and evidence sources. Stop if the requested boundary is not identifiable.
2. Inventory modules/targets, build-time and runtime dependencies, entry points, public contracts, persistence/network layers, navigation, state owners, concurrency boundaries, and tests.
3. Trace representative user/data flows across layers and platforms. Mark every inferred edge that is not directly verified.
4. Map shared versus platform-specific ownership, including KMP `expect`/`actual` and Flutter/React Native bridge boundaries where present.
5. Evaluate dependency direction, coupling/cohesion, lifecycle, state consistency, error/offline handling, testability, security/privacy boundaries, observability, and change isolation.
6. **Finding gate:** for each concern, record evidence, failure or cost scenario, affected quality attribute, severity, confidence, and primary remediation owner. Exclude purely stylistic preferences.
7. Prioritize findings by impact, likelihood, effort, sequencing, and reversibility. Identify quick containment separately from structural migration.
8. Draft incremental recommendations with prerequisites, compatibility, tests, metrics, stop conditions, and rollback considerations. Do not implement them.
9. Ask relevant specialists to validate platform-specific findings when subagents exist; otherwise list required explicit reviews and mark them not performed.

## Errors and stop conditions

- If generated files, external services, or unavailable modules hide a boundary, report the evidence gap rather than guessing.
- Stop before source edits, dependency changes, migrations, or architecture replacement; those require a separately approved implementation workflow.
- Do not rank a finding as proven when it depends on missing runtime evidence.

## Completion classification

Classify every coordinator criterion for this read-only review. Requirements/scope, architecture/configuration inspection, security boundaries, testability, documentation output, and independent validation of material findings are normally required. Compilation, tests, lint, dependency resolution, UI, runtime performance, recovery states, warnings, and regression checks are conditionally required only when needed to verify a claim; explain why each was or was not run.

## Outputs and evidence

Return scope, architecture and responsibility maps, representative flows, observed facts versus inferences, prioritized findings, incremental recommendations, validation/rollback plans, evidence gaps, specialist review status, and completion-classification table.

## Acceptance criteria

- Every architecture edge and finding is traceable to inspected evidence or clearly labeled inference.
- Ownership is unique across shared and platform boundaries.
- Findings include impact, confidence, priority, and verification, not just preferred patterns.
- No source/configuration change or unsupported runtime claim occurs.

## Human review requirements

Humans confirm business constraints, target architecture decisions, migration priority, accepted risks, and authorization for any later implementation.

## Prohibited actions

Do not edit architecture automatically, add dependencies, rewrite modules, invent metrics, claim unavailable specialist review, expose sensitive data, or perform release/deployment operations.
