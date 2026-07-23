# Claude Code Data and AI

This package implements a project-scoped Data and AI specialization for Claude Code. It uses native Claude Code repository configuration only: `CLAUDE.md`, project custom subagents under `.claude/agents/`, Agent Skills under `.claude/skills/`, and `.claude/settings.json` for local safety defaults. It contains no active MCP servers, hooks, connectors, credentials, installers, deployment automation, or production integration.

## Installation And Discovery

Place this directory at `claude-code/data-ai/` and run Claude Code from this specialization directory or add it as an additional directory when explicitly intended. Claude Code discovers:

- `CLAUDE.md` as durable project instructions.
- `.claude/agents/*.md` as project-scoped custom subagents.
- `.claude/skills/*/SKILL.md` as project-scoped Skills, including in cloud sessions that clone this repository.
- `.claude/settings.json` as project settings when this specialization is the working directory.

Do not copy these files into repository root unless the Data and AI specialization should govern the entire repository. Do not enable MCP, connectors, routines, cloud execution, or desktop scheduled tasks by default.

## Component Map

- `CLAUDE.md`: baseline Data and AI operating model, responsibility routing, separation of duties, safety rules, lifecycle workflows, and status contract.
- `data-ai-orchestrator`: intake, portfolio/product framing, routing, dependency control, evidence aggregation, and stop conditions.
- `data-ai-solution-architect-governance`: solution architecture, alternatives to AI, governance, privacy, metadata, model risk, supplier risk, and human oversight.
- `data-architecture-dataset-engineer`: data modeling, semantics, contracts, sourcing, collection, labeling, synthetic-data controls, leakage checks, and dataset acceptance.
- `data-platform-analytics-engineer`: data engineering, pipelines, data products, quality, lineage, observability, governed metrics, analytics, BI, and decision intelligence.
- `data-science-ml-engineer`: statistical studies, causal inference, experiments, features, training pipelines, model comparison, validation implementation, packaging, and model interfaces.
- `genai-rag-agent-engineer`: prompts, embeddings, retrieval, RAG, grounding, vector search, tools, agent orchestration, inference contracts, fallback, and abstention.
- `ai-ops-risk-reviewer`: MLOps/LLMOps readiness, monitoring, drift, incidents, rollback, retirement, responsible AI controls, and risk review.
- `independent-data-ai-assurance-reviewer`: final independent evidence review and completion verdict; it must not build the artifact it approves.
- `.claude/skills/*`: focused reusable workflows for triage, dataset readiness, pipeline/analytics quality, ML/GenAI evaluation, and operations/risk/assurance.

## Invocation And Delegation

Use the orchestrator for new or ambiguous Data and AI work. Delegate implementation or analysis to the specialist that owns the relevant responsibility. Route release, risk, and final-readiness checks to reviewer roles that did not build the artifact. Keep delegation bounded and acyclic; a subagent must return findings to the orchestrator or requesting role with evidence, unresolved risks, and checks not run.

## Permissions, Approval, And Safety

The default behavior is local, repository-scoped, and evidence-based. The settings file disables Claude.ai connectors for this specialization and disables shell execution embedded in Skills. It also denies common destructive, release, publication, deployment, credential, and protected-file access patterns.

Human approval is required before high-impact decisions, production use, external write actions, destructive or irreversible actions, dependency or provider adoption, model release, public claims, legal/privacy escalation, spending, signing, publishing, deployment, or risk acceptance.

Never expose sensitive datasets, secrets, credentials, private endpoints, proprietary prompts, personal data, or production records. Never fabricate data quality results, statistical significance, causal claims, model metrics, benchmarks, costs, latency, robustness, fairness, compliance status, lineage, monitoring state, or runtime validation.

## Optional Integrations

MCP servers, Claude.ai connectors, plugins, scheduled tasks, routines, browser tools, cloud sessions, warehouses, notebooks, issue trackers, BI systems, data catalogs, model registries, vector stores, or observability systems may be useful only after manual enablement outside this package. Use least privilege, trusted sources, source-system permissions, and explicit approval for write or destructive actions.

This package intentionally omits `.mcp.json`, hook commands, connector definitions, plugin manifests, endpoint URLs, and credentials.

## Limitations

Claude Code behavior depends on installed version, surface, account plan, organization policy, enabled tools, permission mode, cloud/local execution mode, and managed settings. Project settings in this directory apply only when Claude Code loads this directory as the project. Cloud and Cowork sessions may load committed project Skills but do not inherit local user Skills. No runtime model behavior, external system state, MCP connection, hook execution, or production action is validated by these files.

## Maintainer Verification

Run these checks from the repository root:

```bash
find claude-code/data-ai -type f | sort
find claude-code/data-ai -type f -name '*.md' -print0 | xargs -0 -n1 sh -c 'test -s "$0"'
jq empty claude-code/data-ai/.claude/settings.json
find claude-code/data-ai -type f \( -name '*.py' -o -name '*.sh' -o -name '.mcp.json' \) -print
git diff -- claude-code/data-ai
```

Expected result: all Markdown files are non-empty, settings JSON is valid, no hook scripts or MCP configuration exist, and changes are limited to `claude-code/data-ai`.
