# OpenCode Mobile Development Instructions

## Verified Native Surface

- Surface: OpenCode project configuration for `opencode/mobile-development/`.
- Local CLI version: unavailable; `opencode` was not installed on `PATH` during setup on 2026-07-15.
- Documentation verified on 2026-07-15 from official OpenCode Rules, Agents, Agent Skills, Plugins, Tools, and MCP servers documentation.
- Native components used: `AGENTS.md`, `opencode.jsonc`, `.opencode/agents/*.md`, `.opencode/skills/*/SKILL.md`, `.opencode/plugins/*.js`, and dependency-free plugin tests under `.opencode/plugins/tests/`.
- Unsupported components omitted: generic `agents/`, `subagents/`, `skills/`, `workflows/`, `hooks/`, `mcp/`; active MCP servers; slash-command workflow duplicates; real external integrations; signing, publication, upload, deployment, destructive device operations, credential import, and spending.

## Scope

Work only inside `opencode/mobile-development/` and mobile projects intentionally placed below it. Support Android, iOS, Kotlin Multiplatform, Flutter, and React Native only after detecting the technology from manifests, build files, package metadata, source layout, or explicit user requirements.

Do not infer package names, bundle identifiers, signing teams, schemes, flavors, API contracts, credentials, endpoints, product behavior, or deployment targets. Ask when those cannot be derived safely.

## Coordination Rules

The primary OpenCode agent is the coordinator. It owns clarification, scope, sequencing, role selection, conflict prevention, validation synthesis, and final reporting. It must not duplicate work assigned to a specialist.

Before changing anything:

1. Read applicable `AGENTS.md`, requested Skill files, current files, relevant project docs, and current changes.
2. Identify platform, requested behavior, owner, reviewers, acceptance criteria, supported toolchain, exact verification commands, risks, and unavailable infrastructure.
3. Preserve user changes and stop if requested work would overwrite or ambiguously overlap them.
4. Use exactly one primary implementation owner per work unit.
5. Require independent review for security, accessibility, performance, release, and final code review when applicable.

## Responsibility Matrix

| Responsibility | Native component | Classification | Exclusive authority | Prohibited overlap |
| --- | --- | --- | --- | --- |
| `mobile-architect` | `.opencode/agents/mobile-architect.md` | native | Architecture, modules, dependency direction, state, navigation, shared/platform boundaries, migrations | Complete feature implementation, release approval |
| `android-engineer` | `.opencode/agents/android-engineer.md` | native | Android Kotlin, SDK, Compose/Views, lifecycle, resources, manifests, permissions, Gradle, Android tests | Shared KMP logic ownership |
| `ios-engineer` | `.opencode/agents/ios-engineer.md` | native | Swift, SwiftUI/UIKit, Apple APIs, lifecycle, Xcode, schemes, entitlements, resources, localization, iOS tests | Shared KMP logic ownership |
| `kmp-engineer` | `.opencode/agents/kmp-engineer.md` | native | KMP source sets, shared logic, targets, dependency placement, `expect`/`actual`, interoperability | Android or iOS UI ownership |
| `flutter-engineer` | `.opencode/agents/flutter-engineer.md` | native | Dart, widgets, navigation, platform channels, packages, flavors, Flutter tests | Native host ownership except bridge scope |
| `react-native-engineer` | `.opencode/agents/react-native-engineer.md` | native | React Native, TypeScript/JavaScript, navigation, Metro, package manager, native bridges, RN tests | Native host ownership except bridge scope |
| `mobile-test-engineer` | `.opencode/agents/mobile-test-engineer.md` | native | Test strategy, levels, fixtures, determinism, regression coverage, synchronization, flakiness, evidence | Production changes merely to pass tests |
| `mobile-security-reviewer` | `.opencode/agents/mobile-security-reviewer.md` | native | Authentication, authorization, secure storage, network security, privacy, permissions, cryptography, WebViews, deep links, logs, telemetry, dependency risk | Source edits by default |
| `mobile-ui-accessibility-reviewer` | `.opencode/agents/mobile-ui-accessibility-reviewer.md` | native | Accessibility, adaptive layouts, orientations, dynamic text, focus, traversal, localization, interaction conventions, UI states | Source edits by default |
| `mobile-performance-reviewer` | `.opencode/agents/mobile-performance-reviewer.md` | native | Startup, rendering, memory, leaks, battery, background work, network/storage efficiency, binary size, profiling | Claimed improvement without measurements |
| `mobile-release-engineer` | `.opencode/agents/mobile-release-engineer.md` | native | Versioning, variants, flavors, schemes, reproducibility, package preparation, signing prerequisites, store readiness | Publishing, upload, submission, distribution, signing with real credentials |
| `mobile-code-reviewer` | `.opencode/agents/mobile-code-reviewer.md` | native | Independent final correctness, maintainability, regression risk, error handling, conventions, evidence | Reviewing own implementation |

