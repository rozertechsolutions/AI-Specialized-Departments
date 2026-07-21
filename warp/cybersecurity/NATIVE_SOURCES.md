# Native Sources

Documentation review date: 2026-07-21.

Product surface: Warp local Agent Mode, Project Rules through `AGENTS.md`, project Skills through `.warp/skills/`, and optional Oz cloud agents outside this repository.

## Official Source Checks

### Check 1 - Current reference documentation

- Warp getting started and Oz overview: https://docs.warp.dev/
- Warp Agents overview: https://docs.warp.dev/agent-platform/local-agents/overview/
- Rules for agents: https://docs.warp.dev/agent-platform/capabilities/rules/
- Skills for agents: https://docs.warp.dev/agent-platform/capabilities/skills/
- MCP capability: https://docs.warp.dev/agent-platform/capabilities/mcp/
- Slash Commands: https://docs.warp.dev/agent-platform/capabilities/slash-commands/

### Check 2 - Release notes or current behavior notes

- Warp Rules and Skills pages were last updated in July 2026.
- Oz CLI reference was last updated on 2026-07-20 and confirms `warp-cli` is deprecated in favor of `oz`.
- Current docs distinguish local Warp agents from Oz cloud agents, environments, schedules, integrations, and API/SDK usage.

### Check 3 - Current product behavior and format

- Project Rules are stored in uppercase `AGENTS.md`; `WARP.md` is still supported and has same-directory priority if both exist.
- Warp automatically applies `AGENTS.md` from the current directory and repository root, with current-subdirectory rules taking precedence.
- Project Skills can live in `.warp/skills/` and must be in their own directory with `SKILL.md` containing `name` and `description` frontmatter.
- Skill discovery is based on the current working directory.
- MCP servers are configured through Warp Drive/Oz settings, not through files retained in this package.

## Current Native Facts

- Area path: `warp/cybersecurity/<area>/`.
- Project Rules: `AGENTS.md`.
- Skills: `.warp/skills/*/SKILL.md`.
- Discovery: launch Warp from the selected area directory.
- Oz cloud agents: not represented as repository files.
- MCP: absent by default; no MCP configuration file is retained.

## Discovery, Precedence, And Trust

- Warp applies the current directory's Project Rules before root Project Rules and Global Rules.
- If `WARP.md` and `AGENTS.md` exist in the same directory, `WARP.md` has priority; this package intentionally uses only `AGENTS.md`.
- Skills are discovered from the current working directory up through the repository root.
- Runtime trust, provider/model selection, Agent Profiles, terminal command approval, MCP, and Oz cloud execution remain user/workspace controlled outside this package.

## File Classification

- Retained: eight `AGENTS.md` Project Rules files and 38 `.warp/skills/*/SKILL.md` project Skills.
- Omitted: repository custom-agent files, WARP.md duplicates, Oz run definitions, Oz schedules, Oz environments, Agent Profiles, MCP configs, Warp settings files, cloud integrations, scanner connectors, hooks, and production actions.
- Deleted: none for this platform stage; no exact duplicate files were found.

## Removed Or Deprecated Field Handling

- No `warp-cli` instructions are used; Oz is documented as the current CLI when cloud/local Oz execution is separately authorized.
- No repository-defined named Warp custom agents are claimed.
- No MCP server, schedule, integration, or cloud environment is simulated.
- No unsupported permissions file is presented as an enforcement mechanism.

## Validation Method

- Inventory of all eight Warp Cybersecurity areas.
- Markdown frontmatter checks for 38 Skills.
- Exact duplicate scan across retained Warp files.
- Hidden-path search for `.warp/skills`.
- Confirmation that no fake custom agents, Oz run definitions, schedules, MCP configs, credentials, or live integrations are present.
- README review for local versus Oz behavior, launch directory, discovery, project-dependent values, user/organization-dependent values, fixed safety baseline, removal, and limitations.
