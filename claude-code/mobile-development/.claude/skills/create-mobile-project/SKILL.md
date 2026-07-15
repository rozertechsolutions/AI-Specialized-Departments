---
name: create-mobile-project
description: Create a secure, minimal mobile project baseline after selecting Android, iOS, Kotlin Multiplatform, Flutter, or React Native targets and verifying the installed toolchain.
when_to_use: Use for a new mobile application, library, shared KMP module, or multi-platform repository baseline; do not use to add a feature to an existing initialized project.
argument-hint: "[technology] [platform-targets] [constraints]"
model: inherit
---

# Objective

Create the smallest production-quality baseline requested in `$ARGUMENTS` without publishing, signing, deploying, or assuming a toolchain.

# Required input and supported scope

Require technology (Android, iOS, KMP, Flutter, React Native, or an explicit combination), target platforms/OS support, application or package identity, product constraints, required architecture, and acceptance criteria. Ask before proceeding if a choice materially changes generated structure, dependencies, persistence, or public APIs.

# Preconditions and inspection

1. Read all project instructions and inspect status, existing/hidden files, parent build configuration, licenses, and reserved identifiers.
2. Confirm the destination is safe and that no user content would be overwritten.
3. Discover installed toolchain and official project generators without installing or upgrading anything.
4. Identify offline/network requirements and request approval before dependency downloads or other external access.

# Ownership

The coordinator selects one implementation owner: `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer`. `mobile-architect` owns the initial boundaries; `mobile-test-engineer`, `mobile-security-reviewer`, and `mobile-ui-accessibility-reviewer` review the baseline; `mobile-code-reviewer` performs the final independent review. Add platform owners for KMP or native-host work.

# Procedure and gates

1. Convert requirements into targets, modules, data/state/navigation boundaries, identifiers, minimum OS/SDK versions, and explicit non-goals. Gate: user resolves material choices.
2. Have `mobile-architect` propose a minimal architecture and dependency direction. Gate: no unapproved migration, framework, or persistence decision.
3. Select the official installed generator or create native files directly according to current project conventions. Do not use remote templates of unverified provenance.
4. Add only required dependencies, pin/lock them using the technology's normal mechanism, and record why each is needed.
5. Establish secure defaults: no secrets, least permissions/entitlements, secure transport, safe logging, no production endpoints or fabricated credentials.
6. Establish accessibility/localization foundations and adaptive root UI appropriate to the selected technology.
7. Add meaningful baseline tests and project documentation for setup, discovered commands, architecture, and non-secret configuration.
8. Discover and run formatting validation, lint/static analysis, dependency resolution, baseline tests, and a non-signing/non-publishing build for each configured target that local infrastructure supports.
9. Obtain security, UI/accessibility, test, and independent code review. Correct findings and repeat affected checks.

# Failure and stop handling

Stop if the destination is non-empty and ownership is unclear, a required toolchain is missing, identifiers conflict, secure completion requires credentials/signing, generation would overwrite user work, the generated diff escapes scope, or a required dependency/build/test/check fails. Preserve existing content, report the exact command/evidence and safe recovery or decision needed, and never present a partial or speculative baseline as complete.

# Evidence and acceptance

Return requirements and decisions; created files/modules; dependency rationale; exact toolchain and commands; pass/fail/unavailable results; reviews; and residual risks. Classify every considered build, test, lint, formatting, security, accessibility, localization, adaptive-layout, and target criterion as `required`, `conditionally-required`, or `not-applicable`, with a concrete reason for each `not-applicable` item.

Accept only when requested targets have a coherent native structure, baseline compilation/build and tests pass where required, configuration contains no secret, documentation is usable, required reviews have no unresolved blocker, and unavailable infrastructure is explicitly reported.

# Human review and prohibited actions

Require human approval for identifiers, architecture, dependencies, permissions/entitlements, persistence, network access, and generated broad diffs. Never overwrite uncertain content, install global tools, add unrequested platforms, use placeholder production logic, weaken validation, access credentials, sign, publish, upload, deploy, or claim unavailable checks passed.
