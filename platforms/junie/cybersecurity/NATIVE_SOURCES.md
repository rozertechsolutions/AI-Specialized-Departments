# Native Sources

Documentation review date: 2026-07-21.

Product surface: JetBrains Junie CLI and Junie in JetBrains IDEs for project guidelines, project `config.json`, custom subagents, Agent Skills, custom slash commands, MCP discovery controls, model discovery controls, and approval behavior.

## Official source checks

### Check 1 - Current reference documentation

- JetBrains Junie documentation: `https://junie.jetbrains.com/docs/`
- Guidelines and memory: `https://junie.jetbrains.com/docs/guidelines-and-memory.html`
- Custom subagents: `https://junie.jetbrains.com/docs/junie-cli-subagents.html`
- Agent Skills: `https://junie.jetbrains.com/docs/agent-skills.html`
- Custom slash commands: `https://junie.jetbrains.com/docs/custom-slash-commands.html`
- CLI reference: `https://junie.jetbrains.com/docs/parameters.html`
- CLI configuration: `https://junie.jetbrains.com/docs/junie-cli-configuration.html`
- MCP configuration: `https://junie.jetbrains.com/docs/junie-cli-mcp-configuration.html`
- Action Allowlist: `https://junie.jetbrains.com/docs/action-allowlist.html`
- Junie IDE plugin: `https://junie.jetbrains.com/docs/junie-ide-plugin.html`

### Check 2 - Official release or product status source

- Junie documentation pages checked above are current as of 2026-07-20/2026-07-21 page dates.
- Junie IDE plugin documentation states supported JetBrains IDE version requirements and license/subscription behavior.
- JetBrains Marketplace evidence was checked through the official Junie IDE plugin documentation because the marketplace plugin page itself was not reliably retrievable through the validation browser.

### Check 3 - Official package, repository, or schema evidence

- JetBrains Junie GitHub repository: `https://github.com/JetBrains/junie`
- Current documentation defines the actual `config.json` fields, custom subagent frontmatter fields, Skill structure, custom slash command format, command-line flags, environment variables, and precedence.
- No local Junie runtime package was installed or executed for this remediation.

## Current native facts

- Project path: open one area as the Junie project root, for example `junie/cybersecurity/governance-risk-compliance-assurance/`.
- Guidelines: `.junie/AGENTS.md` in the project root is the primary project guidelines file; project guidelines take precedence over conflicting global guidelines.
- Configuration: `.junie/config.json` is loaded from the project root by default. Command-line flags have highest precedence, followed by user settings, project config, and user config.
- Configuration fields retained here: `guidelines-location`, `skill-locations`, `skill-default-locations`, `command-locations`, `command-default-locations`, `agent-locations`, `agent-default-location`, `mcp-default-locations`, `model-default-locations`, and `auto-update`.
- Skills: `.junie/skills/<skill-name>/SKILL.md` with YAML frontmatter containing `name` and `description`.
- Commands: `.junie/commands/<command>.md` Markdown files for custom slash commands.
- Subagents: `.junie/agents/*.md` Markdown files with YAML frontmatter. Supported fields include `name`, `description`, `tools`, `disallowedTools`, `mcpServers`, `model`, `reasoningLevel`, `maxTurns`, `skills`, and `allowPromptArgument`.
- Tool groups: Junie built-in subagent tool group labels include `Read`, `Bash`, `Glob`, `Grep`, `Write`, `Edit`, `WebSearch`, and `AskUserQuestion`. A non-empty `tools` allowlist bans other tool groups by default.
- MCP: project MCP files would use `.junie/mcp/mcp.json`, but this package intentionally includes none. Project config disables default MCP discovery.
- Hooks: Junie `config.json` supports `hooks`, but project-default hooks are ignored for safety; this package includes no hooks.
- Model behavior: subagent `model` is optional and accepted values depend on the user's environment. This package omits model overrides so Junie uses the user/session-selected model.
- Trust/account behavior: IDE and CLI use require Junie availability, user authentication or subscription/BYOK setup outside this repository, and a trusted workspace.

## Removed or deprecated field handling

- Removed metadata-only configuration fields with no documented native effect, including `description`, `entrypoint`, `version`, `declaredIncidentOwner`, `humanAuthorizationRequired`, `humanAuthorityRequired`, and `specialistReviewRequired`.
- Removed `model: inherit` from custom subagents because current Junie documentation does not define `inherit` as a portable accepted model value. Omission preserves session/default model behavior.
- Deleted unreferenced legacy appsec Skills `appsec-lifecycle-threat-review` and `code-supply-chain-release-review`; retained current area Skills cover secure SDLC, threat modeling, secure design/code review, supply-chain/release review, testing/PSIRT assurance, and independent review.

## Validation method

- Inventoried all eight `junie/cybersecurity/<area>/` directories.
- Parsed every `config.json`.
- Parsed Markdown/YAML frontmatter for agents and Skills.
- Verified custom subagent tool groups use documented read-only labels `Read`, `Grep`, and `Glob`.
- Verified no unsupported `readonly` frontmatter exists.
- Verified no MCP configuration files, hooks, live workflows, credentials, scanners, or external integrations are present.
- Verified retained Skills and commands are reachable through area-local `.junie` discovery.

## Reasons for omitted mechanisms

- No MCP servers are included because Cybersecurity package validation must not connect external systems or expose hosted tools by default.
- No project hooks are included because hooks can execute shell commands and Junie ignores project-default hooks for safety.
- No BYOK, provider, proxy, or custom model profiles are included because credentials and routing are user/organization-dependent.
- No GitHub Action workflows are included because this package is repository-local guidance and must not create CI automation or production changes.
