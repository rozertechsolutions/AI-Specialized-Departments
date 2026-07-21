# OpenAI Agents SDK - Software Development

<<<<<<< HEAD
This directory is source code for the Software Development specialization on the OpenAI Agents SDK. It is not a deployed service. It is language-, framework-, database-, provider-, model-, and vendor-agnostic. It contains no API key, endpoint, model pin, server, CLI, UI, deployment asset, installer, hook, or operational automation.
=======
The Software Development department is a human-reviewed Python reference implementation for requirements, planning, architecture, implementation, validation, independent code review, engineering risk review, documentation, and release readiness. This package represents the department with OpenAI Agents SDK agents-as-tools, typed inputs/outputs, guardrails, policy helpers, and deterministic tests. It is safe by default: hosts inject models and tools, no API key is required for tests, and the package implements no server, CLI, UI, shell, Git, MCP, deployment, publication, signing, or release action.
>>>>>>> feature/software-development

## Department Overview

<<<<<<< HEAD
- `agents.py` builds one Software Development Lead and seven specialists.
- The Lead remains the active top-level agent. Specialists are exposed through `Agent.as_tool()` so their typed results return to the Lead without transferring the conversation.
- Every specialist has a role-specific typed output model. The Lead has a typed `LeadFinalRecord` output containing requirements, plan, implementation evidence, validation evidence, code review, risk review, documentation/release readiness, limitations, and human decisions.
- `orchestrator.py` applies bounded orchestration limits, host-injected context, SDK interruption inspection, `result.to_state()`, `RunState.approve()`, `RunState.reject()`, resumed `Runner.run()`, and explicit stop states.
- `guardrails.py`, `policies.py`, and `tools.py` separate task text from concrete proposed actions. Keyword mentions such as credentials, deployment, deletion, signing, or release do not block legitimate analysis by themselves.
=======
Use this package as SDK source for a stack-agnostic software-development orchestration pattern. It covers backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, controlled refactoring, tests, security, dependencies, performance, reliability, compatibility, migrations, documentation, and release readiness. Browser-specific Web Development and mobile-platform Mobile Development remain separate.
>>>>>>> feature/software-development

## Possible Uses

<<<<<<< HEAD
Models, repository tools, workspace root, run limits, and approvals are host-injected. `tools.py` defines protocols, SDK `function_tool` wrappers, and deterministic in-memory fakes for tests only. No operational tool is enabled by default, and the package does not implement shell, Git, network, deployment, publication, signing, credential, unrestricted filesystem, or external communication clients.

Sensitive concrete actions use the Agents SDK human-in-the-loop approval flow. Tool calls that require approval surface as `result.interruptions`; the runtime converts the result with `result.to_state()`, exposes pending decisions to the host, applies `RunState.approve()` or `RunState.reject()`, and resumes the original Lead run. Rejected required actions stop safely and are not executed.
=======
- Embed a Lead-plus-specialists department in a host application.
- Validate requirements, architecture, implementation evidence, code-quality review, risk review, and release-readiness state.
- Test safe repository-scope checks, approval decisions, call limits, and evidence-backed final records without calling external models.
- Prototype host integration before injecting real models or tools.

## Included Components
>>>>>>> feature/software-development

- `pyproject.toml`: Python package metadata and bounded Agents SDK dependency.
- `src/software_development_department/models.py`: typed task, evidence, role output, approval, action, and final-record models.
- `src/software_development_department/agents.py`: native SDK construction for one Lead and seven specialists exposed through `Agent.as_tool()`.
- `src/software_development_department/orchestrator.py`: bounded Lead runtime and specialist-call limits.
- `src/software_development_department/guardrails.py`: input/output guardrails and proposed-action approval metadata.
- `src/software_development_department/policies.py`: approval, scope, path, and evidence policies.
- `src/software_development_department/tools.py`: host-injected tool protocols plus deterministic inert fakes.
- `src/software_development_department/skills.py` and `workflows.py`: source-only capability and workflow definitions.
- `tests/`: deterministic `unittest`-discoverable tests for public SDK use and local safety behavior.

<<<<<<< HEAD
The package enforces least privilege by construction: specialists cannot delegate, the Lead aggregates final evidence, implementation does not count as independent review, and output guardrails require typed evidence rather than unsupported completion claims. Candidate paths are normalized against an injected workspace root; absolute paths, traversal, ambiguous components, and scope escapes are rejected. Hosts that implement repository access must resolve real paths and enforce the workspace boundary, including symlink escapes.

Compatibility target: `openai-agents>=0.18.3,<0.19` on Python 3.10 or newer. Verification is performed with exactly `openai-agents==0.18.3`, deterministic injected fake model responses, and `OPENAI_AGENTS_DISABLE_TRACING=1`; no API key, external model call, or external service is required. Test verification creates a temporary environment that must be deleted after the run.
=======
## Prerequisites
>>>>>>> feature/software-development

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
