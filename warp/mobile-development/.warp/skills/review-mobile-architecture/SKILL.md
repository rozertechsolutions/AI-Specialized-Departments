---
name: review-mobile-architecture
description: Review mobile architecture, module boundaries, dependency direction, navigation, state, and shared/platform separation.
---

# Review Mobile Architecture

## Objective

Provide a read-only architecture assessment with actionable findings grounded in repository evidence.

## Trigger

Use when the user asks for architecture review or when a change affects modules, dependency direction, navigation, state, persistence, migrations, or cross-platform boundaries.

## Inputs

Architecture question, affected files, project layout, manifests, dependency graph, navigation/state patterns, and current conventions.

## Supported Technologies

Android, iOS, KMP, Flutter, and React Native.

## Preconditions

Inspect relevant source, manifests, docs, dependency declarations, build configuration, and existing tests. Do not edit production code in this workflow.

## Primary Owner

`mobile-architect`.

## Reviewers

`mobile-code-reviewer`; add platform engineers for factual platform constraints and `mobile-security-reviewer` for trust boundaries.

## Steps

1. Identify current architecture and module boundaries from files, not assumptions.
2. Map dependency direction and ownership.
3. Check state, navigation, persistence, shared/platform separation, and migration risks.
4. Classify findings by severity and evidence.
5. Recommend the smallest changes that resolve each issue.
6. Define validation needed if changes are later approved.

## Conditional Steps

- If a finding depends on platform behavior, verify it against official platform documentation.
- If dependency direction is unclear, inspect build files and imports before assigning severity.
- If remediation would alter public APIs, persistent formats, or migrations, mark it as approval-required.
- If evidence is insufficient, record an open question instead of asserting a finding.

## Validation Gates

Required: read-only inspection, traceable file references, no self-review, no fabricated metrics, and explicit not-applicable criteria.

## Failures and Stop Conditions

Stop when required files are unavailable, the requested architecture change would alter public contracts without approval, or evidence is insufficient.

## Evidence

Record inspected files, diagrams or dependency observations when useful, risks, and official docs consulted for platform constraints.

## Outputs

Findings ordered by severity, open questions, recommended implementation owners, and validation plan.

## Acceptance Criteria

Findings are evidence-based, ownership is unambiguous, and no edits or unsupported constructs are introduced.

## Human Approvals

Required before implementing architecture changes, dependency changes, persistent format changes, migrations, or public API changes.

## Prohibited Actions

Do not implement features, approve releases, create agent files, invent modules, or claim performance/security improvements without evidence.
