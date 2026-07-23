# Claude Data and AI

This directory is a manual-import Data and AI specialization for Claude web and desktop. It uses Claude-native Projects, project instructions, project knowledge, custom Skills, artifacts produced during chats, and manually enabled connectors/integrations. It does not contain Claude Code configuration and does not activate tools, MCP servers, credentials, or external services by being present in the repository.

## Supported Surface

- `project/project-instructions.md`: paste into a Claude Project's project instructions.
- `skills/*/SKILL.md`: package each skill folder as a Claude custom Skill where Skills are available and enabled.
- Project knowledge: upload this README only when maintainers want Claude to reference installation, component, and limitation details.
- Artifacts: use Claude artifacts during conversations for generated plans, cards, tables, model documentation, decision packets, and review outputs; artifacts are chat outputs, not repository configuration.
- Connectors/integrations: enable manually in Claude or organization settings; none are enabled by default here.

## Installation And Use

1. Create a Claude Project for the Data and AI effort.
2. Paste `project/project-instructions.md` into the Project instructions field.
3. Add only necessary project knowledge files. Use paid-plan enhanced project knowledge/RAG where available for larger knowledge sets.
4. For each skill, zip the skill folder so the folder is the archive root, then upload it through Claude's Skills interface or organization Skill provisioning where available.
5. Enable only needed connectors through Claude's connectors directory or organization settings. Restrict write/delete actions to `Needs approval` or `Blocked`.
6. Start each request with the outcome, decision owner, data sources, allowed use, intended users, impact level, production proximity, and evidence expected.

Claude should invoke Project instructions as the baseline and load Skills only for the matching reusable workflow. Skills do not replace human approval, project instructions, or independent assurance.

## Component Map

- Project instructions: responsibility architecture, routing, separation of duties, safety rules, lifecycle workflows, and output status contract.
- `use-case-risk-triage`: use-case intake, feasibility, alternatives to AI, value, risk classification, route, and stop conditions.
- `data-contract-dataset-readiness`: governance, data contracts, source provenance, schemas, semantic models, labeling, synthetic data, leakage checks, and dataset acceptance.
- `pipeline-analytics-quality`: data products, pipelines, quality rules, lineage, observability, governed metrics, analytics, BI, and change control.
- `ml-genai-evaluation`: data science, experiments, ML, RAG, GenAI, agent/tool design, inference contracts, validation, safety tests, and candidate evidence.
- `ops-risk-assurance`: MLOps/LLMOps readiness, monitoring, drift, incidents, rollback, retirement, responsible AI, supplier/model risk, and final independent assurance.

The Delivery Orchestrator coordinates and collects evidence but cannot approve its own work. Builders may test their output but cannot certify release readiness. Responsible AI/model risk defines and reviews risk controls; independent assurance verifies evidence and separation of duties.

## Permissions, Approval, And Safety

Default operation is advisory and evidence-based. Do not authenticate to services, retrieve sensitive data, publish, deploy, sign, submit, spend money, modify external systems, delete data, or perform irreversible actions without explicit human approval and the relevant Claude connector permissions.

Never expose sensitive datasets, credentials, private endpoints, personal data, proprietary prompts, production records, or secrets. Never fabricate data quality results, statistical significance, causal claims, model metrics, benchmark outcomes, fairness findings, compliance status, latency, cost, lineage, or monitoring state.

Require provenance and permitted-use evidence for data, models, prompts, embeddings, libraries, providers, connectors, and third-party components. For RAG and agent work, require prompt-injection, tool-poisoning, data/model-poisoning, exfiltration, unsafe tool-use, excessive-agency, approval-boundary, and partial-failure controls.

## Optional Integrations

Useful connectors may include GitHub, Google Drive, Slack, Linear/Jira-style issue trackers, BI tools, data catalogs, notebooks, documentation systems, warehouses, model registries, vector stores, or ticketing systems when available to the account. Enable them manually, review requested scopes, and use source-system permissions plus Claude action restrictions. Custom remote MCP connectors require a trusted, reachable MCP server and are not represented by this package.

No connector URL, credential, OAuth secret, private endpoint, or account-specific identifier belongs in this repository.

## Limitations

Availability depends on Claude plan, workspace policy, product rollout, desktop/web/mobile surface, Skills settings, code execution settings, connector availability, and organization controls. Projects are available to all users, but free accounts have project limits; enhanced project knowledge with RAG is paid-plan only. Team and Enterprise sharing, organization Skills, and connector restrictions depend on admin configuration. This package does not validate runtime Claude behavior, execute model inference, or install connectors.

## Maintainer Verification

Run these static checks from the repository root:

```bash
find claude/data-ai -type f | sort
find claude/data-ai -type f -name '*.md' -print0 | xargs -0 -n1 sh -c 'test -s "$0"'
find claude/data-ai -type f \( -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.toml' \) -print
git diff -- claude/data-ai
```

Expected result: files are non-empty Markdown import artifacts, no Claude Code files are present, no active connector or MCP configuration is present, and changes are limited to `claude/data-ai`.
