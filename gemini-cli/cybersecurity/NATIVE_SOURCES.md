# Native Sources

Documentation review date: 2026-07-21.

Product surface: Gemini CLI repository configuration for `GEMINI.md`, custom subagents, Agent Skills, command prompt files, policy-engine guidance, MCP where configured, and trusted workspace behavior.

## Official source checks

### Current reference documentation

- Gemini CLI custom subagents - https://github.com/google-gemini/gemini-cli/blob/main/docs/core/subagents.md
- Gemini CLI file-system tools - https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/file-system.md
- Gemini CLI Agent Skills - https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
- Gemini CLI policy engine - https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/policy-engine.md
- Gemini CLI installation - https://geminicli.com/docs/get-started/installation/
- Google Cloud Gemini CLI overview - https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli

### Release/package check

- GitHub releases checked on 2026-07-21. Current stable release evidence showed `v0.51.0` and active `v0.52.0` preview/nightly releases.
- Local `npm` is not installed in this remediation environment, so no package was installed and no Gemini CLI runtime was launched.

### Schema/field check

Current custom agent documentation defines project agents at `.gemini/agents/*.md` and user agents at `~/.gemini/agents/*.md`. Supported frontmatter includes:

- `name`
- `description`
- `kind`
- `tools`
- `mcpServers`
- `model`
- `temperature`
- `max_turns`
- `timeout_mins`

The previous `readonly` and agent-level `skills` fields are not documented custom-agent fields and have been removed. Read-only behavior is represented by native tool allowlists using `read_file`, `grep_search`, `glob`, and `list_directory`.

## Validated project paths

- `gemini-cli/cybersecurity/governance-risk-compliance-assurance/`
- `gemini-cli/cybersecurity/security-architecture-engineering/`
- `gemini-cli/cybersecurity/application-product-devsecops-security/`
- `gemini-cli/cybersecurity/exposure-vulnerability-hardening/`
- `gemini-cli/cybersecurity/defensive-security-operations-detection-intelligence/`
- `gemini-cli/cybersecurity/incident-response-dfir-recovery/`
- `gemini-cli/cybersecurity/offensive-security-authorized-validation/`
- `gemini-cli/cybersecurity/cyber-resilience-specialized-technologies/`

Each area contains `GEMINI.md`, `.gemini/agents/*.md`, `.gemini/skills/*/SKILL.md`, and `.gemini/commands/*.md`.

## Discovery and precedence

Launch Gemini CLI from `gemini-cli/cybersecurity/<area>/` for area isolation. Gemini CLI discovers workspace agents from `.gemini/agents/*.md` and workspace Skills from `.gemini/skills/*/SKILL.md` or `.agents/skills/*/SKILL.md`. When both Skill paths are present at the same tier, `.agents/skills/` has precedence; this package uses only `.gemini/skills/`.

Subagents run in isolated context loops and receive only explicitly granted tools. Skills are discovered and activated separately through the Skill mechanism and are not preloaded by custom-agent frontmatter.

## Permissions and safety behavior

All retained Cybersecurity custom agents now use:

- `kind: local`;
- `model: inherit`;
- `temperature: 0.2`;
- `max_turns: 10`;
- `timeout_mins: 10`;
- `tools: [read_file, grep_search, glob, list_directory]`;
- no inline `mcpServers`;
- no unsupported `readonly`;
- no unsupported agent-level `skills`.

The policy engine supports `allow`, `deny`, and `ask_user` decisions for tools and can match tool names, arguments, approval mode, and subagent names. This repository does not create user-global policy files; organizations can add policies in their approved Gemini CLI configuration outside this reusable package.

## Skill cleanup decision

Unreferenced duplicate or legacy Skill directories were removed after reference checks showed they were mentioned only by their own `SKILL.md` files. Retained Skills are those referenced by commands or otherwise needed as canonical area workflows. Professional role ownership remains in `GEMINI.md` and custom agent bodies.

## Validation method

- Inventory of all eight Gemini CLI Cybersecurity areas.
- Markdown frontmatter parsing for all retained custom agents and Skills.
- Validation that no custom agent contains unsupported `readonly` or agent-level `skills`.
- Validation that every custom agent has a unique `name`, `description`, `kind: local`, native tool IDs, and conservative model/turn/time fields.
- Validation that every command references retained Skills.
- Deletion of unreferenced duplicate/legacy Skill directories after reference checks.
- Hygiene checks for empty files, empty directories, caches, temporary environments, and generated artifacts.

## Omitted mechanisms

No MCP server, remote subagent, browser agent, shell policy, scanner, connector, cloud, ticketing, SIEM, EDR, XDR, SOAR, identity-provider, deployment, or production integration is enabled by this package. Any such integration must be configured separately by an authorized human owner outside this reusable baseline.
