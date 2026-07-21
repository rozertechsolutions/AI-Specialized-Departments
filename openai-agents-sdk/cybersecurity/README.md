# Cybersecurity Department for OpenAI Agents SDK

This Cybersecurity department is a Python SDK implementation for building static, human-reviewed cybersecurity agents with the OpenAI Agents SDK. It helps application teams create evidence-based cybersecurity work products without granting the AI authority to approve risk, run tools, contact providers, or act on live systems.

Possible uses include governance, risk, compliance, and assurance support; security architecture and engineering review; application, product, and DevSecOps security review; exposure, vulnerability, and hardening planning; defensive operations, detection, and threat-intelligence analysis; incident response, DFIR, and recovery planning; explicitly authorized offensive validation planning; and resilience or specialized-technology assurance.

## Department overview

The department contains eight installable Python packages under `openai-agents-sdk/cybersecurity/<area>/`. Each package exposes typed Pydantic output models, OpenAI Agents SDK `Agent` builders, input and output guardrails, `RunConfig` construction, explicit human-approval helpers, and string-based `RunState` persistence helpers.

The SDK components are for application integration. They are not repository-autoloaded coding-agent files and they do not execute by being present in this repository. The AI is not authorized to accept enterprise risk, approve exceptions, authorize offensive testing, approve production changes, close incidents, certify compliance, make legal determinations, or claim live execution without supplied evidence.

## Possible uses

- Build a static GRC review coordinator for supplied control evidence and policy mappings.
- Construct architecture or product-security review agents inside an internal governance app.
- Use guardrails to reject missing authorization, credential-bearing prompts, active scan requests, production-changing requests, and unsupported completion claims.
- Serialize an interrupted HITL review state and restore it later after a human decision.
- Create independent-review workflows that separate creator, reviewer, approver, evidence state, limitations, and residual risk.

## Platform compatibility

Surface: OpenAI Agents SDK for Python, not ChatGPT Projects, Codex, an IDE extension, or a repository-discovered agent format.

Validated on 2026-07-21 with `openai-agents==0.18.3` and `pydantic==2.13.4`. The package metadata supports `openai-agents>=0.18.3,<0.19` and `pydantic>=2.13,<3`; this intentionally avoids a broad pre-1.0 SDK range because the code depends on current guardrail, HITL, `RunConfig`, `Agent.as_tool(needs_approval=True)`, and async `RunState.from_string(...)` behavior.

Python 3.11 or newer is required by the area packages. Repository validation does not require `OPENAI_API_KEY` and does not call a model. A downstream application supplies its own model/provider credentials later, outside this repository, when it intentionally runs agents in an authorized environment.

## Prerequisites

- Python 3.11+.
- A project-local virtual environment.
- `pip` or another Python installer capable of installing local packages.
- No API key for imports, construction, static guardrail tests, HITL helper tests, or persistence tests.

Do not commit credentials, tracing API keys, private endpoints, personal data, customer evidence, incident artifacts, or organization-confidential values to this repository.

## Installation or import

Install only the areas your application needs. From the repository root:

```bash
python3 -m venv .venv-openai-agents-sdk-cyber
source .venv-openai-agents-sdk-cyber/bin/activate
python -m pip install -e openai-agents-sdk/cybersecurity/governance-risk-compliance-assurance
```

Application code imports the package explicitly:

```python
from cybersecurity_governance_risk_compliance_assurance_agents import (
    build_coordinator,
    build_default_run_config,
    evaluate_static_request,
    restore_state,
    serialize_state,
)

coordinator = build_coordinator(model="your-approved-model")
run_config = build_default_run_config()
decision = evaluate_static_request(
    "Authorized scope: review supplied SOC 2 evidence for control gaps.",
    authorized_scope="SOC 2 evidence review",
)
```

This creates SDK objects only. It does not call `Runner.run`, authenticate a provider, connect MCP, start tools, or contact external systems.

## Working directory and discovery

The SDK does not auto-discover `openai-agents-sdk/cybersecurity/` from a working directory. Python discovery occurs through package installation or `PYTHONPATH`.

Use the repository root when installing local packages with the relative paths above. Treat each area as an isolated package rooted at `openai-agents-sdk/cybersecurity/<area>/`. The `src/<package_name>/registry.py` module is the native implementation. `docs/ROLES.md` and `docs/SKILLS.md` are static operational documentation and are not automatically loaded by the SDK.

There is no SDK precedence between areas. Your application decides which area package to import and how to route cross-area handoffs.

## Area map

- `openai-agents-sdk/cybersecurity/governance-risk-compliance-assurance/` - Governance, cyber risk, compliance mapping, policies, assurance, exceptions, and risk-decision support.
- `openai-agents-sdk/cybersecurity/security-architecture-engineering/` - Security architecture, engineering patterns, identity, network, cloud, data, platform, and control design review.
- `openai-agents-sdk/cybersecurity/application-product-devsecops-security/` - Product security, secure SDLC, threat modeling, code/design review, CI/CD, supply chain, PSIRT, and release assurance.
- `openai-agents-sdk/cybersecurity/exposure-vulnerability-hardening/` - Asset exposure, vulnerability triage, prioritization, hardening, remediation governance, and validation evidence.
- `openai-agents-sdk/cybersecurity/defensive-security-operations-detection-intelligence/` - SOC operating model, telemetry, detection engineering, alert triage, hunting, intelligence, and coverage quality.
- `openai-agents-sdk/cybersecurity/incident-response-dfir-recovery/` - Incident planning, evidence governance, DFIR planning, containment planning, recovery coordination, and lessons learned.
- `openai-agents-sdk/cybersecurity/offensive-security-authorized-validation/` - Explicitly authorized assessment planning, rules of engagement, emulation governance, retest planning, and safety review.
- `openai-agents-sdk/cybersecurity/cyber-resilience-specialized-technologies/` - Resilience, ransomware recovery planning, OT/ICS, IoT/embedded, AI security, hardware/firmware, cryptographic agility, and critical-infrastructure assurance.

