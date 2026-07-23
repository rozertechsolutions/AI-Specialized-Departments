# Web Development — OpenAI Agents SDK

## Department overview

This package is a professional Web Development department implemented as executable Python code for the OpenAI Agents SDK. It is already specialized for Web Development; it is not a generic agent template that must be rewritten before use. The department is stack-aware rather than tied to one framework and covers frontend, backend/API, full-stack architecture, authentication and authorization, sessions and cookies, storage and integrations, responsive design, accessibility, performance and Core Web Vitals, SEO and crawlability, browser compatibility, testing, dependency and supply-chain review, security and privacy, observability, and release readiness.

Specialists are selected according to deterministic task applicability and application-owned review planning. Security/privacy and independent final quality review are mandatory whenever the run is allowed. The department is intended to work immediately after installation with project-specific constraints supplied as task scope, snapshot content, acceptance criteria, and caller-owned policy values.

## Possible uses

- Discover an existing web stack from a caller-provided repository snapshot.
- Understand an unfamiliar web repository without reading the real filesystem.
- Plan a new frontend, backend, API, authentication, or full-stack feature.
- Review REST, GraphQL, WebSocket, or webhook API design when present.
- Review sessions, cookies, CSP, CORS, CSRF, validation, privacy, and secure data handling.
- Debug web regressions from supplied files and expected behavior.
- Audit responsive behavior, accessibility, SEO, crawlability, and Core Web Vitals risks.
- Review dependency and supply-chain risk as non-executing analysis.
- Prepare testing, browser compatibility, observability, rollback, and release-readiness evidence.
- Record human approval or risk acceptance for non-executing sensitive analysis transitions.

## Supported product surface

This is static Python package source for the OpenAI Agents SDK, not a CLI plugin, IDE extension, hosted agent, deployment service, or live automation package. It requires Python `>=3.10` and the `openai-agents` Python package. Offline tests do not require an API key. Live model execution requires the caller to configure an OpenAI API key or other supported model provider explicitly.

Native SDK mechanisms used here include `Agent`, `Agent.as_tool()`, `Runner.run(...)`, function tools, guardrails, `RunConfig`, approval interruptions, and `RunState` serialization. The package deliberately contains no tool that deploys, installs dependencies, mutates Git, publishes, authenticates, retrieves secrets, spends money, signs, submits, or destroys data.

## Included native components

- `pyproject.toml`: Python package metadata, Python requirement, SDK dependency, and optional test dependency.
- `src/web_development_department/department.py`: coordinator and specialist `Agent` definitions. Specialists are exposed to the lead with `Agent.as_tool()`; core handoffs are not used.
- `src/web_development_department/workflow.py`: public preflighted run, safe `RunConfig`, strict context serialization, approval application, and resume entry points.
- `src/web_development_department/policy.py`: deterministic application-owned preflight, action-local intent classification, scope assessment, snapshot validation, ledgers, approvals, risk acceptance, review ordering, and final reconciliation.
- `src/web_development_department/models.py`: typed task, snapshot, review, evidence, approval, risk, and context contracts.
- `src/web_development_department/tools.py`: read-only context tools that inspect the trusted in-memory snapshot and record trusted evidence.
- `src/web_development_department/guardrails.py`: SDK guardrails retained as defense in depth after application preflight.
- `src/web_development_department/serialization.py`: JSON-safe typed context serializer/deserializer for strict `RunState` persistence.
- `tests/test_department.py`: offline test suite with no API key, live model call, HTTP call, browser, shell execution, or external filesystem mutation.

## Installation and integration

1. Install Python `>=3.10`; Python 3.12 or later is suitable when supported by your environment.
2. Create a user-owned virtual environment outside production runtime paths:
   ```bash
   python3 -m venv .venv
   . .venv/bin/activate
   ```
3. From this package directory, install the package:
   ```bash
   pip install .
   ```
4. For offline validation only, install tests:
   ```bash
   pip install '.[test]'
   pytest -q
   ```
5. Import the entry points from `web_development_department`.

Copy this whole `openai-agents-sdk/web-development/` package into the codebase or package repository where the SDK application will import it. Do not commit API keys, tokens, private endpoints, or organization identifiers. Keep optional live provider configuration outside this package, usually in environment variables such as `OPENAI_API_KEY`, and enable live execution only in caller-owned application code.

## How to use

