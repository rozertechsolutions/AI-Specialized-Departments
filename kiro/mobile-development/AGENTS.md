# Kiro Mobile Development Instructions

## Verified Native Surface

- Local detection: no `kiro` or `kiro-cli` executable was available in this workspace on 2026-07-15.
- Selected surface: Kiro CLI workspace custom agents using JSON files in `.kiro/agents/`, because the current official CLI documentation defines this format for workspace-scoped custom agents.
- Native components used: `AGENTS.md`, `.kiro/agents/*.json`, `.kiro/skills/*/SKILL.md`, `.kiro/steering/mobile-development.md`, and embedded `preToolUse` hook declarations that invoke `.kiro/hooks/*.py` guards.
- Official Kiro documentation checked on 2026-07-15: CLI custom agents, CLI agent configuration reference, IDE subagents, IDE and CLI Agent Skills, steering, and hooks.
- Unsupported or omitted: duplicate IDE Markdown subagent definitions, generic Kiro Specs, Powers, CLI 3.0 Early Access standalone hook files, active MCP servers, project MCP configuration, real external integrations, signing, publication, upload, deployment, destructive device operations, credential import, and real signing material.

## Scope

Work only inside `kiro/mobile-development/` and mobile projects intentionally placed below it. Support Android, iOS, Kotlin Multiplatform, Flutter, and React Native only when detected from manifests, build files, package files, source layout, or explicit user requirements. Do not modify another platform or specialization.

Before changing anything:

1. Inspect this `AGENTS.md`, relevant `.kiro/steering`, requested Skill, current files, user changes, build configuration, dependency manifests, and applicable project documentation.
2. Detect the actual mobile technology, platform boundaries, acceptance criteria, toolchain, commands, risks, and unavailable infrastructure.
3. Confirm the requested work will not overwrite user changes.
4. Stop for human approval before dependencies, lockfiles, permissions, entitlements, privacy manifests, authentication, cryptography, telemetry, signing configuration, releases, external writes, destructive commands, credential handling, production systems, or spending.

## Responsibility Matrix

| Responsibility | Native component | Classification | Exclusive authority | Prohibited overlap |
| --- | --- | --- | --- | --- |
| `mobile-architect` | `.kiro/agents/mobile-architect.json` | native | Architecture, modules, dependency direction, state, navigation, shared/platform boundaries, migrations | Complete feature implementation, final release approval |
| `android-engineer` | `.kiro/agents/android-engineer.json` | native | Android Kotlin/Java, SDK, Compose/Views, lifecycle, resources, manifests, permissions, Gradle, Android tests | Shared KMP ownership, iOS/Flutter/RN ownership |
| `ios-engineer` | `.kiro/agents/ios-engineer.json` | native | Swift, SwiftUI/UIKit, Apple APIs, lifecycle, Xcode, schemes, entitlements, resources, localization, iOS tests | Shared KMP ownership, Android/Flutter/RN ownership |
| `kmp-engineer` | `.kiro/agents/kmp-engineer.json` | native | KMP source sets, shared logic, targets, dependency placement, `expect`/`actual`, interoperability | Android or iOS UI ownership |
| `flutter-engineer` | `.kiro/agents/flutter-engineer.json` | native | Dart, widgets, navigation, platform channels, packages, flavors, Flutter tests | Native host changes except requested bridge work |
| `react-native-engineer` | `.kiro/agents/react-native-engineer.json` | native | React Native, TypeScript/JavaScript, navigation, Metro, package manager, native bridges, RN tests | Native host implementation except bridge scope |
| `mobile-test-engineer` | `.kiro/agents/mobile-test-engineer.json` | native | Test strategy, test levels, fixtures, determinism, regression coverage, synchronization, flakiness, evidence | Production behavior changes merely to pass tests |
| `mobile-security-reviewer` | `.kiro/agents/mobile-security-reviewer.json` | native | Authentication, authorization, secure storage, network security, privacy, permissions, cryptography, WebViews, deep links, logging, telemetry, dependency risk | Source edits by default, sole implementation approval |
| `mobile-ui-accessibility-reviewer` | `.kiro/agents/mobile-ui-accessibility-reviewer.json` | native | Accessibility, adaptive layouts, orientations, dynamic text, focus, traversal, localization, interaction conventions, complete UI states | Source edits by default |
| `mobile-performance-reviewer` | `.kiro/agents/mobile-performance-reviewer.json` | native | Startup, rendering, memory, leaks, battery, background work, network/storage efficiency, binary size, profiling | Claimed improvement without measurements |
| `mobile-release-engineer` | `.kiro/agents/mobile-release-engineer.json` | native | Versioning, variants, flavors, schemes, reproducibility, package preparation, signing prerequisites, store readiness | Publishing, upload, submission, distribution, signing with real credentials |
| `mobile-code-reviewer` | `.kiro/agents/mobile-code-reviewer.json` | native | Independent final review of correctness, maintainability, regression risk, error handling, conventions, and evidence | Reviewing its own implementation |

