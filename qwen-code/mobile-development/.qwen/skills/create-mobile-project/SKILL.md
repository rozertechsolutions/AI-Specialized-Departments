---
name: create-mobile-project
description: Select and create a new Android, iOS, KMP, Flutter, or React Native project using installed native toolchains, minimal dependencies, secure and accessible defaults, and verified build/test evidence. Use only for an explicit new-project request.
user-invocable: true
---

# Create Mobile Project

## Objective

Create the smallest complete mobile project that satisfies explicitly agreed targets and technology, follows current installed native tooling, and starts with testable, secure, accessible, maintainable defaults.

## Trigger

Use only when the user explicitly asks to create or scaffold a new mobile project. Do not use to add a module or feature to an existing application.

## Inputs

- Product purpose and first required behavior.
- Required platforms, device classes, minimum supported OS versions, and distribution constraints.
- Technology choice, or permission to evaluate Android, iOS, KMP, Flutter, and React Native.
- Project name, identifiers/namespaces, destination directory, language/UI preferences, and offline/network needs.
- Approved dependency, architecture, and generated-file constraints.

## Preconditions

- Read all applicable instructions and inspect the destination, repository status, nearby conventions, and existing files.
- Confirm the destination is new or that every existing file potentially affected is explicitly in scope. Never overwrite uncertain content.
- Discover installed toolchains and their versions without installing or upgrading anything.
- Resolve the technology, targets, identifiers, and material architecture choices with the user before generation.

## Ownership

- Primary implementation owner: exactly one of `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer`, selected from the approved technology.
- Architecture analysis owner: `mobile-architect`.
- Supporting reviewers: `mobile-test-engineer`, `mobile-security-reviewer`, `mobile-ui-accessibility-reviewer`, `mobile-performance-reviewer`, then `mobile-code-reviewer`.
- Native host work for KMP, Flutter, or React Native is separately assigned according to the `QWEN.md` responsibility matrix.

## Tool and permission boundary

Use read/list/search tools for discovery. Use only the already installed official generator and project-defined build tools after normal approval. Limit writes to the approved destination. Do not use MCP, authenticated services, package installation, publishing, signing, deployment, or external writes.

## Sequence and gates

1. **Requirements gate:** Record functional scope, platforms, OS baselines, identifiers, UI/accessibility/localization needs, security/privacy classification, offline/network behavior, tests, and explicit exclusions. Stop on unresolved material requirements.
2. **Toolchain gate:** Inventory installed SDKs, generators, package managers, and versions. Verify the intended generator command from the installed tool or current official documentation. Stop if required tooling is unavailable; do not install it.
3. **Technology gate:** Compare only viable technologies against requirements, native integration, team/project conventions, sharing needs, testability, performance, maintenance, and dependency cost. Obtain human approval for the choice.
4. **Architecture gate:** Have `mobile-architect` define modules/targets, dependency direction, state and navigation ownership, data boundaries, shared/platform split, error/offline model, and test seams. Assign one primary owner per area.
5. **Generation gate:** Preview or document the exact generator command and affected directory. Run it only after approval. Inspect every generated file before changing it; retain only files required by the native generator and project.
6. **Baseline implementation:** Apply identifiers, supported targets, minimal architecture, first runnable state, complete initial UI states, localization structure, accessibility semantics, secure transport/storage defaults, and least permissions. Add no dependency without explicit approval.
7. **Test gate:** Add deterministic baseline unit and UI/widget/component tests at levels supported by the chosen project. Include startup and initial-state behavior; do not fabricate fixtures as production data.
8. **Validation gate:** Discover and run formatting, lint/static analysis/type checking, compilation or non-publishing build, and relevant tests. Review manifests, permissions, entitlements, privacy declarations, warnings, dependency locks, and secret scan results.
9. **Independent review gate:** Obtain test, security, accessibility, and performance review, then final code review. The implementation owner corrects accepted findings; rerun validation and all required reviews after any correction.
10. **Handoff gate:** Classify every `QWEN.md` completion criterion and provide exact setup/build/test commands, limitations, and human-owned signing/distribution steps without executing them.

## Errors and stop conditions

Stop on a non-empty or ambiguous destination, missing toolchain, generator/schema mismatch, conflicting identifiers, unapproved dependency or architecture change, required external authentication, signing request, validation failure, unresolved high-risk finding, or uncertain data/security impact. Preserve generator output for diagnosis unless deleting it is separately approved.

## Outputs and evidence

- Approved requirements and technology decision with alternatives and trade-offs.
- Area-to-owner map and architecture summary.
- Exact generated/changed paths and generator command/version.
- Dependency list with justification and approval, or `none`.
- Exact validation commands, exit codes, targets, and observed results.
- Completion ledger, reviewer results, warnings, unavailable checks, limitations, and human actions.

## Acceptance criteria

- The requested project starts or builds for every locally available required target without publishing or real signing.
- Required baseline tests and configured analysis pass with no unexplained new warning.
- Identifiers, target versions, manifests/entitlements/permissions, dependencies, complete UI states, accessibility, localization, security, and documentation match the approved requirements.
- No existing user file was overwritten, no unsupported template directory was added, and no result is claimed without evidence.

## Human review requirements

Humans approve technology, identifiers, OS baselines, architecture/public contracts, dependencies, destination overwrite risk, credentials, signing, and all distribution actions. Creation does not authorize any external project/service creation.

## Prohibited actions

Do not install/update tools or dependencies, create cloud/store projects, use credentials, generate real signing assets, sign, archive for distribution, publish, upload, submit, deploy, delete uncertain files, weaken security, or bypass failed validation.
