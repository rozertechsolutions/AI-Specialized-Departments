# Local Mobile Development Specification

## Surface

- Specification ID: `ai-specialized-departments.local.mobile-development`
- Specification version: `1.0.0`
- Surface: project-defined local configuration specification
- Runtime dependency: none
- Provider dependency: none

The `local/` platform is intentionally model/runtime independent. Ollama, LM Studio, llama.cpp, vLLM, SGLang, Llama, Gemma, Qwen, DeepSeek, GPT-OSS, and OpenAI-compatible servers are providers, runtimes, or models, not this platform.

## Discovery and Precedence

1. Read `local.yaml`.
2. Validate referenced manifests with `schemas/`.
3. Apply policies before agents, skills, workflows, tools, providers, or MCP examples.
4. Treat disabled examples as documentation until a human enables them in a private, reviewed configuration.
5. Fail closed on malformed, ambiguous, or security-sensitive configuration.

Higher-precedence user/runtime configuration may supply provider endpoints, model IDs, roots, or credentials, but this repository must not contain them.

## Extensibility Policy

Extensibility is allowed only in documented extension locations. Unknown top-level core properties are rejected by schema validation so provider, runtime, or host-specific metadata cannot collide with Local Mobile semantics.

Extensible schemas and locations:

- `local.schema.json`: optional `extensions` for host metadata about discovery or embedding. Core scope, lifecycle, validation, capability negotiation, precedence, and references remain strictly validated.
- `hook.schema.json`: optional manifest-level and per-hook `extensions` for host hook metadata. Hook mode, source mutation, network use, event type, file name, and fail-safe behavior remain strictly validated.
- `mcp-server.schema.json`: optional manifest-level and per-server `extensions` for reviewed MCP host metadata. Server examples must remain disabled, sampling and elicitation must remain disabled, external writes require human approval, and credentials must remain `not_configured`.
- `policy.schema.json`: optional `extensions` for policy metadata, plus `rules`, `guards`, and `audit_logging` maps for policy-specific rule names. Policy identity, classification, approval lists, prohibitions, protected material, and human-control lists remain strictly validated.
- `provider.schema.json`: optional `extensions` for provider metadata and an extensible `configuration` object for provider/runtime-specific settings such as endpoint, model, executable, context length, and hardware limits. Provider examples must remain disabled, capability discovery must be runtime-based, remote use must require explicit consent, and explicit credential placeholders such as `api_key` must remain null.
- `tool.schema.json`: optional `extensions` for host metadata about tool contracts. Tool identity, purpose, allowed and denied operations, inputs, outputs, approval requirement, and fail-safe behavior remain strictly validated.

Extension keys must be namespaced with `x_`, `provider_`, `runtime_`, `host_`, or `vendor_`. Core field names are reserved outside those extension objects, preventing naming collisions and accidental override of Local Mobile semantics.

Extensions are metadata only. They cannot override required security, permission, approval, provider, MCP, hook, policy, or fail-safe semantics. If an extension conflicts with a core field, the core field wins and the host must fail closed when the conflict creates ambiguity.

## Native Capability Classification

Native:

- YAML manifests for roles, skills, workflows, policies, tool contracts, providers, hooks, and MCP examples.
- JSON Schemas for validation.
- Standard-library Python guards that inspect proposed commands, prompts, and file paths.
- Disabled provider and MCP example contracts.

Unsupported:

- Runtime execution, daemon management, external authentication, provider startup, model download, cloud fallback, signing, publishing, upload, deployment, spending, destructive operations, and autonomous execution loops.
- Platform-level multi-agent execution beyond role manifests and deterministic delegation contracts.

## Responsibility Model

The coordinator owns scope, sequencing, delegation, conflict resolution, validation synthesis, and final reporting. Each specialist has one primary professional boundary. Review roles are read-only by default. Implementation roles never perform their own independent final review.

## Workflow Model

Workflows orchestrate processes. Skills provide reusable domain capability only. A process must not be duplicated across commands, prompts, hooks, skills, or agents.

The reusable domain Skills include `mobile-architecture` for architecture review support and `mobile-code-review` for independent final review support. Workflows reference code review only when independent final review is required; implementation owners never review their own work.

## Cross-File Checks

JSON Schema validation confirms local manifest shape only. The host must separately verify that referenced `schema`, `tools`, `agents`, `subagents`, `skills`, `workflows`, policy files, and provider or MCP examples exist, remain inside `local/mobile-development/`, and match the referenced IDs. Missing or ambiguous references fail closed.

## Evidence and Completion

Every workflow must classify completion criteria as `required`, `conditionally-required`, or `not-applicable` with a reason. Claims about compilation, testing, linting, security, accessibility, localization, or performance require evidence from discovered project commands or are reported as unavailable.

## Security

The specialization protects secrets, signing material, private endpoints, local environment files, production data, and authenticated sessions. It distinguishes public mobile client configuration from genuine secrets, but adding or changing client configuration still requires human review.

Hooks never execute commands, modify source, use network, or approve actions. They return findings for the host to enforce.
