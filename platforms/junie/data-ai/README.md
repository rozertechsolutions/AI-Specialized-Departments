# JetBrains Junie Data and AI Specialization

## Purpose
This package provides a Junie-native Data and AI specialization for JetBrains IDE and Junie CLI use. It covers Data and AI strategy, governance, data architecture, datasets, data platforms, analytics, data science, ML, GenAI/RAG, AI applications, operations, responsible AI, and independent assurance.

Supported native surfaces:
- Project guidelines in `.junie/AGENTS.md`.
- Project configuration in `.junie/config.json`.
- Project-scoped custom subagents in `.junie/agents/*.md`.
- Agent Skills in `.junie/skills/<skill>/SKILL.md`.

No MCP servers, commands, GitHub Actions, extensions, global cache content, model settings, environment variables, credentials, or authentication setup are configured. Commands are omitted because the durable guidelines and Skills already cover the required workflows without adding a duplicate invocation surface.

## Installation and Discovery
Use `junie/data-ai/` as the Junie project root for Data and AI tasks, or copy its native artifacts into an existing Junie project using the same relative paths:

- `.junie/AGENTS.md`
- `.junie/config.json`
- `.junie/agents/*.md`
- `.junie/skills/*/SKILL.md`

Junie reads `.junie/AGENTS.md` as project guidelines. Junie CLI discovers subagents from `.junie/agents/` when custom subagents are available and enabled. Junie discovers Skills from `.junie/skills/` when Agent Skills are available.

## Component Map
`.junie/AGENTS.md` defines the Data and AI operating model, lifecycle coverage, safety rules, routing, and completion gates.

`.junie/config.json` enables default Skill, command, and agent lookup locations, disables MCP default locations, and disables Junie auto-update for this project.

Custom subagents provide bounded specialist review:
- `data-ai-orchestrator` coordinates intake, routing, dependency control, evidence collection, and status without approving its own work.
- `data-ai-solution-governance-reviewer` reviews strategy, solution architecture, governance, privacy, metadata, allowed use, and human oversight.
- `data-architecture-dataset-reviewer` reviews modeling, semantic systems, sourcing, contracts, provenance, labeling, synthetic data, lineage, and dataset readiness.
- `data-platform-analytics-reviewer` reviews pipelines, data products, quality, observability, governed metrics, BI, reporting, statistics, and experiments.
- `ml-genai-evaluation-reviewer` reviews ML, GenAI, RAG, agents, inference contracts, evaluation, red-team evidence, and model documentation.
- `ops-risk-assurance-reviewer` reviews MLOps/LLMOps, monitoring, incidents, rollback, retirement, responsible AI, supplier risk, and independent assurance.

Skills provide reusable workflows:
- `use-case-risk-triage`
- `data-contract-dataset-readiness`
- `pipeline-analytics-quality`
- `ml-genai-evaluation`
- `ops-risk-assurance`

## Invocation and Delegation
Start with `.junie/AGENTS.md`. Use the orchestrator for multi-domain Data and AI work, then delegate bounded review to the smallest specialist that owns the concern. Builders may test their own work, but independent evaluation, risk review, release readiness, and final assurance must be handled by a role that did not build the artifact.

Use Skills only for repeatable procedures. Do not add a command just to restate a Skill or guideline.

## Permissions and Safety
This package does not authorize external services, production data access, credential access, MCP tools, model downloads, deployment, publishing, signing, spending, destructive operations, or production mutation.

Human review is required for high-impact decisions and any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, credentialed, or production action. Completion status must be exactly `PASS`, `FAIL`, or `BLOCKED`, based only on direct evidence.

## Optional Integrations
MCP may be enabled later only through explicit project approval, with credentials kept outside the repository and no default server discovery. Commands may be added later only when a workflow needs a distinct Junie-native invocation and does not duplicate a Skill.

## Limitations
Junie behavior depends on IDE version, Junie CLI version, account, plan, model provider, project trust, and feature availability. Subagent usage settings are documented as Early Access Program behavior in Junie CLI, so unsupported environments should rely on `.junie/AGENTS.md` and Skills. Unsupported capabilities are omitted rather than simulated.

Local version detection reported Junie `26.7.6 (2206.4)`.

Infrastructure provisioning, cybersecurity operations, penetration testing, production deployment, and cloud administration remain outside this specialization. This package owns Data and AI operational requirements, risk assumptions, evaluation, monitoring specifications, and rollback criteria.

## Verification
Maintainers may run these checks from the repository root:

```sh
find junie/data-ai -type f | sort
find junie/data-ai -type f -name '*.md' -exec test -s {} \;
jq empty junie/data-ai/.junie/config.json
for f in junie/data-ai/.junie/skills/*/SKILL.md; do d=$(basename "$(dirname "$f")"); grep -q "^name: $d$" "$f" || exit 1; done
for f in junie/data-ai/.junie/agents/*.md junie/data-ai/.junie/skills/*/SKILL.md; do sed -n '1p' "$f" | grep -q '^---$' || exit 1; done
find junie/data-ai -type f \( -name '*.sh' -o -name '*.py' -o -name '*.js' -o -name '*.ts' -o -name '*.yml' -o -name '*.yaml' \) -print
```

Expected result: native Junie files are present, Markdown artifacts are non-empty, configuration JSON is valid, frontmatter exists where required, Skill names match directories, no scripts or active integration configs exist, and local scans return no placeholder markers, credentials, private key material, or real secrets.
