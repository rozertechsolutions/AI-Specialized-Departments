---
name: create-mobile-project
description: Creates a new Android, iOS, Kotlin Multiplatform, Flutter, or React Native project after explicit technology and target selection, using installed toolchains and evidence-based validation. Use only when the user asks to create a new mobile project or target from scratch.
---

# Create Mobile Project

## Objective and trigger

Create a minimal, buildable, tested mobile project with explicit technology,
targets, architecture, security, accessibility, and ownership decisions. Activate
only for a user request to create a new application/project or a genuinely new
target. Do not activate for a feature inside an existing application.

Activation does not grant tools. Use only project-allowed read/write tools and
approved local toolchain commands; never use MCP or remote package executors.

## Inputs

- Product purpose and minimum first behavior.
- Target platforms, supported OS versions, application/package identifiers, and
  destination path.
- Required UI approach, offline/data needs, accessibility/localization scope,
  distribution intent, and compatibility constraints.
- Approved technology, package manager, dependencies, and installed toolchains.

## Preconditions and ownership

The destination must be inside the authorized repository scope and must not
contain uncertain or user-owned content. Inspect it before writing. Confirm all
app identifiers and targets; never invent production identifiers.

The primary implementation owner is selected once from project technology:
`android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or
`react-native-engineer`. Select the matching owner for a native Android, native
iOS, KMP, Flutter, or React Native project respectively; for KMP, Android/iOS
owners receive only explicit native-host files. `mobile-architect` owns the architecture decision;
Android/iOS owners support KMP or cross-platform native hosts. Required reviewers
are `mobile-test-engineer`, `mobile-security-reviewer`,
`mobile-ui-accessibility-reviewer`, and `mobile-code-reviewer`. Add performance
or release review only when their criteria become required.

## Workflow and gates

1. **Scope gate:** inspect instructions, repository status, destination, nearby
   conventions, documentation, and available toolchain versions. Stop if the
   destination is non-empty or ownership is uncertain.
2. **Requirements gate:** resolve technology, targets, OS floors, identifiers,
   architecture needs, data sensitivity, UI states, accessibility, localization,
   tests, and non-goals. Obtain human selection where choices materially differ.
3. **Architecture gate:** ask `mobile-architect` for the smallest module/state/
   navigation/data design. Record the responsibility matrix and dependency
   direction. Do not create speculative modules.
4. **Toolchain gate:** verify the selected generator and build tools are already
   installed and compatible. Do not install or update runtimes, SDKs, plugins,
   packages, or dependencies. Stop and report exact missing prerequisites.
5. **Creation:** assign one primary owner. Generate or write only necessary files
   using the selected platform's native mechanism and existing stable defaults.
   Inspect generator output before further edits.
6. **Baseline implementation:** establish minimal application flow, testable
   state boundaries, error handling, localization resources, accessibility
   semantics, secure transport/storage defaults, and least permissions. Do not
   add external services or credentials.
7. **Test gate:** `mobile-test-engineer` adds the smallest deterministic baseline
   tests. Discover and run compile, unit, configured UI/integration, lint, static
   analysis, and formatting checks. Fix in-scope failures before proceeding.
8. **Review gate:** obtain read-only security and UI/accessibility reviews,
   platform-native review where relevant, and final independent code review.
   Resolve all blocking findings and rerun affected checks.
9. **Documentation gate:** document discovered prerequisites, project structure,
   local non-publishing commands, limitations, and unavailable validation without
   adding secrets or release instructions that execute sensitive actions.

## Completion classification

Before implementation and again at exit, classify every item as `required`,
`conditionally-required`, or `not-applicable` with a project-specific reason:
requirements/scope; configuration; compilation; unit, integration, UI, snapshot,
and E2E tests; lint/static analysis/formatting; dependency resolution; security/
secret review; accessibility/localization/adaptive UI; performance/memory/battery/
network/storage/offline behavior; loading/empty/error/retry/cancellation/recovery
states; documentation; warnings; regressions; independent review; and the
selected technology's native checks. A check is passed only with command evidence.

## Errors and stop conditions

Stop for missing toolchains, unapproved identifiers/technology/dependencies,
non-empty destination, external authentication, costs, security uncertainty,
signing, publication, deployment, conflicting changes, or any failing required
check that cannot be fixed within scope. Preserve partial evidence and do not
claim the project is buildable when compilation was unavailable.

## Outputs, evidence, and acceptance

Return selected technology/targets/owner, architecture decision, exact files,
generator and validation commands with results, test/review evidence, completion
ledger, warnings, unavailable checks, prerequisites, and remaining human actions.

Acceptance requires the minimal requested project, no placeholder-only files,
successful available compile/test/lint checks, resolved blocking reviews, no
secrets/external integrations, and an independent `mobile-code-reviewer` pass.

## Human review and prohibited actions

Humans choose material technology/identifier/dependency trade-offs and retain
control of credentials, signing, distribution, and publication. Never overwrite
content, install packages/toolchains, use real credentials, enable MCP/external
services, sign, publish, upload, deploy, submit, distribute, perform destructive
operations, or commit/push without exact authorization.
