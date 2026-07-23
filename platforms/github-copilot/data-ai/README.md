# GitHub Copilot Data and AI Specialization

## Purpose
This package provides a GitHub Copilot-native Data and AI specialization for repository and cloud-agent use. It covers Data and AI strategy, governance, data architecture, datasets, data platforms, analytics, data science, ML, GenAI/RAG, AI applications, operations, responsible AI, and independent assurance.

Supported native surfaces:
- Repository-wide custom instructions in `.github/copilot-instructions.md`.
- Path-specific custom instructions in `.github/instructions/data-ai.instructions.md`.
- Copilot custom agents in `.github/agents/*.agent.md`.
- Agent Skills in `.github/skills/<skill>/SKILL.md`.

No Actions workflows, hooks, MCP servers, secrets, variables, code-review automation, prompt-file commands, plugins, extensions, or external integrations are configured. GitHub Copilot surfaces vary between IDEs, Copilot CLI, GitHub.com cloud agent, and code review; the durable instructions remain usable even when agents or Skills are not enabled in a specific surface.

## Installation and Discovery
Use `github-copilot/data-ai/` as the repository root for the Data and AI specialization, or copy these native artifacts into the root of a target repository:

- `.github/copilot-instructions.md`
- `.github/instructions/data-ai.instructions.md`
- `.github/agents/*.agent.md`
- `.github/skills/*/SKILL.md`

Repository-wide instructions apply broadly to Copilot-supported surfaces. Path-specific instructions apply when the active file or task matches their `applyTo` glob. Custom agents are available to supported Copilot cloud agent, Copilot CLI, and IDE surfaces when custom agents are enabled. Skills are discovered from `.github/skills/` in supported surfaces and loaded only when relevant.

## Component Map
`.github/copilot-instructions.md` defines the workspace-wide Data and AI operating model, safety rules, responsibility routing, and completion gates.

`.github/instructions/data-ai.instructions.md` reinforces Data and AI lifecycle requirements for path-specific Copilot contexts.

Custom agents provide bounded specialist review:
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
Start with repository instructions. Use the orchestrator for multi-domain Data and AI work, then delegate bounded review to the smallest specialist that owns the concern. Builders may test their own work, but independent evaluation, risk review, release readiness, and final assurance must be handled by a role that did not build the artifact.

Use Skills only for repeatable procedures. Do not add prompt files or hooks to restate the same workflow.

## Permissions and Safety
This package does not authorize external services, production access, credential access, MCP tools, model downloads, deployment, publishing, signing, spending, destructive operations, pull-request automation, or code-review automation.

Human review is required for high-impact decisions and any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, credentialed, or production action. Completion status must be exactly `PASS`, `FAIL`, or `BLOCKED`, based only on direct evidence.

## Optional Integrations
MCP servers may be configured later through GitHub repository or Copilot settings only after explicit approval, because Copilot cloud agents may invoke configured MCP tools autonomously. Hooks may be added later only if a supported Copilot surface requires deterministic local validation and the scripts are reviewed, tested, and disabled from external side effects.

## Limitations
Custom agent, Skill, MCP, code review, IDE, CLI, and cloud-agent behavior depends on Copilot plan, repository host, organization policy, IDE support, CLI version, feature availability, and account settings. Managed user accounts and disabled cloud-agent settings can limit custom-agent use. Unsupported capabilities are omitted rather than simulated.

Infrastructure provisioning, cybersecurity operations, penetration testing, production deployment, and cloud administration remain outside this specialization. This package owns Data and AI operational requirements, risk assumptions, evaluation, monitoring specifications, and rollback criteria.

## Verification
Maintainers may run these checks from the repository root:

```sh
find github-copilot/data-ai -type f | sort
find github-copilot/data-ai -type f -name '*.md' -exec test -s {} \;
for f in github-copilot/data-ai/.github/skills/*/SKILL.md; do d=$(basename "$(dirname "$f")"); grep -q "^name: $d$" "$f" || exit 1; done
for f in github-copilot/data-ai/.github/agents/*.agent.md github-copilot/data-ai/.github/instructions/*.instructions.md github-copilot/data-ai/.github/skills/*/SKILL.md; do sed -n '1p' "$f" | grep -q '^---$' || exit 1; done
find github-copilot/data-ai -type f \( -name '*.json' -o -name '*.yml' -o -name '*.yaml' -o -name '*.sh' -o -name '*.py' -o -name '*.js' -o -name '*.ts' \) -print
```

Expected result: native Copilot files are present, Markdown artifacts are non-empty, frontmatter exists where required, Skill names match directories, no scripts or active integration configs exist, and local scans return no placeholder markers, credentials, private key material, or real secrets.
