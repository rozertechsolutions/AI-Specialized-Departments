# Qwen Code Data and AI Specialization

## Purpose
This package implements a native Qwen Code Data and AI specialization for strategy, governance, data architecture, datasets, data platforms, analytics, data science, ML, GenAI/RAG, AI applications, MLOps/LLMOps, evaluation, responsible AI, human oversight, and independent assurance.

Supported native product surface:
- `QWEN.md` project instructions.
- `.qwen/settings.json` project settings, permissions, MCP exclusion, and local hook registration.
- `.qwen/agents/*.md` declarative subagents.
- `.qwen/skills/*/SKILL.md` Agent Skills.
- `.qwen/commands/*.md` custom commands.
- `.qwen/hooks/data-ai-safety-guard.py` deterministic local PreToolUse hook.

No active MCP servers, authentication, providers, model selection, extensions, scheduled tasks, unattended loops, model downloads, external endpoints, deployments, or production integrations are configured.

## Installation and Discovery
Open this directory with Qwen Code:

```sh
cd qwen-code/data-ai
qwen
```

Qwen Code discovers project instructions from `QWEN.md`, project subagents from `.qwen/agents/`, Skills from `.qwen/skills/`, commands from `.qwen/commands/`, and settings/hooks from `.qwen/settings.json`. Project subagents take precedence over user-level agents.

## Component Map
Subagents:
- `data-ai-orchestrator`
- `data-ai-solution-governance-reviewer`
- `data-architecture-dataset-reviewer`
- `data-platform-analytics-reviewer`
- `ml-genai-evaluation-reviewer`
- `ops-risk-assurance-reviewer`

Skills:
- `use-case-risk-triage`
- `data-contract-dataset-readiness`
- `pipeline-analytics-quality`
- `analytics-experiment-review`
- `ml-genai-evaluation`
- `ops-risk-assurance`

Commands:
- `use-case-intake-triage`
- `source-dataset-component-onboarding`
- `data-contract-dataset-acceptance`
- `pipeline-analytics-quality`
- `analytics-experiment-lifecycle`
- `ml-genai-release-review`
- `ops-risk-monitoring-rollback`
- `final-data-ai-assurance`

Hook:
- `data-ai-safety-guard`

## Invocation and Delegation
Start with `data-ai-orchestrator`. It classifies scope, records assumptions, identifies owners, and delegates bounded review to non-overlapping specialists. Specialists return evidence-based findings and cannot approve their own work. `ops-risk-assurance-reviewer` owns operational risk and final independent assurance.

Use Skills for reusable procedures and commands for explicit lifecycle workflows. Completion status must be exactly `PASS`, `FAIL`, or `BLOCKED`.

## Permissions and Safety
Project settings disable managed auto memory, auto skills, team memory, interactive shell, computer use, MCP, selected slash commands, telemetry, cron, agent teams, and artifacts. Shell, web, MCP, protected path, and secret-like tool inputs are denied. Edits and subagent use require approval.

Subagents run in `approvalMode: plan`, use read/search tools only, disallow shell/write/edit/MCP tools, and do not configure a model override. The local hook is deterministic, network-free, and non-destructive.

Human review is required for high-impact decisions and any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, credentialed, or production action. Evidence must support all quality, statistical, causal, model, benchmark, cost, latency, robustness, fairness, compliance, and readiness claims.

## Optional Integrations
Optional MCP servers, extensions, providers, authentication, model settings, scheduled tasks, memory sync, tools, or shell permissions must be enabled manually outside this default package after human review of data exposure, cost, provider terms, permission boundaries, monitoring, rollback, and approval obligations. Keep secrets and private endpoints out of this repository.

## Limitations
Behavior depends on the installed Qwen Code version, account/auth state, folder trust, manually selected model/provider outside this package, terminal/IDE surface, operating system, and enabled tools. This package supplies static project configuration and instructions; it does not perform model inference, external API calls, data profiling, benchmark execution, deployment, publication, or production mutation.

Unsupported capabilities are omitted rather than simulated.

## Verification
Maintainers may run these checks from the repository root:

```sh
find qwen-code/data-ai -type f | sort
find qwen-code/data-ai -type f -name '*.md' -exec test -s {} \;
jq empty qwen-code/data-ai/.qwen/settings.json
python3 - <<'PY'
from pathlib import Path
compile(Path('qwen-code/data-ai/.qwen/hooks/data-ai-safety-guard.py').read_text(), 'data-ai-safety-guard.py', 'exec')
PY
```

Expected result: JSON parses, Markdown is non-empty, hook code compiles and denies unsafe payloads, all subagent/Skill/command artifacts are present, MCP/provider/auth/model configuration is absent, and no generated validation artifacts remain.
