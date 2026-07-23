---
name: create-mobile-project
description: Creates a validated baseline for an Android, iOS, KMP, Flutter, or React Native project. Use when starting a new mobile project.
---

# Create Mobile Project

## Objective

Define and, only with adequate tools and approval, create the smallest valid mobile project baseline that matches the user's selected technology, targets, identifiers, architecture, and quality requirements.

## Trigger

Use when the user asks to start, initialize, scaffold, or establish a new mobile application or library. Do not use for adding a feature to an existing project.

## Inputs

- product objective and initial acceptance criteria;
- exactly one primary technology or an explicitly justified KMP arrangement;
- target platforms and minimum supported operating-system versions;
- user-approved application name, package or bundle identifiers, organization or namespace, and repository location;
- UI approach, navigation, state, networking, persistence, localization, and testing requirements;
- required variants, flavors, schemes, modules, and release channels;
- allowed toolchain versions and dependency policy;
- available tools, SDKs, network access, and human approvals.

Never invent an identifier, signing team, endpoint, credential, flavor, scheme, or product decision.

## Supported technologies

Native Android, native iOS, KMP, Flutter, and React Native. Compose Multiplatform applies only when explicitly selected. A project that combines unrelated frameworks requires a documented user-approved reason and separate ownership boundaries.

## Preconditions

- Project instructions and relevant knowledge are available.
- The target directory is empty or its existing content has been fully inspected.
- Surface, plan or workspace, tool access, installed or declared SDK versions, and network limits are recorded.
- The user has selected the technology and approved identifiers and target versions.
- Any generator, template, package download, dependency addition, or network action is known and separately approved.
- Signing, publication, deployment, external service setup, and real credentials are out of scope.

## Primary owner and reviewers

Select exactly one primary implementation owner:

- Android: android-engineer.
- iOS: ios-engineer.
- KMP: kmp-engineer.
- Flutter: flutter-engineer.
- React Native: react-native-engineer.

mobile-architect reviews boundaries before implementation. mobile-test-engineer reviews the test baseline. mobile-security-reviewer reviews permissions, dependencies, storage, network, and privacy. mobile-ui-accessibility-reviewer reviews UI foundations. mobile-code-reviewer performs final read-only review. Add native host reviewers for KMP, Flutter channels, or React Native bridges.

## Ordered workflow

1. Restate the objective, technology, targets, identifiers, acceptance criteria, exclusions, and evidence limitations.
2. Inspect the destination, repository instructions, current changes, installed tools, and existing files without modification.
3. Verify the selected toolchain and generator syntax from current official documentation when repository evidence is absent.
4. Have mobile-architect produce a minimal boundary decision: modules, dependency direction, state and navigation ownership, shared versus platform code, and migration posture.
5. Define a file and directory plan containing only native files needed by the chosen technology. Exclude universal adapters, common runtimes, extra frameworks, placeholder modules, empty files, and speculative services.
6. Define dependency and plugin choices. Prefer platform and standard-library capabilities; require explicit approval for every external dependency or package.
7. Define test levels, static analysis, formatting, localization, accessibility, error states, offline expectations, security controls, and validation commands.
8. Present the creation plan, generator or file operations, dependencies, and side effects for human approval.
9. If approved tools exist, create only the agreed baseline. If no edit tool exists, return an exact file plan and mark creation unavailable; do not claim files were created.
10. Inspect every generated or created file. Remove no unexpected file without approval. Reject placeholder-only output and hidden telemetry, analytics, sample credentials, or publishing automation.
11. Run discovered targeted configuration, formatting, analysis, compilation, and baseline tests using unsigned and non-publishing paths.
12. Obtain all required reviews, correct in-scope findings through the primary owner, and rerun validation.
13. Perform the three Project review passes and final verification.

## Conditional steps

- KMP: define targets and source-set hierarchy; validate expect and actual boundaries; assign Android and iOS hosts to native owners.
- Flutter or React Native: review generated native host projects and platform permissions; assign non-trivial host changes to native owners.
- UI present: require accessibility, localization, dynamic text, orientation, and loading or empty or error-state foundations.
- Remote API or persistence present: require approved contracts, security review, failure behavior, migration or offline strategy, and tests.
- Existing non-empty destination: stop unless the user explicitly confirms how to preserve or integrate its contents.

## Validation gates

- Gate 1: technology, targets, identifiers, scope, and ownership are explicit.
- Gate 2: architecture and dependency plan has human approval.
- Gate 3: every created file is necessary, non-empty, native, and inspected.
- Gate 4: applicable configuration, compilation, analysis, formatting, and baseline tests pass.
- Gate 5: security, UI, test, and final code reviews have no unresolved required finding.
- Gate 6: criterion ledger and final prohibition confirmation are complete.

## Failures

On generator, dependency, build, or test failure, preserve exact output, stop mutation, classify the failure, and correct only an in-scope cause. Do not change toolchain versions, identifiers, signing, targets, security controls, or dependencies merely to pass. If a generator creates unexpected content, report it and request approval before any removal.

## Stop conditions

Stop for missing technology choice, identifier, target, acceptance criteria, SDK, generator review, dependency approval, non-empty destination conflict, sensitive configuration, credential or signing request, network install without approval, destructive operation, or any publication or deployment step.

## Evidence

Record destination state before and after, source or documentation for generator syntax, tool versions, exact created files, dependency decisions, commands, exit statuses, warnings, test results, reviewer findings, corrections, and unavailable checks.

## Outputs

- created baseline or an explicitly unavailable implementation plan;
- architecture and ownership record;
- complete file inventory and dependency rationale;
- discovered developer and validation commands;
- test and quality baseline;
- criterion ledger, review record, and human next steps.

## Acceptance criteria

The baseline uses the selected native technology, contains no unnecessary or placeholder-only component, preserves unique ownership, builds or is explicitly blocked with evidence, has a usable test and quality foundation, includes no secret or active integration, and passes independent final review.

## Human approvals

Require approval for identifiers, architecture, targets, dependencies, generators or downloads, network use, destination writes, permissions, entitlements, privacy behavior, analytics, persistence, authentication, build configuration, and every sensitive change.

## Prohibited actions

Do not invent product values, add speculative dependencies, create a common adapter, use real credentials, configure external services, sign, publish, upload, submit, deploy, distribute, spend money, perform destructive operations, or run Git write commands.
