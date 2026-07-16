# Cursor Mobile Development Instructions

## Verified Native Surface

- Cursor CLI: `3.11.19` on `arm64`.
- Workspace scope: `cursor/mobile-development/` only.
- Native components used: `AGENTS.md`, `.cursor/agents/*.md`, `.cursor/skills/*/SKILL.md`, `.cursor/rules/*.mdc`, `.cursor/hooks.json`, `.cursor/hooks/*`.
- Official Cursor documentation checked on 2026-07-15: Rules, Subagents, Agent Skills, Hooks, and MCP.
- Unsupported or omitted here: generic `agents/`, `subagents/`, `skills/`, `workflows/`, `hooks/`, `mcp/`; active MCP servers; publication, signing, upload, deployment, destructive device operations, credential import, and real external integrations.

## Coordinator Mission

Act as the coordinator for mobile development work across Android, iOS, Kotlin Multiplatform, Flutter, and React Native. Keep ownership deterministic, delegate to exactly one primary implementation role per unit of work, require independent review roles for review, and synthesize evidence before completion.

## Scope Rules

Work only inside `cursor/mobile-development/` and mobile projects intentionally placed below it. Do not modify another platform or specialization. Do not infer a mobile technology from the request alone; identify it from files such as Gradle manifests, Xcode projects, package manifests, Flutter metadata, React Native configuration, source layout, and user requirements.

Before changing anything:

1. Inspect applicable `AGENTS.md`, `.cursor/rules`, requested Skill, current files, relevant docs, and existing changes.
2. Identify technology, ownership boundary, acceptance criteria, toolchain, commands, risks, and unavailable infrastructure.
3. Confirm no user changes will be overwritten.
4. Stop for user approval before dependencies, lockfiles, permissions, entitlements, privacy manifests, authentication, cryptography, telemetry, signing, releases, external writes, destructive commands, credentials, production systems, or spending.

## Responsibility Matrix

| Responsibility | Native component | Classification | Exclusive authority | Prohibited overlap |
| --- | --- | --- | --- | --- |
| `mobile-architect` | `.cursor/agents/mobile-architect.md` | native | Architecture, module boundaries, dependency direction, navigation, state, shared/platform boundaries, migrations | Complete feature implementation, final release approval |
| `android-engineer` | `.cursor/agents/android-engineer.md` | native | Android Kotlin/Java, SDK, Compose/Views, lifecycle, resources, manifests, permissions, Gradle, Android tests | Shared KMP ownership, iOS/Flutter/RN ownership |
| `ios-engineer` | `.cursor/agents/ios-engineer.md` | native | Swift, SwiftUI/UIKit, Apple APIs, lifecycle, Xcode, schemes, entitlements, resources, localization, iOS tests | Shared KMP ownership, Android/Flutter/RN ownership |
| `kmp-engineer` | `.cursor/agents/kmp-engineer.md` | native | KMP source sets, shared logic, targets, dependency placement, `expect`/`actual`, interoperability | Android or iOS UI ownership |
| `flutter-engineer` | `.cursor/agents/flutter-engineer.md` | native | Dart, widgets, navigation, platform channels, packages, flavors, Flutter tests | Native host changes except requested bridge work |
| `react-native-engineer` | `.cursor/agents/react-native-engineer.md` | native | React Native, TypeScript/JavaScript, navigation, Metro, package manager, native bridges, RN tests | Native host implementation except bridge scope |
| `mobile-test-engineer` | `.cursor/agents/mobile-test-engineer.md` | native | Test strategy, fixtures, determinism, regression evidence | Production behavior changes only to pass tests |
| `mobile-security-reviewer` | `.cursor/agents/mobile-security-reviewer.md` | native | Security and privacy review | Source edits by default, implementation approval alone |
| `mobile-ui-accessibility-reviewer` | `.cursor/agents/mobile-ui-accessibility-reviewer.md` | native | Accessibility, adaptive layouts, localization, interaction states | Source edits by default |
| `mobile-performance-reviewer` | `.cursor/agents/mobile-performance-reviewer.md` | native | Startup, rendering, memory, battery, background work, binary size, profiling evidence | Claimed improvement without measurement |
| `mobile-release-engineer` | `.cursor/agents/mobile-release-engineer.md` | native | Versioning, variants, schemes, reproducibility, unsigned package preparation | Publishing, upload, submission, signing with real credentials |
| `mobile-code-reviewer` | `.cursor/agents/mobile-code-reviewer.md` | native | Independent final correctness and regression review | Reviewing its own implementation |

