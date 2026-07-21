# Native Sources

Documentation review date: 2026-07-21.

Product surface: OpenCode CLI with `AGENTS.md`, `opencode.jsonc`, `.opencode/agents/`, `.opencode/commands/`, `.opencode/skills/`, permissions, and MCP configuration.

## Official Source Checks

### Check 1 - Current reference documentation

- Config: https://opencode.ai/docs/config/
- Rules: https://opencode.ai/docs/rules/
- Agents: https://opencode.ai/docs/agents/
- Commands: https://opencode.ai/docs/commands/
- Agent Skills: https://opencode.ai/docs/skills/
- Permissions: https://opencode.ai/docs/permissions/
- MCP servers: https://opencode.ai/docs/mcp-servers/

### Check 2 - Release notes or current behavior notes

- Current docs state that legacy boolean `tools` config is deprecated as of OpenCode `v1.1.1` and merged into `permission`.
- Current docs state that configuration files are merged rather than replaced, with later configs overriding conflicting keys.
- Current docs state that auto mode does not override explicit `deny` permissions.

### Check 3 - Current package, schema, or parser behavior

- Current schema URL: https://opencode.ai/config.json.
- OpenCode supports JSON and JSONC config formats.
- Project config is loaded from the project root and `.opencode` directories provide agents, commands, and plugins.
- Markdown agents support frontmatter fields including `description`, `mode`, `model`, `temperature`, and `permission`.
- Permissions resolve to `allow`, `ask`, or `deny`.

## Current Native Facts

- Area path: `opencode/cybersecurity/<area>/`.
- Primary rules: `AGENTS.md`.
- Area config: `opencode.jsonc`.
- Agents: `.opencode/agents/*.md`.
- Commands: `.opencode/commands/*.md`.
- Skills: `.opencode/skills/*/SKILL.md`.
- MCP: `mcp` is `{}` in every area config.
- Discovery: start OpenCode from the selected area directory.

## Discovery, Precedence, And Trust

- Rule files are found by traversing upward from the current directory; local `AGENTS.md` wins over compatible fallback rule files at the same level.
- Config files are merged from remote, global, custom env, project config, `.opencode` directories, and inline env content.
- Later config overrides conflicting keys, but non-conflicting upstream settings are preserved.
- Because the intended launch root is `opencode/cybersecurity/<area>/`, each area retains its own `opencode.jsonc` so the area config is available when launched directly.
- Runtime trust and provider authentication remain user-controlled outside this repository.

## File Classification

- Retained: eight `AGENTS.md` files, eight `opencode.jsonc` files, 41 Markdown agents, 38 custom command files, and 53 Skills.
- Retained Skill variants without command references because `.opencode/skills/*/SKILL.md` is the native Skill discovery path and the retained files provide distinct Skill names and procedures rather than exact duplicate content.
- Retained duplicate `opencode.jsonc` files intentionally: each area is an isolated runnable OpenCode project root and needs the same local safety config when launched directly.
- Corrected: removed undocumented `write` permission entries and replaced them with current documented permission keys.
- Omitted: providers, models, credentials, MCP servers, plugins, hooks, LSP servers, formatters, scanner connectors, cloud integrations, schedules, and production actions.
- Deleted: none for this platform stage.

## Removed Or Deprecated Field Handling

- Deprecated boolean `tools` config is not used.
- No provider/model credentials are committed.
- No MCP server is configured.
- No unsupported descriptive-only permission metadata is used.
- Area configs use `permission` rather than relying on text-only safety claims.

## Validation Method

- Inventory of all eight OpenCode Cybersecurity areas.
- JSON parse validation for `opencode.jsonc` files.
- Current OpenCode config schema validation against `https://opencode.ai/config.json`.
- Markdown frontmatter checks for agents, commands where applicable, and Skills.
- Hidden-path search using `rg -uu` for `.opencode` artifacts.
- Exact duplicate scan and retention rationale for the eight area configs.
- README review for area launch directory, discovery, permissions, project-dependent values, user/organization-dependent values, fixed safety baseline, removal, and limitations.
