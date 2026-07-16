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