## Native components

Each area contains:

- `pyproject.toml` - installable Python package metadata and validated dependency range.
- `src/<package_name>/registry.py` - SDK builders, typed output models, guardrail helpers, HITL helpers, and persistence helpers.
- `src/<package_name>/__init__.py` - public exports for application imports.
- `docs/ROLES.md` and `docs/SKILLS.md` - static role and procedure documentation for implementers.

The platform-level `tests/` directory contains offline validation tests for all eight packages.

## How to use the department

Select the area that owns the work, install that package, and call its registry builders. Provide authorized scope, exclusions, accountable owner, requester, intended audience, evidence inventory, assumptions, constraints, reviewer, approver role, and the human decision being supported.

Use `build_specialists()` from the registry when an application needs individual role agents. Use `build_coordinator()` when an application wants the area coordinator to expose specialists through `Agent.as_tool(..., needs_approval=True)`. Use `build_default_run_config()` to keep tracing disabled in the baseline.

Example HITL persistence contract:

```python
from agents import RunState

saved_state = serialize_state(run_state)  # string from RunState.to_string()
restored_state = await restore_state(coordinator, saved_state)
assert isinstance(restored_state, RunState)
```

`restore_state` is intentionally async because OpenAI Agents SDK `RunState.from_string(...)` is async. Do not treat it as a synchronous helper. Persisted state can include application context and trace or tool metadata; store it deliberately, encrypt it where appropriate, and avoid including tracing API keys or secrets.

## Permissions and safety

The baseline SDK objects have no MCP servers, no hosted tools, no shell tools, no computer tools, no scanners, no cloud connectors, and no default network integrations. Repository validation monkeypatches `Runner.run`, `Runner.run_sync`, and `Runner.run_streamed` as forbidden paths.

Guardrails block or flag missing authorization, active scan or exploitation requests, credential-bearing requests, production-changing requests, outputs without evidence, unsupported approval claims, and low-confidence completion claims. Human approval helpers require a selected interruption and never set `always_approve` or `always_reject`.

## Configuration and customization

### Project-dependent configuration

Adapt repository paths, source directories, application architecture, technology stack, deployment model, CI/CD structure, telemetry locations, assets, threat-model scope, approved targets, evidence locations, and area-specific working directories in your application layer. Do not hard-code those values into the reusable baseline.

### User/organization-dependent configuration

Supply account, subscription, user identity, organization policies, frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, API credentials, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, authorized offensive-testing scope, data-retention requirements, and legal/privacy constraints outside this repository. Real secrets and confidential values must not be committed.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, disabled tracing by default, no MCP/hosted/shell/computer tools by default, prohibited unauthorized actions, stop conditions, and human-approval gates unless a formal governance review approves a change.

## Validation

Static validation covers Python AST parsing, package imports, SDK object construction, `RunConfig` construction, guardrail helper behavior, HITL helper behavior with fakes, API signature checks, string persistence using `RunState.to_string()` and awaited `RunState.from_string(...)`, and forbidden-runtime checks. It does not run an agent, call a model, authenticate, start MCP, use hosted tools, connect a scanner, or touch a live target.

Run the shared offline tests from a disposable environment after installing all eight area packages:

```bash
python -m pytest -q -p no:cacheprovider openai-agents-sdk/cybersecurity/tests
```

## Troubleshooting

- If an import fails, confirm the selected area package was installed from its exact `openai-agents-sdk/cybersecurity/<area>/` path.
- If `restore_state(...)` appears to return a coroutine, the caller forgot to `await` it.
- If dependency resolution selects an older SDK, check that the installed package honors `openai-agents>=0.18.3,<0.19`.
- If `Agent.as_tool(..., needs_approval=True)` fails, re-check the installed SDK minor version against `NATIVE_SOURCES.md`.
- If a downstream app wants live execution, configure credentials, model provider, storage, approvals, and retention outside this repository and run only in an authorized environment.

## Removal or uninstall

Uninstall the area packages from the project-local environment:

```bash
python -m pip uninstall cybersecurity-governance-risk-compliance-assurance-agents
```

Repeat for any other installed area package, then remove the virtual environment if it is no longer needed. Delete the repository directory only if the organization no longer wants the reusable source package. Do not delete organizational evidence, persisted HITL state, audit logs, or application configuration without explicit human authorization.

## Limitations

This package is a static SDK baseline, not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing tool, incident-response platform, legal opinion, compliance certification, or production-control system. OpenAI Agents SDK is pre-1.0, so minor releases can change APIs; validate the supported dependency range before upgrading.

## Security notice

Offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and use of sensitive evidence require explicit authorization, validated scope, and human control. Do not use these components to bypass approval, access secrets, contact external systems, or claim live execution without evidence.
