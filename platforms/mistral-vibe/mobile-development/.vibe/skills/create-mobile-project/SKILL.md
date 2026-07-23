---
name: create-mobile-project
description: Use when the user explicitly asks to create a new Android, iOS, Kotlin Multiplatform, Flutter, or React Native project from an approved local toolchain and defined identifiers.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - todo
  - ask_user_question
  - task
  - write_file
  - edit
  - bash
---

# Create Mobile Project

## Objective and trigger

Create a minimal, buildable mobile project with explicit technology/targets, architecture, security/accessibility defaults, tests, and documentation. Use only for a user-requested new project; do not treat an ordinary feature request as authorization to scaffold or replace a project.

## Inputs

- Technology, target platforms, product name, package/bundle identifiers, destination, supported OS/SDK versions, and required form factors.
- Approved local toolchain/template versions and any approved baseline dependencies.
- Functional seed scope, architecture constraints, state/navigation expectations, and acceptance criteria.
- Required build, lint, test, security, accessibility, and documentation gates.

Never invent an identifier, signing team, deployment target, dependency, service, API contract, or credential.

## Preconditions and ownership

Inspect instructions, status/diff, destination contents, installed toolchains, and generator help/version without installing or updating anything. Stop if the destination has conflicting content, a required toolchain is absent, generation would install software, or identifiers/targets are unresolved.

`mobile-architect` owns the read-only boundary proposal. Partition a mixed scaffold into non-overlapping shared/framework/native-host units; exactly one of `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer` owns each unit, its production files, and its platform-specific baseline tests. `mobile-test-engineer` owns test strategy/reusable fixtures and only an explicitly separated test-only unit; security and UI/accessibility review are required; `mobile-code-reviewer` is final and independent.

## Sequence and gates

1. Record requirements, traceability, destination, targets, tool versions, and prohibited actions.
2. Architecture gate: define modules/source sets, dependency direction, state/navigation ownership, platform/shared boundaries, data/security boundaries, and test seams. Obtain user approval for material trade-offs or dependencies.
3. Generation gate: preview the exact native generator command and its effects. Run only an existing official/local tool with explicit approval; never fetch a template or install a runtime/package.
4. Inspect every generated file. Remove only unnecessary generated content whose purpose is understood; do not edit unsupported generated files manually.
5. Implement the smallest approved seed behavior and complete loading/empty/error/recovery states where applicable.
6. Apply secure defaults: no secrets, production endpoints, broad permissions, unsafe transport, sensitive logging, or external integrations.
7. Apply UI/accessibility defaults: adaptive layout, semantics, scalable text, localization-ready strings, focus/order, and platform conventions.
8. The assigned test owner adds deterministic baseline tests using existing frameworks; `mobile-test-engineer` validates level selection, fixtures, determinism, and coverage.
9. Run discovered formatting/static/lint, compilation, and tests through unsigned/non-publishing paths. Any required failure blocks progress.
10. Obtain security, UI/accessibility, and independent code review; correct scoped findings and rerun all affected gates.
11. Document prerequisites, structure, safe commands, supported targets, and known limitations according to project convention.

## Errors and stop conditions

Stop on ambiguous product behavior, identifiers, targets, architecture, or ownership; unapproved dependencies/plugins; missing toolchains; generator side effects outside scope; signing/provisioning; credentials; production access; destructive commands; external services; or unrelated validation failures. Return the exact decision or environment requirement.

## Outputs and evidence

Provide the technology/architecture decision, complete file list, generator/tool versions and exact command, dependency justification, commands/results, test coverage, review findings, criterion classifications, limitations, and safe local run instructions.

## Acceptance and human review

The project is accepted only when the requested targets compile through safe paths, required static/test gates pass, identifiers/versions match approved inputs, security/accessibility reviews have no unresolved required finding, documentation is accurate, and no unrelated file changed. Human approval is mandatory for identifiers, dependencies, platform permissions/entitlements, persistent/public contracts, and any sensitive configuration.

## Prohibited actions

Do not install/update tools or packages, fetch unapproved templates, enable MCP/connectors, add credentials, sign/archive/export, publish/submit/deploy, initialize or mutate Git, overwrite existing work, use production data, or claim unavailable targets passed.
