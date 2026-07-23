# OpenCode Data and AI Specialization

## Purpose
This package implements a native OpenCode Data and AI specialization for strategy, governance, data architecture, datasets, data platforms, analytics, data science, ML, GenAI/RAG, AI applications, MLOps/LLMOps, evaluation, responsible AI, human oversight, and independent assurance.

Supported native product surface:
- `AGENTS.md` durable project instructions.
- `opencode.json` project configuration and permissions.
- `.opencode/agents/*.md` bounded specialist agents.
- `.opencode/skills/*/SKILL.md` reusable Data and AI procedures.
- `.opencode/commands/*.md` explicit lifecycle workflow commands.

No active MCP servers, custom providers, credentials, share settings, plugins, global configuration, model downloads, deployments, or production integrations are configured.

## Installation and Discovery
Open this directory with OpenCode:

```sh
cd opencode/data-ai
opencode
```

OpenCode discovers `AGENTS.md`, `opencode.json`, `.opencode/agents/`, `.opencode/skills/`, and `.opencode/commands/` from the project. Use commands explicitly for lifecycle workflows and route review work through the configured subagents.

## Component Map
Agents:
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

## Invocation and Delegation
Start with `data-ai-orchestrator`. It classifies scope, records assumptions, identifies owners, and delegates bounded review to non-overlapping specialists. Specialists return evidence-based findings and cannot approve their own work. `ops-risk-assurance-reviewer` owns operational risk and final independent assurance.

Use Skills for reusable procedures and commands for explicit user-invoked lifecycle workflows. Completion status must be exactly `PASS`, `FAIL`, or `BLOCKED`.

## Permissions and Safety
The project denies `bash` and `webfetch` by default and requires approval for edits. Review specialists deny edits, shell, and web fetch. Destructive, Git, external, credentialed, deployment, publication, signing, submission, spending, and production actions remain prohibited unless a human explicitly changes project permissions outside this package.

Human review is required for high-impact decisions and any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, credentialed, or production action. Evidence must support all quality, statistical, causal, model, benchmark, cost, latency, robustness, fairness, compliance, and readiness claims.

## Optional Integrations
Optional MCP servers, plugins, custom providers, tools, credentials, share settings, or global configuration must be enabled manually outside the default package after human review of data exposure, cost, provider terms, permission boundaries, monitoring, rollback, and approval obligations. Keep secrets and private endpoints out of this repository.

## Limitations
Behavior depends on the installed OpenCode version, account/plan, local project trust, configured model/provider outside this package, editor/terminal surface, operating system, and manually enabled tools. This package supplies static project configuration and instructions; it does not perform model inference, external API calls, data profiling, benchmark execution, deployment, publication, or production mutation.

Unsupported capabilities are omitted rather than simulated.

## Verification
Maintainers may run these checks from the repository root:

```sh
find opencode/data-ai -type f | sort
find opencode/data-ai -type f -name '*.md' -exec test -s {} \;
jq empty opencode/data-ai/opencode.json
```

Expected result: JSON parses, Markdown is non-empty, all agent prompt paths exist, commands and Skills are present, permissions deny shell/web fetch, no active MCP/provider/plugin/credential configuration exists, and no generated validation artifacts remain.