Only the coordinator resolves role conflicts. Reviewers are read-only by default and cannot approve their own implementation. Implementation roles cannot perform independent final review.

## Workflow Matrix

Use exactly one Skill for each reusable process:

- `create-mobile-project`
- `implement-mobile-feature`
- `fix-mobile-bug`
- `review-mobile-architecture`
- `add-mobile-screen`
- `integrate-mobile-api`
- `add-mobile-tests`
- `optimize-mobile-performance`
- `audit-mobile-security`
- `prepare-mobile-release`

Do not duplicate these processes as generic workflows, commands, prompts, MCP servers, hooks, or extra agents.

## Routing

- Android files and Android Gradle configuration: `android-engineer`.
- iOS host files, Xcode, Swift, entitlements, schemes: `ios-engineer`.
- Shared KMP source sets and multiplatform Gradle logic: `kmp-engineer`.
- Flutter app code, Dart tests, `pubspec.yaml`, Flutter tooling: `flutter-engineer`.
- React Native app code, Metro, JavaScript/TypeScript, native bridge contracts: `react-native-engineer`.
- Test-only strategy and fixtures: `mobile-test-engineer`.
- Cross-module architecture or migration plans: `mobile-architect`.
- Security, UI/accessibility, performance, release, and final correctness reviews: corresponding read-only reviewers.

## Security Baseline

Never include secrets, tokens, passwords, certificates, private keys, provisioning profiles, keystores, service-account files, private URLs, real endpoints, production personal data, or real environment values.

Require human control before changes to authentication, authorization, privacy, manifests, entitlements, network security, deep links, WebViews, analytics, telemetry, dependencies, lockfiles, build/signing configuration, external writes, credential import, destructive commands, publishing, deployment, and financial actions.

OpenCode MCP entries remain disabled. Do not enable or authenticate MCP without explicit user approval after describing exposed data, requested scope, possible external writes, and approval behavior.

Plugin tests are provided for manual execution with `node --test .opencode/plugins/tests/mobile-guards.test.js`. They use only `node:test` and `node:assert` and were not executed during static generation.

## Verification

Discover actual project commands. Prefer wrappers and declared scripts. Never guess schemes, destinations, flavors, targets, package managers, or scripts.

Classify each completion criterion as:

- `required`: directly affected by the request or needed for correctness.
- `conditionally-required`: applicable only when detected project infrastructure exists.
- `not-applicable`: concrete reason required.

Validate as applicable: traceability, configuration, compilation, unit/integration/UI/snapshot/end-to-end tests, static analysis, lint, formatting, dependency resolution, security, secret detection, accessibility, localization, adaptive layouts, performance, memory, battery, network/storage behavior, offline/loading/empty/error/retry/cancellation/recovery states, documentation, warnings, regressions, and independent review.

Unavailable infrastructure is reported as unavailable, never passed.

## Triple Validation

Before completion, repeat until clean:

1. Native conformance: paths, formats, schemas, fields, events, permissions, version or surface compatibility, native/unsupported classification, no simulations, no unnecessary files, no out-of-scope changes.
2. Responsibility and workflow precision: all twelve responsibilities, all ten workflows, unique ownership, deterministic delegation, no cycles, no conflicts, no self-review.
3. Security and quality: no secrets, least privilege, inactive integrations, no publication, signing, upload, deployment, spending, destruction, unsafe guard behavior, or fabricated evidence.

## Completion Report

Report changed files, native capabilities used, unsupported capabilities omitted, responsibilities and workflows implemented, security controls, MCP decision, validation evidence, corrections, remaining limitations, and confirmation that no secret, active integration, publication, signing, upload, deployment, destructive action, or out-of-scope modification occurred.
