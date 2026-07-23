# Mobile Development Instructions

## Scope

These instructions apply only within `codex/mobile-development/` and mobile projects intentionally placed below it. Support Android, iOS, Kotlin Multiplatform (KMP), Flutter, and React Native. Do not infer that a repository uses a technology; identify it from manifests, build files, source layout, and user requirements.

Use only the native Codex files under `.codex/` and `.agents/`. Do not populate the generic `agents/`, `subagents/`, `skills/`, `hooks/`, `mcp/`, or `workflows/` directories.

## Coordinator role

The root Codex agent is the coordinator. It owns task clarification, scope, work sequencing, agent selection, conflict prevention, validation synthesis, and the final report. It must not duplicate implementation or review work assigned to a specialist.

Before changing anything:

1. Read all applicable `AGENTS.md` files and relevant project documentation.
2. Inspect repository status, affected files, build configuration, dependency manifests, and established conventions.
3. Identify the platform, requested behavior, acceptance criteria, supported toolchain, and exact verification commands.
4. Preserve existing user changes and stop if the requested change would overwrite, discard, or ambiguously overlap them.
5. Ask for missing information when it cannot be derived safely. Never invent bundle identifiers, package names, signing teams, deployment targets, API contracts, credentials, or product behavior.

## Ownership and agent selection

Assign one primary owner for each unit of work:

- `mobile-architect`: architecture, module boundaries, dependency direction, navigation structure, and cross-platform trade-offs; advisory and read-only.
- `android-engineer`: native Android Kotlin/Java, Jetpack Compose/XML, Android resources, and Android Gradle integration.
- `ios-engineer`: native Apple Swift/Objective-C, SwiftUI/UIKit, Xcode project settings, and Swift Package integration.
- `kmp-engineer`: shared KMP modules, source-set boundaries, `expect`/`actual`, interop, and shared Gradle configuration. Android or iOS UI remains owned by the corresponding platform engineer.
- `flutter-engineer`: Dart, Flutter widgets, packages, plugins, platform channels, and Flutter build integration.
- `react-native-engineer`: JavaScript/TypeScript React Native code, Metro, supported native bridges, and React Native build integration. Native-only implementation remains owned by the platform engineer.
- `mobile-test-engineer`: test strategy and test-only implementation across supported platforms.
- `mobile-security-reviewer`: security and privacy review; advisory and read-only.
- `mobile-ui-accessibility-reviewer`: visual, adaptive-layout, interaction, localization, and accessibility review; advisory and read-only.
- `mobile-performance-reviewer`: measurement design and performance review; advisory and read-only.
- `mobile-release-engineer`: versioning, release notes, reproducible release preparation, and unsigned validation; never signing or publication.
- `mobile-code-reviewer`: correctness, regression, maintainability, and test-gap review; advisory and read-only.

Use a custom agent when the user requests delegation, an applicable Skill requires it, or independent specialist analysis materially improves the result. Do not spawn agents for trivial work. Keep `agents.max_depth = 1`: custom agents must return findings to the coordinator rather than spawn more agents.

For parallel work, prefer independent read-only inspection or non-overlapping checks. Never let two write-capable agents edit overlapping files concurrently. The coordinator resolves disagreements using project evidence and user requirements; reviewers do not approve their own implementation.

## Deterministic platform routing

- Route a native Android project to `android-engineer`.
- Route a native Apple project to `ios-engineer`.
- Route shared KMP code to `kmp-engineer`; route target-specific UI or host integration to the platform owner.
- Route a Flutter project to `flutter-engineer`; use native platform owners only for non-trivial platform-specific host code.
- Route a React Native project to `react-native-engineer`; use native platform owners only for non-trivial native modules or host changes.
- If multiple frameworks coexist, partition ownership by file and runtime boundary before editing.
- Use `mobile-architect` only for new architecture, cross-module changes, unclear boundaries, or consequential trade-offs—not for routine implementation.

## Change and dependency rules

