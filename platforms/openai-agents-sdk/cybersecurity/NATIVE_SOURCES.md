# Native Sources

Documentation review date: 2026-07-21.

Product surface: OpenAI Agents SDK for Python packages under `openai-agents-sdk/cybersecurity/<area>/`. This is an SDK implementation, not a repository-autoloaded coding-agent, IDE rule, ChatGPT Project, or hosted custom GPT package.

## Official source checks

### Current reference documentation

- OpenAI Agents SDK: Agents - https://openai.github.io/openai-agents-python/agents/
- OpenAI Agents SDK: Guardrails - https://openai.github.io/openai-agents-python/guardrails/
- OpenAI Agents SDK: Human-in-the-loop - https://openai.github.io/openai-agents-python/human_in_the_loop/
- OpenAI Agents SDK: Running agents - https://openai.github.io/openai-agents-python/running_agents/
- OpenAI Agents SDK API reference: `RunState` - https://openai.github.io/openai-agents-python/ref/run_state/
- OpenAI Agents SDK API reference: `RunConfig` and `Runner` - https://openai.github.io/openai-agents-python/ref/run/

### Release/package check

- PyPI package inspected on 2026-07-21: `openai-agents==0.18.3`.
- Installed dependency set used for validation: `openai-agents==0.18.3`, `pydantic==2.13.4`.
- Current validated package range in every area `pyproject.toml`: `openai-agents>=0.18.3,<0.19`, `pydantic>=2.13,<3`.

### API/schema check

The installed package and official API reference agree on these contracts:

- `RunState.from_string(initial_agent, state_string, *, context_override=None, context_deserializer=None, strict_context=False)` is an async static method.
- `RunState.from_json(initial_agent, state_json, ...)` is also async.
- `RunState.to_string(..., include_tracing_api_key=False)` returns the matching string persistence format.
- `RunState.to_json(..., include_tracing_api_key=False)` returns the matching mapping persistence format.
- This package uses only the string persistence pair: `RunState.to_string()` and awaited `RunState.from_string(...)`.
- `RunConfig` supports `tracing_disabled`, input guardrails, and output guardrails.
- `Agent.as_tool(..., needs_approval=True)` is used to surface explicit HITL interruptions; this package does not auto-approve those interruptions.

## Validated project paths

- `openai-agents-sdk/cybersecurity/governance-risk-compliance-assurance/`
- `openai-agents-sdk/cybersecurity/security-architecture-engineering/`
- `openai-agents-sdk/cybersecurity/application-product-devsecops-security/`
- `openai-agents-sdk/cybersecurity/exposure-vulnerability-hardening/`
- `openai-agents-sdk/cybersecurity/defensive-security-operations-detection-intelligence/`
- `openai-agents-sdk/cybersecurity/incident-response-dfir-recovery/`
- `openai-agents-sdk/cybersecurity/offensive-security-authorized-validation/`
- `openai-agents-sdk/cybersecurity/cyber-resilience-specialized-technologies/`

Each area contains an installable Python package with `pyproject.toml`, `src/<package_name>/registry.py`, public exports in `src/<package_name>/__init__.py`, and static implementer documentation under `docs/`.

## Discovery and precedence

The SDK does not auto-discover repository files based on the shell working directory. Applications import an installed area package explicitly. Python package installation or `PYTHONPATH` determines import discovery. The application determines routing and cross-area handoff precedence.

`docs/ROLES.md` and `docs/SKILLS.md` are retained because they document the static role and procedure contracts; the OpenAI Agents SDK does not automatically load them as Skills.

## Permissions and safety behavior

Baseline SDK construction has:

- tracing disabled by default through `set_tracing_disabled(True)` and `RunConfig(tracing_disabled=True)`;
- no MCP servers;
- no hosted tools;
- no shell tools;
- no computer tools;
- no scanner, connector, cloud, SIEM, EDR, XDR, SOAR, ticketing, or identity-provider integration;
- no `Runner.run`, `Runner.run_sync`, or `Runner.run_streamed` call during repository validation.

Input guardrails and output guardrails are attached to constructed SDK agents. HITL approval helpers require an explicit selected interruption and call `approve(..., always_approve=False)` or `reject(..., always_reject=False)`.

## Removed or corrected fields and APIs

- The previous synchronous `restore_state(...)` helper returned the coroutine produced by async `RunState.from_string(...)`. All eight area registries now expose `async def restore_state(...)` and await `RunState.from_string(initial_agent=agent, state_string=serialized_state)`.
- The previous broad dependency range `openai-agents>=0.7,<1` was narrowed because current guardrail, HITL, `RunConfig`, `Agent.as_tool(needs_approval=True)`, and async state-restoration behavior were validated against the current `0.18.x` minor line, not every pre-1.0 version.
- No tracing API key is included by the baseline persistence helper. Applications must treat serialized `RunState` strings as potentially sensitive because application context and tool/trace metadata may be present.

## Validation method

- Inventory of all eight SDK area packages.
- Python AST parsing for every retained `.py` file.
- TOML parsing for every area `pyproject.toml`.
- Offline import tests for all eight packages and registries.
- Offline construction tests for specialists, coordinators, and `RunConfig`.
- Pure guardrail helper tests for authorized static requests, missing authorization, active scan/exploit requests, credential-bearing requests, production-changing requests, unsupported completion claims, and low-confidence evidence gaps.
- Mock/fake HITL helper tests for explicit approval and rejection without automatic approval.
- State persistence tests using `RunState.to_string()` and awaited `restore_state(...)`.
- API contract tests using `inspect.iscoroutinefunction(...)` and `inspect.signature(...)`.
- Forbidden-runtime tests that fail if validation invokes `Runner.run`, `Runner.run_sync`, or `Runner.run_streamed`, or instantiates hosted, shell, computer, MCP, or code-interpreter tools.

## Omitted mechanisms

Fake MCP servers, generated live hooks, hosted scanner integrations, cloud actions, external endpoints, credentials, production automation, and model calls are intentionally omitted from this repository baseline. A downstream application may configure providers, models, credentials, approvals, storage, and integrations only in its own authorized runtime environment.
