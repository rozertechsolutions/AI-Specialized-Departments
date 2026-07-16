# OpenAI Agents SDK Mobile Development

This specialization implements a native Python package for the OpenAI Agents SDK. It coordinates mobile development work across Android, iOS, Kotlin Multiplatform, Flutter, and React Native while keeping security-sensitive and release actions under human control.

## Verified Surface

- Platform: OpenAI Agents SDK for Python.
- Package checked: `openai-agents` version `0.18.2`, requiring Python `>=3.10`.
- Native capabilities used: `Agent`, `Runner`, function tools, agents-as-tools, handoffs where ownership transfers, input/output/tool guardrails, sessions, tracing controls, and host-injected human approval contracts.
- Unsupported or intentionally omitted: active MCP connections, hosted web/file/code-interpreter tools, daemon/UI/server processes, deployment, signing, publishing, uploading, store submission, automatic dependency installation, and any real credential import.

## Responsibility Model

The coordinator owns routing and synthesis. The twelve specialists preserve exclusive responsibility boundaries:

1. `mobile-architect`
2. `android-engineer`
3. `ios-engineer`
4. `kmp-engineer`
5. `flutter-engineer`
6. `react-native-engineer`
7. `mobile-test-engineer`
8. `mobile-security-reviewer`
9. `mobile-ui-accessibility-reviewer`
10. `mobile-performance-reviewer`
11. `mobile-release-engineer`
12. `mobile-code-reviewer`

Review roles are read-only by default. Implementation roles do not perform their own independent final review. `mobile-code-reviewer` is the final independent reviewer and never reviews its own implementation.

## Workflows

The package defines ten typed workflows:

- `create-mobile-project`
- `implement-mobile-feature`
- `fix-mobile-bug`
- `review-mobile-architecture`
- `add-mobile-screen`
- `integrate-mobile-api`
- `add-mobile-tests`
- `optimize-mobile-performance`
- `audit-mobile-security`
- `prepare-mobile-release`

Each workflow declares triggers, supported technologies, preconditions, ordered steps, validation gates, stop conditions, evidence requirements, outputs, acceptance criteria, human approvals, and prohibited actions.

## Runtime Notes

The package declares the SDK dependency but does not install dependencies or run OpenAI API calls during import. Host applications must inject project tools through `ToolHost`.

`run_workflow()` wraps the host in `GuardedToolHost`, passes an `SDKWorkflowContext` to `Runner.run`, and exposes three SDK function tools:

- `read_project_file`
- `edit_project_file`
- `run_validation_command`

The edit and validation tools require SDK approval interruptions. Tool input and output guardrails wrap every host function tool. Agent-level input guardrails attach to the coordinator, and output guardrails attach to the final coordinator boundary.

Human-in-the-loop helpers in `runtime.py` expose pending approval interruptions, run-state serialization, explicit approve/reject operations, and resume through the SDK `Runner`. The package never auto-approves interrupted tool calls.

Use `OPENAI_AGENTS_MODEL` to select a model at runtime. No model is hardcoded.

## Validation

Network-free tests cover:

- workflow ownership and reviewer routing
- no self-review
- approval gating for risky actions
- shell/path guard behavior
- secret redaction and detection
- completion criteria classification
- package import without live API calls
- SDK wiring for coordinator guardrails, function-tool guardrails, agent-as-tool approval, host context, pending interruptions, and bounded runner execution

The tests are offline and use deterministic fakes for SDK wiring. They are provided for manual execution by a host developer; this static package generation task did not run them.

Official documentation consulted:

- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/agents/
- https://openai.github.io/openai-agents-python/running_agents/
- https://openai.github.io/openai-agents-python/tools/
- https://openai.github.io/openai-agents-python/handoffs/
- https://openai.github.io/openai-agents-python/guardrails/
- https://openai.github.io/openai-agents-python/sessions/
- https://openai.github.io/openai-agents-python/human_in_the_loop/
