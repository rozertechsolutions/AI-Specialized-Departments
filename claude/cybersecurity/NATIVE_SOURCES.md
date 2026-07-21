<<<<<<< HEAD
# Native Source Verification

Official sources checked on 2026-07-20:

- Claude Help Center, "What are projects?", `https://support.claude.com/en/articles/9517075-what-are-projects`.
- Claude Help Center, "How can I create and manage projects?", `https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects`.
- Claude Help Center, "Use skills in Claude", `https://support.claude.com/en/articles/12512180-use-skills-in-claude`.
- Claude Help Center, "What are skills?", `https://support.claude.com/en/articles/12512176-what-are-skills`.
- Claude Help Center, "Use connectors to extend Claude's capabilities", `https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities`.
- Claude Help Center, "Get started with custom connectors using remote MCP", `https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp`.
- Claude Help Center, "Create and edit files with Claude", `https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude`.
- Claude Help Center, "Release notes", `https://support.claude.com/en/articles/12138966-release-notes`.

## Product surface

The current Claude web/desktop surfaces relevant to this package are Projects, Project instructions, Project knowledge, automatic RAG for large Project knowledge, Claude Skills, artifacts, code execution and file creation, and separately configured connectors. Projects create self-contained workspaces with their own chats, instructions, and knowledge. Skills are reusable workflows that can be uploaded, enabled, shared, or provisioned depending on plan and organization settings. Connectors and custom remote MCP connectors are external integrations that can access or change data in connected services.

## Current version or date

Claude web and desktop are hosted products without a repository-pinnable package version. This evidence records the official documentation date checked: 2026-07-20. Release notes around this period describe the unified Chat/Cowork home and projects, artifacts, plugins, and Skills availability across supported surfaces.

## Project paths and filenames

This package uses:

- `PROJECT_INSTRUCTIONS.md` for manual Project instruction import.
- `knowledge/*.md` for Project knowledge uploads.
- `skills/<skill-name>/SKILL.md` for custom Skill bundles.
- `templates/*.md` for uploaded output schemas.
- `workflows/*.md` for uploaded workflow guidance.
- `README.md` and `NATIVE_SOURCES.md` as repository documentation only.

Claude web and desktop do not automatically discover these paths from disk. Users must manually paste instructions, upload knowledge files, or upload Skills.

## Schema fields and removed fields

Custom Skill bundles use a top-level `SKILL.md` with `name` and `description` YAML frontmatter. This package does not use repository-local fields for models, tools, subagents, hooks, MCP servers, connectors, approvals, or permissions because those are not loaded from `claude/cybersecurity/` by Claude web or desktop Projects.

## Discovery, precedence, and trust

Project instructions apply only inside the selected Claude Project. Project knowledge is available to chats inside that Project; context is not shared across chats unless information is added to Project knowledge or memory features apply. RAG activates automatically when Project knowledge approaches context limits. Skills activate dynamically when enabled and relevant. Uploaded Skills and files must be reviewed before use because Skills may contain instructions and supporting resources that affect Claude's behavior.

## Permissions and limitations

Skills require code execution and file creation to be enabled. Code execution, file creation, network egress, connectors, and custom remote MCP are controlled by personal or organization settings depending on plan. Connectors inherit the user's permissions in the connected service and may take actions. Custom remote MCP connectors are beta, require network-reachable remote servers, and should not be used for this static package unless separately approved. This package configures no connector, remote MCP server, local MCP server, browser action, scheduled task, or write-capable integration.

## Omitted mechanisms and reason

Claude Code `CLAUDE.md`, `.claude/skills/`, commands, hooks, subagents, local MCP, desktop extension manifests, Cowork plugin packages, and executable automation are omitted because this `claude/` package targets Claude web/desktop Projects and manual Skill import, not Claude Code or plugin packaging. Fake connector definitions and dummy endpoints are omitted because they would misrepresent installation and safety behavior.

## Validation method

Validation is static: local file inventory, Markdown/frontmatter parsing, reference inspection, official-documentation comparison, and confirmation that no executable integration artifacts are present. No generated agent, Skill, workflow, connector, MCP server, model call, browser action, or live system was executed.
=======
# Native Sources

Documentation review date: 2026-07-21.

Product surface: Claude web and desktop Projects, project instructions, project knowledge, and Claude Agent Skills.

Official source evidence checked or retained for this platform:

- https://www.anthropic.com/news/projects
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://github.com/anthropics/skills

Validation method:

- Inventory of `claude/cybersecurity/` files and native support directories.
- Static syntax parsing for JSON, TOML, YAML where applicable.
- Reference resolution for retained repository-local prompts, Skills, agents, and config files where applicable.
- Removal of redundant area-level source copies after this platform-wide source file replaced them.

Current native facts recorded:

- Project paths: `claude/cybersecurity/<area>/` for all eight Cybersecurity areas.
- Discovery: use the platform-specific README and open/import from the documented working directory or manual UI location.
- Permissions: read-only/static by default; shell, network, MCP, connector, hosted tool, scanner, deployment, and production actions absent or denied unless a human explicitly configures them outside this baseline.
- Trust: repository-local configuration is effective only when the platform trusts or imports the project according to its current documentation.
- Precedence: nearest area-level instructions or manually selected area package govern the selected work; platform-level README and this file provide package-wide evidence.
- Omitted mechanisms: fake MCP servers, generated live hooks, external endpoints, credentials, cloud actions, scanners, and deployment automation are intentionally omitted.

Removed or deprecated field handling:

- Unsupported descriptive-only metadata is not treated as a permission control.
- Platform-specific frontmatter and config fields must be verified against current vendor documentation before use.
- For SDK packages, runtime API compatibility must be validated in an isolated environment without model calls before production use.
>>>>>>> feature/cybersecurity-department
