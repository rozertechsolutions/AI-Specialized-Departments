# Gemini CLI Data and AI Specialization

## Purpose
This package provides a Gemini CLI-native Data and AI specialization for strategy, governed data delivery, analytics, data science, ML, GenAI/RAG, AI applications, operations, responsible AI, and independent assurance.

Supported native surfaces:
- Workspace context through `GEMINI.md`.
- Project-local subagents under `.gemini/agents/*.md`.
- Workspace Agent Skills under `.gemini/skills/<skill>/SKILL.md`.
- Project settings in `.gemini/settings.json` with MCP disabled by default.

Hooks, MCP servers, extensions, remote subagents, provider setup, credentials, and authentication are intentionally omitted. Agent Skills are documented by Gemini CLI but may depend on preview availability and explicit user consent in the target CLI environment.

## Installation and Discovery
Use `gemini-cli/data-ai/` as the Gemini CLI workspace root for Data and AI tasks, or copy its native artifacts into an existing Gemini CLI workspace using the same relative paths:

- `GEMINI.md`
- `.gemini/settings.json`
- `.gemini/agents/*.md`
- `.gemini/skills/*/SKILL.md`

Run `/memory reload` in Gemini CLI after adding or changing `GEMINI.md`. Subagents are exposed to the main Gemini session as delegation tools when supported. Skills are discovered from `.gemini/skills/` and require activation consent before their full instructions are injected.

## Component Map
`GEMINI.md` defines the workspace-wide operating model, safety rules, lifecycle coverage, ownership, and evidence requirements.

`.gemini/settings.json` keeps `mcpServers` empty so no remote server or credentialed integration is active by default.

Project-local subagents provide bounded specialist review:
- `data-ai-orchestrator` coordinates intake, routing, dependency control, evidence collection, and status without approving its own work.
- `data-ai-solution-governance-reviewer` reviews strategy, solution architecture, governance, privacy, allowed use, metadata, and human oversight.
- `data-architecture-dataset-reviewer` reviews modeling, semantics, data contracts, sourcing, provenance, annotation, synthetic data, lineage, and dataset readiness.
- `data-platform-analytics-reviewer` reviews pipelines, data products, quality, observability, metrics, BI, reporting, statistics, and experiments.
- `ml-genai-evaluation-reviewer` reviews ML, GenAI, RAG, agents, inference contracts, evaluation, red-team evidence, and model documentation.
- `ops-risk-assurance-reviewer` reviews MLOps/LLMOps, monitoring, incidents, rollback, retirement, responsible AI, supplier risk, and independent assurance.

Skills provide reusable workflows:
- `use-case-risk-triage`
- `data-contract-dataset-readiness`
- `pipeline-analytics-quality`
- `ml-genai-evaluation`
- `ops-risk-assurance`

## Invocation and Delegation
Use `GEMINI.md` for durable guidance on every Data and AI task. Invoke the orchestrator for multi-domain work, then route bounded review to the smallest specialist that owns the concern. Builders may test their own work, but independent evaluation, risk review, release readiness, and final assurance must be performed by a role that did not build the artifact.

Use Skills for repeatable checklists and workflows. Do not activate a Skill only to duplicate instructions already present in `GEMINI.md` or a subagent.

## Permissions and Safety
This package does not authorize secret access, production data access, external API calls, credentialed MCP servers, model downloads, publishing, deployment, signing, spending, submission, destructive operations, or production mutation.

Human review is required for high-impact decisions and any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, credentialed, or production action. Completion status must be exactly `PASS`, `FAIL`, or `BLOCKED`, based only on direct evidence.

## Optional Integrations
Hooks may be added later only for deterministic local validation or policy enforcement. MCP servers may be added later only for approved catalogs, registries, BI systems, or documentation systems, with credentials supplied outside the repository and disabled by default until explicitly enabled by a maintainer.

Extensions are not included because this package does not need a bundle/install lifecycle beyond native workspace files.

## Limitations
Gemini CLI feature availability can depend on installed version, release channel, account, plan, workspace trust, and settings. This package was authored from current public documentation; local CLI compatibility could not be executed when `gemini` is unavailable. If subagents or Skills are unavailable in a target environment, keep the behavior in `GEMINI.md` and treat unsupported automation as omitted rather than simulated.

Infrastructure provisioning, cybersecurity operations, penetration testing, production deployment, and cloud administration remain outside this specialization. This package owns Data and AI operational requirements, risk assumptions, evaluations, monitoring specifications, and rollback criteria.

## Verification
Maintainers may run these checks from the repository root:

```sh
find gemini-cli/data-ai -type f | sort
find gemini-cli/data-ai -type f -name '*.md' -exec test -s {} \;
jq empty gemini-cli/data-ai/.gemini/settings.json
for f in gemini-cli/data-ai/.gemini/skills/*/SKILL.md; do d=$(basename "$(dirname "$f")"); grep -q "^name: $d$" "$f" || exit 1; done
find gemini-cli/data-ai -type f \( -name '*.js' -o -name '*.ts' -o -name '*.sh' -o -name '*.py' \) -print
```

Expected result: native Gemini CLI files are present, Markdown artifacts are non-empty, settings JSON is valid, Skill names match their directories, no scripts exist, no MCP server is configured, and local scans return no placeholder markers, credentials, private key material, or real secrets.
