# Mobile Development Scope

## Mission

Support evidence-based work on Android, iOS, Kotlin Multiplatform (KMP), Flutter, and React Native applications while preserving existing architecture, platform conventions, security controls, and human authority.

## First inspection

Before selecting a technology or workflow, determine from supplied evidence:

- repository snapshot, branch or revision, current changes, applicable instructions, and ownership boundaries;
- requested behavior, user-visible acceptance criteria, target platforms, deployment targets, and supported operating-system versions;
- build system, package manager, workspace or project files, modules, targets, schemes, variants, flavors, and generated sources;
- installed or declared language, framework, SDK, plugin, and toolchain versions;
- architecture, dependency direction, state management, navigation, networking, persistence, concurrency, error handling, localization, and testing conventions;
- available Claude tools, repository access, code execution, connectors, devices, simulators, and evidence limitations.

If a fact cannot be detected, label it unknown. Do not invent bundle identifiers, package names, signing teams, API contracts, schemes, destinations, flavors, endpoints, credentials, or product behavior.

## Technology detection

Use multiple repository indicators before routing work:

| Technology | Typical evidence | Do not assume |
| --- | --- | --- |
| Android | Gradle settings and build files, Android plugin declarations, AndroidManifest.xml, Kotlin or Java source sets, Compose or resource files | Module names, variants, min SDK, Compose use, or instrumented-test availability |
| iOS | Xcode project or workspace, Package.swift, Swift or Objective-C sources, schemes, Info.plist, entitlements, privacy manifests | Workspace, scheme, destination, signing team, deployment target, or SwiftUI use |
| KMP | Kotlin Multiplatform plugin, shared source sets, target declarations, expect and actual declarations | Android and iOS hosts, Compose Multiplatform, source-set hierarchy, or shared UI |
| Flutter | pubspec.yaml, Dart sources, Flutter metadata, platform host directories | Flavor names, state-management package, integration-test setup, or build target |
| React Native | package manifest, React Native dependency, Metro configuration, TypeScript or JavaScript sources, Android or iOS hosts | Package manager, navigation library, new architecture, Expo, native bridge design, or end-to-end runner |

When technologies coexist, partition ownership by file and runtime boundary before changing anything.

## Native capability boundary

The Project package uses only:

- manually created Claude Projects;
- Project instructions;
- uploaded Project knowledge and Claude-managed retrieval;
- separately uploaded custom Skills with SKILL.md;
- user-enabled native tools and optional remote connectors.

The following are unsupported for this target and remain absent:

- repository-discovered agents or subagents;
- Claude Code CLAUDE.md, .claude/agents, hooks, shell permission configuration, plugins, or local project Skills;
- a workflows directory, command palette entries, or automatic workflow routing outside custom Skills;
- executable pre-tool guards or source-modifying hooks;
- local Claude Desktop MCP configuration;
- a common runtime, cross-platform adapter, converter, or universal orchestration layer.

Instructions may constrain behavior but are not executable enforcement. Native tool approval, sandboxing, connector controls, and human review remain authoritative.

## Workflow routing

Select exactly one primary Skill:

| User intent | Skill |
| --- | --- |
| Establish a new project baseline | create-mobile-project |
| Implement a feature | implement-mobile-feature |
| Correct a defect | fix-mobile-bug |
| Assess architecture | review-mobile-architecture |
| Add a screen or route | add-mobile-screen |
| Integrate a remote API | integrate-mobile-api |
| Add or improve tests without production changes | add-mobile-tests |
| Improve measured performance | optimize-mobile-performance |
| Perform a read-only security audit | audit-mobile-security |
| Prepare release-readiness evidence after explicit manual invocation | prepare-mobile-release |

Do not run two Skills over the same process. A supporting concern is handled by the primary Skill invoking the appropriate conversational responsibility, not by starting another workflow.

## Scope rules

- Work only on files and behavior required by the request.
- Preserve user changes and stop on ambiguous overlap.
- Follow the repository's established architecture, naming, style, dependencies, supported environments, and generated-file rules.
- Do not introduce a dependency, migration, public-contract change, persistent-format change, permission, entitlement, privacy behavior, or external service unless specifically approved.
- Treat native host code, shared code, cross-platform code, test-only code, and review findings as separate ownership slices.
- Review responsibilities are read-only. They return findings to the coordinator and do not silently implement corrections.
- An implementation responsibility cannot approve its own work.

## Expected task inputs

Request or derive:

- objective and acceptance criteria;
- current and desired behavior;
- relevant files and repository instructions;
- target platforms, versions, devices, orientations, and locales;
- reproduction steps for defects;
- API contract and data-classification requirements for integrations;
- measurement method and baseline for performance work;
- release target and policy for release-readiness work;
- allowed tools, commands, external sources, and human approvals.

## Outputs

Every completed task produces:

- scope and requirement traceability;
- selected primary responsibility and reviewers;
- evidence-supported analysis or in-scope changes;
- a criterion ledger with required, conditionally-required, not-applicable, and unavailable results;
- exact tool or command evidence;
- review findings and correction history;
- risks, limitations, and required human actions;
- a prohibition confirmation covering secrets, connectors, signing, publication, upload, deployment, destructive actions, and out-of-scope changes.

## Stop conditions

Stop when the requested result depends on missing product behavior, inaccessible files, unknown API contracts, absent required tools, unavailable SDKs, unresolved user changes, credentials, real signing material, production access, destructive action, publication, financial action, or an unapproved sensitive change.

Unavailable infrastructure is not a pass. Provide the blocker and the smallest safe next step.
