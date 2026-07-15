---
name: review-mobile-architecture
description: Map and review an existing mobile architecture, dependencies, state, navigation, shared/platform boundaries, testability, security boundaries, and maintainability without rewriting it.
user-invocable: true
---

# Review Mobile Architecture

## Objective

Produce an evidence-based, prioritized architecture assessment of the current project without editing or automatically rewriting it.

## Trigger

Use when the user requests architecture review, dependency/boundary analysis, migration assessment, or maintainability analysis. Do not use as implicit authorization to implement recommendations.

## Inputs

- Review question, platforms/targets, scope, constraints, and known pain points.
- Desired quality attributes and acceptable migration horizon when provided.
- Relevant diagrams or decisions, treated as claims to verify against code.

## Preconditions

- Read all instructions and documentation.
- Inspect the relevant tree, build/dependency configuration, entry points, modules/targets, state/navigation/data flow, native/shared boundaries, tests, and current changes.
- Establish the review boundary and evidence limitations.

## Ownership

- Primary owner: `mobile-architect`.
- Supporting read-only reviewers: security, accessibility, and performance reviewers only when those boundaries are in scope.
- `mobile-code-reviewer` may independently review the report for evidence/precision. No implementation agent edits during this workflow.

## Tool and permission boundary

Use read/list/search and official documentation fetch only. Do not edit, write, execute project commands, invoke MCP, install tools, or perform external/authenticated actions.

## Sequence and gates

1. **Scope gate:** Define systems, platforms, quality attributes, decisions, and exclusions. Stop if the requested boundary is too ambiguous to assess.
2. **Inventory gate:** Map modules/targets/source sets, entry points, dependency/build files, public interfaces, generated boundaries, and tests with exact paths.
3. **Runtime map:** Trace navigation, state ownership, data/domain layers, persistence/networking, concurrency, lifecycle, background work, error/recovery, and offline behavior as applicable.
4. **Dependency gate:** Record actual dependency direction, cycles, boundary leaks, shared/platform splits, native bridges, and external service boundaries. Distinguish intended from observed architecture.
5. **Quality review:** Assess change isolation, testability, compatibility, security/privacy boundaries, accessibility ownership, performance-sensitive paths, observability, and maintainability using concrete evidence.
6. **Ownership comparison:** Compare observed responsibilities with the `QWEN.md` matrix and identify ambiguous or duplicated ownership without reassigning it silently.
7. **Finding gate:** Prioritize findings by impact, likelihood, breadth, and remediation cost. Include positive constraints worth preserving.
8. **Recommendation gate:** Provide incremental options, prerequisites, trade-offs, migration stages, validation/rollback gates, and explicit decisions requiring humans. Do not prescribe a rewrite without proof.
9. **Independent report review:** Verify every path/reference resolves, each finding has evidence, responsibilities do not conflict, and recommendations stay within the requested scope.
10. **Completion gate:** Classify `QWEN.md` criteria; most execution criteria may be not applicable because this workflow is read-only, with concrete reasons.

## Errors and stop conditions

Stop on inaccessible required code, conflicting instructions, undocumented generated/runtime boundaries that prevent a supported conclusion, need for secrets/production access, or a material product/architecture choice only a human can make.

## Outputs and evidence

- Current architecture map with exact paths and evidence confidence.
- Dependency, state, navigation, data, shared/platform, test, security, and performance maps as applicable.
- Prioritized findings with impact, evidence, and affected contracts.
- Incremental options, trade-offs, stages, validation, rollback, owners, and human decisions.
- Completion ledger and explicit limitations; no implementation claim.

## Acceptance criteria

- Every conclusion is traceable to inspected code/documentation or labeled inference.
- The report covers the requested quality attributes and all relevant technology boundaries.
- Findings are prioritized, ownership is unique, references resolve, and recommendations are actionable without hidden scope expansion.
- No file is modified and no rewrite is initiated.

## Human review requirements

Humans select architecture options, approve public/persistent contract changes, dependencies, migrations, rollout, and any later implementation scope.

## Prohibited actions

Do not edit, generate diagrams/files, run builds, invent architecture, mandate fashionable patterns, recommend unrelated refactors, expose project data externally, or treat the assessment as implementation/release approval.
