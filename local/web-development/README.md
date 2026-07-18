# Web Development — Local Provider-Independent Package

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- Neutral department specification
- Role instructions
- Agent Skills
- Workflow specifications
- JSON Schemas
- Declarative permissions and disabled integration examples

## Intentionally omitted or disabled
- No runtime, model, provider, endpoint, command, token, tool, MCP server, or executable is selected
- No automatic discovery, installation or authentication

## Platform notes
This is a provider-independent configuration package, not an executable runtime or enforcement layer. A user or downstream open-source runtime must explicitly select the runtime, provider, and model, then map these neutral files to its own supported schema after review.

Disabled examples are non-binding extension points. They may be adapted to a local runtime such as Ollama, LM Studio, or another provider only after explicit user selection and review. This package does not require or prefer any model, provider, endpoint, local path, token, command, server, or network service.

Extension points are limited to roles, workflows, skills, schemas, and declarative policies. Downstream runtimes are responsible for enforcing permissions, disabled integrations, quality gates, and any approval workflow they choose to implement.

## Conformance expectations
- Validate `department.yaml` against `schemas/department.schema.json` after adapting it to a runtime that supports JSON Schema validation.
- Keep `provider_agnostic: true`, `default_state: disabled`, and `runtime_binding: none` unless a human explicitly selects and configures a downstream runtime outside this package.
- Treat reviewer roles as read-only unless a human reassigns implementation authority.
- Treat missing validation, measurements, approvals, or external execution as `NOT EXECUTED` or `BLOCKED`; never infer success.
- Preserve the disabled defaults in `policies/permissions.json` and `policies/integrations.json` until a downstream runtime implements explicit enforcement.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://json-schema.org/draft/2020-12
- https://openagentskills.dev/docs/specification
