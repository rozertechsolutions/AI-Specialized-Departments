# Native Sources

Documentation review date: 2026-07-21.

Product surface: GitHub Copilot in VS Code, Copilot CLI, Copilot coding agent/cloud agent where enabled, custom instructions, prompt files, custom agents, Agent Skills, hooks, MCP, and agent permissions.

Official source evidence checked or retained for this platform:

- GitHub Copilot custom agents: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents
- GitHub Copilot repository custom instructions: https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
- VS Code custom agents: https://code.visualstudio.com/docs/agent-customization/custom-agents
- VS Code Agent Skills: https://code.visualstudio.com/docs/agent-customization/agent-skills
- VS Code prompt files: https://code.visualstudio.com/docs/agent-customization/prompt-files
- VS Code custom instructions: https://code.visualstudio.com/docs/agent-customization/custom-instructions
- VS Code hooks: https://code.visualstudio.com/docs/agent-customization/hooks
- VS Code MCP customization: https://code.visualstudio.com/docs/agent-customization/mcp

Validation method:

- Inventory of `github-copilot/cybersecurity/` files and native support directories.
- Static parsing of Markdown/YAML frontmatter for agents, prompt files, Skills, and instructions.
- Reference resolution for retained repository-local prompt files, Skills, agents, and instruction files.
- Native field review against current GitHub Copilot and VS Code documentation for `.agent.md`, `.prompt.md`, `.github/copilot-instructions.md`, `.github/skills`, hooks, MCP, and tool identifiers.
- Removal of redundant area-level source copies after this platform-wide source file replaced them.

Current native facts recorded:

- Project paths: `github-copilot/cybersecurity/<area>/` for all eight Cybersecurity areas.
- Discovery: open `github-copilot/cybersecurity/<area>/` as the VS Code/Copilot workspace root so that area's `.github/copilot-instructions.md`, `.github/agents/*.agent.md`, `.github/prompts/*.prompt.md`, and `.github/skills/<name>/SKILL.md` are loaded.
- Custom instructions: `.github/copilot-instructions.md` automatically applies to chat requests in the selected workspace.
- Custom agents: workspace agents live under `.github/agents`; files use the `.agent.md` extension. VS Code also detects `.md` files in that folder, but this package uses the explicit `.agent.md` form.
- Custom agent fields used: `name`, `description`, and `tools`.
- Custom agent model behavior: this package omits `model` so Copilot uses the currently selected/available model according to user, plan, and organization policy.
- Custom agent tools used: `search/codebase` and `search/usages`, matching VS Code/GitHub Copilot tool identifiers for read/search behavior.
- Prompt files: `.github/prompts/*.prompt.md` are manual slash-command style prompts. Prompt files can define `description`, `name`, `argument-hint`, `agent`, `model`, and `tools`; this package keeps prompt files as prompt-only Markdown artifacts without unnecessary frontmatter.
- Agent Skills: project Skills live under `.github/skills/<skill-name>/SKILL.md`. Skill names must match their parent directory, use lowercase letters, numbers, and hyphens, and include required `name` and `description` frontmatter.
- Hooks: hooks are a real preview-capable mechanism but are not provided by this package.
- MCP: MCP is a real customization surface but no MCP configuration is provided by this package.
- Trust and precedence: parent repository discovery, organization instructions/agents, user profile Skills/prompts/agents, active tool selections, and cloud/coding-agent policies can affect runtime behavior; strict area isolation requires opening the selected area as the workspace root and checking Copilot diagnostics.
- Omitted mechanisms: fake MCP servers, generated live hooks, external endpoints, credentials, cloud actions, scanners, hosted tools, and deployment automation are intentionally omitted.

Removed or deprecated field handling:

- Replaced non-native copied tool labels `Read`, `Grep`, and `Glob` with VS Code/GitHub Copilot tool identifiers `search/codebase` and `search/usages`.
- Removed unsupported `model: inherit`; model selection is left to the Copilot surface, account, and organization policy.
- Did not introduce unsupported `readonly` or `skills` custom-agent frontmatter.
- Removed two orphaned app-security Skill directories that were not referenced by agents, prompts, README, or native discovery requirements after retained Skills preserved workflow coverage.
- Platform-specific frontmatter and config fields must be verified against current vendor documentation before use.
