# OpenAI Agents SDK - Software Development

This directory is a static Python reference implementation of the Software Development specialization for the OpenAI Agents SDK. It is language-, framework-, database-, provider-, model-, and vendor-agnostic. It contains no API key, endpoint, model pin, server, CLI, UI, deployment asset, installer, hook, or operational automation.

## Native SDK shape

- `agents.py` builds one Software Development Lead and seven specialists.
- The Lead remains the active top-level agent. Specialists are exposed through `Agent.as_tool()` so their typed results return to the Lead without transferring the conversation.
- Every specialist has a role-specific typed output model. The Lead has a typed `LeadFinalRecord` output containing requirements, plan, implementation evidence, validation evidence, code review, risk review, documentation/release readiness, limitations, and human decisions.
- `orchestrator.py` applies bounded orchestration limits and explicit stop states.
- `guardrails.py`, `policies.py`, and `tools.py` separate task text from concrete proposed actions. Keyword mentions such as credentials, deployment, deletion, signing, or release do not block legitimate analysis by themselves.

## HITL and tools

Operational tools are host-injected. `tools.py` defines protocols and deterministic inert fakes only. It does not implement shell, Git, network, deployment, publication, signing, credential, unrestricted filesystem, or external communication tools.

Sensitive concrete actions are represented as `ProposedToolAction` values and require human approval. A denied approval returns a safe failure result and executes nothing. Hosts that wire real SDK tools must use the Agents SDK human-in-the-loop approval flow for those tool calls and resume the original Lead run after approval or rejection.

## Safety and evidence

The package enforces least privilege by construction: specialists cannot delegate, the Lead aggregates final evidence, implementation does not count as independent review, and output guardrails require typed evidence rather than unsupported completion claims. Candidate paths are normalized against an injected workspace root; absolute paths, traversal, ambiguous components, and scope escapes are rejected.

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
