# Mistral Vibe Data and AI Specialization

## Purpose
This package implements a native Mistral Vibe Data and AI specialization for strategy, governance, data architecture, datasets, data platforms, analytics, data science, ML, GenAI/RAG, AI applications, MLOps/LLMOps, evaluation, responsible AI, human oversight, and independent assurance.

Supported native product surface:
- Project configuration in `.vibe/config.toml`.
- Custom agents and subagents in `.vibe/agents/*.toml`.
- System prompts in `.vibe/prompts/*.md`.
- Agent Skills in `.vibe/skills/*/SKILL.md`.
- Project hook configuration in `.vibe/hooks.toml` with local hook code in `.vibe/hooks/`.
- Project instructions in `AGENTS.md`.

This package does not use deprecated Mistral Code Enterprise formats. It does not configure providers, API keys, profiles, telemetry choices, ACP installation, active MCP servers, connectors, model downloads, external endpoints, deployments, or production access.

## Installation and Discovery
Use `mistral-vibe/data-ai/` as the Vibe working directory:

```sh
cd mistral-vibe/data-ai
vibe
```

Vibe loads project `.vibe/config.toml`, `.vibe/hooks.toml`, `.vibe/agents/`, `.vibe/prompts/`, `.vibe/skills/`, and `AGENTS.md` only when the folder is trusted. In CLI automation, temporary trust is granted by the user with `vibe --trust` for that invocation only. The CLI, VS Code extension, and supported web/ACP surfaces share the same customization layer, but local filesystem and shell behavior depends on the surface.

The default interactive agent is `data-ai-orchestrator`. Skills are available as slash commands when the package is loaded from a trusted folder.

## Component Map
Default agent:
- `data-ai-orchestrator`

Independent specialist subagents:
- `data-ai-solution-governance-reviewer`
- `data-architecture-dataset-reviewer`
- `data-platform-analytics-reviewer`
- `ml-genai-evaluation-reviewer`
- `ai-ops-risk-reviewer`
- `data-ai-assurance-reviewer`

Skills:
- `use-case-risk-triage`
- `data-contract-dataset-readiness`
- `pipeline-analytics-quality`
- `analytics-experiment-review`
- `ml-system-evaluation`
- `genai-rag-agent-evaluation`
- `ai-ops-risk-readiness`
- `responsible-ai-assurance`

Hook:
- `data-ai-deny-unsafe-tooling`

## Invocation and Delegation
Start with the orchestrator for new Data and AI work. The orchestrator classifies scope, records assumptions, identifies owners, and delegates bounded review to the smallest applicable specialist. Specialists return evidence-based findings and cannot approve their own work. Final assurance belongs to `data-ai-assurance-reviewer`, which verifies traceability, evidence, separation of duties, unresolved risk, and completion claims.

Use Skills for repeatable workflows: use-case triage, source/dataset onboarding, data contracts, governed data products, analytics and experiments, ML evaluation, GenAI/RAG/agent evaluation, AI operations readiness, responsible AI, and final assurance. Completion status must be exactly `PASS`, `FAIL`, or `BLOCKED`.

## Permissions and Safety
The default configuration enables only `grep`, `read_file`, and `task`. It disables `bash`, `write_file`, `edit`, MCP tools, and connector tools. Tool permissions allow read/search automatically and require approval for delegation. The hook guard denies write-capable, shell, MCP, and connector tools by default and blocks tool input that appears to reference secrets or private key material.

Human review is required for high-impact decisions and any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, credentialed, or production action. The package requires provenance and permitted-use evidence for data, models, prompts, embeddings, libraries, and third-party components. It blocks fabricated data quality results, statistical significance, causal claims, model metrics, benchmarks, costs, latency, robustness, fairness, compliance status, and release readiness.

## Optional Integrations
Optional MCP servers, connectors, providers, models, profiles, API keys, telemetry choices, ACP installation, or IDE-specific setup must be enabled manually by a maintainer outside this package's default configuration. Keep every optional integration disabled until a human reviews the tool permissions, data exposure, cost, provider terms, and approval boundaries. Do not add secrets or live private endpoints to this repository.

## Limitations
Native behavior depends on the installed Vibe version, plan, account, trusted-folder state, CLI/VS Code/web surface, ACP client support, operating system, and available tools. Vibe Code Web uses a remote sandbox rather than the local working tree. The CLI and VS Code extension require a local install. Custom project configuration and `AGENTS.md` load only from trusted folders. This package provides static configuration and instructions; it does not perform model inference, runtime validation, data profiling, benchmark execution, external API calls, deployment, publication, or production mutation.

Unsupported capabilities are omitted rather than simulated.

## Verification
Maintainers may run these checks from the repository root:

```sh
find mistral-vibe/data-ai -type f | sort
find mistral-vibe/data-ai -type f -name '*.md' -exec test -s {} \;
python3 - <<'PY'
from pathlib import Path
compile(Path('mistral-vibe/data-ai/.vibe/hooks/data_ai_guard.py').read_text(), 'data_ai_guard.py', 'exec')
PY
cd mistral-vibe/data-ai && python3 ./.vibe/hooks/data_ai_guard.py <<'JSON'
{"tool_name":"read_file","tool_input":{"path":"README.md"}}
JSON
```

Validate TOML with any available TOML parser. If no parser is installed, use a disposable environment outside the repository, remove it immediately after validation, and verify deletion. Expected result: TOML parses, Markdown is non-empty, the hook passes safe read tool payloads, denies unsafe tool payloads, and no providers, API keys, active MCP servers, connectors, model downloads, credentials, or generated validation artifacts are present.
