# Cline Mobile Development Specialization

This specialization is implemented for Cline project configuration under `cline/mobile-development/`.

## Verified Surface

- Product surface: Cline project configuration for IDE, CLI, and SDK compatible workspaces.
- Local detection: `cline` was not installed on `PATH`, so an installed local Cline version, plan, and workspace account type could not be verified.
- Official documentation consulted on 2026-07-15:
  - `https://docs.cline.bot/getting-started/config`
  - `https://docs.cline.bot/customization/cline-rules`
  - `https://docs.cline.bot/customization/skills`
  - `https://docs.cline.bot/customization/hooks`
  - `https://docs.cline.bot/customization/clineignore`
  - `https://docs.cline.bot/features/subagents`
  - `https://docs.cline.bot/mcp/mcp-overview`
  - `https://docs.cline.bot/sdk/plugins`

## Native Components

| Component | Classification | Reason |
| --- | --- | --- |
| `.cline/rules/mobile-development.md` | native | Cline project rules are documented project configuration. |
| `.cline/skills/*/SKILL.md` | native | Project skills under `.cline/skills/` with YAML frontmatter are documented. |
| `.clineignore` | native | Cline documents `.clineignore` at the project root using gitignore syntax. |
| Ten workflow process skills | native | Current official workflow URL redirects to rules; workflow files are not documented as stable project files, so the strongest stable reusable mechanism is Cline Skills. |

## Unsupported Or Omitted Components

| Component | Classification | Reason |
| --- | --- | --- |
| Production implementation subagents | unsupported | Cline subagents are documented as experimental and read-only research agents. |
| Project agent definitions for the twelve roles | unsupported | Current public docs list `.cline/agents/` but do not provide a stable project-scoped agent schema. |
| Standalone project workflow files | unsupported | Current workflow documentation redirects to rules and no stable project workflow schema was available. |
| Standalone executable hook scripts | unsupported | Current hooks page points to SDK plugin hooks; no stable `.cline/hooks` file schema was available. |
| MCP server configuration | unsupported for default activation | MCP requires explicit server configuration and credentials; no inactive project MCP state was present. |

## Rules Location Decision

Current Cline documentation is not worded identically across pages: the Rules page describes `.clinerules/` as the primary workspace rule format, while the Config page lists `.cline/rules/` as the project-level configuration location. This specialization targets the stable project configuration surface, so it keeps a single coordinator rule in `.cline/rules/mobile-development.md` and does not duplicate it into `.clinerules/`.

## Responsibilities Implemented

The twelve required responsibilities are implemented as focused Cline skills:

1. `mobile-architect`
2. `android-engineer`
3. `ios-engineer`
4. `kmp-engineer`
5. `flutter-engineer`
6. `react-native-engineer`
7. `mobile-test-engineer`
8. `mobile-security-reviewer`
9. `mobile-ui-accessibility-reviewer`
10. `mobile-performance-reviewer`
11. `mobile-release-engineer`
12. `mobile-code-reviewer`

The coordinator rule owns routing, overlap prevention, delegation, human approval gates, and final independent review requirements.

## Workflows Implemented

The ten required processes are implemented as workflow-specific Cline skills:

1. `create-mobile-project`
2. `implement-mobile-feature`
3. `fix-mobile-bug`
4. `review-mobile-architecture`
5. `add-mobile-screen`
6. `integrate-mobile-api`
7. `add-mobile-tests`
8. `optimize-mobile-performance`
9. `audit-mobile-security`
10. `prepare-mobile-release`

Each workflow skill defines objective, trigger, inputs, supported technologies, preconditions, owner, reviewers, ordered and conditional steps, validation gates, failures, stop conditions, evidence, outputs, acceptance criteria, human approvals, and prohibited actions.

## Security Controls

- Secrets, signing material, private service accounts, generated outputs, dependencies, and large binaries are excluded through `.clineignore`.
- Security-sensitive changes require human approval before edits: authentication, authorization, privacy, manifests, entitlements, network security, deep links, WebViews, analytics, telemetry, dependency and lockfile changes, build/signing configuration, external writes, destructive commands, publishing, credential import, and financial actions.
- Review roles are read-only by default and cannot self-approve implementation work.
- Public mobile client configuration is not automatically treated as a secret, but it must be reviewed for private endpoints, embedded credentials, or privileged keys.
- Because standalone executable hooks are not documented as a stable project format, guard behavior is implemented as mandatory rule and skill gates, not as simulated hook files.

## Completion Criteria Classification

| Criterion | Classification | Reason |
| --- | --- | --- |
| Requirements traceability | required | Every task must map requested behavior to owner, files, evidence, and acceptance criteria. |
| Project configuration discovery | required | Commands and project structure must be discovered before use. |
| Compilation/build validation | conditionally-required | Required when the target mobile project has build tooling available. |
| Unit/integration/UI/snapshot/E2E tests | conditionally-required | Required when the project has the relevant test layer or the change affects that layer. |
| Static analysis, lint, formatting | conditionally-required | Required when configured by the project. |
| Dependency resolution | conditionally-required | Required when dependencies or lockfiles are involved. |
| Secret detection and security review | required | Always required before completion. |
| Accessibility, localization, adaptive layout | conditionally-required | Required for UI or user-facing changes. |
| Performance, memory, battery, network, storage | conditionally-required | Required when performance-sensitive areas are changed or optimization is requested. |
| Offline/loading/empty/error/retry/cancel/recovery states | conditionally-required | Required for user workflows, API flows, and async behavior. |
| Documentation | conditionally-required | Required when public behavior, setup, commands, or contracts change. |
| Independent review | required | The final review must be performed by `mobile-code-reviewer` and cannot be done by the implementation owner. |
| Publication, signing, upload, deployment | not-applicable | Explicitly prohibited unless a human separately initiates and approves non-publishing validation. |

## Validation Evidence

- Inspected `cline/mobile-development/`; it contained only empty scaffold directories before implementation.
- Verified `cline` was not available on `PATH`; version and plan are unavailable locally.
- Confirmed current official documentation supports project `.cline/` rules and skills plus root `.clineignore`.
- Confirmed current official documentation does not provide stable project schemas for production subagents, standalone workflow files, or standalone hook scripts.

No secrets, active integrations, publication, signing, upload, deployment, destructive action, or out-of-scope platform modification were introduced.
