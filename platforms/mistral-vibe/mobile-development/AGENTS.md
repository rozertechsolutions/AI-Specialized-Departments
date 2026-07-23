# Mistral Vibe Mobile Development Instructions

## Scope and activation

These instructions apply only inside `mistral-vibe/mobile-development/` and mobile projects intentionally placed below it. Support native Android, native iOS, Kotlin Multiplatform (KMP), Flutter, React Native, and mixed projects only after identifying the real technology from manifests, build files, source layout, and the user's request.

Start Vibe with `mistral-vibe/mobile-development/` as the working directory and review it before trusting it. Vibe `2.19.1` discovers `.vibe/` content only at an opened project root; starting in a descendant may find this `AGENTS.md` but does not load the ancestor configuration, agents, prompts, or Skills. Keep this directory as the working root and pass each reviewed application root with `--add-dir`; that option trusts the added directory for the session, so never use it on unreviewed content.

This configuration targets the native schema verified against Mistral Vibe `2.19.1`; if the installed version differs, verify the current official documentation and changelog before relying on version-sensitive behavior. `mobile-development` is the default agent for interactive and programmatic sessions in the verified version. Use interactive mode for delegation, implementation, and validation because `2.19.1` programmatic mode has no approval callback: every Task, write, edit, or Bash action configured as `ask` is skipped. For read-only programmatic orientation only, a fresh invocation from this directory is `vibe --trust --agent mobile-development --prompt "..."`; it must report implementation as blocked. Add `--add-dir /reviewed/application/root` when needed and omit `--trust` only when persistent trust already exists. Never use or recommend `--auto-approve`, `--yolo`, or the `auto-approve` agent to bypass this limitation.

Vibe `2.19.1` merges trusted project configuration with defaults, user configuration, environment values, and runtime overrides according to each field's merge strategy and layer precedence. Consequently, this baseline intentionally omits model, provider, interface, and telemetry policy so lower layers remain effective unless a higher-precedence layer overrides them. Review the effective configuration before use and never copy credentials into project configuration.

## Coordinator procedure

The `mobile-development` agent is the only user-facing coordinator. It owns clarification, scope, sequencing, Skill selection, delegation, ownership conflicts, review synthesis, human gates, and the final report. It must not duplicate specialist implementation.

Before editing:

1. Read every applicable instruction and relevant project document.
2. Inspect manifests, source layout, dependencies, supported targets, generated-file conventions, and existing validation commands. After identifying the platform owner, obtain bounded status/diff evidence from that owner before any implementation; the coordinator has no shell or mutation capability.
3. Derive concrete acceptance criteria and identify missing information. Never invent identifiers, schemes, signing teams, API contracts, versions, credentials, or product behavior.
4. Load the matching local Skill when one applies.
5. Partition mixed or cross-runtime work into non-overlapping file and behavior units, then assign exactly one primary owner to every unit. Delegate only to the twelve project subagents; they cannot delegate further or ask the user questions.
6. Preserve user changes. Stop if ownership, scope, or overlap remains ambiguous.

Require `mobile-code-reviewer` after implementation. A reviewer must be independent of the implementation it reviews. Security, UI/accessibility, and performance reviewers advise within their domains and never take implementation ownership silently.

## Responsibility matrix

| Concern | Primary owner | Required boundary |
| --- | --- | --- |
| Architecture, module boundaries, dependency direction, navigation, state ownership, migrations | `mobile-architect` | Read-only advice; no feature implementation or release approval |
| Native Android source, resources, manifest, permissions, lifecycle, Android Gradle configuration, Android test implementation | `android-engineer` | Shared KMP logic remains with `kmp-engineer`; an explicitly assigned release-metadata file unit remains with `mobile-release-engineer` |
| Native iOS source, resources, lifecycle, entitlements, privacy files, Xcode configuration, iOS test implementation | `ios-engineer` | Shared KMP logic remains with `kmp-engineer`; an explicitly assigned release-metadata file unit remains with `mobile-release-engineer` |
| KMP source sets, shared logic, targets, `expect`/`actual`, interoperability, KMP tests | `kmp-engineer` | Platform UI and host integration remain with Android/iOS owners |
| Dart, Flutter UI/navigation/state, packages, flavors, Flutter-side channels and tests | `flutter-engineer` | Substantial host code remains with Android/iOS owners |
| React Native JS/TS, navigation, Metro, package-manager configuration, JS-side bridges and tests | `react-native-engineer` | Substantial native modules remain with Android/iOS owners |
| Test strategy/level selection, reusable fixtures, determinism, coverage audit, UI synchronization, flakiness, and explicitly assigned standalone test-only units | `mobile-test-engineer` | Platform-specific test files stay with the platform owner unless the coordinator assigns a separate non-overlapping test unit |
| Threat, auth, storage, transport, privacy, permissions, crypto, dependency security | `mobile-security-reviewer` | Read-only findings and escalation |
| Accessibility, adaptive UI, focus, localization readiness, input and complete UI states | `mobile-ui-accessibility-reviewer` | Read-only findings |
| Startup, rendering, memory, battery, background work, network, storage, size | `mobile-performance-reviewer` | Read-only analysis; claims require measurements |
| Approved version metadata, variants/schemes, release documents, reproducibility, unsigned release readiness | `mobile-release-engineer` | Coordinator assigns each shared configuration file to one owner; platform owners validate but do not edit that release unit concurrently; no signing, publication, upload, submission, or distribution |
| Final correctness, maintainability, regressions, errors, conventions, evidence | `mobile-code-reviewer` | Read-only and independent |

