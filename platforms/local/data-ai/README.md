# Local Data and AI Specialization

## Purpose
This package is a provider-agnostic local specification for Data and AI work. It covers strategy, governance, data architecture, datasets, platforms, analytics, data science, ML, GenAI/RAG, AI applications, operations, responsible AI, and independent assurance.

Supported native product surface:
- `local.yaml` provider-neutral package manifest.
- JSON Schemas in `schemas/`.
- Safety and permission policies in `policies/`.
- Specialist definitions in `subagents/`.
- Reusable procedure definitions in `skills/`.
- User-invoked workflow definitions in `workflows/`.

This is not an Ollama, LM Studio, OpenAI-compatible endpoint, daemon, server, UI, installer, universal adapter, orchestration framework, model downloader, dependency installer, or executable runtime. Providers, runtimes, endpoints, vector stores, tools, storage backends, execution capabilities, and permissions are disabled by default.

## Installation and Discovery
Use `local/data-ai/` as a standalone specification package. A local runner or provider wrapper may import it by validating `local.yaml` against `schemas/local.schema.json`, loading listed policies, then loading listed subagents, skills, and workflows.

No provider is selected by default. To use a runtime later, a maintainer must add a separate local-only provider configuration outside this package or extend `local.yaml` with an explicit disabled-by-default provider entry and validate it against project policy.

## Component Map
`local.yaml` declares the package, disabled defaults, subagents, skills, workflows, and policies.

Policies:
- `policies/permissions.yaml`
- `policies/safety.yaml`

Subagents:
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
- `ml-genai-evaluation`
- `ops-risk-assurance`

Workflows:
- `use-case-intake-triage`
- `dataset-contract-readiness`
- `pipeline-analytics-quality`
- `ml-genai-release-review`
- `ops-risk-final-assurance`

## Invocation and Delegation
Use the orchestrator for multi-domain Data and AI work, then route bounded review to the smallest specialist that owns the concern. Builders may test their own work, but independent evaluation, risk review, release readiness, and final assurance must be handled by a role that did not build the artifact.

Use skills for reusable methods and workflows for explicit user-invoked lifecycle procedures. Completion status must be exactly `PASS`, `FAIL`, or `BLOCKED`.

## Permissions and Safety
All external integrations, execution tools, provider endpoints, model downloads, vector stores, storage backends, shell commands, filesystem writes, network access, production access, and credential use are disabled by default.

Human review is required for high-impact decisions and any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, credentialed, or production action. Never fabricate data quality results, statistical significance, causal claims, model metrics, benchmarks, latency, cost, robustness, fairness, compliance status, or readiness evidence.

## Optional Integrations
Optional local-only providers such as Ollama, LM Studio, llama.cpp, vLLM, SGLang, or OpenAI-compatible local endpoints may be added later as disabled examples only. Any example endpoint must be loopback-only, non-secret, clearly replaceable, and not selected as default.

## Limitations
This package has no runtime behavior by itself. Compatibility depends on the user-selected local runner, schema validator, provider, model, hardware, operating system, and policy implementation. Unsupported capabilities are omitted rather than simulated.

## Verification
Maintainers may run these checks from the repository root:

```sh
find local/data-ai -type f | sort
find local/data-ai -type f -name '*.md' -exec test -s {} \;
for f in local/data-ai/**/*.yaml; do ruby -e 'require "yaml"; YAML.load_file(ARGV[0])' "$f" || exit 1; done
for f in local/data-ai/schemas/*.json; do jq empty "$f" || exit 1; done
```

Expected result: files are present, Markdown is non-empty, YAML and JSON schemas parse, no active provider/integration exists, and local scans return no placeholder markers, credentials, private key material, or real secrets.
