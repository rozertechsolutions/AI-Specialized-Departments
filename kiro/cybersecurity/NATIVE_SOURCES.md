# Native Sources

Documentation review date: 2026-07-21.

Product surface: Kiro IDE and CLI steering/AGENTS.md, custom agents JSON, Skills, hooks, Specs, MCP, and resource references.

Official source evidence checked or retained for this platform:

- https://kiro.dev/docs/cli/custom-agents/configuration-reference/
- https://kiro.dev/docs/steering/
- https://kiro.dev/docs/hooks/
- https://kiro.dev/docs/mcp/

Validation method:

- Inventory of `kiro/cybersecurity/` files and native support directories.
- Static syntax parsing for JSON, TOML, YAML where applicable.
- Reference resolution for retained repository-local prompts, Skills, agents, and config files where applicable.
- Removal of redundant area-level source copies after this platform-wide source file replaced them.

Current native facts recorded:

- Project paths: `kiro/cybersecurity/<area>/` for all eight Cybersecurity areas.
- Discovery: use the platform-specific README and open/import from the documented working directory or manual UI location.
- Permissions: read-only/static by default; shell, network, MCP, connector, hosted tool, scanner, deployment, and production actions absent or denied unless a human explicitly configures them outside this baseline.
- Trust: repository-local configuration is effective only when the platform trusts or imports the project according to its current documentation.
- Precedence: nearest area-level instructions or manually selected area package govern the selected work; platform-level README and this file provide package-wide evidence.
- Omitted mechanisms: fake MCP servers, generated live hooks, external endpoints, credentials, cloud actions, scanners, and deployment automation are intentionally omitted.

Removed or deprecated field handling:

- Unsupported descriptive-only metadata is not treated as a permission control.
- Platform-specific frontmatter and config fields must be verified against current vendor documentation before use.
- For SDK packages, runtime API compatibility must be validated in an isolated environment without model calls before production use.
