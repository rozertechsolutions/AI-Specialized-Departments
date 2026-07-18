# Kilo Code Data and AI Specialization

## Purpose
This package provides a Kilo Code-native Data and AI specialization for VS Code, JetBrains, and CLI surfaces. It covers Data and AI strategy, governance, data architecture, datasets, data platforms, analytics, data science, ML, GenAI/RAG, AI applications, operations, responsible AI, and independent assurance.

Supported native surfaces:
- Project configuration in `kilo.jsonc`.
- Project instructions in `AGENTS.md`.
- Project rules in `.kilo/rules/*.md`.
- Custom subagents in `.kilo/agents/*.md`.
- Agent Skills in `.kilo/skills/<skill>/SKILL.md`.
- User-invoked workflows/slash commands in `.kilo/commands/*.md`.
- Scope exclusions in `.kilocodeignore`.

No MCP servers, hosted KiloClaw infrastructure, Gateway configuration, organization management, provider credentials, plugins, model downloads, or environment configuration are included. Deprecated Memory Bank and deprecated Orchestrator Mode are not used.

## Installation and Discovery
Use `kilo-code/data-ai/` as the Kilo project root for Data and AI work, or copy its native artifacts into an existing Kilo project using the same relative paths:

- `kilo.jsonc`
- `AGENTS.md`
- `.kilocodeignore`
- `.kilo/rules/*.md`
- `.kilo/agents/*.md`
- `.kilo/skills/*/SKILL.md`
- `.kilo/commands/*.md`

Kilo loads instructions from `kilo.jsonc`, applies matching project rules, discovers project-specific custom agents and Skills, and exposes project commands as slash-command workflows where the selected Kilo surface supports them.

## Component Map
`kilo.jsonc` applies `.kilo/rules/*.md` and keeps permissions conservative: all unspecified actions ask, shell execution is denied, and web fetch is denied.

`AGENTS.md` defines the workspace-level operating model, safety rules, lifecycle coverage, and completion gates.

Rules:
- `.kilo/rules/00-data-ai-core.md`
- `.kilo/rules/90-data-ai-assurance.md`

Custom subagents provide bounded specialist review:
- `data-ai-orchestrator`
- `data-ai-solution-governance-reviewer`
- `data-architecture-dataset-reviewer`
- `data-platform-analytics-reviewer`
- `ml-genai-evaluation-reviewer`
- `ops-risk-assurance-reviewer`

Skills provide reusable procedures:
- `use-case-risk-triage`
- `data-contract-dataset-readiness`
- `pipeline-analytics-quality`
- `ml-genai-evaluation`
- `ops-risk-assurance`

Commands provide explicit user-invoked workflows:
- `data-ai-intake-triage`
- `ml-genai-release-review`
- `ops-risk-final-assurance`

## Invocation and Delegation
Start with the rules and `AGENTS.md`. Use the orchestrator for multi-domain Data and AI work, then delegate bounded review to the smallest specialist that owns the concern. Builders may test their own work, but independent evaluation, risk review, release readiness, and final assurance must be handled by a role that did not build the artifact.

Use Skills for repeatable methods and commands for explicit user-invoked workflow entry points. Do not use commands to bypass permission prompts or human-review gates.

## Permissions and Safety
This package does not authorize external services, production data access, credential access, MCP tools, Gateway usage, model downloads, deployment, publishing, signing, spending, destructive operations, or production mutation.

Human review is required for high-impact decisions and any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, credentialed, or production action. Completion status must be exactly `PASS`, `FAIL`, or `BLOCKED`, based only on direct evidence.

## Optional Integrations
MCP, KiloClaw, Gateway, organization settings, provider credentials, plugins, and scheduled automation may be enabled later only after explicit approval and review. Credentials must remain outside the repository, and broad unattended execution must remain disabled.

## Limitations
Kilo behavior depends on VS Code extension, JetBrains extension, CLI version, account, plan, model provider, workspace trust, and surface-specific feature availability. Unsupported capabilities are omitted rather than simulated.

Infrastructure provisioning, cybersecurity operations, penetration testing, production deployment, and cloud administration remain outside this specialization. This package owns Data and AI operational requirements, risk assumptions, evaluation, monitoring specifications, and rollback criteria.

## Verification
Maintainers may run these checks from the repository root:

```sh
find kilo-code/data-ai -type f | sort
find kilo-code/data-ai -type f -name '*.md' -exec test -s {} \;
jq empty kilo-code/data-ai/kilo.jsonc
for f in kilo-code/data-ai/.kilo/skills/*/SKILL.md; do d=$(basename "$(dirname "$f")"); grep -q "^name: $d$" "$f" || exit 1; done
for f in kilo-code/data-ai/.kilo/agents/*.md kilo-code/data-ai/.kilo/skills/*/SKILL.md kilo-code/data-ai/.kilo/commands/*.md; do sed -n '1p' "$f" | grep -q '^---$' || exit 1; done
find kilo-code/data-ai -type f \( -name '*.js' -o -name '*.ts' -o -name '*.sh' -o -name '*.py' -o -name '*.yml' -o -name '*.yaml' \) -print
```

Expected result: native Kilo files are present, Markdown artifacts are non-empty, configuration JSON is valid, frontmatter exists where required, Skill names match directories, no scripts or active integration configs exist, and local scans return no placeholder markers, credentials, private key material, or real secrets.