Only the coordinator resolves ownership conflicts. Implementation roles may not perform their own independent final review. Review roles are read-only by default.

## Routing

- Android files and Android Gradle configuration: `android-engineer`.
- Apple host files, Swift, SwiftUI/UIKit, Xcode projects/workspaces/schemes, entitlements, privacy manifests, and localization: `ios-engineer`.
- Shared KMP source sets, shared Gradle multiplatform configuration, `expect`/`actual`, and shared logic: `kmp-engineer`.
- Flutter Dart code, `pubspec.yaml`, widgets, plugins, platform channels, flavors, and Flutter tests: `flutter-engineer`.
- React Native JavaScript/TypeScript, Metro, package manager, native bridge contracts, and RN tests: `react-native-engineer`.
- Test strategy, fixtures, determinism, and test-only changes: `mobile-test-engineer`.
- Cross-module architecture, migration plans, dependency direction, and platform boundary decisions: `mobile-architect`.
- Security, UI/accessibility, performance, release, and final code review: corresponding read-only reviewers.

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

Do not duplicate these processes as generic workflows, Specs, Powers, commands, MCP servers, or additional prompts. `prepare-mobile-release` must be manually initiated and must never publish, upload, submit, distribute, deploy, spend money, or use real signing credentials.

## Security Baseline

Never include secrets, tokens, passwords, private keys, certificates, provisioning profiles, keystores, service-account files, private URLs, real endpoints, production personal data, or real environment values. Distinguish genuine secrets from public mobile client configuration, but do not fabricate values.

Require human control for authentication/authorization changes, privacy, manifests, entitlements, network security, deep links, WebViews, analytics, telemetry, dependencies, lockfiles, build/signing configuration, external writes, credential import, destructive commands, publishing, deployment, and financial actions.

MCP remains inactive by default. No MCP server is configured in this specialization. Before enabling or authenticating MCP, explain exposed data, requested scopes, possible external writes, approval behavior, and rollback.

Static hook tests are provided in `.kiro/hooks/tests/test_hooks.py` for manual execution with `python3 -m unittest discover -s .kiro/hooks/tests`; they are dependency-free and were not executed during static generation.

## Validation

Discover actual project commands instead of assuming them. Prefer checked-in wrappers and declared scripts. Never guess Android Gradle tasks, Xcode schemes or destinations, Flutter flavors, React Native package managers, KMP targets, or test commands.

Classify every completion criterion as:

- `required`: directly affected by the request or necessary for correctness.
- `conditionally-required`: applicable only when the detected project supports the tool or infrastructure.
- `not-applicable`: unsupported or irrelevant, with a concrete reason.

Validate as applicable: requirement traceability, project configuration, compilation, unit/integration/UI/snapshot/end-to-end tests, static analysis, lint, formatting, dependency resolution, security, secret detection, accessibility, localization, adaptive layouts, performance, memory, battery, network/storage behavior, offline/loading/empty/error/retry/cancellation/recovery states, documentation, warnings, regressions, and independent review.

Unavailable infrastructure is reported as unavailable, never passed.

## Triple Validation

Before completion, perform and repeat until clean:

1. Native conformance: paths, formats, schemas, fields, events, permissions, version/surface compatibility, native/unsupported classification, no simulations, no unnecessary files, no out-of-scope changes.
2. Responsibility/workflow precision: all twelve responsibilities, all ten workflows, unique ownership, deterministic delegation, no cycles, no conflicts, no self-review, exact references, and completion gates.
3. Security/quality: no secrets, least privilege, inactive integrations, no automatic publication/signing/upload/deployment/spending/destruction, safe guards, measurable evidence, and no fabricated results.

## Completion Report

Report verified version/surface, official documentation consulted, files created/modified/removed/omitted, native capabilities used, unsupported capabilities omitted, responsibilities and workflows implemented, security controls, MCP decision, validation evidence, corrections, remaining limitations, and confirmation that no secret, active integration, publication, signing, upload, deployment, destructive action, or out-of-scope modification occurred.
