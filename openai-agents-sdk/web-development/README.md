# Web Development — OpenAI Agents SDK (Python)

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- Python package defining typed OpenAI Agents SDK agents, manager orchestration, tools, guardrails, approval lifecycle helpers, structured outputs and offline tests
- Manager-controlled specialist orchestration through `Agent.as_tool()`
- Function tools that operate only on caller-supplied in-memory repository snapshots
- Human-in-the-loop approval requests through SDK tool approval settings
- Structured dataclass contracts for inputs, evidence, proposals, findings, approvals, risks and final verdicts

## Intentionally omitted or disabled
- No server, UI, deployment, installer, environment file, API key or MCP server
- No model is pinned
- No executable shell or computer-use tool

## Platform notes
Verified against OpenAI Agents SDK Python 0.18.3 documentation and release metadata accessed on 2026-07-18. The lead agent remains the manager and calls specialists as tools; handoffs are intentionally unused because this package requires coordinator control after every specialist result.

The code is a reference SDK implementation. Importing it constructs agents, tools, guardrails and structured contracts only. It does not run a model, read the local filesystem, execute shell commands, mutate Git, install packages, deploy, publish, authenticate, or connect to external services. Runtime callers provide in-memory repository snapshots and explicitly invoke workflow entry points.

Sensitive action requests use the SDK approval surface and default to interruption before execution. The included sensitive-action tool returns an approval request after human approval; it still does not execute the sensitive action.

Example in-memory invocation shape:

```python
from web_development_department import RepositoryFile, RepositorySnapshot, TaskScope, run_web_development_request

scope = TaskScope(
    goal="Add accessible validation to the signup form.",
    acceptance_criteria=["Invalid email is rejected with an accessible error."],
    affected_paths=["src/signup.tsx"],
)
snapshot = RepositorySnapshot(
    files=[RepositoryFile(path="src/signup.tsx", content="...", language="tsx")]
)
result = await run_web_development_request(scope, snapshot)
```

Approval lifecycle:

1. Run `run_web_development_request(...)`.
2. If the result has `interruptions`, call `serialize_interrupted_run(result)` and present each interruption to a human.
3. Build `ApprovalDecision` values.
4. Call `resume_web_development_request(serialized_state, decisions)`.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Compatibility
- Python `>=3.10`
- `openai-agents==0.18.3`
- Offline tests use `pytest>=8,<9`

## Testing scope
The offline test suite verifies agent wiring, manager retention of control, specialist tool availability, reviewer read-only constraints, guardrail attachment, policy predicates, approval-tool configuration, workflow serialization guards and structured verdict rules. It does not make live API calls or verify model behavior.

## Limitations
- Final model-generated behavior is not verified without an explicit caller-run SDK execution.
- The package intentionally omits SDK handoffs, hosted tools, shell tools, filesystem tools, MCP, server/UI integration and deployment workflows.
- Tool guardrails apply to function tools; specialist `Agent.as_tool()` calls are guarded by agent-level manager policy and reviewer tool restrictions.

## Official sources reviewed
- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/agents/
- https://openai.github.io/openai-agents-python/tools/
- https://openai.github.io/openai-agents-python/handoffs/
- https://openai.github.io/openai-agents-python/guardrails/
- https://openai.github.io/openai-agents-python/human_in_the_loop/
- https://openai.github.io/openai-agents-python/results/
- https://openai.github.io/openai-agents-python/ref/run_state/
- https://github.com/openai/openai-agents-python/releases
- https://pypi.org/project/openai-agents/
