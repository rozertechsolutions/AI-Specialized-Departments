# Junie Mobile Development Specialization

This specialization is native for Junie CLI and Junie in JetBrains IDEs. It is scoped to this directory:

`junie/mobile-development/`

## Verified Surface

- Verified date: 2026-07-15.
- Installed CLI detected locally: `Junie version: 26.6.29 (2144.9)`.
- Current stable native project files used here:
  - `.junie/AGENTS.md`: project guidelines.
  - `.junie/config.json`: project configuration with supported fields only.
  - `.junie/agents/*.md`: custom subagents with YAML frontmatter.
  - `.junie/skills/<skill-name>/SKILL.md`: agent skills.
  - `.junie/commands/*.md`: custom slash commands that only dispatch to skills.
- Native but intentionally omitted:
  - `.junie/mcp/mcp.json`: omitted because manually added MCP configurations are enabled by default and may require secrets, OAuth, local executables, or remote services.
  - Hooks: omitted because hooks from default project config are ignored for safety and shell automation must not be simulated.
- Unsupported for this specialization:
  - Root-level `agents/`, `subagents/`, `skills/`, `workflows/`, `hooks/`, and `mcp/` directories outside `.junie/`.
  - Universal adapters, shared runtimes, cross-platform converters, placeholder trees, fake hook systems, fake MCP connectors, automatic publication, automatic signing, and active external integrations.

## Operating Rules

- Work only inside `junie/mobile-development/` unless the user gives explicit approval for another path.
- Inspect existing project files before changing production code.
- Preserve user changes and do not discard, overwrite, stage, commit, branch, pull, push, merge, rebase, reset, restore, clean, publish, deploy, upload, sign, submit, or spend money.
- Do not hardcode model versions, provider keys, BYOK values, proxies, private URLs, tokens, passwords, signing keys, certificates, provisioning profiles, keystores, API keys, or real endpoint values.
- Do not activate, trust, approve, authenticate, connect, or start external integrations by default.
- Detect actual project technologies and commands before using them. Report unavailable infrastructure as unavailable.
- Treat generated build outputs, caches, and reports as evidence only after the relevant command actually succeeds.
- If official documentation contradicts this specialization, follow the documentation, make the smallest valid correction, and record it.

## Responsibility Matrix

| Responsibility | Classification | Primary scope | May edit production code | Final review authority | Mandatory reviewers |
|---|---|---|---:|---:|---|
| `mobile-architect` | native subagent | Architecture, modules, dependency direction, state, navigation, shared/platform boundaries, migrations | No complete feature implementation | No | `mobile-code-reviewer` |
| `android-engineer` | native subagent | Android Kotlin, SDK, Compose/Views, lifecycle, resources, manifests, permissions, Gradle, Android tests | Yes, Android only | No | `mobile-test-engineer`, `mobile-code-reviewer` |
| `ios-engineer` | native subagent | Swift, SwiftUI/UIKit, Apple APIs, lifecycle, Xcode, schemes, entitlements, resources, localization, iOS tests | Yes, iOS only | No | `mobile-test-engineer`, `mobile-code-reviewer` |
| `kmp-engineer` | native subagent | KMP source sets, shared logic, targets, dependencies, `expect`/`actual`, interoperability | Yes, KMP shared/platform only | No | `mobile-test-engineer`, `mobile-code-reviewer` |
| `flutter-engineer` | native subagent | Dart, widgets, navigation, platform channels, packages, flavors, state conventions, Flutter tests | Yes, Flutter only | No | `mobile-test-engineer`, `mobile-code-reviewer` |
| `react-native-engineer` | native subagent | React Native, TypeScript/JavaScript, navigation, Metro, package manager, native bridges, tests | Yes, React Native only | No | `mobile-test-engineer`, `mobile-code-reviewer` |
| `mobile-test-engineer` | native subagent | Test strategy, tests, fixtures, determinism, regression evidence, flakiness | Tests only | No | `mobile-code-reviewer` |
| `mobile-security-reviewer` | native subagent | Auth, authorization, secure storage, network security, privacy, permissions, crypto, WebViews, deep links, logs, telemetry, dependency risk | Read-only by default | No | Human for sensitive changes |
| `mobile-ui-accessibility-reviewer` | native subagent | Accessibility, adaptive layouts, orientation, dynamic text, focus, traversal, localization, interaction conventions, UI states | Read-only by default | No | Human for UX or accessibility risk acceptance |
| `mobile-performance-reviewer` | native subagent | Startup, rendering, memory, leaks, battery, background work, network/storage efficiency, binary size, profiling | Read-only by default | No | Human for performance risk acceptance |
| `mobile-release-engineer` | native subagent | Versioning, variants, flavors, schemes, reproducibility, package preparation, signing prerequisites, store readiness | Release metadata/docs only | No | `mobile-security-reviewer`, `mobile-code-reviewer`, human |
| `mobile-code-reviewer` | native subagent | Independent final review of correctness, maintainability, regression risk, errors, conventions, evidence | Read-only | Yes, independent only | Human for unresolved risk |

