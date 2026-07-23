# ChatGPT Data and AI

This package is a manual-import ChatGPT configuration for professional Data and AI work. It uses only current ChatGPT-native surfaces: Projects with project instructions and uploaded knowledge, native Skills where the account or workspace supports them, optional Workspace Agent instructions, and manually enabled apps/connectors. Repository files do not activate ChatGPT features by themselves.

## Supported Surface

- `project/project-instructions.md`: paste into a ChatGPT Project's project instructions.
- `skills/*/SKILL.md`: upload or recreate as ChatGPT Skills when Skills are available for the account and enabled by workspace policy.
- `workspace-agent/agent-instructions.md`: optional Workspace Agent source instructions for recurring, tool-based coordination work.
- Apps/connectors: enabled manually in ChatGPT or workspace settings only; this package includes no credentials, live connection definitions, or automatic connector activation.

## Installation And Use

1. Create a ChatGPT Project named for the Data and AI effort.
2. Set project memory to project-only for sensitive or shared work when available.
3. Paste `project/project-instructions.md` into the Project instructions field.
4. Upload this README as project knowledge only if the user wants the component map and operating limits available in chat.
5. Upload Skills from `skills/*` through ChatGPT Skills upload/editor where available, or keep the Project instructions as the durable baseline when Skills are unavailable.
6. For recurring workflows that read from approved business systems, create a Workspace Agent manually and paste `workspace-agent/agent-instructions.md`.
7. Enable any app/plugin connector manually, choose the least-privilege permission mode, and keep write actions behind human approval.

Start requests with the use case, decision owner, data sources, intended users, impact level, allowed data use, target environment, and evidence expected. The Project routes work to the responsible role and returns `PASS`, `FAIL`, or `BLOCKED` based on evidence.

## Component Map

- Project instructions: baseline operating model, responsibility boundaries, routing, safety rules, lifecycle workflows, output contract, and final status rules.
- `use-case-risk-triage` Skill: intake, feasibility, alternatives to AI, impact, value, ownership, and route selection.
- `data-contract-dataset-readiness` Skill: data sourcing, governance, contracts, schemas, semantic modeling, labeling, dataset acceptance, provenance, and leakage controls.
- `pipeline-analytics-quality` Skill: data products, pipeline design, quality rules, lineage, observability, governed metrics, analytics, BI, and decision intelligence.
- `ml-genai-evaluation` Skill: data science, experimentation, ML engineering, RAG, GenAI, agent design, inference contracts, benchmarks, safety tests, and evidence packages.
- `ops-risk-assurance` Skill: MLOps/LLMOps readiness, monitoring, drift, incident response, rollback, retirement, responsible AI, supplier/model risk, and independent assurance.
- Workspace Agent instructions: repeatable intake routing, evidence follow-up, monitoring-summary drafting, and owner notification using manually approved tools.

The coordinator may route work and collect evidence but cannot approve its own output. Builders may test their work but cannot provide independent final approval. Responsible AI/model-risk review is separate from independent assurance.

## Permissions, Approval, And Safety

The default mode is advisory and static. Do not authenticate, deploy, publish, submit, sign, spend money, change production, delete data, modify external systems, or expose sensitive information unless the user and the relevant workspace controls explicitly authorize the action. High-impact decisions, external write actions, irreversible actions, provider/model adoption, risk acceptance, release readiness, and production rollout require human approval.

Never fabricate data quality results, statistical significance, causal claims, model metrics, benchmark results, fairness findings, latency, costs, compliance status, lineage, or monitoring evidence. Require provenance and permitted-use evidence for data, models, prompts, embeddings, libraries, third-party systems, and generated/synthetic data.

For RAG and agents, require source provenance, retrieval quality, groundedness, citation correctness, stale-source behavior, prompt-injection controls, tool allowlists, bounded delegation, loop limits, stop conditions, idempotency, approval boundaries, and partial-failure handling.

## Optional Integrations

Apps/connectors may be useful for Google Drive, Slack, data catalogs, issue trackers, BI workspaces, notebooks, warehouses, model registries, vector databases, documentation systems, or ticketing systems when they are available in ChatGPT or a workspace plugin. Configure them manually in ChatGPT, grant only the minimum required scopes, and prefer `Always ask` or `Any changes` permission modes for sensitive data. Write actions remain disabled unless a human explicitly approves each action.

Do not store credentials, connection strings, private endpoints, account identifiers, production data, or real secrets in this package.

## Limitations

Availability depends on ChatGPT plan, workspace policy, admin controls, region, and product rollout. Projects require a logged-in ChatGPT account. Project file limits, project sharing, memory behavior, Skills, plugins/apps, and Workspace Agents vary by account type and admin configuration. Native Skills may need separate installation per ChatGPT surface. Repository files are source artifacts only; they do not enforce permissions, run hooks, connect apps, or execute validation inside ChatGPT.

## Maintainer Verification

Run these static checks from the repository root after changes:

```bash
find chatgpt/data-ai -type f | sort
find chatgpt/data-ai -type f -name '*.md' -print0 | xargs -0 -n1 sh -c 'test -s "$0"'
find chatgpt/data-ai -type f \( -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.toml' \) -print
git diff -- chatgpt/data-ai
```

Expected result: all files are non-empty Markdown source artifacts, no structured runtime configuration is present, no credentials or live connector definitions are present, and changes are limited to `chatgpt/data-ai`.
