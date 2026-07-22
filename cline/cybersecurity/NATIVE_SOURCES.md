# Native Sources

Documentation review date: 2026-07-22.

Product surface: Cline IDE extension, TUI, CLI, `AGENTS.md` Rule sources, `.clinerules/workflows/` custom workflows, `.cline/skills/` Skills, hooks when separately configured, Cline-managed read-only subagents, Agent Teams on supported SDK/CLI/Kanban surfaces, MCP configuration when separately approved, and approval controls.

Official source evidence checked or retained for this platform:

- https://docs.cline.bot/cline-overview
- https://docs.cline.bot/getting-started/config
- https://docs.cline.bot/features/subagents
- https://docs.cline.bot/cli/agent-teams
- https://docs.cline.bot/customization/cline-rules
- https://docs.cline.bot/customization/skills
- https://docs.cline.bot/core-workflows/using-commands
- https://docs.cline.bot/customization/hooks
- https://docs.cline.bot/mcp/mcp-overview
- https://docs.cline.bot/tools-reference/all-cline-tools
- https://docs.cline.bot/usage/cli-overview

Validation method:

- Inventory of `cline/cybersecurity/` files and native support directories.
- Static syntax parsing for JSON, TOML, YAML where applicable.
- Reference resolution for retained repository-local `AGENTS.md` baselines, custom workflows, Skills, and config files where applicable.
- Removal of redundant area-level source copies after this platform-wide source file replaced them.
- Documentation comparison across Cline configuration, subagent, Agent Teams, Rules, Skills, commands, hooks, MCP, tools, CLI, and overview pages.

Current native facts recorded:

- Project paths: `cline/cybersecurity/<area>/` for all eight Cybersecurity areas.
- Discovery: Cline documents `AGENTS.md` and `.clinerules/` as Rule sources, custom workflows under `.clinerules/workflows/`, project Skills, hooks, MCP, plugins, and CLI/TUI usage. This package treats each area directory as the effective Cline workspace root for area isolation.
- Canonical baseline: `AGENTS.md` is retained as the single always-on area instruction file. The previous duplicate rule copies were removed.
- Workflows: custom workflow Markdown is retained under `.clinerules/workflows/*.md`. The previous workflow location was removed.
- Skills: project Skills remain under `.cline/skills/<skill>/SKILL.md`; workflows and Skills are distinct native entry points.
- Subagents: Cline-managed `use_subagents` workers are experimental, read-only research workers. They can read, list, search, run restricted read-only commands, and use Skills. They cannot write, use browser/web search, access MCP, or spawn nested subagents.
- Agent Teams: available for Cline SDK, CLI, and Kanban; not applicable to VS Code or JetBrains extensions according to the current Agent Teams page.
- Permissions: read-only/static by default; shell, network, MCP, connector, hosted tool, scanner, deployment, and production actions absent or denied unless a human explicitly configures them outside this baseline. Cline approval settings and auto-approval remain user/platform controls.
- Trust: repository-local configuration is effective only when the platform trusts or imports the project according to its current documentation.
- Precedence: nearest area-level `AGENTS.md`, workflows, and Skills govern the selected work; platform-level README and this file provide package-wide evidence.
- Omitted mechanisms: fake MCP servers, generated live hooks, external endpoints, credentials, cloud actions, scanners, and deployment automation are intentionally omitted.

Removed or deprecated field handling:

- Unsupported descriptive-only metadata is not treated as a permission control.
- Duplicate rule copies were removed in favor of `AGENTS.md`.
- Workflow files were migrated to `.clinerules/workflows/*.md`.
- `.cline/agents/*.md` files are omitted. The current official documentation checked for this remediation does not establish that path as a repository-native declarative custom-agent format for project-defined named subagents.
- Platform-specific frontmatter and config fields must be verified against current vendor documentation before use.
- For SDK packages, runtime API compatibility must be validated in an isolated environment without model calls before production use.
