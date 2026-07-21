# Native Sources

Documentation review date: 2026-07-21.

Product surface: Claude Code CLI repository configuration for project memory, custom subagents, Skills, legacy commands, project settings, permissions, hooks where configured, and MCP where configured.

## Official source checks

### Current reference documentation

- Claude Code subagents - https://code.claude.com/docs/en/sub-agents
- Claude Code Skills - https://code.claude.com/docs/en/skills
- Claude Code settings and permissions - https://code.claude.com/docs/en/settings
- Claude Code hooks guide/reference - https://docs.anthropic.com/en/docs/claude-code/hooks-guide and https://docs.anthropic.com/en/docs/claude-code/hooks
- Claude Code MCP - https://docs.anthropic.com/en/docs/claude-code/mcp
- Claude Code Agent SDK overview for filesystem configuration locations - https://code.claude.com/docs/en/agent-sdk/overview

### Release/changelog check

- Claude Code changelog checked from https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md on 2026-07-21.
- Recent notes confirm ongoing changes to permission checks, plan-mode behavior, subagent restoration, background sessions, Skill/command discovery, and MCP handling. This package therefore avoids unsupported fields and relies on current documented subagent frontmatter.

### Schema/field check

Current Claude Code subagent documentation supports fields including `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `skills`, `mcpServers`, hooks, memory, background, effort, isolation, color, and initial prompt behavior. `readonly` is not a documented field and has been removed from all Cybersecurity subagents.

The `skills` field is retained because current documentation states it preloads Skill content into a subagent context. It does not restrict all Skill access by itself; access is still governed by available tools, `Skill` tool availability, parent permissions, and settings.

## Validated project paths

- `claude-code/cybersecurity/governance-risk-compliance-assurance/`
- `claude-code/cybersecurity/security-architecture-engineering/`
- `claude-code/cybersecurity/application-product-devsecops-security/`
- `claude-code/cybersecurity/exposure-vulnerability-hardening/`
- `claude-code/cybersecurity/defensive-security-operations-detection-intelligence/`
- `claude-code/cybersecurity/incident-response-dfir-recovery/`
- `claude-code/cybersecurity/offensive-security-authorized-validation/`
- `claude-code/cybersecurity/cyber-resilience-specialized-technologies/`

Each area contains `CLAUDE.md`, `.claude/agents/*.md`, `.claude/skills/*/SKILL.md`, and `.claude/commands/*.md`. Some high-risk areas also contain `.claude/settings.json` deny rules for Bash, WebFetch, and MCP.

## Discovery and precedence

Claude Code should be launched from `claude-code/cybersecurity/<area>/` for area isolation. Project `CLAUDE.md` and `.claude/` configuration are discovered from the project context. Skills are discovered from `.claude/skills/*/SKILL.md`; legacy commands remain supported from `.claude/commands/*.md`, though current documentation recommends Skills for new command-like workflows.

Managed settings have highest precedence, followed by command-line arguments, local settings, project settings, and user settings. Parent-session permission modes can take precedence over subagent `permissionMode`, so project-local agent fields are not the only enforcement layer.

## Permissions and safety behavior

All retained Cybersecurity subagents now use:

- `permissionMode: plan`;
- `tools: [Read, Grep, Glob]`;
- `disallowedTools: [Write, Edit, MultiEdit, NotebookEdit, Bash, WebFetch, WebSearch, "mcp__*"]`;
- no inline `mcpServers`;
- retained canonical `skills` entries that resolve to existing area Skills.

These fields provide real Claude Code controls for static read/search behavior. They do not authorize active scans, exploitation, deployment, shell execution, MCP use, hosted connectors, or production actions.

## Skill cleanup decision

The previous package contained older generated Skill directories with names such as `governance-policy-and-frameworks`, `risk-exceptions-and-remediation`, `secure-sdlc-requirements-threat-modeling`, `resilience-recovery-core`, `incident-command-evidence`, and `authorization-assessment-planning`. Agents and commands referenced the newer canonical Skills, not those legacy directories.

The legacy Skills repeated the same generic procedure, evidence, stop-condition, human-review, and prohibited-action structure already present in the retained canonical Skills, while role-specific ownership is preserved in `CLAUDE.md` and agent bodies. They were deleted after reference checks confirmed no retained agent or command depended on them.

## Validation method

- Inventory of all eight Claude Code Cybersecurity areas.
- Markdown frontmatter parsing for all retained subagents and Skills.
- JSON parsing for retained `.claude/settings.json` files.
- Validation that no subagent contains unsupported `readonly`.
- Validation that every subagent has a unique `name`, supported `tools`, `disallowedTools`, `permissionMode: plan`, and Skill references that resolve to retained `SKILL.md` files.
- Validation that every command references retained Skills.
- Deletion of superseded legacy Skill directories after reference and content comparison.
- Hygiene checks for empty files, empty directories, caches, temporary environments, and generated artifacts.

## Omitted mechanisms

No MCP server is configured by this package. No hooks execute security actions. No shell, scanner, connector, cloud, ticketing, SIEM, EDR, XDR, SOAR, identity-provider, deployment, or production integration is enabled. Any such integration must be configured separately by an authorized human owner outside this reusable baseline.
