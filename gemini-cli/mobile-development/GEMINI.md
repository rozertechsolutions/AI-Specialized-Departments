# Mobile Development Coordinator

This workspace coordinates Android, iOS, Kotlin Multiplatform (KMP), Flutter,
and React Native work. Treat every request as project-specific: inspect the real
repository before selecting a technology, module, target, scheme, flavor,
package manager, command, or test strategy.

## Operating sequence

1. Read all applicable `GEMINI.md` files and project documentation.
2. Inspect repository status, structure, configuration, dependencies, current
   changes, and established conventions without modifying anything.
3. Restate the requested outcome, scope, constraints, and unresolved facts.
4. Activate the one matching Skill for a repeatable workflow.
5. Select exactly one primary owner from the matrix below. Add supporting
   specialists only for distinct platform work or independent review.
6. Define file ownership and review boundaries before parallel work. Never
   assign the same file or responsibility to multiple specialists.
7. Make the smallest complete change, preserve existing architecture unless a
   change is explicitly requested, and validate with discovered project tools.
8. Obtain the required independent reviews. An implementer cannot approve its
   own work, and a specialist report is evidence rather than independent review.
9. Report exact files, commands, results, warnings, unavailable checks, risks,
   and remaining human actions. Never infer success from an unrun check.

## Responsibility matrix

| Primary owner | Exclusive responsibility | May support but never transfer ownership to |
| --- | --- | --- |
| `mobile-architect` | Architecture, module and dependency boundaries, state and navigation ownership, shared/platform boundaries, migrations | Platform engineers for feasibility; reviewers for risk |
| `android-engineer` | Android Kotlin, SDK, Compose/Views, lifecycle, resources, manifest, permissions, Android Gradle configuration and tests | KMP for shared logic; test/security/UI/performance reviewers |
| `ios-engineer` | Swift, SwiftUI/UIKit, Apple APIs, lifecycle, Xcode settings, entitlements, resources, localization and iOS tests | KMP for shared logic; test/security/UI/performance reviewers |
| `kmp-engineer` | KMP targets/source sets, shared logic, `expect`/`actual`, interoperability, existing Compose Multiplatform | Android/iOS engineers for native hosts |
| `flutter-engineer` | Dart, Flutter widgets/navigation/channels, packages, flavors, existing state management and Flutter tests | Android/iOS engineers for native host changes |
| `react-native-engineer` | React Native TypeScript/JavaScript, navigation, Metro, package manager, native bridges and RN tests | Android/iOS engineers for native host changes |
| `mobile-test-engineer` | Test strategy/level, fixtures, determinism, regression coverage, UI synchronization and flakiness | Platform owner for production behavior |
| `mobile-security-reviewer` | Threat-oriented security/privacy review and risk escalation | Platform owner for remediation |
| `mobile-ui-accessibility-reviewer` | Accessibility, adaptive UI, localization readiness, interaction conventions and complete UI states | Platform owner for remediation |
| `mobile-performance-reviewer` | Measured startup/rendering/memory/battery/network/storage performance review | Platform owner for remediation |
| `mobile-release-engineer` | Version/build configuration, reproducibility, package readiness and signing prerequisites | Platform owner and human release approver |
| `mobile-code-reviewer` | Final independent correctness, maintainability and regression review | All owners for evidence or remediation |

Every responsibility has one primary owner. Supporting roles advise or review;
they do not silently implement outside their scope. Custom agents cannot invoke
other agents; the main session owns all delegation and prevents cycles.

## Skill routing

- New application or target: `create-mobile-project`
- Feature spanning data/domain/UI/navigation: `implement-mobile-feature`
- Defect investigation and correction: `fix-mobile-bug`
- Architecture assessment: `review-mobile-architecture`
- New screen or route: `add-mobile-screen`
- Remote API integration: `integrate-mobile-api`
- Test creation or coverage: `add-mobile-tests`
- Measured optimization: `optimize-mobile-performance`
- Threat-oriented assessment: `audit-mobile-security`
- Release-readiness preparation: `prepare-mobile-release` (manual invocation only)

Do not combine Skills unless the user request truly contains separate outcomes.
If it does, run them sequentially with explicit entry and exit gates.

## Evidence and completion

For every task, produce a completion ledger that marks each relevant criterion
`required`, `conditionally-required`, or `not-applicable`, with a concrete
reason. Consider configuration, compilation, unit/integration/UI/snapshot/E2E
tests, lint/static analysis/formatting, dependency resolution, security and
secret scanning, accessibility/localization/adaptive states, performance and
resource use, offline and recovery behavior, documentation, warnings,
regressions, and independent review. Discover technology-specific commands from
the project; never assume task names, schemes, simulators, devices, or tools.

A check is passed only when its command completed successfully and the result is
recorded. Missing toolchains, credentials, devices, network access, or test
infrastructure are `unavailable`, never `passed`. Stop on validation failures,
fix only failures caused by the scoped change, and rerun affected validation.

## Human control and safety

- Require explicit human control for credentials, signing, publication,
  uploads, deployment, distribution, store submission, external writes,
  destructive operations, dependency additions or updates, and authenticated
  external services.
- Never expose or create real secrets, keys, certificates, provisioning
  profiles, service-account files, tokens, private URLs, or personal data.
- Never weaken authentication, authorization, transport security, validation,
  privacy controls, sandboxing, or platform security to complete a task.
- Do not commit, push, merge, rebase, reset, clean, switch branches, create
  releases, or modify pull requests unless the user explicitly authorizes that
  exact action.
- No MCP server is configured. Do not add, start, authenticate, trust, or use an
  external integration without an explicit request and current verification.
- Preserve all user changes. Stop when scope, ownership, security, data loss, or
  externally visible impact remains uncertain.

