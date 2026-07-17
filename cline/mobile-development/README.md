# Cline Mobile Development Specialization

This specialization uses Cline CLI/SDK project configuration as the canonical repository-versionable baseline for `cline/mobile-development/`.

## Surface Decision

Current Cline documentation supports shared project configuration under `.cline/` for rules, skills, hooks, agents, plugins, and cron. The Rules page also documents `.clinerules/` as the primary workspace rule format across Cline applications. This package keeps one authoritative coordinator rule in `.cline/rules/mobile-development.md` because the Config page confirms `.cline/rules/` for project configuration, and it avoids duplicating the same rule into `.clinerules/`.

The baseline is intentionally not described as identical across VS Code, JetBrains, CLI, SDK, and Kanban. Official docs state that plugins and Agent Teams currently apply to Cline SDK, CLI, and Kanban, and are not applicable to VS Code or JetBrains extensions.

## Capability Matrix

| Capability | Canonical status | Notes |
| --- | --- | --- |
| Rules | Implemented | One project coordinator rule lives at `.cline/rules/mobile-development.md`. `.clinerules/` is documented as the primary cross-application rule location, but is not duplicated here. |
| Skills | Implemented | `.cline/skills/*/SKILL.md` contains the twelve responsibility skills and ten workflow skills. Each directory name matches its `name` frontmatter. |
| Hooks | Omitted | The public Hooks page points to SDK plugin hooks. No stable standalone project hook schema is implemented here. |
| Plugins | Omitted | Project plugins are documented under `.cline/plugins/`, but no plugin is created because guard behavior would require exact SDK hook context and blocking semantics beyond this static package. |
| Project agents | Omitted | The Config page lists `.cline/agents/`, but the inspected docs do not provide a complete stable project-agent schema for twelve least-privilege specialists. |
| Experimental subagents | Documented only | `use_subagents` is read-only research, not twelve write-capable production specialists. |
| Agent Teams | Documented only | CLI/SDK/Kanban feature, not a repository agent schema; no team state is committed. |
| MCP | Omitted | No active or inactive project MCP server configuration is added. MCP remains a manual, explicit approval topic. |
| Commands/workflows | Implemented as skills | No separate workflow file schema is used. The ten reusable processes are workflow skills and release preparation remains manual and non-publishing. |
| `.clineignore` | Implemented | Real secrets, signing material, service accounts, dependencies, caches, build outputs, and binaries are ignored while example environment templates and public mobile client config remain visible. |

## Native Components

- `.cline/rules/mobile-development.md`: coordinator rule for routing, responsibility boundaries, validation gates, and safety policy.
- `.cline/skills/*/SKILL.md`: modular Cline Skills for role guidance and workflow processes.
- `.clineignore`: project ignore rules for sensitive files and generated artifacts.

## Responsibilities

The twelve required responsibilities are represented as focused Cline Skills:

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

The coordinator rule owns routing, overlap prevention, human approval gates, and final independent review requirements. Review roles remain read-only by default.

## Workflow Skills

The ten required reusable processes are represented as workflow Skills:

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

`prepare-mobile-release` is readiness-only. It must not publish, upload, submit, deploy, distribute, spend money, import credentials, or sign with real credentials.

## Security Controls

- `.clineignore` excludes real `.env` files, private keys, certificates, provisioning profiles, keystores, service-account files, dependencies, caches, generated outputs, and large binaries.
- Example environment templates remain visible through negation rules after broad `.env` patterns.
- Public mobile client files such as `google-services.json` and `GoogleService-Info.plist` are not globally ignored; they remain inspectable for review.
- Security-sensitive changes require human approval before edits: authentication, authorization, privacy, manifests, entitlements, network security, deep links, WebViews, analytics, telemetry, dependency or lockfile changes, build/signing configuration, external writes, destructive commands, publishing, credential import, and financial actions.

## Omitted Components

- No `.cline/hooks/` executable hook files are added.
- No `.cline/plugins/` plugin is added.
- No `.cline/agents/` agent definitions are added.
- No `.clinerules/` duplicate rule is added.
- No MCP configuration, connector, schedule, autonomous team state, install script, or external integration is added.

## Manual Runtime Checks

When Cline CLI/SDK is available, manually verify:

- Project rules are discovered from `.cline/rules/mobile-development.md`.
- All Skills in `.cline/skills/` are visible and enabled.
- `.clineignore` keeps real secrets ignored while public client config and example templates remain readable.
- The CLI/SDK behavior matches the documented surface in the installed Cline version.

No tests are included because no executable hooks or plugins are created.

## Official Documentation Consulted

- https://docs.cline.bot/getting-started/config
- https://docs.cline.bot/customization/cline-rules
- https://docs.cline.bot/customization/skills
- https://docs.cline.bot/customization/hooks
- https://docs.cline.bot/customization/plugins
- https://docs.cline.bot/sdk/plugins
- https://docs.cline.bot/features/subagents
- https://docs.cline.bot/cli/agent-teams
- https://docs.cline.bot/cline-overview
