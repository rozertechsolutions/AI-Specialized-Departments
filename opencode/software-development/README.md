# OpenCode — Software Development

This directory implements the Software Development specialization for OpenCode using only platform-appropriate, repository-scoped content.

## Department scope

This specialization covers requirements analysis, architecture, backend services, APIs, desktop applications, command-line applications, libraries, SDKs, general-purpose software, implementation, maintenance, debugging, refactoring, testing, code quality, software security, dependencies, performance, reliability, technical documentation, and release readiness.

It does not replace the independent Web Development or Mobile Development specializations. Browser-specific frontend work and mobile-platform-specific implementation belong there. Shared or technology-agnostic code may be handled here when the task originates in Software Development.

The configuration is language-, framework-, database-, provider-, model-, and vendor-agnostic. It must inspect and respect the repository's existing stack instead of imposing one.

## Native content

- AGENTS.md
- opencode.jsonc project permissions
- .opencode/agents
- .opencode/skills
- .opencode/commands

## Manual or auxiliary content

- None.

## Intentionally omitted

- MCP configuration
- hooks
- automatic shell/web access
- global configuration or provider/model credentials

## Safe-by-default behavior

The package contains no executable hooks, active MCP servers, credentials, real endpoints, installers, launchers, deployment assets, release automation, or automatic authentication. External and sensitive actions require explicit human control.


## Installation

Copy this `software-development` directory to the corresponding platform directory in the repository. Follow the platform-specific manual steps described here. Do not execute generated scripts because this package contains none.

## Validation status

The package has been checked statically for file presence, non-empty content, JSON/TOML/YAML syntax where applicable, Python syntax, internal references, prohibited executable file types, and scope boundaries. Platform loading and runtime behavior were not executed.
