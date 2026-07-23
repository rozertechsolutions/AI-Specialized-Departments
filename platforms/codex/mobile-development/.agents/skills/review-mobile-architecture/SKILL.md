---
name: review-mobile-architecture
description: Perform a read-only architecture audit of an Android, iOS, KMP, Flutter, React Native, or mixed mobile codebase and produce evidence-based findings. Do not use to implement a redesign.
---

# Review Mobile Architecture

## Objective

Assess current mobile architecture, dependency direction, module ownership, state/data/navigation boundaries, cross-platform sharing, and changeability without editing the repository.

## Required inputs

- Review goal and scope: whole project, module, feature, migration, or cross-platform boundary.
- Supported platforms/targets and known quality attributes.
- Relevant architecture decisions, diagrams, constraints, and pain points.
- Base revision or diff when reviewing a proposed change.

When quality priorities conflict, ask for ranking rather than inventing it.

## Preconditions

1. Confirm this is a read-only review.
2. Read instructions and architecture/project documentation.
3. Inspect status/diff, module graph, manifests, entry points, dependency injection, navigation, state, networking, storage, build configuration, and representative tests.
4. Identify generated code and external boundaries.
5. Record missing or stale documentation as evidence, not as inferred design.
6. Classify every completion criterion as required, conditionally required, or not applicable with a documented reason.

## Agent ownership

`mobile-architect` is the primary reviewer. The coordinator may ask the relevant platform agents for independent read-only feasibility evidence: `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer`. Invoke `mobile-security-reviewer` only for threat boundaries and `mobile-performance-reviewer` only for architecture-level performance constraints. `mobile-code-reviewer` is not a substitute for the architecture owner.

No agent may edit. Parallelize only independent read-only areas and have the coordinator reconcile results.

## Execution

1. **Define evaluation criteria.** State required qualities such as maintainability, testability, offline behavior, modularity, startup, privacy, and target reuse.
2. **Map the current system.** Identify entry points, modules/source sets, ownership, dependency edges, data sources, state containers, navigation, platform adapters, persistence, and external APIs.
3. **Validate the map.** Cross-check documentation against code and build files. Mark discrepancies.
4. **Evaluate boundaries.** Check dependency direction, cycles, domain/platform leakage, shared-code suitability, lifecycle ownership, concurrency, error propagation, test seams, and public/persistent contracts.
5. **Platform feasibility.** Obtain targeted platform evidence for material recommendations; do not assume an API or toolchain supports them.
6. **Risk reviews.** Add security/privacy and performance findings only through the corresponding specialist when material.
7. **Compare options.** For each major issue, provide the minimal correction and at least one alternative when trade-offs are consequential. Include migration and compatibility cost.
8. **Independent consistency gate.** Verify that recommendations do not conflict, duplicate ownership, require unapproved dependencies, or silently change behavior/contracts.
9. **Final read-only gate.** Confirm repository status is unchanged by the review.

## Error handling and stop conditions

Stop or narrow conclusions when key modules/docs are unavailable, supported targets are unknown, generated/external code cannot be inspected, requirements conflict, or a recommendation depends on unverified current platform behavior. State uncertainty and required evidence. Do not turn the audit into implementation.

## Outputs

- Scope, criteria, evidence sources, and current-state architecture map.
- Findings ordered by impact, each with evidence and affected quality attribute.
- Recommended target state and ownership boundaries.
- Incremental migration sequence, compatibility/test plan, risks, and rollback points.
- Completion matrix with required/conditional/not-applicable status, reasons, and exact results.
- Explicit limitations and no-finding areas.

## Acceptance criteria

- Every finding is tied to repository evidence and a concrete impact.
- Recommendations preserve stated behavior/contracts or identify approval required to change them.
- Platform feasibility, testing, security, performance, and migration implications are addressed where relevant.
- No files or external systems were modified.

## Prohibited actions

Do not edit code/docs/config, add dependencies, generate diagrams into the repo, run mutating tools, invent requirements, access production/private services, sign, publish, deploy, or present style preferences as architectural defects.
