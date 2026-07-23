# Native Sources

Documentation review date: 2026-07-21.

Product surface: OpenAI Codex in ChatGPT desktop app, Codex CLI, and Codex IDE extension; AGENTS.md; project `.codex/config.toml`; custom agents; Skills; hooks; MCP; custom prompts; permissions.

## Official Source Checks

### Check 1 - Current reference documentation

- Configuration reference: https://developers.openai.com/codex/config-reference
- Advanced configuration: https://developers.openai.com/codex/config-advanced
- AGENTS.md: https://developers.openai.com/codex/agent-configuration/agents-md
- Subagents and custom agents: https://developers.openai.com/codex/subagents
- Build Skills: https://developers.openai.com/codex/build-skills
- MCP: https://developers.openai.com/codex/mcp
- Custom prompts: https://developers.openai.com/codex/custom-prompts
- Rules: https://developers.openai.com/codex/rules

### Check 2 - Official release notes or changelog

- Codex changelog: https://developers.openai.com/codex/changelog

Recent notes checked for plugins, Skills, MCP, managed configuration, Codex SDK, admin controls, and permission behavior. No release note made repository `.codex/commands/` or `.codex/skills/` the preferred native surface.

### Check 3 - Current schema and documented fields

- Project `.codex/config.toml` may set project-scoped overrides only when the project is trusted.
- Project config cannot override provider/auth/profile/telemetry/notification routing keys.
- Custom agent files are TOML files under `.codex/agents/` or `~/.codex/agents/`.
- Each standalone custom agent file must define `name`, `description`, and `developer_instructions`.
- Optional custom-agent settings may include normal config keys such as `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers`, and `skills.config`.
- Codex repository Skills are discovered from `.agents/skills` in the current working directory and parent directories up to the repository root.
- Custom prompts are deprecated, are stored under `~/.codex/prompts/`, and should be replaced by Skills for reusable repository workflows.

## Current Native Facts

- Area path: `codex/cybersecurity/<area>/`.
- Intended working directory: the selected area directory.
- Instructions: `AGENTS.md` at the selected area root.
- Project config: `.codex/config.toml` with `sandbox_mode = "read-only"` and `approval_policy = "on-request"`.
- Custom agents: `.codex/agents/*.toml`.
- Skills: `.agents/skills/<skill>/SKILL.md`.
- Hooks: no `hooks.json` or inline `[hooks]` tables are retained.
- MCP: no `[mcp_servers]` entries are retained.
- Commands/prompts: no `.codex/commands/` files are retained because current custom prompts are deprecated and user-home based.

## Discovery, Precedence, And Trust

- Codex discovers `AGENTS.md` by building an instruction chain from global guidance and then from the project root down to the current working directory.
- Codex loads project `.codex/config.toml` layers from the project root down to the current working directory, with the closest setting winning when trusted.
- Project `.codex/` layers, including config, hooks, and rules, are ignored when the project is untrusted.
- Repository Skills under `.agents/skills` are scanned from the current working directory upward to the repository root.
- Custom agents in project `.codex/agents/` define spawned-session config layers and can override normal Codex session config for that agent.
- User-level and managed configuration can still impose broader or stricter behavior than this package.

## File Classification

- Retained: eight `AGENTS.md` files, eight `.codex/config.toml` files, 41 `.codex/agents/*.toml` files, and 47 `.agents/skills/*/SKILL.md` files.
- Moved: Skills from `.codex/skills/` to `.agents/skills/` because current Codex repo Skill discovery uses `.agents/skills`.
- Deleted: `.codex/commands/*.md` prompt artifacts because Codex custom prompts are deprecated and live under user-home `~/.codex/prompts/`, while retained Skills preserve the workflows.
- Omitted: hooks, MCP servers, provider credentials, profile selectors, telemetry routing, notification commands, shell allowlists, hosted scanners, cloud integrations, and deployment automation.

## Removed Or Deprecated Field Handling

- No project-local `profile` or provider selector is used.
- No unsupported custom authority or handoff tables are used.
- No metadata-only permission controls are treated as effective.
- No `readonly` field is used; read-only behavior is represented by `sandbox_mode = "read-only"` and human approval gates.

## Validation Method

- Inventory of all eight Codex Cybersecurity areas.
- TOML parsing for config and custom agents.
- Required custom-agent field checks for `name`, `description`, and `developer_instructions`.
- Sandbox and approval checks for retained config and agents.
- Skill frontmatter checks for `name` and `description`, including folder/name match.
- Confirmation that `.codex/skills`, `.codex/commands`, hooks, MCP server definitions, provider/auth/profile keys, and metadata-only permission files are absent.