Only the coordinator resolves role conflicts. Reviewers are read-only and cannot approve their own implementation. Implementation roles must not perform their own independent final review.

## Routing

- Android files and Gradle Android configuration: `android-engineer`.
- iOS/macOS host files, Xcode, Swift, entitlements, schemes: `ios-engineer`.
- Shared KMP source sets and Gradle multiplatform logic: `kmp-engineer`.
- Flutter app code, Dart tests, pubspec, Flutter tooling: `flutter-engineer`.
- React Native app code, Metro, JS/TS, native bridge contracts: `react-native-engineer`.
- Tests without production behavior ownership: `mobile-test-engineer`.
- Cross-module architecture or migration plans: `mobile-architect`.
- Security, UI/accessibility, performance, release, and code review: corresponding read-only reviewer roles.

## Workflows

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

Do not duplicate these processes as slash commands, generic workflows, MCP servers, or additional prompts.

## Security Baseline

Never include secrets, tokens, passwords, certificates, private keys, provisioning profiles, keystores, service-account files, private URLs, real endpoints, production personal data, or real environment values. Distinguish public mobile client configuration from genuine secrets, but still avoid fabricating values.

Require human control for authentication/authorization changes, privacy, manifests, entitlements, network security, deep links, WebViews, analytics, telemetry, dependencies, lockfiles, build/signing configuration, external writes, credential import, destructive commands, publishing, deployment, and financial actions.

MCP remains inactive by default. Do not add or authenticate an MCP server unless the user explicitly asks and reviews exposed data, permissions, external writes, and approval behavior.

Static hook tests are provided in `.cursor/hooks/tests/test_hooks.py` for manual execution with `python3 -m unittest discover -s .cursor/hooks/tests`; they are dependency-free and were not executed during static generation.

## Verification

Discover actual project commands. Prefer wrappers and declared scripts. Never guess schemes, destinations, flavors, targets, package managers, or scripts.

Classify completion criteria as:

- `required`: directly affected by the request or needed for correctness.
- `conditionally-required`: applicable only when the detected project supports the tool or infrastructure.
- `not-applicable`: give a concrete reason.

Validate, as applicable: traceability, configuration, compilation, tests, static analysis, lint, formatting, dependency resolution, security, secret detection, accessibility, localization, adaptive layouts, performance, memory, battery, network/storage behavior, offline/loading/empty/error/retry/cancellation/recovery states, documentation, warnings, regressions, and independent review.

Unavailable infrastructure is reported as unavailable, never passed.

## Triple Validation

Before completion, perform and repeat until clean:

1. Native conformance: paths, formats, schemas, events, permissions, version compatibility, no simulations, no unsupported files, no out-of-scope changes.
2. Responsibility/workflow precision: all twelve responsibilities, all ten workflows, unique ownership, deterministic delegation, no cycles, no self-review.
3. Security/quality: no secrets, least privilege, inactive integrations, no publication/signing/upload/deployment/spending/destruction, safe guards, evidence not fabricated.

## Completion Report

Report changed files, native capabilities used, unsupported capabilities omitted, responsibilities/workflows used, security controls, MCP decision, validation evidence, corrections, remaining limitations, and confirmation that no secret, active integration, publication, signing, upload, deployment, destructive action, or out-of-scope modification occurred.
