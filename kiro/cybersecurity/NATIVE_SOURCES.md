# Native Sources

Documentation review date: 2026-07-22.

Product surface: Kiro IDE and CLI `AGENTS.md`, Agent Skills, CLI custom agents, IDE custom subagents, Specs, hooks, MCP, and custom-agent resources.

## Official Source Checks

### Check 1 - Current reference documentation

- Kiro CLI custom-agent configuration reference: https://kiro.dev/docs/cli/custom-agents/configuration-reference/
- Kiro CLI custom-agent creation: https://kiro.dev/docs/cli/custom-agents/creating/
- Kiro Agent Skills: https://kiro.dev/docs/skills/
- Kiro Steering and AGENTS.md: https://kiro.dev/docs/steering/
- Kiro Specs: https://kiro.dev/docs/specs/
- Kiro Hooks: https://kiro.dev/docs/hooks/
- Kiro IDE subagents: https://kiro.dev/docs/chat/subagents/

### Check 2 - Release notes or changelog

- Kiro changelog: https://kiro.dev/changelog/

Relevant 2026 notes checked: IDE 1.0.x trust, hooks, MCP, custom-agent behavior, CLI 2.10.0 default-resource inheritance control, CLI 2.12.x MCP OAuth, and CLI 2.13.0 v3 global hooks and introspect subagent. These updates did not require repository hooks or MCP for this static package.

### Check 3 - Current schema or package behavior

- The current Kiro CLI custom-agent configuration reference documents JSON fields used here: `name`, `description`, `prompt`, `mcpServers`, `tools`, `toolAliases`, `allowedTools`, `toolsSettings`, `resources`, `hooks`, `includeMcpJson`, `model`, `keyboardShortcut`, and `welcomeMessage`.
- The current Kiro Skills documentation requires each `SKILL.md` to use Agent Skills frontmatter with at least `name` and `description`; `name` must match the folder name.
- The current Kiro steering documentation documents workspace `.kiro/steering/`, global `~/.kiro/steering/`, AGENTS.md support, precedence favoring workspace steering over global steering, and optional inclusion frontmatter.
- The current Kiro CLI custom-agent configuration reference documents that custom agents inherit default steering, Skills, and `AGENTS.md` by default. `chat.disableInheritingDefaultResources` defaults to `false` and can disable inheritance only when explicitly set.

## Current Native Facts

- Area path: `kiro/cybersecurity/<area>/`.
- Intended working directory: the selected area directory, not the platform root.
- CLI custom-agent path: `.kiro/agents/*.json` inside the selected area.
- IDE custom-subagent path: `.kiro/agents/*.md`; intentionally not used in this package.
- Skill path: `.kiro/skills/<skill>/SKILL.md` inside the selected area.
- Canonical baseline path: `AGENTS.md` at the selected area root.
- Custom-agent resource model: Model A, default inheritance. Retained JSON agents do not explicitly declare `file://AGENTS.md` or `skill://.kiro/skills/**/SKILL.md` because current custom agents inherit those default resources when the selected area is the workspace.
- Tools: retained JSON agents expose and allow only Kiro's built-in `read` tool.
- MCP: retained JSON agents set `mcpServers` to `{}` and `includeMcpJson` to `false`.
- Hooks: no hook files are retained because hooks can execute shell commands or agent prompts automatically.
- Specs: no flat `.kiro/specs/*.md` files are retained. Native Kiro Specs are generated IDE workflows using `requirements.md` or `bugfix.md`, `design.md`, and `tasks.md`.

## Discovery, Precedence, And Trust

- Kiro CLI local agents are loaded from `.kiro/agents/` in the current workspace and take precedence over same-named global agents.
- Kiro workspace Skills under `.kiro/skills/` take precedence over same-named global Skills.
- Kiro supports AGENTS.md as always-included steering; AGENTS.md does not support steering inclusion modes.
- Custom agents inherit default resources such as steering, Skills, and AGENTS.md unless the user changes Kiro CLI default-resource inheritance settings.
- Repository-local configuration is effective only when the user opens or trusts the selected area workspace according to Kiro's current trust behavior.

## File Classification

- Retained: 41 Kiro CLI custom-agent JSON files, 47 Kiro Skills, and eight `AGENTS.md` files.
- Deleted: eight `.kiro/steering/<area>.md` files because each was byte-identical to the retained area `AGENTS.md`, had no inclusion-mode frontmatter, had no unique file references, and would duplicate the same default-inherited always-on baseline.
- Removed from retained JSON agents: redundant `file://AGENTS.md` and `skill://.kiro/skills/**/SKILL.md` resource declarations because they duplicate current default resource inheritance.
- Deleted: unreferenced flat `.kiro/specs/*.md` prompt artifacts because they do not match current native Kiro Spec structure and their workflow content is represented by retained Skills.
- Deleted: four superseded AppSec legacy Skills with no references beyond themselves; retained AppSec Skills preserve the professional coverage.
- Omitted: fake MCP servers, generated live hooks, hosted scanners, cloud integrations, deployment automation, credentials, IDE subagent Markdown duplicates, and production-action workflows.

## Removed Or Deprecated Field Handling

- No `staticOnly` metadata is used as a permission control.
- `includeMcpJson` is current and retained with value `false`.
- No unsupported Kiro custom-agent fields were added.
- No model pin is used; Kiro falls back to the user's selected/default model according to current product behavior.

## Validation Method

- Inventory of all eight Kiro Cybersecurity areas.
- JSON parsing and supported-key checks for all retained Kiro CLI custom agents.
- Default-inheritance checks for area `AGENTS.md` and `.kiro/skills/<skill>/SKILL.md` in each area.
- Skill frontmatter checks for `name` and `description`, including folder/name match.
- Confirmation that no hooks, MCP server definitions, obsolete flat Specs, or metadata-only permission files remain.
- Duplicate review confirmed no identical AGENTS.md/Steering copy remains and no JSON custom agent redundantly declares inherited `AGENTS.md` or Skill resources.
