# OpenAI Agents SDK Data and AI Specialization

## Purpose
This package implements a native OpenAI Agents SDK Data and AI specialization. It covers strategy, portfolio ownership, orchestration, solution architecture, governance, data architecture, datasets, data platforms, analytics, data science, ML, GenAI/RAG, AI applications, operations, evaluation, responsible AI, human oversight, and independent assurance.

Supported native product surface:
- Python package under `src/data_ai_agents_sdk/`.
- Real `Agent` objects created by `build_data_ai_agents()`.
- Explicit coordinator-to-specialist handoffs.
- Structured Pydantic input and output contracts.
- Input and output guardrails.
- A function tool that uses the SDK human-in-the-loop approval mechanism for sensitive action requests.
- Offline run configuration with hosted tracing disabled and sensitive trace capture disabled.
- Serialization helpers and offline tests.

## Installation and Discovery
From this directory, install only into an isolated environment:

```sh
python -m venv /tmp/openai-agents-sdk-data-ai-venv
/tmp/openai-agents-sdk-data-ai-venv/bin/python -m pip install -e ".[test]"
```

Import the package:

```python
from data_ai_agents_sdk import build_data_ai_agents, build_run_config

agents = build_data_ai_agents()
coordinator = agents["data-ai-orchestrator"]
run_config = build_run_config()
```

No API key, provider profile, server, web UI, database, background worker, deployment, MCP server, hosted tool, model download, or external endpoint is configured by default.

## Component Map
Coordinator:
- `data-ai-orchestrator`

Specialists:
- `data-ai-solution-governance-reviewer`
- `data-architecture-dataset-reviewer`
- `data-platform-analytics-reviewer`
- `ml-genai-evaluation-reviewer`
- `ai-ops-risk-reviewer`
- `data-ai-assurance-reviewer`

Native modules:
- `agents.py` builds the coordinator and specialists.
- `models.py` defines structured contracts and canonical `PASS`, `FAIL`, `BLOCKED` status.
- `guardrails.py` defines input/output guardrails.
- `tools.py` defines the human approval request tool.
- `tracing.py` disables hosted tracing for offline construction and tests.
- `serialization.py` round-trips structured review output.
- `workflows.py` declares lifecycle workflow contracts.

## Invocation and Delegation
Start with `data-ai-orchestrator`. It owns intake, decomposition, routing, dependency control, evidence collection, status, and stop conditions. It has handoffs to every specialist and no specialist has a reverse handoff, preventing circular delegation.

Specialists return `ReviewOutput` objects and must use exactly `PASS`, `FAIL`, or `BLOCKED`. Builders may test their work, but independent review and final assurance remain separate. The assurance reviewer verifies evidence, traceability, separation of duties, unresolved risk, human approvals, monitoring, rollback, and completion claims.

## Permissions and Safety
The package contains no shell tools, file mutation tools, hosted tools, MCP servers, connectors, or provider configuration. The included function tool only creates a human approval request and is configured with `needs_approval`; it does not perform the sensitive action.

Guardrails block secret-like inputs or outputs and unsupported completion claims without evidence. Human approval is required for high-impact decisions and any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, credentialed, or production action. Tracing is disabled in code and run config for offline tests, and sensitive trace capture is disabled.

## Optional Integrations
To run model-backed flows, a maintainer must separately provide an OpenAI API key, model configuration, tracing policy, deployment/runtime host, persistence, external tools, or MCP servers. Keep those integrations outside the default package until human review confirms data exposure, cost, provider terms, approval boundaries, and monitoring obligations.

## Limitations
This package constructs SDK objects and validates offline contracts. It does not call a model, run inference, contact OpenAI APIs, enable hosted tracing, execute external tools, profile data, benchmark models, deploy services, mutate production, or persist run state. Runtime behavior depends on the installed `openai-agents` version, Python version, account/API availability, model choice, tracing settings, and any separately enabled tools or storage.

Unsupported capabilities are omitted rather than simulated.

## Verification
From this directory in a disposable environment:

```sh
python -m pip install -e ".[test]"
python -m pytest
```

Expected result: package imports, SDK agents construct offline, coordinator handoffs are acyclic, guardrails and approval predicates are present, serialization round-trips structured output, lifecycle coverage is complete, tests make no model calls, and no temporary environment, caches, coverage files, or reports remain in the repository.
