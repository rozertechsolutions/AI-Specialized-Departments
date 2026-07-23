# Codex Data and AI

This package implements a project-scoped Data and AI specialization for Codex. It uses native Codex configuration only: `AGENTS.md`, `.codex/config.toml`, `.codex/agents/*.toml`, and `.agents/skills/*/SKILL.md`. It contains no hooks, MCP servers, plugins, provider configuration, credentials, model pins, scheduled tasks, worktree setup, or Git automation.

## Installation And Discovery

Use `codex/data-ai/` as the working directory when this specialization should apply. Codex discovers:

- `AGENTS.md` as durable project instructions.
- `.codex/config.toml` as trusted project configuration.
- `.codex/agents/*.toml` as custom agent definitions.
- `.agents/skills/*/SKILL.md` as project Skills.

Project `.codex/` config and agents require project trust. Do not copy these files to repository root unless the Data and AI specialization should govern the entire repository.

## Component Map

- `AGENTS.md`: Data and AI operating model, routing, lifecycle workflows, safety rules, and completion gates.
- `.codex/config.toml`: local project defaults with approval required, workspace-write sandboxing, network disabled, and bounded agent depth.
- `data-ai-orchestrator`: product framing, intake, routing, dependencies, evidence aggregation, and stop conditions.
- `data-ai-solution-architect-governance`: solution architecture, governance, privacy, responsible AI, model/supplier risk, and human oversight.
- `data-architecture-dataset-engineer`: data models, semantics, contracts, sources, labeling, synthetic data, leakage checks, splits, and dataset acceptance.
- `data-platform-analytics-engineer`: pipelines, data products, quality, lineage, observability, governed metrics, analytics, BI, and reproducible reporting.
- `data-science-ml-engineer`: studies, experiments, causal inference, ML features, training, validation, packaging, interfaces, and model documentation.
- `genai-rag-agent-engineer`: prompts, embeddings, retrieval, RAG, tools, agents, inference contracts, fallback, and abstention.
- `ai-ops-risk-reviewer`: MLOps/LLMOps readiness, monitoring, drift, incidents, rollback, retirement, responsible AI controls, and risk review.
- `independent-data-ai-assurance-reviewer`: final evidence review and completion verdict; it must not build what it approves.
- `.agents/skills/*`: focused reusable workflows for triage, dataset readiness, pipeline/analytics quality, ML/GenAI evaluation, and operations/risk/assurance.

## Invocation And Delegation

Start new or ambiguous work with the orchestrator. Delegate to the one specialist that owns the next decision or implementation area. Route risk, evaluation, and final readiness to agents that did not build the artifact. Delegation must be bounded, acyclic, and returned with evidence, unresolved risks, and checks not run.

## Permissions, Approval, And Safety

The package is local and repository-scoped. Project config disables network access inside workspace-write sandboxing and requires approvals for actions outside automatic safe operation. Human approval is required before high-impact decisions, production use, external writes, destructive or irreversible operations, dependency/provider/model adoption, public claims, spending, signing, publishing, deployment, legal/privacy escalation, release readiness, or risk acceptance.

Never expose sensitive datasets, secrets, credentials, private endpoints, proprietary prompts, personal data, or production records. Never fabricate data quality results, statistical significance, causal claims, model metrics, benchmarks, costs, latency, robustness, fairness, compliance status, lineage, monitoring state, or runtime validation.

## Optional Integrations

MCP servers, plugins, browser tools, cloud sessions, data catalogs, notebooks, warehouses, BI tools, issue trackers, model registries, vector stores, observability systems, and external providers must be enabled manually outside this package. Store secrets outside the repository, use least privilege, keep network disabled unless explicitly needed, and require human approval for external writes.

## Limitations

Codex behavior depends on CLI/app/IDE/cloud surface, installed version, account plan, workspace trust, sandbox profile, approval policy, user-selected model, and organization settings. This package does not validate live Codex loading, run model inference, authenticate services, or connect external systems.

## Maintainer Verification

Run these checks from the repository root:

```bash
find codex/data-ai -type f | sort
find codex/data-ai -type f -name '*.md' -print0 | xargs -0 -n1 sh -c 'test -s "$0"'
python3 - <<'PY'
import pathlib, re
for path in pathlib.Path("codex/data-ai").rglob("*.toml"):
    text = path.read_text()
    if text.count('"""') % 2:
        raise SystemExit(f"unclosed multiline string: {path}")
    stripped = re.sub(r'""".*?"""', '"MULTILINE"', text, flags=re.S)
    for line_number, line in enumerate(stripped.splitlines(), 1):
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith("#"):
            continue
        if stripped_line.startswith("[") and stripped_line.endswith("]"):
            continue
        if "=" not in stripped_line:
            raise SystemExit(f"invalid TOML-like line {path}:{line_number}: {line}")
PY
tmp_file="${TMPDIR:-/tmp}/codex-data-ai-prompt-input.json"
codex -C codex/data-ai debug prompt-input "config validation" > "$tmp_file" && test -s "$tmp_file" && rm "$tmp_file"
find codex/data-ai -type f \( -name '*.py' -o -name '*.sh' -o -name 'hooks.json' -o -name '.mcp.json' \) -print
git diff -- codex/data-ai
```

Expected result: Markdown files are non-empty, TOML syntax is sanity-checked, Codex's local config loader succeeds without model inference, no hook scripts or MCP configuration exist, and changes are limited to `codex/data-ai`.
