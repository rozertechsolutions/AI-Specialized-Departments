# Native Sources

Documentation review date: 2026-07-21.

Product surface: Mistral Vibe Code CLI/VS Code surfaces, project `.vibe/config.toml`, native TOML agent profiles, project and user prompt directories, Skills, tool filters, permissions, hooks configuration, MCP settings, and update/telemetry settings.

Official source evidence checked or retained for this platform:

- https://docs.mistral.ai/vibe/code/cli/install-setup
- https://docs.mistral.ai/vibe/code/cli/configuration
- https://docs.mistral.ai/vibe/code/cli/agents
- https://github.com/mistralai/mistral-vibe
- `mistral-vibe==2.21.0` package schema inspected in a deleted disposable environment
- repository `.vibe/config.toml` and `.vibe/agents/*.toml` files

Validation method:

- Inventory of `mistral-vibe/cybersecurity/` files and native support directories.
- Static syntax parsing for JSON, TOML, YAML where applicable.
- Reference resolution for retained repository-local prompts, Skills, agents, and config files where applicable.
- Removal of redundant area-level source copies after this platform-wide source file replaced them.
- Isolated package inspection confirmed config schema fields and prompt search behavior without running agents or calling models.

Current native facts recorded:

- Project paths: `mistral-vibe/cybersecurity/<area>/` for all eight Cybersecurity areas.
- Discovery: launch from the selected area directory; Vibe discovers project config, agents, prompts, and Skills from area-local `.vibe/` when that directory is the trusted project root. `VIBE_HOME="$PWD/.vibe"` is a repository-local way to keep user-home prompt/config resolution out of `~/.vibe` during manual use.
- Prompt resolution: current package source searches discovered project prompt directories and the user Vibe home prompt directory. Every retained agent `system_prompt_id` has a matching retained prompt file.
- Config schema: `enable_experimental_hooks` is not present in `mistral-vibe==2.21.0`; `enable_auto_update` and `enable_update_checks` exist, but this package does not add either unless needed.
- Agent schema: retained TOML profiles use `agent_type`, `display_name`, `description`, `safety`, `system_prompt_id`, enabled/disabled tools, and per-tool permissions. Sparse duplicate legacy agent profiles were removed.
- Permissions: read-only/static by default; shell, network, MCP, connector, hosted tool, scanner, deployment, and production actions absent or denied unless a human explicitly configures them outside this baseline.
- Trust: repository-local configuration is effective only when the platform trusts or imports the project according to its current documentation.
- Precedence: nearest area-level instructions or manually selected area package govern the selected work; platform-level README and this file provide package-wide evidence.
- Omitted mechanisms: fake MCP servers, generated live hooks, external endpoints, credentials, cloud actions, scanners, and deployment automation are intentionally omitted.

Removed or deprecated field handling:

- Unsupported descriptive-only metadata is not treated as a permission control.
- Obsolete `enable_experimental_hooks` config entries were removed; hooks remain absent unless configured through current hook files by an authorized user.
- Unreferenced workflow-like prompt Markdown and exact duplicate prompt/agent pairs were removed after verifying retained prompts cover every `system_prompt_id`.
- Platform-specific frontmatter and config fields must be verified against current vendor documentation before use.
- For SDK packages, runtime API compatibility must be validated in an isolated environment without model calls before production use.
