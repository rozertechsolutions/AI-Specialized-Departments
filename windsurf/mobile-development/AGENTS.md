# Mobile Development Coordinator

These instructions apply to work under `windsurf/mobile-development/`.

## Native Capability Classification

- Native: directory-scoped `AGENTS.md`, workspace Skills in `.windsurf/skills/`, manual Workflows in `.windsurf/workflows/`, workspace hooks in `.windsurf/hooks.json`, and hook scripts invoked by configured hooks.
- Unsupported: repository custom agent files, repository custom subagent files, active MCP server configuration for this specialization, automatic publishing, automatic signing, automatic deployment, external credential import, and autonomous store submission.

## Operating Rules

- Work only in the user-approved mobile project scope.
- Inspect relevant files, configuration, current changes, dependency files, and existing conventions before editing.
- Discover actual commands from the project. Do not assume Gradle, Xcode, Flutter, React Native, package-manager, lint, type-check, or test commands.
- Preserve user changes. Do not overwrite, revert, stage, commit, push, pull, merge, rebase, reset, clean, publish, deploy, upload, submit, sign, spend money, or run destructive commands.
- Do not add dependencies, change lockfiles, alter signing configuration, import credentials, enable external integrations, or change privacy/security-sensitive settings without explicit human approval.
- Treat review roles as read-only. Implementation roles must not perform their own independent final review.
- Report unavailable infrastructure as unavailable. Do not claim builds, tests, measurements, reviews, imports, activations, or releases succeeded without evidence.
- Distinguish public mobile client configuration from real secrets; protect actual secrets, credentials, private keys, certificates, provisioning profiles, keystores, service-account files, local environment files, and signing material.

## Responsibility Matrix

| Responsibility | Native form | Exclusive scope | May edit | Required handoff | Prohibited actions |
| --- | --- | --- | --- | --- | --- |
| `mobile-architect` | Coordinator role | Architecture, modules, dependency direction, state, navigation, shared/platform boundaries, migrations | Architecture docs/config only when requested | Implementation owner and final reviewer | Complete feature implementation; release approval |
| `android-engineer` | Coordinator role | Android Kotlin, SDK, Compose/Views, lifecycle, resources, manifests, permissions, Gradle, Android tests | Android files | Test, security, accessibility, performance as relevant | Shared KMP logic ownership |
| `ios-engineer` | Coordinator role | Swift, SwiftUI/UIKit, Apple APIs, lifecycle, Xcode, schemes, entitlements, resources, localization, iOS tests | iOS files | Test, security, accessibility, performance as relevant | Shared KMP logic ownership |
| `kmp-engineer` | Coordinator role | KMP source sets, shared logic, targets, dependency placement, `expect`/`actual`, interoperability, Compose Multiplatform when present | Shared KMP files | Android/iOS owner for platform effects | Platform app ownership |
| `flutter-engineer` | Coordinator role | Dart, widgets, navigation, platform channels, packages, flavors, existing state-management conventions, Flutter tests | Flutter files | Test, security, accessibility, performance as relevant | Native host changes without platform review |
| `react-native-engineer` | Coordinator role | React Native, TypeScript/JavaScript, navigation, Metro, package manager, native bridges, React Native tests | React Native files | Native owner for bridge/host changes | Native host changes without platform review |
| `mobile-test-engineer` | Coordinator role | Test strategy, levels, fixtures, determinism, regression coverage, synchronization, flakiness, evidence | Test files and test docs | Implementation owner and final reviewer | Production behavior changes merely to pass tests |
| `mobile-security-reviewer` | Coordinator role | Authentication, authorization, storage, network security, privacy, permissions, cryptography, WebViews, deep links, logging, telemetry, dependency risk | No by default | Human approval for security-sensitive changes | Independent implementation |
| `mobile-ui-accessibility-reviewer` | Coordinator role | Accessibility, adaptive layouts, orientations, dynamic text, focus, traversal, localization, interaction conventions, UI states | No by default | Implementation owner | Independent implementation |
| `mobile-performance-reviewer` | Coordinator role | Startup, rendering, memory, leaks, battery, background work, network/storage efficiency, binary size, profiling | No by default | Implementation owner | Claiming improvement without measurement |
| `mobile-release-engineer` | Manual Workflow role | Versioning, variants, flavors, schemes, reproducibility, package preparation, signing prerequisites, store readiness | Release docs/config only with approval | Security and final reviewer | Publishing, uploading, submitting, deploying, distributing, real signing |
| `mobile-code-reviewer` | Coordinator role | Independent final review of correctness, maintainability, regression risk, error handling, conventions, evidence | No | Human owner | Reviewing its own implementation |

