# Native Source Summary

Official Junie documentation checked on 2026-07-15:

- Guidelines and memory: documents `.junie/AGENTS.md`, `AGENTS.md`, and `.junie/guidelines` discovery, plus project guideline precedence.
- Custom subagents: documents `.junie/agents/*.md`, YAML frontmatter fields, automatic delegation, supported tool groups, and `.agents` aliases.
- Agent skills: documents `.junie/skills/<skill-name>/SKILL.md`, required `SKILL.md`, `name` and `description` frontmatter, project/user scope, and progressive disclosure.
- Custom slash commands: documents `.junie/commands/*.md`, YAML frontmatter, named arguments, and project/user scope.
- Hooks: documents shell-command hooks and default safety behavior; omitted here because this package must not execute commands.
- MCP configuration: reviewed to omit MCP because it can expose external services and credentials.

## Native Components Used

- `.junie/AGENTS.md`
- `.junie/config.json`
- `.junie/agents/*.md`
- `.junie/skills/*/SKILL.md`
- `.junie/commands/*.md`

## Components Omitted

- Hooks are omitted because they run shell commands automatically during Junie sessions.
- MCP is omitted because this GRC area must not connect external tools, APIs, repositories, ticketing systems, evidence stores, or cloud services.
- Scripts are omitted because the package is static and Skills are instruction-only.

