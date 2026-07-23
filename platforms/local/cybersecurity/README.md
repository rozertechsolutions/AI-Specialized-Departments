# Local Cybersecurity Department

This Cybersecurity department is a provider-neutral, runtime-neutral specification package for local implementations. It covers governance, risk, compliance, assurance, security architecture and engineering, application/product/DevSecOps security, exposure and hardening, defensive operations and intelligence, incident response and recovery, authorized offensive validation, and resilience or specialized technology security.

It solves the problem of giving implementers a reusable cybersecurity contract that can be mapped into their own local runner, documentation system, orchestration layer, or review process without binding the repository to Ollama, LM Studio, a specific model, a vector store, an endpoint, or a commercial AI platform. Possible uses include policy review, control mapping, risk exception support, architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection planning, incident readiness, authorized validation planning, resilience review, and independent assurance.

## Department Overview

The department contains eight area packages under `local/cybersecurity/<area>/`. Each area provides project-defined YAML contracts, JSON Schema definitions, role manifests, Skill definitions, workflows, tools, policies, and Markdown specifications for static cybersecurity work.

The local package defines contracts only. It does not provide a model, runner, server, vector database, credential store, connector, scanner, shell integration, MCP server, or production integration. A human implementer remains accountable for runtime mapping, authorization, validation, approvals, risk decisions, and operational controls.

## Possible Uses

- Use `local.yaml` as the area manifest for a custom internal runner.
- Validate role, Skill, workflow, tool, and policy YAML files against the retained JSON Schemas.
- Map the neutral contracts into an organization's own review workflow.
- Generate static decision packages, evidence requests, review checklists, and assurance artifacts.
- Use the portable `SKILL.md` files as human-readable procedures or as input to a compatible Skill system.

## Platform Compatibility

Validated on 2026-07-21 against the repository-defined local contracts and JSON Schema Draft 2020-12 declarations embedded in `schemas/*.schema.json`.

Supported local surface:

- Provider-neutral YAML manifests.
- JSON Schema Draft 2020-12 schema files.
- Static Markdown specifications and Skill procedure files.
- Implementation-defined runners that deliberately map these contracts into their own environment.

Unsupported by design:

- Bundled model providers, endpoints, local model servers, vector stores, orchestration frameworks, cloud services, scanners, connectors, MCP servers, hooks, and production automation.

## Prerequisites

- A repository checkout.
- A YAML parser and JSON Schema validator selected by the implementer for local validation.
- A human-approved implementation plan before mapping the contracts into any runtime.
- Redacted static evidence for review work.

No provider account, API key, model, local model server, endpoint, connector, scanner, cloud account, SIEM/EDR/XDR/SOAR system, ticketing system, or production access is required by this baseline.

## Installation Or Import

Use one area at a time.

For static review:

1. Open the selected area, for example `local/cybersecurity/governance-risk-compliance-assurance/`.
2. Read `SPECIFICATION.md` when present, then `local.yaml`.
3. Load the area `policies/`, `agents/`, `skills/`, `workflows/`, `tools/`, and `schemas/` files as static contract inputs.
4. Provide redacted project evidence and an explicit scope.
5. Produce only static artifacts and human decision packages.

For a custom local runner:

1. Choose the runner outside this repository.
2. Map `local.yaml` and each YAML contract field into the runner's native configuration.
3. Validate YAML syntax and JSON Schema constraints before use.
4. Keep `runtime_binding: none` in the reusable baseline; store runtime-specific bindings in the consuming project.
5. Add credentials, endpoints, connectors, and tool integrations only in the consuming environment after human approval.

## Working Directory And Discovery

No AI platform auto-discovers `local/cybersecurity/`. Consumers load files deliberately.

Recommended launch or import directory:

```text
local/cybersecurity/<area>/
```

Area-local references are relative to that selected area. For example, `agents/grc-coordinator.yaml` may reference `subagents/governance-policy-frameworks-agent.yaml`, `policies/permissions.yaml`, or `tools/project-read.yaml`.

Precedence is implementation-defined, but a safe default is:

1. `local.yaml`.
2. area policies.
3. coordinator or primary agent.
4. selected subagent or Skill.
5. selected workflow.
6. output artifact schema.

Do not mix area contracts unless a human explicitly approves a cross-area handoff.

## Area Map

- `governance-risk-compliance-assurance/`: governance, policy, control mapping, compliance, risk records, exceptions, assurance, evidence, suppliers, maturity, and reporting.
- `security-architecture-engineering/`: security architecture, engineering patterns, identity, cloud, network, data, containers, infrastructure as code, automation, and architecture assurance.
- `application-product-devsecops-security/`: product security, secure SDLC, threat modeling, secure code/design review, CI/CD, software supply chain, PSIRT, release readiness, and appsec assurance.
- `exposure-vulnerability-hardening/`: exposure management, vulnerability triage, prioritization, hardening, remediation governance, validation, and reporting.
- `defensive-security-operations-detection-intelligence/`: SOC governance, telemetry, detection engineering, triage, hunting, intelligence, malware-analysis planning, automation review, and coverage quality.
- `incident-response-dfir-recovery/`: incident command, evidence governance, DFIR planning, containment planning, recovery coordination, scenarios, crisis review, and corrective action.
- `offensive-security-authorized-validation/`: authorization, scope, rules of engagement, assessment planning, deconfliction, emulation, Purple Team validation, findings, cleanup, retest, and safety review.
- `cyber-resilience-specialized-technologies/`: resilience programs, ransomware recovery, backups, specialized technology security, OT/ICS, IoT, embedded, AI systems, firmware, cryptographic agility, critical infrastructure, and transition governance.