```python
from web_development_department import RepositoryFile, RepositorySnapshot, TaskScope, run_web_development_request

scope = TaskScope(
    goal="Review the React checkout form and backend session cookie handling.",
    acceptance_criteria=[
        "Identify frontend, backend, security, accessibility, performance, SEO, and release-readiness risks.",
        "Do not deploy, install packages, mutate Git, or read secrets.",
    ],
    affected_paths=["src/checkout/Form.tsx", "api/session.ts"],
)

snapshot = RepositorySnapshot(files=[
    RepositoryFile(path="src/checkout/Form.tsx", content="...", language="tsx"),
    RepositoryFile(path="api/session.ts", content="...", language="ts"),
])

result = await run_web_development_request(scope, snapshot)
```

The public workflow runs deterministic preflight before `Runner.run(...)`. If preflight blocks, no model call occurs. If a sensitive non-executing transition is needed, approvals use stable action IDs, stable decision IDs, and human identity. Final `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE`, and `NOT_EXECUTED` are interpreted from trusted ledgers, not model prose.

## Operating model

1. Task and scope intake through `TaskScope`.
2. Existing-project stack discovery from `RepositorySnapshot`.
3. Acceptance criteria validation.
4. Application-owned specialist selection.
5. Non-mutating proposal or analysis through trusted context tools.
6. Cross-cutting security/privacy review.
7. Accessibility, performance, SEO, testing, and release-readiness review.
8. Independent final quality review after every other applicable required review reaches terminal trusted state.
9. Evidence reconciliation through application-owned evidence IDs.
10. Human approval or risk acceptance where required.
11. Final result enforcement.

Framework-specific behavior is adapted from supplied project evidence; users supply local constraints instead of rewriting the department.

## Examples

- Feature planning: pass a snapshot containing `app/routes.tsx` and `api/orders.ts`, then ask for a checkout flow plan. The lead selects frontend, backend/API, security/privacy, testing/release, and independent final review.
- Review/audit: ask "Review deployment readiness without deploying." The classifier treats deployment as a non-executing review, not a deployment.
- Stack-based specialist selection: a task mentioning REST API auth for a mobile client remains Web Development on the API side; native mobile implementation is rejected as out of scope.
- Project customization: set acceptance criteria such as "WCAG 2.2 AA, Playwright smoke tests, p95 LCP budget 2.5s, Node 22, pnpm only" without editing package source.
- Sensitive action: "Prepare a publication checklist; do not publish" can be reviewed. "Publish the package" is blocked because no publication tool exists.

## Project-specific and user-specific configuration

Already specialized and normally not modified: agents, specialists, Skills-equivalent instructions, workflows, review responsibilities, security responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model.

Values that legitimately depend on the project include framework and runtime versions, package manager policy, monorepo layout, lint/format/test commands, coverage thresholds, browser support, WCAG target, performance budgets, SEO requirements, API conventions, auth provider, storage technology, approved dependencies, deployment target, CI/CD names, environments, feature flags, observability provider, security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed integrations, model/provider configuration, private endpoints, organization IDs, and workspace IDs.

Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

The package can analyze, document, propose, classify, record trusted evidence, record non-executing approval decisions, and resume SDK state. It cannot itself edit files, run shell commands, install packages, deploy, publish, mutate Git, authenticate, retrieve secrets, spend money, sign, submit, or destroy data. Approval authorizes only a non-executing transition such as continuing sensitive analysis, preparing a human-executed plan, or recording human-owned risk acceptance.

## Limitations

Repository evidence is limited to caller-provided in-memory snapshots. Native SDK loading is validated by construction and offline tests, but live model behavior, browser behavior, deployment, publication, external integrations, and provider authentication are `NOT_EXECUTED` unless the caller separately performs and supplies trusted evidence. The offline tests use no API key and make no OpenAI API request.

## Validation

Validated on July 21, 2026: Python syntax, package construction, safe `RunConfig`, preflight, action-local policy, scope assessment, snapshot validation, trusted context binding, trusted snapshot tools, review ledger, evidence ledger, approval ledger, risk ledger, final verdict enforcement, context serializer/deserializer, and offline tests. Live model calls, browser tests, build tests for caller repositories, deployment tests, and external integration tests were not executed by this package.

## Official documentation

Verified July 21, 2026:

- OpenAI Agents SDK: https://openai.github.io/openai-agents-python/
- Agents: https://openai.github.io/openai-agents-python/agents/
- Tools: https://openai.github.io/openai-agents-python/tools/
- Guardrails: https://openai.github.io/openai-agents-python/guardrails/
- Human in the loop: https://openai.github.io/openai-agents-python/human_in_the_loop/
- RunState: https://openai.github.io/openai-agents-python/ref/run_state/
- RunConfig: https://openai.github.io/openai-agents-python/ref/run_config/
- Tracing: https://openai.github.io/openai-agents-python/tracing/
- Releases: https://openai.github.io/openai-agents-python/release/
- PyPI package: https://pypi.org/project/openai-agents/
