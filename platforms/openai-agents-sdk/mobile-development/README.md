# OpenAI Agents SDK Mobile Development

This specialization implements a native Python package for the OpenAI Agents SDK. It coordinates mobile development work across Android, iOS, Kotlin Multiplatform, Flutter, and React Native while keeping security-sensitive and release actions under human control.

## Verified Surface

- Platform: OpenAI Agents SDK for Python.
- Package checked: `openai-agents` version `0.18.2`, requiring Python `>=3.10`.
- Native capabilities used: `Agent`, `Runner`, function tools, agents-as-tools, handoffs where ownership transfers, input/output/tool guardrails, sessions, tracing controls, `RunState`, and SDK human-in-the-loop approval interruptions.
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

The edit and validation tools require SDK approval interruptions through `needs_approval=True`. SDK HITL is the authoritative approval mechanism for those function tools. The host wrapper still validates project-relative paths, non-destructive validation commands, and secret-free edit/output content, but it does not ask for a second approval after the SDK has approved the same tool call. Direct non-SDK callers may still provide an explicit `ApprovalProvider` to `GuardedToolHost` when they want a separate host-level approval path.

Human-in-the-loop helpers in `runtime.py` expose pending approval interruptions, run-state serialization, explicit approve/reject operations, deserialization, and resume through the SDK `Runner`. The package never auto-approves interrupted tool calls.

The HITL lifecycle is:

1. `Runner.run(coordinator, prompt, context=SDKWorkflowContext(...), run_config=..., max_turns=12)` starts the top-level coordinator.
2. If a function tool or approved agent-as-tool needs approval, the SDK pauses and returns `result.interruptions`.
3. `pending_approval_interruptions(result)` returns safe UI metadata while preserving the actual pending approval item object.
4. Persist the paused run with `serialize_run_state(result)` or `serialize_run_state(state)`, which uses `RunState.to_string(...)` and explicit `SDKWorkflowContext` serialization. The injected host object and tracing API key are not serialized.
5. Resolve a pending item with `approve_pending_item(state, id, always_approve=False, workflow_context=context)` or `reject_pending_item(state, id, reason, always_reject=False, workflow_context=context)`. These helpers look up the current pending item from `state.get_interruptions()` and call the official SDK signatures with the actual approval item object. The optional workflow context records safe approval audit entries without storing secrets.
6. Resume with `resume_approved_run(coordinator, state, max_turns=12)`, which calls `Runner.run(coordinator, state, ...)` using the original top-level coordinator. New interruptions can pause the run again and must be resolved through the same flow.

For durable resume, use `load_run_state_from_string(coordinator, state_string, tool_host=...)` or `load_run_state_from_json(coordinator, state_json, tool_host=...)`. Long-lived paused state is compatible only with matching `openai-agents==0.18.2`, matching agent/tool definitions, and the `mobile-development-sdk-workflow-context.v1` context schema.

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
- SDK wiring for coordinator guardrails, function-tool guardrails, agent-as-tool approval, host context, pending interruptions, official approve/reject signatures, serialization/deserialization, repeated pauses, and bounded runner execution

The tests are offline and use deterministic SDK doubles that enforce the public signatures used by this package. They are provided for manual execution by a host developer; this static package generation task did not run them. Importing this package makes no OpenAI API call, starts no external integration, stores no credential, and installs no dependency.

Official documentation consulted:

- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/agents/
- https://openai.github.io/openai-agents-python/running_agents/
- https://openai.github.io/openai-agents-python/tools/
- https://openai.github.io/openai-agents-python/handoffs/
- https://openai.github.io/openai-agents-python/guardrails/
- https://openai.github.io/openai-agents-python/ref/run_state/
- https://openai.github.io/openai-agents-python/ref/tool/
- https://openai.github.io/openai-agents-python/ref/tool_guardrails/
- https://openai.github.io/openai-agents-python/sessions/
- https://openai.github.io/openai-agents-python/human_in_the_loop/