## Native Components

Native to this local package:

- `local.yaml`: provider-neutral area manifest.
- `schemas/*.schema.json`: project-defined JSON Schema contracts.
- `agents/*.yaml`: coordinator and role contracts.
- `subagents/*.yaml`: lightweight delegation contracts where the area includes explicit subagent mappings.
- `skills/*.yaml`: structured Skill contracts where present.
- `skills/*/SKILL.md`: portable human-readable Skill procedures.
- `workflows/*.yaml`: manual static workflows.
- `tools/*.yaml`: static tool capability contracts where present.
- `policies/*.yaml` and `policies/*.md`: safety, permissions, evidence, and security policy contracts.
- `SPECIFICATION.md`: area specification where present.

Project-defined fields such as `static_only`, `manual_static_only`, `provider_neutral`, and `runtime_binding` are valid local contract fields. They are not vendor configuration fields and should not be removed merely because a commercial platform does not use them.

## How To Use The Department

Select the area that owns the work and provide:

- authorized scope and explicit exclusions;
- accountable owner, requester, reviewer, approver role, and intended audience;
- evidence inventory with provenance, period, freshness, and limitations;
- decision needed, assumptions, constraints, and required output.

Example input:

```text
Using local/cybersecurity/exposure-vulnerability-hardening, map the uploaded static vulnerability export into an evidence-backed remediation plan. Scope is static review only. Exclude live scanning and ticket updates. Return normalized findings, prioritization rationale, evidence gaps, owner questions, and required human approvals.
```

Expected output is a scoped artifact with evidence tables, findings separated by evidence state, assumptions, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact, closure-facing, exception, release, incident, offensive, or external-facing outputs must go to an independent reviewer that did not create the artifact.

Stop when authorization is missing, evidence is unredacted or insufficient, scope is unclear, a live action is requested, an output would self-review, or a human-only decision is requested.

## Permissions And Safety

The baseline is static and read-only by default:

- `provider_neutral: true`.
- `runtime_binding: none`.
- `active_integrations: false`.
- `mcp_servers: []`.
- shell, network, and live system actions denied.

Repository writes, if a consuming implementation supports them, must stay inside the selected `local/cybersecurity/<area>/` directory and require an explicit user task to update static artifacts. Shell, network, installation, deployment, scanning, exploitation, recovery execution, remote Git operations, MCP connections, hosted tools, connectors, and external integrations are prohibited by default.

Human approval is required for risk acceptance, exception approval, policy publication, architecture approval, release readiness, incident declaration or closure, external distribution, supplier decisions, offensive authorization, production recovery, and critical finding closure.

## Configuration And Customization

### Project-dependent configuration

Adapt repository paths, source directories, application architecture, build systems, languages, deployment model, cloud provider, CI/CD structure, telemetry locations, asset inventory, data-flow scope, threat-model scope, vulnerability evidence, approved test scope, area-specific working directories, and repository-specific policies per consuming project.

### User/organization-dependent configuration

Supply or approve runner choice, account identity, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, API credentials, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, authorized offensive-testing scope, retention rules, and legal/privacy constraints outside this repository. Do not commit secrets or confidential values.

### Fixed baseline configuration

Keep provider neutrality, runtime neutrality, area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, static-by-default behavior, prohibited unauthorized actions, stop conditions, no live integrations by default, and human approval gates intact.

## Validation

Repository validation can check JSON parsing, YAML parsing, JSON Schema syntax, required area coverage, Skill frontmatter, file existence, exact duplicates, empty files, empty directories, and absence of provider-specific runtime bindings.

Runtime behavior, model behavior, connector behavior, scanner output, incident actions, recovery, and production changes require a separately authorized consuming implementation and were not executed by this repository package.

## Troubleshooting

- If a consuming runner cannot load an area, start from `local.yaml` in the selected area and resolve relative paths from that area directory.
- If a schema validator rejects a YAML file, confirm the correct project-defined schema is being used for that contract type.
- If a runner requires provider, model, endpoint, or vector-store settings, place those in the consuming project's private configuration, not in this reusable baseline.
- If permissions appear broader than intended, inspect the consuming runtime configuration and deny shell, network, MCP, connector, deployment, scanner, and remote Git access.
- If an area lacks a subdirectory such as `subagents/` or `tools/`, treat it as intentionally absent unless the selected area manifest references it.

## Removal Or Uninstall

Remove the selected `local/cybersecurity/<area>/` contracts from the consuming runner or delete the imported copy from the consuming project. Disconnect or delete any runtime-specific provider, endpoint, connector, MCP, vector-store, or credential configuration in the consuming environment according to that environment's approved process. Do not delete unrelated organization evidence or global runtime settings without human approval.

## Limitations

This package is a static professional baseline and contract set, not a runner, model, model server, vector store, orchestration framework, managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing platform, incident command system, recovery orchestrator, legal opinion, compliance certification, or production-control system.

## Security Notice

Explicit authorization and human control are mandatory for offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and sensitive evidence handling. Do not use this package to bypass approval, access secrets, contact external systems, or claim execution without evidence.
