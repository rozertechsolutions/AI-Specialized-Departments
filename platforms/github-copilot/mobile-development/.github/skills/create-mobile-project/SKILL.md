---
name: create-mobile-project
description: Creates a new Android, iOS, Kotlin Multiplatform, Flutter, or React Native project from explicit requirements using installed toolchains, minimal dependencies, secure and accessible defaults, and verified local checks. Use only when the user asks to create a mobile project.
---

# Create a mobile project

## Objective

Create the smallest complete project that satisfies confirmed technology, target, architecture, security, accessibility, test, and validation requirements without installing tools, inventing identifiers, enabling external services, or preparing a signed/published release.

## Trigger

Use only for an explicit request to create or scaffold a mobile project. Do not use for adding a module or feature to an existing project.

## Inputs

Require or discover safely:

- product scope and first runnable behavior;
- technology and target platforms;
- supported OS/runtime versions and form factors;
- destination path and whether it must be empty;
- application/library name and required package or bundle identifiers;
- UI, navigation, persistence, networking, offline, localization, and accessibility requirements;
- dependency constraints and approved licenses;
- available toolchains and required validation environments.

Do not fabricate missing identifiers, signing teams, endpoints, credentials, or business rules. Ask when a missing value changes generated structure or public identity.

## Preconditions

- Read all applicable instructions and confirm the destination will not overwrite unrelated content.
- Confirm the selected technology from the user's requirement, not from preference.
- Inspect installed toolchain versions and existing repository conventions. Do not install or update anything.
- Confirm every proposed dependency is necessary, compatible, maintained, license-acceptable, and explicitly approved.
- Define acceptance criteria and the completion-classification table from the coordinator instructions.

## Ownership

Primary owner: the selected technology engineer. For a KMP project, `kmp-engineer` is primary and Android/iOS owners handle only their host partitions. `mobile-architect` reviews boundaries; test, security, UI/accessibility, performance, and code reviewers support their domains.

## Sequence and intermediate gates

1. **Scope gate:** record requirements, targets, identifiers, versions, exclusions, first runnable behavior, and acceptance criteria. Stop if technology or destination is ambiguous.
2. **Environment gate:** inspect installed SDKs, generators, package managers, licenses already accepted, and non-publishing validation commands. Report unavailable targets before creating files.
3. **Architecture gate:** define modules, dependency direction, state ownership, navigation, data boundaries, shared/platform ownership, error/offline strategy, and test seams. Prefer platform templates and standard libraries. Obtain approval for every added dependency.
4. Generate into the confirmed destination using the installed official toolchain or create the documented native structure directly. Inspect generated content before modifying it.
5. Remove generated sample behavior only when its replacement is complete and verified. Preserve required toolchain files and generated metadata.
6. Establish secure defaults: no secrets; least permissions; secure transport assumptions; safe storage boundaries; non-sensitive logging; no active analytics, crash, backend, design, or MCP integration.
7. Establish accessibility and localization defaults: externalized strings, semantic labels where needed, dynamic text, focus, contrast-aware theme tokens, adaptive layout, and complete initial loading/empty/error/content states when applicable.
8. Add the minimum deterministic tests and project-consistent lint/static-analysis configuration supplied by the native toolchain. Do not introduce a separate framework without approval.
9. **Build gate:** resolve only approved dependencies, compile applicable targets, run configured static analysis and targeted tests, and capture exact commands and output. Use unsigned/non-publishing modes.
10. **Review gate:** obtain architecture, security, UI/accessibility, and independent code review. Request performance review when startup, rendering, background work, networking, storage, or size is material.
11. Fix accepted findings through the primary owner and repeat affected validation and reviews.

## Errors and stop conditions

- On generator, resolution, build, lint, or test failure, preserve the first useful error, identify whether the cause is code, configuration, toolchain, network, or unavailable infrastructure, and correct only in-scope causes.
- Do not delete and regenerate an uncertain destination. Do not weaken validation or substitute a different technology to obtain a pass.
- Stop before dependency installation, SDK installation, signing setup, credentials, external service activation, publication, or destructive cleanup unless the user separately authorizes the exact operation.
- Stop if the requested project cannot be created completely with the available native capabilities.

## Completion classification

Classify every coordinator criterion. Requirements, configuration, applicable compilation, native static checks, dependency resolution, security, accessibility/localization, documentation, warnings, regression evidence, and independent review are normally required. Each test level, adaptive/offline/recovery state, and performance domain is conditionally required based on product scope and supported infrastructure; record the concrete condition and result.

## Outputs and evidence

Return the created file list, architecture and ownership map, dependency rationale, secure/accessibility defaults, exact commands with results, tests and environments, warnings, unavailable checks, review findings and resolutions, and the completion-classification table.

## Acceptance criteria

- The confirmed first behavior compiles and is covered at the lowest effective test level on every locally available required target.
- Configuration matches requested identifiers and versions without credentials or signing assets.
- No unapproved dependency, integration, permission, generated placeholder behavior, or unexplained warning remains.
- Required reviewers report no unresolved blocking finding.

## Human review requirements

Humans must approve identifiers, dependency additions, permissions/entitlements, security/privacy decisions, external-service setup, and any unavailable required target. Final release and signing decisions are outside this Skill.

## Prohibited actions

Do not install tools or dependencies without approval; enable external integrations; use real secrets or signing materials; publish, upload, submit, distribute, deploy, or sign; perform destructive cleanup; or claim unavailable targets passed.
