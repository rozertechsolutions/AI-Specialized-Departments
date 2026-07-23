---
name: review-mobile-architecture
description: Reviews mobile architecture and dependency boundaries without editing production code. Use for Android, iOS, KMP, Flutter, or React Native assessments.
---

# Review Mobile Architecture

## Objective

Provide an evidence-based, read-only assessment of module boundaries, dependency direction, state, navigation, shared versus platform responsibilities, interoperability, maintainability, and migration risk.

## Trigger

Use for an architecture review, boundary decision, migration assessment, technical-debt analysis, or cross-platform design comparison. Do not use to implement the recommendation.

## Inputs

- review question and decision horizon;
- repository snapshot, diagrams, configuration, modules, packages, and representative call paths;
- target platforms, supported versions, product constraints, team constraints, and known pain points;
- performance, security, testability, and release constraints;
- proposed architecture or migration when one exists.

## Supported technologies

Android, iOS, KMP, Flutter, and React Native, including hybrid repositories and native host boundaries.

## Preconditions

- Review scope, affected systems, and desired decision are explicit.
- Relevant source and build configuration are available and current.
- The review is read-only.
- Unknown runtime behavior is labeled and not inferred from diagrams alone.

## Primary owner and reviewers

mobile-architect is primary. Consult the relevant technology owners for feasibility without transferring architecture authority. mobile-security-reviewer reviews trust boundaries, mobile-performance-reviewer reviews measurable resource implications, mobile-test-engineer reviews testability, and mobile-code-reviewer reviews the final analysis for evidence and contradictions. Human maintainers own the decision.

## Ordered workflow

1. Define the architecture question, quality attributes, constraints, non-goals, and decision authority.
2. Inspect repository instructions, status, modules, source sets, dependency declarations, navigation, state, data, networking, storage, concurrency, tests, and build boundaries.
3. Reconstruct the current architecture from source evidence, distinguishing intended design from observed implementation.
4. Map dependencies and ownership; identify cycles, layering violations, duplicated authority, unstable boundaries, platform leakage, and generated-code constraints.
5. Trace representative user and data flows across UI, state, domain, data, storage, network, shared code, bridges, and native hosts.
6. Evaluate security, privacy, testability, accessibility, performance, release, and migration implications.
7. Compare viable options against explicit quality attributes. Include retain-current-state when it is viable.
8. Recommend one option only when evidence supports it; state trade-offs, prerequisites, migration stages, rollback, and validation.
9. Consult relevant technology owners and reviewers; record disagreements and evidence rather than averaging opinions.
10. Perform mobile-code-reviewer assessment of the report, then triple validation and final verification.

## Conditional steps

- KMP: inspect target and source-set topology, expect and actual boundaries, dependency placement, and shared UI only if present.
- Flutter or React Native: inspect package boundaries, state and navigation ownership, platform-channel or bridge contracts, and native host responsibilities.
- Migration: define compatibility, incremental stages, observability, data migration, rollback, and criteria for stopping.
- Proposed dependency: assess necessity, maintenance, compatibility, licensing, supply-chain risk, and migration cost; do not install it.

## Validation gates

- Gate 1: current architecture is derived from actual source and configuration.
- Gate 2: every finding has a path, dependency, or flow as evidence.
- Gate 3: ownership is unique and no recommendation creates a cycle or common universal runtime.
- Gate 4: alternatives and migration risks are explicit.
- Gate 5: specialist and final report review identify no unresolved contradiction.
- Gate 6: report makes no implementation, measurement, or compatibility claim without evidence.

## Failures

If relevant modules or runtime evidence are missing, narrow the review and mark coverage unavailable. Do not fill gaps with framework stereotypes. If architecture documentation conflicts with source, report both and treat source behavior as observed evidence, not necessarily intended policy.

## Stop conditions

Stop for incomplete critical source, unknown product requirements, inaccessible build configuration, sensitive data exposure, user request to change production during the read-only review, or a decision that requires unapproved business or security authority.

## Evidence

Record inspected paths, dependency and flow traces, configuration, observed cycles or boundaries, alternatives, reviewer consultations, unknown areas, and source freshness.

## Outputs

- current-state architecture description;
- responsibility and dependency matrix;
- evidence-backed findings by severity;
- alternatives, recommendation, trade-offs, and migration plan when requested;
- validation plan, residual risks, and human decisions.

## Acceptance criteria

The report is read-only, scoped, traceable to source, technology-correct, explicit about uncertainty, free of ownership conflicts and cycles, and reviewed independently for evidence quality.

## Human approvals

Humans decide architecture, migrations, dependencies, public contracts, persistence, security boundaries, staffing implications, and implementation sequencing.

## Prohibited actions

Do not edit production code, install dependencies, perform migration, present a diagram as runtime proof, approve release, self-review, use credentials, sign, publish, upload, deploy, destroy data, or run Git write commands.