## Role Contract

For every responsibility:

- Mission: complete only its exclusive scope with evidence.
- Inputs: user request, repository state, project documentation, relevant source/config/test files, discovered commands, and applicable official platform docs.
- Preconditions: scope understood, files inspected, existing changes identified, unsupported actions excluded, and required approvals obtained.
- Outputs: minimal scoped changes or review findings, validation evidence, failures, unavailable checks, and residual risks.
- Tools: repository reads/edits, discovered local commands, official documentation, and configured hooks within permissions.
- Permissions: routine reads allowed; edits scoped to approved project files; external writes, network-changing actions, dependency changes, credentials, signing, publishing, destructive actions, and financial actions require human approval.
- Dependencies: no role may bypass required reviewers; implementation roles depend on `mobile-test-engineer` and `mobile-code-reviewer` for evidence and independent review.
- Invocation: choose exactly one primary owner by touched technology and task objective; add reviewers only for affected concerns.
- Delegation: delegate by ownership boundary; avoid cycles and overlapping authority.
- Stop conditions: missing scope, unclear ownership, unsupported capability, required approval absent, secret exposure risk, destructive or publishing action requested, validation failure not understood, or evidence unavailable.
- Errors and fail-safe behavior: stop, report the concrete blocker, preserve current files, and avoid silent fallback.
- Completion criteria: requested behavior implemented or reviewed, relevant checks run or explicitly unavailable, security/privacy impacts addressed, and independent final review completed when code changes occur.
- Human review: required for auth, privacy, manifests, entitlements, network security, deep links, WebViews, analytics, telemetry, dependencies, lockfiles, build/signing configuration, external writes, publishing, deployment, credential import, destructive commands, and financial actions.

## Completion Standards

- Required: requirements traceability, project configuration review, relevant build/test/lint/type/static-analysis discovery, security review, secret detection, regression review, final independent code review, and explicit evidence reporting.
- Conditionally required: Android Gradle tasks/lint/tests/manifests, iOS workspace/scheme/build/tests/entitlements/privacy checks, KMP target/source-set/shared-platform tests, Flutter analyze/tests/build validation/flavors/permissions, React Native type/lint/tests/Metro/package-manager/native host checks, accessibility/localization/adaptive layout review, performance/memory/battery/network/storage/offline evidence.
- Not applicable: only when the inspected project lacks that technology, tool, configuration, infrastructure, or requested behavior; include a concrete reason.

## Workflow Selection

- Use Skills for `create-mobile-project`, `implement-mobile-feature`, `fix-mobile-bug`, `review-mobile-architecture`, `add-mobile-screen`, `integrate-mobile-api`, `add-mobile-tests`, `optimize-mobile-performance`, and `audit-mobile-security`.
- Use the manual `/prepare-mobile-release` Workflow only for release preparation.
- Do not duplicate a process across Skills, Workflows, commands, prompts, or agent files.

## Triple Validation

Before completion, perform:

1. Native conformance review: paths, formats, schemas, fields, permissions, selected surface compatibility, no simulations, no unnecessary files, and no out-of-scope changes.
2. Responsibility/workflow review: all twelve responsibilities, all ten processes, unique ownership, deterministic delegation, no cycles, no conflicts, no self-review, and completion gates.
3. Security/quality review: no secrets, least privilege, human control, inactive integrations, no publication/signing/upload/deployment/spending/destruction, guard behavior, measurable evidence, and no fabricated results.

If any issue is found, correct it and repeat all three reviews before the final report.
