# Local Cybersecurity GRC Assurance Specification

## Surface

- Specification ID: `ai-specialized-departments.local.cybersecurity.governance-risk-compliance-assurance`
- Specification version: `1.0.0`
- Surface: project-defined local configuration specification
- Runtime dependency: none
- Provider dependency: none

The `local/` platform is intentionally model/runtime independent. Ollama, LM Studio, llama.cpp, vLLM, SGLang, Llama, Gemma, Qwen, DeepSeek, GPT-OSS, and OpenAI-compatible servers are providers, runtimes, or models, not this platform.

## Discovery and Precedence

1. Read `local.yaml`.
2. Validate referenced manifests with `schemas/`.
3. Apply policies before agents, subagents, skills, workflows, or tools.
4. Treat all external integrations as absent until a human supplies a private, reviewed configuration.
5. Fail closed on malformed, ambiguous, or security-sensitive configuration.

## Native Capability Classification

Native:

- YAML manifests for roles, skills, workflows, policies, and tool contracts.
- JSON Schemas for static manifest validation.
- Static reference documentation.

Unsupported:

- Runtime execution, daemon management, external authentication, provider startup, model download, cloud fallback, MCP activation, hooks, scripts, regulator submission, risk acceptance, compliance certification, deployment, spending, destructive operations, and autonomous execution loops.

## Responsibility Model

The coordinator owns scope, sequencing, delegation, conflict resolution, validation synthesis, and final reporting. Each specialist has one primary professional boundary. Review roles are read-only by default. Implementation roles never perform their own independent final review.

## Workflow Model

Workflows orchestrate processes. Skills provide reusable domain capability only. A process must not be duplicated across commands, prompts, hooks, skills, or agents.

## Evidence and Completion

Every workflow must classify completion criteria as `required`, `conditionally-required`, or `not-applicable` with a reason. Claims about compliance, certification, audit readiness, control effectiveness, risk acceptance, testing, or remediation closure require supplied evidence and human approval or are reported as unavailable.

## Security

The specialization protects secrets, credentials, private endpoints, local environment files, customer data, employee data, audit evidence, vendor contracts, vulnerability data, and regulator communications. It distinguishes public framework references from protected evidence, but external distribution and formal claims still require human review.
