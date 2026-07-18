# Cursor Data and AI Specialization

## Purpose
This package provides a Cursor-native Data and AI specialization for use-case intake, governed data delivery, analytics, data science, ML, GenAI/RAG, AI application readiness, operations, responsible AI, and independent assurance.

Supported native surfaces:
- Project instructions through `AGENTS.md`.
- Cursor project rules under `.cursor/rules/*.mdc`.
- Cursor custom subagents under `.cursor/agents/*.md`.
- Cursor Agent Skills under `.cursor/skills/<skill>/SKILL.md`.

Hooks, MCP servers, external connectors, cloud agents, marketplace plugins, credentials, and provider configuration are intentionally omitted. They may be enabled manually by a maintainer only after reviewing current Cursor documentation, local policy, and the target workspace risk.

## Installation and Discovery
Copy or keep `cursor/data-ai/` as the Cursor workspace root for Data and AI work, or merge its native artifacts into an existing Cursor workspace using the same relative paths:

- `AGENTS.md`
- `.cursor/rules/*.mdc`
- `.cursor/agents/*.md`
- `.cursor/skills/*/SKILL.md`

Open the folder in Cursor. Cursor should discover the project instructions, rules, agents, and skills from those paths. Do not move these files into another specialization, and do not mix them with unrelated platform packages.

## Component Map
`AGENTS.md` defines the workspace-level operating contract, evidence requirements, safety boundaries, and completion status vocabulary.

`.cursor/rules/00-data-ai-core.mdc` is the always-on rule for scope, lifecycle coverage, ownership, and engineering behavior.

`.cursor/rules/90-data-ai-assurance.mdc` is the always-on rule for independent evaluation, responsible AI review, risk controls, release readiness, incidents, retirement, and final assurance.

Custom subagents provide bounded specialist delegation:
- `data-ai-orchestrator` coordinates intake, routing, dependency tracking, evidence collection, and status without approving its own work.
- `data-ai-solution-governance-reviewer` reviews use-case strategy, governance, privacy, architecture, allowed use, and human oversight.
- `data-architecture-dataset-reviewer` reviews data contracts, modeling, provenance, lineage, annotation, representativeness, and dataset readiness.
- `data-platform-analytics-reviewer` reviews pipelines, data products, observability, governed metrics, BI, reporting, and experiments.
- `ml-genai-evaluation-reviewer` reviews ML, RAG, GenAI, agents, AI application contracts, inference behavior, evaluation design, and model documentation.
- `ops-risk-assurance-reviewer` reviews MLOps/LLMOps readiness, monitoring, incidents, rollback, retirement, responsible AI, supplier risk, and final assurance evidence.

Skills provide reusable procedures:
- `use-case-risk-triage`
- `data-contract-dataset-readiness`
- `pipeline-analytics-quality`
- `ml-genai-evaluation`
- `ops-risk-assurance`

## Invocation and Delegation
Start with the project rules and `AGENTS.md`. Use the orchestrator for non-trivial Data and AI work that spans more than one domain. Delegate specialist review only when the requested work touches that agent's scope. Builders may run focused checks for their own work, but independent approval must come from a reviewer or assurance role that did not build the artifact.

Use Skills when the task needs a repeatable checklist, decision workflow, or review method. Do not invoke a Skill merely to restate a short instruction already covered by the rules.

## Permissions and Safety
This package does not grant permission to access secrets, production records, sensitive datasets, external services, paid tools, deployment systems, or credentials. Require human review before any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, credentialed, or production action.

Completion status must be exactly `PASS`, `FAIL`, or `BLOCKED`, based on evidence. Never fabricate data quality results, statistical significance, model metrics, benchmarks, costs, latency, safety status, fairness status, compliance status, or production readiness.

## Optional Integrations
Optional hooks may be added later for deterministic local checks, but none are included here. Optional MCP servers or connectors may be added later for approved data catalogs, experiment trackers, model registries, BI systems, or documentation systems, but they must remain disabled by default and must not contain credentials.

## Limitations
Cursor feature availability can depend on product version, plan, IDE build, account settings, and workspace trust. If a native component is not available in the target Cursor environment, keep the durable behavior in `AGENTS.md` and project rules, and treat unsupported automation as omitted rather than simulated.

Infrastructure provisioning, cybersecurity operations, penetration testing, production deployment, and cloud administration remain outside this specialization. This package owns Data and AI requirements, evidence, risk assumptions, evaluation, operational readiness, monitoring specifications, and rollback criteria.

## Verification
Maintainers may run these checks from the repository root:

```sh
find cursor/data-ai -type f | sort
find cursor/data-ai -type f -name '*.md' -o -name '*.mdc'
for f in cursor/data-ai/.cursor/skills/*/SKILL.md; do d=$(basename "$(dirname "$f")"); grep -q "^name: $d$" "$f" || exit 1; done
find cursor/data-ai -type f \( -name '*.json' -o -name '*.js' -o -name '*.ts' -o -name '*.sh' -o -name '*.py' \) -print
```

Expected result: native Cursor files are present, Markdown artifacts are non-empty, Skill names match their directories, no scripts or active integrations exist, and local scans return no placeholder markers, credentials, private key material, or real secrets.
