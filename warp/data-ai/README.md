# Warp / Oz Data and AI

This package implements the Data and AI specialization for Warp using repository-native project rules, project Skills, and manually importable Warp Drive/Profile content. It is provider-, model-, data-platform-, warehouse-, lakehouse-, BI-, vector-store-, and framework-neutral.

## Supported Native Surface

- `AGENTS.md`: Warp project rules applied when working in `warp/data-ai`.
- `.agents/skills/*/SKILL.md`: project Skills discoverable by Warp agents from the repository.
- `warp-drive/workflows/*.md`: manual Warp Drive workflow content for reusable lifecycle prompts.
- `warp-drive/agent-profiles/data-ai-safe-profile.md`: manual profile settings for Warp Settings > Agents > Profiles.

No autonomous cloud agents, schedules, triggers, active MCP servers, credentials, environment variables, provider configs, deployments, publishing actions, or production integrations are included.

## Installation and Discovery

1. Open Warp in this repository or in the `warp/data-ai` directory.
2. Let Warp read the project rules from `warp/data-ai/AGENTS.md`.
3. Ask the agent, `What skills do I have?`, and confirm the Data and AI skills under `.agents/skills`.
4. Optionally import the Markdown files under `warp-drive/workflows` into Warp Drive as saved prompts or workflows.
5. Optionally create a Warp Agent profile using `warp-drive/agent-profiles/data-ai-safe-profile.md`.

## Component Map

- `AGENTS.md`: scope, routing, separation of duties, safety rules, and evidence gates.
- `use-case-risk-triage`: intake, value, feasibility, alternatives to AI, impact, risk class, and route.
- `data-contract-dataset-readiness`: data contracts, schemas, semantics, provenance, collection, annotation, leakage, splits, and acceptance.
- `data-platform-analytics-quality`: ingestion, transformations, data products, lineage, quality, observability, governed metrics, BI, and decision intelligence.
- `analytics-experiment-review`: statistical studies, causal design, uncertainty, calibration, segmentation, experiments, and metric certification.
- `ml-genai-system-evaluation`: ML, RAG, prompts, agents, inference contracts, evaluation, red-team evidence, groundedness, and release candidate selection.
- `ops-risk-assurance`: MLOps, LLMOps, monitoring, drift, provider change, incidents, rollback, retirement, deletion/rectification propagation, and final assurance.
- `warp-drive/workflows`: end-to-end lifecycle prompts that call the minimum necessary Skills and preserve independent review.
- `warp-drive/agent-profiles`: manual cautious profile content for approval-controlled Data and AI work.

## Invocation and Delegation

Start with the orchestrator rules in `AGENTS.md` for new or ambiguous work. Invoke a focused Skill when the user request matches its description. Use the Warp Drive workflows for lifecycle work that spans several Skills. Builders must return evidence to a separate reviewer before any release-readiness or final assurance claim.

## Permissions and Safety

Use a restrictive Warp Agent profile for this specialization:

- Apply code diffs: always prompt for confirmation.
- Read files: let the agent decide for repository-local non-sensitive files.
- Create plans: let the agent decide.
- Execute commands: always prompt for confirmation.
- Interact with running commands: never unless explicitly authorized for the task.
- Ask clarifying questions: allow when evidence, authority, or scope is missing.
- Command denylist: deny destructive commands, deployment/publishing commands, credential access, external data transfer, model downloads, and package installation unless the human explicitly authorizes the exact action.
- MCP permissions: disabled by default.

Human review is required before high-impact decisions, provider/model selection, risk acceptance, policy exceptions, external integration activation, destructive actions, production changes, releases, publication, spending, or access expansion.

## Optional Integrations

MCP servers, cloud agents, Oz runs, schedules, triggers, external data catalogs, warehouses, BI tools, vector stores, experiment trackers, model registries, and observability platforms are intentionally not configured. If needed, enable them manually in Warp only after the human provides scope, credentials handling instructions, allowed data boundaries, and approval rules. Do not add `.warp/.mcp.json` unless the project explicitly authorizes a concrete server definition.

## Limitations

Warp behavior depends on the installed Warp version, account plan, model/provider settings, folder trust, indexing state, and manual Warp Drive/Profile configuration. This package does not authenticate Warp, run Oz cloud agents, validate model output, inspect production systems, contact external APIs, or prove live platform loading.

## Maintainer Verification

Run these repository-local checks:

```bash
find warp/data-ai -type f | sort
find warp/data-ai -type f -name '*.md' -exec test -s {} \;
python3 - <<'PY'
from pathlib import Path
for path in Path('warp/data-ai/.agents/skills').glob('*/SKILL.md'):
    text = path.read_text()
    assert text.startswith('---\n'), path
    assert '\nname:' in text and '\ndescription:' in text, path
print('skill frontmatter ok')
PY
python3 - <<'PY'
from pathlib import Path
needles = ['TO'+'DO', 'FIX'+'ME', 'BEGIN '+'RSA', 'BEGIN '+'OPENSSH', 'BEGIN '+'PRIVATE']
hits = []
for path in Path('warp/data-ai').rglob('*'):
    if path.is_file():
        text = path.read_text(errors='ignore')
        hits.extend((str(path), item) for item in needles if item in text)
assert not hits, hits
PY
test ! -e warp/data-ai/.warp/.mcp.json
find warp/data-ai -type f \( -name '.DS_Store' -o -name '._*' -o -name 'AUDIT.md' -o -name 'VALIDATION.md' -o -name 'REPORT.md' \) -print
```
