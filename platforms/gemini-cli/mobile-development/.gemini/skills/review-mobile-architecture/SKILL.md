---
name: review-mobile-architecture
description: Performs a read-only evidence-based review of mobile modules, dependencies, state, navigation, shared/platform boundaries, testability, security boundaries, maintainability, and migration risks. Use when the user asks for architecture assessment or planning.
---

# Review Mobile Architecture

## Objective and trigger

Map and assess the current mobile architecture without rewriting it. Activate for
architecture review, boundary analysis, migration planning, or maintainability
assessment. The workflow is read-only unless the user later requests a separate
implementation workflow.

Activation is read-only and grants no tools. Use only project-allowed read tools;
do not use shell, write, replace, MCP, or external services.

## Inputs

- Review question, business/technical constraints, target platforms, and scope.
- Known pain points, compatibility promises, proposed direction, and time horizon.
- Repository root, relevant modules/targets, documentation, and test evidence.

## Preconditions and ownership

Inspect applicable instructions and current repository state. Confirm exact
review boundaries; do not scan unrelated platforms or specializations.

`mobile-architect` is primary owner. Platform engineers may supply feasibility
evidence for their own platforms. `mobile-security-reviewer`,
`mobile-ui-accessibility-reviewer`, `mobile-performance-reviewer`, and
`mobile-test-engineer` support only when their boundaries are materially involved.
Because no code is changed, `mobile-code-reviewer` is not required unless the
review evaluates an existing proposed diff.

## Workflow and gates

1. **Scope gate:** define questions, modules, targets, constraints, exclusions,
   decision authority, and required level of detail.
2. **Evidence gate:** read architecture docs and actual build/module config,
   entry points, dependency injection, navigation, state/data flows, persistence,
   networking, shared/platform sources, public APIs, and tests. Cite paths/lines.
3. **Map gate:** produce current module graph, dependency direction, state and
   navigation ownership, lifecycle/concurrency boundaries, shared/platform
   contracts, data/security boundaries, and test seams.
4. **Assessment gate:** evaluate cohesion, coupling, cycles, layering, platform
   leakage, testability, error propagation, compatibility, maintainability, and
   migration constraints. Separate observation, inference, and unknown.
5. **Specialist gate:** obtain targeted read-only review for security boundaries,
   UI architecture, performance-critical paths, or testability when applicable.
6. **Recommendation gate:** prioritize findings by impact/effort/risk. Offer the
   smallest viable decision, alternatives/trade-offs, staged migration, gates,
   rollback points, and one owner per responsibility. Do not automatically edit.

## Completion classification

Classify requirements/scope, configuration mapping, build/test evidence,
dependencies, security boundaries, accessibility/localization architecture,
performance/resources/offline/recovery, documentation accuracy, warnings,
regression/migration risk, specialist review, proposed validation, and each
platform's native constraints as `required`, `conditionally-required`, or
`not-applicable` with reasons. Compilation/tests are evidence inputs, not assumed
requirements for a purely read-only review; unavailable evidence is explicit.

## Errors and stop conditions

Stop for undefined scope, inaccessible material files, contradictory constraints,
missing platform/compatibility facts, uncertain persistent/public contract
impact, or any request to edit under this Skill. Never infer runtime architecture
solely from folder names or generic best practices.

## Outputs, evidence, and acceptance

Return scope/exclusions, architecture and responsibility maps, evidence index,
findings with severity/confidence, alternatives/trade-offs, prioritized staged
migration, risks/rollback/gates, specialist findings, completion ledger,
unknowns, and questions requiring human decisions.

Acceptance requires traceable current-state mapping, unique ownership, complete
technology coverage within scope, prioritized actionable findings, explicit
unknowns, no edits, and no unsupported claims.

## Human review and prohibited actions

Humans choose architecture and migration trade-offs. Never edit files, introduce
dependencies/frameworks, access secrets/external systems, enable MCP, sign,
publish, deploy, upload, perform destructive operations, or present a proposal
as an approved decision.
