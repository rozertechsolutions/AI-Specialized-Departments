# Warp Mobile Development Rules

## Scope

These project rules apply only inside `warp/mobile-development/` and mobile projects intentionally placed below it. Support Android, iOS, Kotlin Multiplatform, Flutter, and React Native only when the current repository content or user request proves that technology is in scope.

Use Warp-native project rules and skills only:

- Native: `AGENTS.md` project rules.
- Native: `.warp/skills/<workflow>/SKILL.md` reusable workflow skills.
- Conditionally native: `.warp/.mcp.json` project MCP config, only for an authoritative server that is necessary, contains no secrets, and remains subject to explicit Warp startup approval.
- Unsupported in this specialization: generic `agents/`, `subagents/`, `hooks/`, `mcp/`, `skills/`, `workflows/`, cloud schedules, cloud environments, integration triggers, Skills-as-Agents, agent profile files, automatic publication, automatic signing, automatic upload, and external autonomous execution.

Do not create `WARP.md`. Warp recognizes `AGENTS.md` as the default project rules file; `WARP.md` is only backward compatibility and would take priority if both existed.

## Native Surface Verification

Verified against official Warp documentation on 2026-07-15:

- Warp project rules are stored in `AGENTS.md` or backward-compatible `WARP.md`, and `AGENTS.md` is recommended for new projects.
- Warp skills are Markdown files with frontmatter, each in its own subdirectory under a supported project skill path such as `.warp/skills/`.
- Warp project MCP config is `.warp/.mcp.json`; project-scoped servers require explicit approval and do not auto-spawn.
- Warp cloud agents and Oz runs support schedules, integrations, environments, and observable background runs, but those are not repository-local native files for this specialization and must not be simulated here.

If current official Warp documentation contradicts these rules, follow the documentation, make the smallest valid correction, and record the correction in the final report.

## Required Inspection Before Edits

Before changing any mobile project file:

1. Read all applicable `AGENTS.md` files and relevant project documentation.
2. Inspect status, diffs, manifests, build files, package files, source layout, existing tests, and existing conventions.
3. Identify the actual platform, product surface, plan, SDK/toolchain versions, workspace type, and project commands where relevant.
4. Classify each requested capability as `native`, `conditionally-native`, or `unsupported`.
5. Preserve user changes. Stop if the requested edit would overwrite, discard, or ambiguously overlap existing changes.
6. Do not invent bundle identifiers, package names, signing teams, deployment targets, endpoints, credentials, product behavior, or validation results.

## Responsibility Matrix

Exactly one primary owner must be assigned for each work unit. Review roles are read-only unless the user explicitly asks for review-only documentation changes.

| Component | Native form | Exclusive scope | Write permission | Final review allowed |
| --- | --- | --- | --- | --- |
| `mobile-architect` | Rule-defined Warp role | Architecture, modules, dependency direction, state, navigation, shared/platform boundaries, migrations | Advisory by default | No |
| `android-engineer` | Rule-defined Warp role | Android Kotlin/Java, SDK, Compose/Views, lifecycle, resources, manifests, permissions, Gradle, Android tests | Android files only | No |
| `ios-engineer` | Rule-defined Warp role | Swift/Objective-C, SwiftUI/UIKit, Apple APIs, lifecycle, Xcode, schemes, entitlements, resources, localization, iOS tests | Apple files only | No |
| `kmp-engineer` | Rule-defined Warp role | KMP source sets, shared logic, targets, dependencies, `expect`/`actual`, interoperability | Shared KMP files only | No |
| `flutter-engineer` | Rule-defined Warp role | Dart, widgets, navigation, platform channels, packages, flavors, state management, Flutter tests | Flutter files only | No |
| `react-native-engineer` | Rule-defined Warp role | React Native JS/TS, navigation, Metro, package manager, native bridges, RN tests | RN files only | No |
| `mobile-test-engineer` | Rule-defined Warp role | Test strategy, levels, fixtures, determinism, regression coverage, synchronization, flakiness, evidence | Test files only | No |
| `mobile-security-reviewer` | Rule-defined Warp role | Auth, authorization, secure storage, network security, privacy, permissions, crypto, WebViews, deep links, logging, telemetry, dependency risk | Read-only | Yes, security only |
| `mobile-ui-accessibility-reviewer` | Rule-defined Warp role | Accessibility, adaptive layouts, orientation, dynamic text, focus, traversal, localization, UI states | Read-only | Yes, UI/accessibility only |
| `mobile-performance-reviewer` | Rule-defined Warp role | Startup, rendering, memory, leaks, battery, background work, network/storage efficiency, binary size, profiling | Read-only | Yes, performance only |
| `mobile-release-engineer` | Rule-defined Warp role | Versioning, variants, flavors, schemes, reproducibility, package preparation, signing prerequisites, store readiness | Release-prep files only, no credentials | No |
| `mobile-code-reviewer` | Rule-defined Warp role | Independent final review of correctness, maintainability, regression risk, error handling, conventions, evidence | Read-only | Yes, final code review only |

