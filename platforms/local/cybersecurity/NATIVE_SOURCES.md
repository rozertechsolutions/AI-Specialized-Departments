# Native Sources

Documentation review date: 2026-07-21.

Product surface: provider-neutral local specification, YAML manifests, JSON Schema Draft 2020-12 schemas, role contracts, workflows, policies, tools, and portable Skill procedures.

## Source Checks

### Check 1 - Current reference surface

- Repository-defined local manifests: `local/cybersecurity/<area>/local.yaml`.
- Repository-defined contract schemas: `local/cybersecurity/<area>/schemas/*.schema.json`.
- Repository-defined area specifications: `local/cybersecurity/<area>/SPECIFICATION.md` where present.

### Check 2 - Change and compatibility review

- The local platform is intentionally not a vendor product and has no external release-note stream.
- Compatibility is defined by the repository contracts, JSON Schema Draft 2020-12 declarations, and provider-neutral fields in the retained YAML files.
- The audit verified that the package remains model-neutral, endpoint-neutral, runtime-neutral, and provider-neutral.

### Check 3 - Current schema and parser behavior

- JSON files parse successfully.
- YAML files parse successfully with Ruby's standard YAML parser.
- Area `local.yaml` files preserve `provider_neutral: true`, `runtime_binding: none`, `active_integrations: false`, `mcp_servers: []`, and denied shell/network/live-system actions.
- Project-defined fields such as `manual_static_only`, `static_only`, `provider_neutral`, and `runtime_binding` are valid local contract fields.

## Current Native Facts

- Area path: `local/cybersecurity/<area>/`.
- Primary manifest: `local.yaml`.
- Schemas: `schemas/*.schema.json`.
- Agents: `agents/*.yaml`.
- Subagents: `subagents/*.yaml` where present and referenced.
- Skills: structured `skills/*.yaml` where present and portable `skills/*/SKILL.md`.
- Workflows: `workflows/*.yaml`.
- Tools and policies: `tools/*.yaml` and `policies/*` where present.
- Discovery: deliberate consumer load only; no AI platform autoload.
- Runtime binding: none in the reusable baseline.

## Discovery, Precedence, And Trust

- Consumers should launch or import from `local/cybersecurity/<area>/`.
- Area-local relative paths are resolved from the selected area directory.
- Recommended precedence: `local.yaml`, policies, coordinator or primary agent, subagent or Skill, workflow, artifact schema.
- The consuming runtime is responsible for trust prompts, path isolation, and enforcement.
- Runtime-specific provider, model, endpoint, credential, vector-store, connector, and tool settings belong outside this reusable baseline.

## File Classification

- Retained: all eight area roots, eight `local.yaml` files, 155 YAML files, 32 JSON schema files, 47 portable Skill Markdown files, area policies, tools, workflows, and specifications.
- Retained `agents/` and `subagents/` pairs where present because `agents/` define full contracts and coordinators while `subagents/` provide referenced delegation targets for consuming runners.
- Retained project-defined static policy fields because they are local contract fields, not unsupported vendor metadata.
- Deleted: none for this platform stage; no exact duplicate files were found.
- Omitted: bundled model provider, Ollama or LM Studio binding, vector store, orchestration framework, MCP runtime, connectors, scanners, hooks, cloud integrations, schedules, and production actions.

## Removed Or Deprecated Field Handling

- No vendor-specific configuration schema is applied to the local package.
- No provider, model, endpoint, or external integration is hard-coded.
- No project-defined `static_only` or equivalent static policy fields were removed.
- No fake repository agent, hook, MCP, scanner, or live integration is simulated.

## Validation Method

- Inventory of all eight local Cybersecurity areas.
- JSON parsing for 32 schema files.
- YAML parsing for 155 YAML files.
- Static local-contract validation for area manifests, disabled integrations, empty MCP lists, denied shell/network/live actions, and Skill frontmatter.
- Exact duplicate scan across retained local files.
- README review for implementation mapping, project-dependent values, user/organization-dependent values, fixed safety baseline, removal, and limitations.
