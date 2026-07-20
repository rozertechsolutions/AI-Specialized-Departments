# OpenAI Agents SDK - Software Development

The Software Development department is a human-reviewed Python reference implementation for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package represents the department with OpenAI Agents SDK agents-as-tools, typed inputs/outputs, guardrails, policy helpers, and deterministic tests. It is safe by default: hosts inject models and tools, no API key is required for tests, and the package implements no server, CLI, UI, shell, Git, MCP, deployment, publication, signing, or release action.

## Department Overview

Use this package as SDK source for a stack-agnostic software-development orchestration pattern. It covers backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, documentation, and release readiness. Browser-specific Web Development and mobile-platform Mobile Development remain separate.

## Possible Uses

- Embed a Lead-plus-specialists department in a host application.
- Validate requirements, architecture, implementation evidence, code-quality review, risk review, and release-readiness state.
- Test safe repository-scope checks, approval decisions, call limits, and evidence-backed final records without calling external models.
- Prototype host integration before injecting real models or tools.

## Included Components

- `pyproject.toml`: Python package metadata and bounded Agents SDK dependency.
- `src/software_development_department/models.py`: typed task, evidence, role output, approval, action, and final-record models.
- `src/software_development_department/agents.py`: native SDK construction for one Lead and seven specialists exposed through `Agent.as_tool()`.
- `src/software_development_department/orchestrator.py`: bounded Lead runtime and specialist-call limits.
- `src/software_development_department/guardrails.py`: input/output guardrails and proposed-action approval metadata.
- `src/software_development_department/policies.py`: approval, scope, path, and evidence policies.
- `src/software_development_department/tools.py`: host-injected tool protocols plus deterministic inert fakes.
- `src/software_development_department/skills.py` and `workflows.py`: source-only capability and workflow definitions.
- `tests/`: deterministic `unittest`-discoverable tests for public SDK use and local safety behavior.

## Prerequisites

Use Python 3.10 or newer and a virtual environment. Install the declared `openai-agents` version range exactly as pinned by your lock or verification process. A host application must provide any real model, repository reader/writer, approval UI, or operational tool. Human approval is required before writes, commands, Git mutation, dependency changes, external services, deployment, publication, signing, release, or destructive actions.

## Installation or Setup

1. Create and activate a virtual environment outside source control.
2. From `openai-agents-sdk/software-development/`, install dependencies with your package manager, respecting `pyproject.toml`.
3. For local source execution without editable install, set `PYTHONPATH=src`.
4. Keep API keys and model/provider configuration in the host environment, not in this package.
5. Inject safe model and tool implementations explicitly from the host; do not expose shell, Git, network, deployment, publication, signing, credential, or unrestricted filesystem tools by default.

## Usage

Import the package, build the department agents, and run the Lead only from a host that supplies models/tools and handles SDK human-in-the-loop approvals.

Example requests for a host:

- "Construct the Lead and seven specialists with deterministic test models."
- "Run a scoped task and reject a proposed write to confirm no tool executes."
- "Require independent code-quality and risk evidence before final completion."

Run offline deterministic tests with:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Operating Model

The Lead remains the top-level agent. The seven specialists are exposed as tools, not handoffs, so typed results return to the Lead. Implementation evidence does not count as independent review. Completion requires typed evidence, validation status, human decisions, limitations, and explicit stop state.

## Safety and Human Review

Use least privilege. Paths are normalized against an injected workspace root and reject absolute paths, traversal, ambiguous components, and symlink escapes. Sensitive `ProposedToolAction` values require approval; denial returns a safe result and executes nothing. SDK textual guardrails do not replace host enforcement, sandboxing, or human review.

## Platform Limitations

This is source code, not a production service. It includes no real API invocation, credentials, account identifiers, endpoints, fixed model, UI, CLI, server, installer, shell tool, Git tool, network tool, MCP server, deployment, publication, signing, release, purchase, submission, or external communication implementation. Real HITL approval/resume must be wired by the host through the Agents SDK.

## Updating and Removal

To update, merge `pyproject.toml`, `src/`, `tests/`, and README changes while preserving host-specific integration code outside this package. To remove, delete `openai-agents-sdk/software-development/` from the copied destination and remove any host import references. Credentials and integrations are not stored here.