No implementation role may perform its own independent final review. The `mobile-code-reviewer` must not review changes it authored.

## Delegation Rules

- Select exactly one primary owner per task unless the repository contains multiple mobile technologies that are directly affected.
- Delegate architecture decisions to `mobile-architect` before broad module, navigation, state, dependency, or migration changes.
- Delegate platform code to the matching platform engineer.
- Delegate shared KMP logic only to `kmp-engineer`.
- Delegate test design and regression coverage to `mobile-test-engineer`.
- Delegate read-only security, accessibility, and performance reviews when the task affects their domains.
- Delegate release readiness only to `mobile-release-engineer`, and require human approval for any real signing, credential import, store submission, upload, deployment, distribution, destructive operation, or cost.
- End with `mobile-code-reviewer` for an independent review when implementation changed files.

## Workflow Inventory

These workflows are implemented only as native skills. Slash commands are thin manual entry points that tell Junie to use the matching skill and must not duplicate workflow steps.

| Workflow | Classification | Native location | Primary owner |
|---|---|---|---|
| `create-mobile-project` | native skill | `.junie/skills/create-mobile-project/SKILL.md` | `mobile-architect` |
| `implement-mobile-feature` | native skill | `.junie/skills/implement-mobile-feature/SKILL.md` | Technology-specific engineer |
| `fix-mobile-bug` | native skill | `.junie/skills/fix-mobile-bug/SKILL.md` | Technology-specific engineer |
| `review-mobile-architecture` | native skill | `.junie/skills/review-mobile-architecture/SKILL.md` | `mobile-architect` |
| `add-mobile-screen` | native skill | `.junie/skills/add-mobile-screen/SKILL.md` | Technology-specific UI engineer |
| `integrate-mobile-api` | native skill | `.junie/skills/integrate-mobile-api/SKILL.md` | Technology-specific engineer |
| `add-mobile-tests` | native skill | `.junie/skills/add-mobile-tests/SKILL.md` | `mobile-test-engineer` |
| `optimize-mobile-performance` | native skill | `.junie/skills/optimize-mobile-performance/SKILL.md` | `mobile-performance-reviewer` plus implementer |
| `audit-mobile-security` | native skill | `.junie/skills/audit-mobile-security/SKILL.md` | `mobile-security-reviewer` |
| `prepare-mobile-release` | native skill | `.junie/skills/prepare-mobile-release/SKILL.md` | `mobile-release-engineer` |

## Security Baseline

- Actual secrets, credentials, private keys, certificates, provisioning profiles, keystores, service-account files, local environment files, and signing material are protected data.
- Public mobile client configuration is not automatically a secret, but it must be reviewed for privacy, abuse, endpoint exposure, and environment separation.
- Human approval is required before changing authentication, authorization, privacy declarations, manifests, entitlements, network security config, deep links, WebViews, analytics, telemetry, dependencies, lockfiles, build/signing configuration, external writes, publishing, deployment, credential import, destructive commands, or financial actions.
- Review roles are read-only by default. They may propose patches but must not apply them unless the user explicitly changes the scope.
- Network and meaningful shell actions must remain denied or approval-controlled by default.
- Guards and review procedures must detect malformed input, path traversal, quoted paths, spaces, command chaining, redirection, substitution, encoded commands, POSIX paths, Windows paths, and false positives. Guards must not modify source automatically.

## Completion Standards

For each task, classify criteria as `required`, `conditionally-required`, or `not-applicable`. Every `not-applicable` result needs a concrete reason.

Validate the applicable set:

- Requirements traceability.
- Project configuration.
- Compilation or non-publishing build validation.
- Unit, integration, UI, snapshot, and end-to-end tests.
- Static analysis, lint, and formatting.
- Dependency resolution and dependency risk.
- Secret detection and security review.
- Accessibility, localization, adaptive layouts, orientation, focus, traversal, and complete UI states.
- Performance, memory, battery, background work, binary size, network, storage, and offline behavior.
- Loading, empty, error, retry, cancellation, and recovery states.
- Documentation, warnings, regressions, and independent review.

Technology-specific evidence:

- Android: Gradle tasks, Android lint, manifest and permissions review, unit tests, instrumented or UI tests where available.
- iOS: workspace or project and scheme discovery, non-publishing build or build-for-testing, unit/UI tests, compiler warnings, configured lint, entitlements, privacy declarations, and no real signing credentials.
- KMP: target compilation, source-set dependencies, shared/platform tests, `expect`/`actual`, interoperability, and Compose Multiplatform only when present.
- Flutter: `flutter analyze`, unit/widget/integration tests, non-publishing build validation, flavors, packages, and permissions.
- React Native: type checking, lint, unit/component/end-to-end tests, Metro/package manager, native host builds when available, and bridge review.

## Stop Conditions

Stop and ask the user when the task requires credentials, private data, paid resources, authenticated external writes, destructive operations, publication, signing, store submission, deployment, ambiguous business rules, unsupported native Junie capabilities, or out-of-scope paths.
