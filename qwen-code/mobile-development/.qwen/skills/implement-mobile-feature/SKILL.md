---
name: implement-mobile-feature
description: Implement a bounded mobile feature across data, domain, UI, navigation, errors, offline behavior, tests, and independent reviews while preserving the existing architecture. Use for explicit feature work in an existing project.
user-invocable: true
---

# Implement Mobile Feature

## Objective

Deliver the smallest complete feature that meets traceable requirements, preserves established contracts and architecture, handles relevant states and failures, and has proportionate validation and independent review.

## Trigger

Use when the user asks to add or change functional mobile behavior in an existing project. Use `add-mobile-screen` when the work is solely a new screen and `integrate-mobile-api` when the primary request is an API integration.

## Inputs

- User-visible behavior and acceptance criteria.
- Platforms/targets and explicitly excluded behavior.
- Data, domain, UI, navigation, persistence, networking, offline, analytics, security, accessibility, and performance expectations as applicable.
- Compatibility, rollout, migration, and testing constraints.

## Preconditions

- Inspect instructions, status/diff, architecture, affected flows, contracts, data models, tests, commands, and user changes.
- Reproduce or observe current behavior where possible.
- Resolve material ambiguity and approve any public API, persistent format, dependency, permission, or architecture change before editing.

## Ownership

- Primary owner: exactly one specialist per implementation area from the `QWEN.md` matrix; select from observed code ownership, not the requested platform name alone.
- `mobile-architect` supports cross-boundary design only.
- `mobile-test-engineer` owns test strategy; security, accessibility, and performance reviewers participate when their criteria are applicable; `mobile-code-reviewer` reviews last.

## Tool and permission boundary

Begin read-only. Use edit/write and only discovered project commands through the assigned primary specialist under normal approval. No MCP, package installation, authenticated external action, signing, publishing, deployment, or unrelated refactoring.

## Sequence and gates

1. **Requirement gate:** Convert each requirement into observable acceptance criteria and list non-goals. Identify loading, empty, content, error, retry, cancellation, recovery, permission-denied, offline, and stale-data behavior as applicable.
2. **Discovery gate:** Trace the existing flow across entry point, navigation, state, domain/data, persistence/network, native boundaries, resources/localization, and tests. Record exact paths and conventions.
3. **Ownership gate:** Partition non-overlapping implementation areas and assign one primary owner to each. Stop on ambiguous or unowned boundaries.
4. **Design gate:** Specify state ownership, data contracts, dependency direction, navigation, concurrency/cancellation, error mapping, offline/cache behavior, telemetry/privacy, accessibility, and test seams. Obtain approval for material contract/architecture changes.
5. **Implementation gate:** Implement in dependency order—contracts/data, domain/state, UI/navigation, native boundary—only where applicable. Preserve compatibility and provide complete state transitions.
6. **Test gate:** Add deterministic regression and feature coverage at the lowest effective levels, including relevant failures, boundaries, lifecycle, concurrency, and recovery. Do not weaken behavior to pass tests.
7. **Validation gate:** Run targeted format/lint/type/static checks, compilation/non-publishing builds, and affected tests using discovered targets/configurations. Review dependency/lock changes, warnings, manifests/entitlements/permissions, and secret scan.
8. **Specialist review gate:** Obtain test strategy review plus security, accessibility, and performance review when applicable. Primary owners correct accepted findings and rerun the full validation relevant to the correction.
9. **Independent code-review gate:** `mobile-code-reviewer` verifies requirement traceability, scope, correctness, regression risk, error handling, tests, and evidence. Any correction invalidates the prior pass and requires a full repeat.
10. **Completion gate:** Classify all `QWEN.md` criteria with reasons and evidence; report unavailable infrastructure honestly.

## Errors and stop conditions

Stop on unrecoverable ambiguity, inability to preserve a contract, unapproved dependency/permission/schema/architecture change, required credential or external write, missing owner, unexpected unrelated diff, failing required check, unexplained warning, or unresolved high/critical review finding.

## Outputs and evidence

- Requirement-to-code-to-test traceability.
- Area-to-owner map and Skill boundaries.
- Exact changed paths and behavior by state.
- Exact commands, exit codes, targets, and observed results.
- Completion ledger, independent findings/corrections, limitations, and human actions.

## Acceptance criteria

- Every approved requirement and applicable state is implemented and tested at a justified level.
- Existing contracts and validated behavior remain compatible unless an approved change says otherwise.
- Required builds, analysis, and tests pass with no unexplained warning.
- Required security, accessibility, performance, test, and code reviews have no unresolved blocker.

## Human review requirements

Humans decide ambiguous product behavior and approve dependencies, permissions, public/persistent contracts, migrations, credentials, external services, signing, and release actions.

## Prohibited actions

Do not broaden scope, refactor unrelated code, add frameworks/dependencies without approval, hide errors, fabricate states/results, weaken tests/security, use production data or credentials, sign, publish, upload, deploy, or self-approve.