## Component Contract

Every component above uses this contract:

- Mission: complete its exclusive scope without crossing ownership boundaries.
- Inputs: user request, inspected repository files, platform manifests, relevant official docs, project rules, skill instructions, command output, and reviewer findings.
- Preconditions: project scope is clear, target technology is proven, user changes are protected, and required tools are available or their absence is reported.
- Outputs: scoped implementation or findings, files changed or reviewed, evidence, unresolved risks, and required human actions.
- Evidence: exact files, commands, outputs, screenshots or measurements when applicable, and official documentation references for platform-specific behavior.
- Tools: repository reads, safe local edits, project wrappers, declared scripts, static analysis, tests, simulators/emulators only when safe and available, and official documentation.
- Permissions: least privilege; project-local reads and scoped edits only. External writes, credentials, signing, publication, destructive operations, dependency changes, and MCP activation require explicit human approval.
- Dependencies: existing project dependencies and declared tooling only unless the user approves a change.
- Invocation: route by deterministic platform ownership. Use one primary owner and relevant reviewers. Do not create separate project agent files.
- Delegation: implementation owners may request reviewer findings; reviewers do not implement fixes and do not review their own implementation.
- Stop conditions: ambiguous requirements, unsupported native surface, missing required tools, conflicting user changes, security uncertainty, production or paid service access, credentials, signing, publication, destructive operations, or unrelated validation failures.
- Errors: report command, failure, affected criteria, likely cause, and safe next options. Do not hide failures with broad catches or arbitrary defaults.
- Fail-safe behavior: stop before risk, preserve files, keep integrations inactive, keep credentials out of source, and report unavailable infrastructure as unavailable.
- Completion criteria: all required criteria pass, conditional criteria are justified, not-applicable criteria have concrete reasons, independent review is complete, and no prohibited action occurred.
- Human review: required for permissions, entitlements, privacy manifests, network security, exported components, signing config, release automation, auth, crypto, secure storage, telemetry, dependencies, lockfiles, external writes, publishing, deployment, credential import, destructive commands, and financial actions.
- Prohibited actions: real signing, publishing, submitting, distributing, uploading artifacts or symbols, using production credentials, modifying signing credentials, destructive simulator/device operations, fabricated evidence, out-of-scope edits, and self-review.

## Platform Routing

- Android files route to `android-engineer`.
- Native Apple files route to `ios-engineer`.
- Shared KMP source sets and Gradle shared logic route to `kmp-engineer`.
- Flutter files route to `flutter-engineer`.
- React Native JS/TS, Metro, and RN package files route to `react-native-engineer`.
- Tests route to `mobile-test-engineer` after the implementation owner defines the behavior under test.
- Architecture, security, UI/accessibility, performance, release, and code review roles are invoked only when the change affects their scope.
- If multiple frameworks coexist, partition ownership by runtime boundary before editing.

## Security Baseline

Protect actual secrets, credentials, private keys, certificates, provisioning profiles, keystores, service-account files, local environment files, and signing material. Public mobile client configuration can be present only when the platform treats it as public and the project already follows that convention.

Never add real endpoints, tokens, passwords, certificates, signing keys, private URLs, production personal data, or authenticated session material. Never activate, trust, approve, authenticate, start, or connect MCP servers or external integrations by default.

Executable guard logic, when requested, must validate malformed input, path traversal, quoted paths, spaces, shell chaining, redirection, substitution, encoded commands, POSIX paths, Windows paths, and false positives. Guards must report findings and must not automatically modify source.

## Validation Standards

Discover commands from the repository. Prefer wrappers and declared scripts. Do not guess schemes, destinations, flavors, targets, workspaces, or scripts.

Classify completion criteria:

- Required: directly affected behavior, project configuration, compile/build on an unsigned or simulator-safe path, relevant tests, lint/type/static analysis, formatting, dependency consistency, secret review, and independent code review.
- Conditionally required: UI/accessibility, localization, adaptive layout, performance, memory, battery, network, storage, offline behavior, loading/empty/error/retry/cancellation/recovery states, documentation, and release checks when the change touches those surfaces.
- Not applicable: criteria unrelated to the detected platform or unchanged behavior, with a concrete reason.

Unavailable infrastructure must be reported as unavailable, never passed. Do not claim improvement without measurements. Do not weaken validation to make checks pass.

## Completion Report

Every completed workflow must report:

- Verified Warp version or surface and official documentation consulted.
- Files created, modified, migrated, removed, and omitted.
- Native capabilities used and unsupported capabilities omitted.
- Primary owner, reviewers, responsibility boundaries, and workflows used.
- Security controls and MCP/connectors decision.
- Validation evidence, including commands run and results.
- Corrections made during review.
- Remaining limitations and required human actions.
- Confirmation that no secret, active integration, publication, signing, upload, deployment, destructive action, or out-of-scope modification occurred.
