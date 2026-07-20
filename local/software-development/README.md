# Local - Software Development

The Software Development department is a human-reviewed, provider-neutral specification for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This Local package represents the department as declarative YAML specifications, JSON Schemas, examples, and documentation rather than a runtime. It is safe by default: all providers, runtimes, models, tools, integrations, endpoints, and credentials are disabled or unselected.

## Department Overview

Use this department to describe a stack-agnostic software engineering specialization that can be adapted to a local or private runtime. It covers backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, documentation, and release readiness. Browser-specific Web Development and mobile-platform Mobile Development remain separate.

## Possible Uses

- Validate a local department definition against schemas before adapting it to a runtime.
- Map requirements, architecture, implementation, validation, review, risk, documentation, and release-readiness responsibilities.
- Review provider/runtime selection boundaries, safety policy, human-review policy, quality gates, Skills, and workflows.
- Customize a private implementation without inheriting credentials, endpoints, or vendor assumptions.

## Included Components

- `spec/department.yaml`: manual-source department definition.
- `spec/capabilities.yaml`: manual-source capability map.
- `spec/roles/*.yaml`: manual-source role definitions for all eight responsibility areas.
- `spec/skills/*.yaml`: manual-source reusable capability definitions.
- `spec/workflows/*.yaml`: manual-source workflow definitions.
- `spec/policies/*.yaml`: manual-source safety, human-review, and quality-gate policy.
- `schemas/*.schema.json`: schema-required JSON Schema files for validation.
- `config/providers.example.yaml` and `config/runtime.example.yaml`: inert examples only, not selected runtime config.
- `docs/*.md`: auxiliary references for capability mapping and customization.

Nothing auto-loads or executes.

## Prerequisites

You need a local validation or integration process that can read YAML and JSON Schema. Any runtime, provider, model, tool, database, endpoint, or integration must be selected separately by a human or host application. Human approval is expected before enabling tools, file writes, shell execution, network access, credentials, Git mutation, deployment, publication, signing, release, or destructive operations.

## Installation or Setup

1. Copy `local/software-development/` into the destination documentation or configuration repository if you need a standalone source package.
2. Validate YAML files against the matching files in `schemas/` using your chosen local validator.
3. Treat `config/*.example.yaml` as examples to adapt manually; do not rename them into active runtime config unless your own host requires and approves that.
4. Select providers, models, tools, endpoints, and credentials outside this package through your host's secure configuration process.

## Usage

Use the YAML files as source-of-truth inputs for a local host or review process. Begin with `spec/department.yaml`, then read roles, policies, Skills, and workflows needed for the task.

Example requests:

- "Validate that our local implementation preserves all eight software-development responsibilities."
- "Review this runtime adapter against the safety and human-review schemas."
- "Map this workflow to our private tool host without adding provider defaults."

## Operating Model

The specification preserves the Software Development Lead plus seven specialist responsibility areas. The Lead owns intake, routing, approvals, dependency control, and final evidence aggregation. Implementation cannot certify itself; code-quality review and engineering-risk review are independent.

## Safety and Human Review

Use least privilege and do not store secrets in these files. Schemas and policy text are not runtime enforcement by themselves. A host implementation must enforce approvals for writes, commands, credentials, external services, Git, dependencies, deployment, publication, signing, release, spending, submissions, and destructive actions.

## Platform Limitations

This is not an installer, launcher, agent runtime, validator, server, CLI, hook, MCP server, or provider integration. It contains no real endpoints, credentials, account identifiers, model defaults, executable code, generated build outputs, or active environment configuration. Runtime behavior depends entirely on the host that imports the specification.

## Updating and Removal

To update, merge changed `spec/`, `schemas/`, `config/*.example.yaml`, and `docs/` files while preserving local adaptations. To remove, delete only this department's copied Local specification files. No integrations, credentials, providers, models, or endpoints are stored here.
