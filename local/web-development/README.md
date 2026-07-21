# Web Development — Local

## Department overview

This is a provider-neutral local specification for a stack-aware Web Development department. It supports frontend, backend, full-stack architecture, APIs, authentication, accessibility, performance, SEO, testing, security, privacy, and release-readiness work without assuming one framework, model, provider, or runtime. Components are applicability-based; an adopting runtime maps only the relevant roles, workflows, Skills, and policies.

## Possible uses

- Discovering an existing web stack.
- Planning a web feature.
- Implementing or reviewing frontend changes.
- Designing or reviewing APIs, authentication, sessions, cookies, CSP, CORS, and privacy behavior.
- Debugging regressions.
- Auditing accessibility, performance, responsive behavior, and SEO.
- Reviewing dependencies and supply-chain risk.
- Preparing release-readiness evidence.
- Reviewing architecture and migration decisions.

## Supported product surface

This package is a static, provider-independent local specification. It is not executable by itself and has no automatic discovery behavior.

- `department.yaml`: neutral department manifest.
- `schemas/department.schema.json`: JSON Schema Draft 2020-12 schema for the manifest.
- `roles/*.md`: role instructions for an adopter to map into its runtime.
- `skills/*/SKILL.md`: Agent Skills using the open Agent Skills format.
- `workflows/*.md`: workflow specifications for manual or runtime-adapted invocation.
- `policies/*.json`: declarative, disabled-by-default policy examples.
- No runtime, model, provider, endpoint, command, token, tool, MCP server, executable, installer, or authentication is selected.

## Included native components

- `department.yaml`: provider-neutral department declaration.
- `instructions.md`: shared department instructions.
- `roles/*.md`: lead, implementation, architecture, review, and release-readiness role guidance.
- `skills/*/SKILL.md`: reusable web-development procedures.
- `workflows/*.md`: repeatable workflow specifications.
- `quality-gates.md`: quality and evidence gates.
- `policies/permissions.json`: disabled default permission policy.
- `policies/integrations.json`: disabled default integration policy.
- `schemas/department.schema.json`: schema for `department.yaml`.
- `README.md`: human setup and validation guide.

## Installation and integration

1. Copy `local/web-development/` into the target repository or local agent configuration repository.
2. Select a downstream runtime explicitly. This package does not prefer Ollama, LM Studio, llama.cpp, vLLM, OpenAI-compatible endpoints, or any hosted provider.
3. Map `department.yaml`, roles, Skills, workflows, and policies into the runtime’s supported configuration format.
4. Keep `provider_agnostic: true`, `default_state: disabled`, and `runtime_binding: none` unless a human explicitly adapts the package outside this source.
5. Preserve disabled policy defaults until the downstream runtime implements explicit enforcement and approval handling.
6. Validate the adapted manifest and all internal file references before use.

## How to use

Use this package as a source specification. An adopter can map `web-development-lead.md` to a coordinator, map specialist role files to runtime agents or prompts, expose `workflows/*.md` as manual commands, and import `skills/*/SKILL.md` as Agent Skills if the runtime supports them. Expected output should cite evidence, preserve provider neutrality, and mark unavailable execution as `NOT EXECUTED`.

## Operating model

The intended runtime first confirms scope, discovers the stack, maps the task to the relevant roles and workflows, keeps implementation and independent review separate, applies quality gates, and reports final `PASS`, `FAIL`, `BLOCKED`, `NOT APPLICABLE`, or `NOT EXECUTED` status with direct evidence. Downstream runtimes are responsible for enforcing permissions, disabled integrations, approval flows, and repository access.

## Safety and human approval

This package does not authorize automatic deployment, publication, authentication, secret use, spending, signing, submission, destructive operations, dependency installation, Git mutation, provider selection, model selection, endpoint use, MCP use, tool execution, shell commands, or production changes. Every sensitive or external action requires exact human authorization in the downstream runtime.

## Limitations

- Static specification only; no runtime enforcement is included.
- Schema validation checks the neutral manifest shape, not runtime behavior.
- Policies are declarative examples until an adopter implements enforcement.
- No runtime validation, browser checks, builds, tests, model calls, provider calls, MCP, shell commands, or deployment were executed.

## Validation

- Syntax validation: JSON policy files, JSON Schema, Skill frontmatter, and manifest key/value structure were parsed.
- Schema/static validation: `department.yaml` was checked against `schemas/department.schema.json` with local deterministic validation for the schema fields used here, and internal references were checked.
- Actual product loading: `NOT EXECUTED`.
- Runtime tests: `NOT EXECUTED`.
- Browser/build/deployment checks: `NOT EXECUTED`.

## Official documentation

Verified on July 20, 2026:

- JSON Schema: Draft 2020-12 - https://json-schema.org/draft/2020-12
- JSON Schema: Documentation - https://json-schema.org/learn
- Agent Skills: Specification - https://agentskills.io/specification
