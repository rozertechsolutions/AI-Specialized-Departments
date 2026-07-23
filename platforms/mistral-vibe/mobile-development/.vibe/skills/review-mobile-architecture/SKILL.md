---
name: review-mobile-architecture
description: Use for a read-only evidence-based architecture review of an Android, iOS, Kotlin Multiplatform, Flutter, React Native, or mixed mobile codebase; never for automatic redesign.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - todo
  - ask_user_question
  - task
---

# Review Mobile Architecture

## Objective and trigger

Map and evaluate current module/dependency, state, navigation, data, shared/platform, security, performance, and testability boundaries without modifying the repository.

## Inputs

- Review scope and goal, supported platforms, relevant quality attributes and their priority, known constraints/pain points, architecture records, and base revision/diff when applicable.

## Preconditions and ownership

Confirm read-only execution. Inspect instructions, status/diff, documentation, manifests/build graph, entry points, state/navigation/data/storage/networking, generated boundaries, and representative tests. `mobile-architect` is primary; platform specialists may provide bounded read-only feasibility evidence. Use security/performance reviewers only for their domains. No participant edits.

## Sequence and gates

1. Criteria gate: state scope, required qualities, evidence sources, exclusions, and unresolved priorities.
2. Map modules/source sets, entry points, dependency edges, ownership, state containers, navigation, data sources, persistence, external APIs, platform adapters, and test seams.
3. Validate the map against build files and code; mark documentation drift.
4. Evaluate direction/cycles, leakage, lifecycle/concurrency, error propagation, coupling, public/persistent contracts, testability, security boundaries, and performance constraints.
5. Ask platform specialists for independent feasibility evidence on material recommendations; verify current API/toolchain facts before relying on them.
6. For each major finding, provide evidence, impact, smallest correction, alternatives when consequential, compatibility/migration cost, validation, and rollback point.
7. Consistency gate: ensure recommendations do not conflict, duplicate ownership, require unapproved dependencies, or silently change behavior.
8. Confirm final repository status is unchanged.

## Errors and stop conditions

Stop or narrow conclusions when critical modules/docs are unavailable, targets/requirements conflict, generated/external code cannot be inspected, evidence is insufficient, or feasibility depends on unverified behavior. Return the missing evidence instead of inventing it.

## Outputs and evidence

Provide current-state map, findings ordered by impact with file/build evidence, target boundaries, responsibility assignments, incremental migration sequence, compatibility/test/security/performance implications, alternatives, rollback points, no-finding areas, and limitations.

## Acceptance and human review

Every finding is evidence-backed and linked to a concrete quality impact; recommendations preserve stated behavior/contracts or identify required approval; ownership is unique; migration/validation is actionable; and status proves no modification. Humans decide whether to adopt consequential trade-offs.

## Prohibited actions

Do not edit, generate repo artifacts, run mutating commands, add dependencies, rewrite architecture automatically, invent requirements, access private/production services, sign/publish/deploy, or present style preference as a defect.
