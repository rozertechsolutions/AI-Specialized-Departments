# OpenAI Agents SDK - Software Development

This directory is source code for the Software Development specialization on the OpenAI Agents SDK. It is not a deployed service. It is language-, framework-, database-, provider-, model-, and vendor-agnostic. It contains no API key, endpoint, model pin, server, CLI, UI, deployment asset, installer, hook, or operational automation.

## Native SDK shape

- `agents.py` builds one Software Development Lead and seven specialists.
- The Lead remains the active top-level agent. Specialists are exposed through `Agent.as_tool()` so their typed results return to the Lead without transferring the conversation.
- Every specialist has a role-specific typed output model. The Lead has a typed `LeadFinalRecord` output containing requirements, plan, implementation evidence, validation evidence, code review, risk review, documentation/release readiness, limitations, and human decisions.
- `orchestrator.py` applies bounded orchestration limits, host-injected context, SDK interruption inspection, `result.to_state()`, `RunState.approve()`, `RunState.reject()`, resumed `Runner.run()`, and explicit stop states.
- `guardrails.py`, `policies.py`, and `tools.py` separate task text from concrete proposed actions. Keyword mentions such as credentials, deployment, deletion, signing, or release do not block legitimate analysis by themselves.

## HITL and tools

Models, repository tools, workspace root, run limits, and approvals are host-injected. `tools.py` defines protocols, SDK `function_tool` wrappers, and deterministic in-memory fakes for tests only. No operational tool is enabled by default, and the package does not implement shell, Git, network, deployment, publication, signing, credential, unrestricted filesystem, or external communication clients.

Sensitive concrete actions use the Agents SDK human-in-the-loop approval flow. Tool calls that require approval surface as `result.interruptions`; the runtime converts the result with `result.to_state()`, exposes pending decisions to the host, applies `RunState.approve()` or `RunState.reject()`, and resumes the original Lead run. Rejected required actions stop safely and are not executed.

## Safety and evidence

The package enforces least privilege by construction: specialists cannot delegate, the Lead aggregates final evidence, implementation does not count as independent review, and output guardrails require typed evidence rather than unsupported completion claims. Candidate paths are normalized against an injected workspace root; absolute paths, traversal, ambiguous components, and scope escapes are rejected. Hosts that implement repository access must resolve real paths and enforce the workspace boundary, including symlink escapes.

Compatibility target: `openai-agents>=0.18.3,<0.19` on Python 3.10 or newer. Verification is performed with exactly `openai-agents==0.18.3`, deterministic injected fake model responses, and `OPENAI_AGENTS_DISABLE_TRACING=1`; no API key, external model call, or external service is required. Test verification creates a temporary environment that must be deleted after the run.

## Included source

- `src/software_development_department/models.py`: typed task, evidence, role output, action, approval, and final record models.
- `src/software_development_department/agents.py`: manager-as-tools SDK construction.
- `src/software_development_department/orchestrator.py`: bounded top-level Lead run.
- `src/software_development_department/guardrails.py`: task, proposed-action, and evidence guardrails.
- `src/software_development_department/policies.py`: approval, scope, and evidence policies.
- `src/software_development_department/tools.py`: host-injected tool protocols and inert fakes.
- `src/software_development_department/skills.py`: fourteen capability definitions.
- `src/software_development_department/workflows.py`: eleven differentiated workflow definitions.
- `tests/`: static source tests and deterministic policy/tool tests.

## Intentionally omitted

- concrete API invocation, credentials, account identifiers, endpoints, fixed models, or provider defaults
- server, CLI, UI, deployment, publication, signing, release, or installer entry points
- shell, Git, network, MCP, external communication, or unrestricted filesystem implementations
- automatic approval, automatic Git mutation, issue/PR submission, package publication, release, signing, notarization, store submission, purchase, spending, account change, or external communication