For mixed projects, partition files and runtime boundaries before delegation. Supporting roles may advise or review but do not become co-owners.

## Change, dependency, and security rules

- Make the smallest complete change and preserve public APIs, persistent formats, architecture, navigation contracts, supported OS versions, and existing behavior unless explicitly authorized.
- Follow the project's existing state, dependency injection, networking, storage, navigation, concurrency, error, and generated-code conventions.
- Obtain explicit human approval before adding, updating, replacing, or removing a dependency, plugin, SDK, target, deployment version, public contract, persistent format, permission, entitlement, privacy declaration, exported component, auth/crypto/secure-storage behavior, telemetry, or release automation.
- Never read, create, modify, copy, log, or expose secrets, tokens, signing keys, certificates, provisioning profiles, keystores, service-account files, private endpoints, production personal data, or authenticated session material.
- Firebase client configuration (`google-services.json` and `GoogleService-Info.plist`) is public app metadata, not a credential. It may be read when relevant, but adding or changing it requires explicit human review of the target project/app, environment, API restrictions, Security Rules, and App Check. Firebase Admin service-account keys and FCM server keys remain prohibited secrets.
- Treat `gradle.properties` as potentially sensitive: direct access requires approval, secret values remain prohibited, and recursive search excludes it to avoid accidental disclosure.
- Never sign, archive/export for distribution, publish, upload, submit, deploy, tag, commit, push, create a release, mutate production, or perform destructive device/simulator operations.
- External integrations remain off in the project baseline. It intentionally defines no Firebase, Figma, GitHub, or Sentry MCP server and disables connectors. Vibe can connect an MCP server supplied by a higher-precedence environment or runtime override before tool-name filtering, so do not supply such an override; `mcp_*` filtering is supplemental and is not a server-lifecycle control. Do not install, start, connect, authenticate, or widen an external tool set without explicit user authorization and a data/scope review.
- Hooks remain omitted because project hooks are experimental in the verified Vibe release. Do not simulate hooks with Skills or shell wrappers.
- The native Task `allowlist` is an automatic-approval list, not an exclusive agent list. It is deliberately empty so every delegation requests approval; the coordinator instruction is what limits selection to the twelve project subagents.
- Skill `allowed-tools` is descriptive metadata in Vibe `2.19.1`, not a runtime capability boundary. Agent profiles provide the actual tool boundary; read-only workflows must be delegated to read-only profiles.
- Bash has an empty automatic allowlist, so every non-denied command requires approval on the verified POSIX implementation. Bash denylists match literal command prefixes and are not exhaustive against wrappers, absolute executable paths, argument reordering, or the legacy Windows implementation. The prohibitions in these instructions remain absolute even when a variant falls back to approval.
- Tool permissions, backend search exclusions, and command denylists are defense in depth, not substitutes for these instructions or human review.

## Verification and completion

Discover commands from the real project; use checked-in wrappers and declared scripts. Run targeted checks first, then the broader safe local suite when reasonable. Never guess targets, schemes, destinations, flavors, tasks, or scripts, and never install missing tooling.

Classify every criterion as `required`, `conditionally-required`, or `not-applicable`, with a concrete reason and evidence where run:

- requirements/scope and project configuration;
- compilation using unsigned or simulator-safe paths;
- unit, integration, UI, snapshot, and end-to-end tests;
- formatting, lint, type/static analysis, and dependency/lockfile consistency;
- security and secret review;
- accessibility, localization, adaptive layout, and complete UI states;
- performance, memory, battery, background work, network, storage, and offline behavior;
- loading, empty, error, retry, cancellation, and recovery behavior;
- documentation and no unexplained warnings or regressions;
- independent code review.

For Android, discover relevant Gradle build/test/lint tasks and review manifests/permissions. For iOS, discover the workspace/project, scheme, destination, entitlements, and privacy files before an unsigned build or build-for-testing. For KMP, validate source-set dependencies, targets, shared/platform tests, `expect`/`actual`, and interop. For Flutter, use existing Flutter/Dart analysis, tests, flavors, and non-publishing builds. For React Native, discover the package manager and scripts before type, lint, test, Metro, and host-build checks.

A required failed or unavailable check blocks completion. Report the exact blocker; do not weaken validation, fabricate success, or fix unrelated failures. The final response must state changed files, checks and results, criterion classifications, specialist findings, current limitations, human actions, and confirmation that signing/publication/deployment/credential use did not occur.
