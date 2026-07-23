# Native Sources

Documentation review date: 2026-07-21.

Product surface: Cursor IDE and Cursor CLI nested `AGENTS.md`, Project Rules, Agent Skills, Subagents, custom commands, hooks, MCP, and agent permissions.

Official source evidence checked or retained for this platform:

- Cursor documentation index: https://cursor.com/docs
- Cursor Subagents: https://cursor.com/docs/subagents
- Cursor Agent Skills: https://cursor.com/docs/skills
- Cursor Rules and `AGENTS.md`: https://cursor.com/docs/rules
- Cursor Hooks: https://cursor.com/docs/hooks
- Cursor MCP: https://cursor.com/docs/mcp
- Cursor 2.4 changelog, Subagents and Skills: https://cursor.com/changelog/2-4

Validation method:

- Inventory of `cursor/cybersecurity/` files and native support directories.
- Static parsing of Markdown/YAML frontmatter and `.mdc` rule frontmatter.
- Reference resolution for retained Skills, commands, agents, `AGENTS.md`, and rule files.
- Native field review against current Cursor docs for subagents, Skills, rules, AGENTS.md, hooks, MCP, and permissions.
- Removal of redundant area-level source copies after this platform-wide source file replaced them.

Current native facts recorded:

- Project paths: `cursor/cybersecurity/<area>/` for all eight Cybersecurity areas.
- Discovery: open `cursor/cybersecurity/<area>/` in Cursor IDE or Cursor CLI so the selected area's `AGENTS.md`, `.cursor/agents/*.md`, `.cursor/skills/<name>/SKILL.md`, `.cursor/commands/*.md`, and retained `.cursor/rules/*.mdc` are project-local.
- Subagent locations: project subagents live under `.cursor/agents/`; user subagents live under `~/.cursor/agents/`. This package uses only project-local area subagents.
- Custom subagent fields retained: `name`, `description`, `model`, and `readonly`.
- Custom subagent fields omitted: `skills` is not a documented custom-subagent frontmatter field; Skill discovery is handled separately through `.cursor/skills/`.
- Tool scoping: Cursor docs document `readonly: true` as restricted write permissions. The package does not rely on a copied Claude-style `tools` list for Cursor custom agents.
- Skills: Cursor Agent Skills live under `.cursor/skills/<skill-name>/SKILL.md`; agents can discover/apply Skills when relevant and users can invoke Skills through the slash menu.
- Rules: Cursor project rules live under `.cursor/rules/*.mdc` and require rule frontmatter for native rule behavior. `AGENTS.md` is also a documented plain-Markdown instruction surface and supports nested subdirectories.
- Commands: retained `.cursor/commands/*.md` files are prompt artifacts for manual invocation where enabled; Skills remain the primary procedural mechanism.
- MCP: no `.cursor/mcp.json` is provided. Cursor subagents can inherit parent MCP tools if MCP is configured externally, so MCP must remain unconfigured or disabled for this static package unless a human explicitly authorizes it outside the repository baseline.
- Hooks: no hooks are provided by this package. Cursor hooks are a real feature, but live hook execution is intentionally omitted.
- Trust and precedence: user/team rules, user-level Skills or subagents, parent-session tools, and plan/model policy can affect runtime behavior. The selected area package is the reusable baseline; humans must verify active Cursor mode and settings before use.
- Omitted mechanisms: fake MCP servers, generated live hooks, external endpoints, credentials, cloud actions, scanners, hosted tools, browser automation, and deployment automation are intentionally omitted.

Removed or deprecated field handling:

- Removed unsupported `skills` frontmatter from Cursor custom subagents and kept Skills in `.cursor/skills/`.
- Removed non-documented copied agent `tools` frontmatter from Cursor custom subagents; read-only behavior is represented by `readonly: true`.
- Deleted exact duplicate `.cursor/rules/<area>.mdc` files that copied `AGENTS.md` without Cursor rule frontmatter. Nested `AGENTS.md` remains as the canonical plain-Markdown instruction channel; retained `.mdc` files have rule frontmatter and independent native value.
- Platform-specific frontmatter and config fields must be rechecked against current Cursor documentation before use.