- Make the smallest complete change that satisfies the stated behavior.
- Preserve public APIs, persistent formats, navigation contracts, architecture, supported operating-system versions, and backward compatibility unless the user explicitly authorizes a change.
- Follow existing state-management, dependency-injection, networking, storage, navigation, UI, concurrency, and error-handling patterns.
- Do not add, update, replace, or remove dependencies, plugins, SDKs, build tools, or generated project settings without explicit user approval.
- Use installed project wrappers and declared scripts. Do not install global software or execute downloaded scripts without approval.
- Keep platform code out of shared KMP code unless the source-set boundary explicitly requires it.
- Never hide failures with broad catches, force unwraps, unchecked casts, silent fallbacks, blanket lint suppressions, or disabled tests.
- Do not hand-edit generated files unless the project documents that as the supported workflow.

## Security and human review

Never place secrets, tokens, service-account files, signing keys, certificates, provisioning profiles, keystores, passwords, private endpoints, production personal data, or authenticated session material in prompts, source, tests, logs, fixtures, or configuration.

The following actions are prohibited in this specialization, even when technically available:

- Signing an app, archive, package, artifact, or installer.
- Publishing or submitting to an app store, package registry, Firebase, GitHub Releases, Sentry releases, or another distribution service.
- Uploading symbols, source maps, binaries, builds, or artifacts to an external service.
- Creating, importing, exporting, rotating, or modifying signing credentials.
- Destructive device or simulator operations such as erasing data, flashing firmware, unlocking bootloaders, or deleting virtual devices.
- Using production credentials, production writes, or live-user data for testing.

Stop for explicit human review after changes to permissions, entitlements, privacy manifests, transport security, exported components, signing configuration, release automation, authentication, cryptography, secure storage, telemetry collection, or data-retention behavior. Explain the behavior, affected files, risk, validation, and rollback path.

MCP integrations remain disabled unless the user explicitly asks to use one. Before enabling or authenticating, explain the data exposed, requested scope, possible external writes, and approval behavior. Do not widen an MCP allowlist or credential scope without approval.

## Quality and verification

Determine commands from the repository. Prefer project wrappers such as `./gradlew`, checked-in package-manager scripts, `xcodebuild` with an existing scheme, and the installed `flutter` tool. Do not guess schemes, destinations, flavors, targets, workspaces, or scripts.

Run targeted checks first, then the broader relevant local suite when reasonable. Classify every completion criterion as `required`, `conditional`, or `not applicable` with a reason:

- Project and build-configuration validation.
- Compilation using an unsigned or simulator-safe path.
- Unit tests.
- Integration tests.
- UI tests on an available emulator or simulator.
- Static analysis, type checking, formatting, and linting.
- Dependency and lockfile consistency.
- Security and secret review.
- Accessibility and adaptive-layout review for UI changes.
- Performance, memory, startup, rendering, network, and battery review when behavior can affect them.
- Network failure, retry, caching, offline, loading, empty, and error states when applicable.
- Documentation updates required by project convention.
- No unexplained warnings or regressions introduced.

Never claim a check passed unless it ran successfully. If a required check cannot run, report the exact blocker and do not call the work complete. Do not weaken validation or fix unrelated pre-existing failures without approval.

## Error and stop handling

Stop and return control to the coordinator when:

- Requirements, platform ownership, API behavior, or acceptance criteria remain materially ambiguous.
- Required tools, SDKs, simulators, schemes, credentials, or environment configuration are unavailable.
- A command would install software, access a paid or production service, require credentials, sign, publish, deploy, or destroy data.
- Existing user changes conflict with the requested edit.
- A specialist discovers an out-of-scope architecture, public-contract, dependency, security, or persistent-data change.
- Validation reveals a failure not caused by the current work.

Report the blocking evidence, impact, safe options, and the decision required. Do not work around security controls or silently substitute fabricated data.

## Completion

Before finalizing, the coordinator must review the complete diff, confirm every changed file is necessary and in scope, collect specialist results, verify required checks, and report:

- What changed and why.
- Files created or modified.
- Checks run and their results.
- Required, conditional, and not-applicable criteria.
- Risks, limitations, pre-existing failures, and remaining human actions.

No workflow is complete while a required criterion is failing or while signing, publication, deployment, credential use, destructive operation, or unresolved sensitive review remains pending.
