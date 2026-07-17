import json
import sys
import types
import unittest
from pathlib import PurePath

from mobile_development_agents.context import (
    MobileProjectContext,
    MobileTechnology,
    SDKWorkflowContext,
    WorkflowRequest,
)
from mobile_development_agents.tools.contracts import GuardedToolHost, ToolResult


class FakeToolApprovalItem:
    def __init__(self, call_id="call_1", tool_name="edit_project_file", arguments=None):
        self.call_id = call_id
        self.tool_name = tool_name
        self.name = tool_name
        self.arguments = arguments or json.dumps({"path": "app/File.kt"})
        self.agent = types.SimpleNamespace(name="mobile-development-coordinator")


class FakeRunState:
    from_string_calls = []
    from_json_calls = []

    def __init__(self, interruptions=(), context=None):
        self._interruptions = list(interruptions)
        self._context = types.SimpleNamespace(context=context) if context is not None else None
        self.approved = []
        self.rejected = []

    def get_interruptions(self):
        return tuple(self._interruptions)

    def approve(self, approval_item, *, always_approve=False):
        if not isinstance(approval_item, FakeToolApprovalItem):
            raise TypeError("approve requires a ToolApprovalItem")
        if not isinstance(always_approve, bool):
            raise TypeError("always_approve must be bool")
        self._interruptions.remove(approval_item)
        self.approved.append((approval_item, always_approve))
        return None

    def reject(self, approval_item, *, always_reject=False, rejection_message=None):
        if not isinstance(approval_item, FakeToolApprovalItem):
            raise TypeError("reject requires a ToolApprovalItem")
        if not isinstance(always_reject, bool):
            raise TypeError("always_reject must be bool")
        self._interruptions.remove(approval_item)
        self.rejected.append((approval_item, always_reject, rejection_message))
        return None

    def to_string(
        self,
        *,
        context_serializer=None,
        strict_context=False,
        include_tracing_api_key=False,
    ):
        if strict_context is not True:
            raise AssertionError("strict_context must be true")
        if include_tracing_api_key is not False:
            raise AssertionError("tracing API key must not be serialized")
        context_payload = None
        if self._context is not None:
            if context_serializer is None:
                raise AssertionError("context_serializer is required")
            context_payload = context_serializer(self._context.context)
        return json.dumps({"context": context_payload, "approvals": len(self._interruptions)})

    def to_json(
        self,
        *,
        context_serializer=None,
        strict_context=False,
        include_tracing_api_key=False,
    ):
        return json.loads(
            self.to_string(
                context_serializer=context_serializer,
                strict_context=strict_context,
                include_tracing_api_key=include_tracing_api_key,
            )
        )

    @staticmethod
    async def from_string(
        initial_agent,
        state_string,
        *,
        context_deserializer=None,
        strict_context=False,
    ):
        FakeRunState.from_string_calls.append(
            {
                "initial_agent": initial_agent,
                "state_string": state_string,
                "context_deserializer": context_deserializer,
                "strict_context": strict_context,
            }
        )
        payload = json.loads(state_string)
        context = context_deserializer(payload["context"]) if context_deserializer else None
        return FakeRunState(context=context)

    @staticmethod
    async def from_json(
        initial_agent,
        state_json,
        *,
        context_deserializer=None,
        strict_context=False,
    ):
        FakeRunState.from_json_calls.append(
            {
                "initial_agent": initial_agent,
                "state_json": state_json,
                "context_deserializer": context_deserializer,
                "strict_context": strict_context,
            }
        )
        context = context_deserializer(state_json["context"]) if context_deserializer else None
        return FakeRunState(context=context)


class FakeFunctionTool:
    def __init__(self, func, kwargs):
        self.func = func
        self.tool_name = func.__name__
        self.tool_kwargs = kwargs
        self.needs_approval = kwargs.get("needs_approval", False)
        self.tool_input_guardrails = kwargs.get("tool_input_guardrails") or []
        self.tool_output_guardrails = kwargs.get("tool_output_guardrails") or []

    def invoke(self, ctx, **kwargs):
        return self.func(ctx, **kwargs)


class FakeAgent:
    def __init__(
        self,
        *,
        name,
        instructions,
        tools=None,
        input_guardrails=None,
        output_guardrails=None,
        **kwargs,
    ):
        allowed = {"handoff_description", "model"}
        unknown = set(kwargs) - allowed
        if unknown:
            raise TypeError(f"unexpected Agent kwargs: {unknown}")
        self.name = name
        self.instructions = instructions
        self.tools = tools or []
        self.input_guardrails = input_guardrails or []
        self.output_guardrails = output_guardrails or []
        self.extra = kwargs

    def as_tool(
        self,
        *,
        tool_name,
        tool_description,
        max_turns=None,
        run_config=None,
        hooks=None,
        previous_response_id=None,
        conversation_id=None,
        session=None,
        needs_approval=False,
        parameters=None,
        input_builder=None,
        include_input_schema=False,
    ):
        if not isinstance(needs_approval, bool) and not callable(needs_approval):
            raise TypeError("needs_approval must be bool or callable")
        return types.SimpleNamespace(
            kind="agent_tool",
            tool_name=tool_name,
            tool_description=tool_description,
            needs_approval=needs_approval,
            max_turns=max_turns,
            run_config=run_config,
            hooks=hooks,
            previous_response_id=previous_response_id,
            conversation_id=conversation_id,
            session=session,
            parameters=parameters,
            input_builder=input_builder,
            include_input_schema=include_input_schema,
        )


class FakeRunner:
    calls = []

    @staticmethod
    async def run(agent, input, *, context=None, run_config=None, max_turns=None, **kwargs):
        allowed = {
            "session",
            "conversation_id",
            "previous_response_id",
            "auto_previous_response_id",
        }
        unknown = set(kwargs) - allowed
        if unknown:
            raise TypeError(f"unexpected Runner.run kwargs: {unknown}")
        FakeRunner.calls.append(
            {
                "agent": agent,
                "input": input,
                "context": context,
                "run_config": run_config,
                "max_turns": max_turns,
                **kwargs,
            }
        )
        return types.SimpleNamespace(
            interruptions=(),
            final_output="ok",
            to_state=lambda: FakeRunState(),
        )


class FakeRunConfig:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class FakeToolExecutionConfig:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class FakeGuardrailFunctionOutput:
    def __init__(self, output_info=None, tripwire_triggered=False):
        self.output_info = output_info
        self.tripwire_triggered = tripwire_triggered


class FakeToolGuardrailFunctionOutput:
    @staticmethod
    def allow(output_info=None):
        return types.SimpleNamespace(decision="allow", output_info=output_info)

    @staticmethod
    def reject_content(message, output_info=None):
        return types.SimpleNamespace(
            decision="reject_content",
            message=message,
            output_info=output_info,
        )


def _mark(kind):
    def decorator(fn=None, **kwargs):
        allowed = {"name"} if kind.startswith("tool_") else {"run_in_parallel", "name"}
        unknown = set(kwargs) - allowed
        if unknown:
            raise TypeError(f"unexpected guardrail kwargs: {unknown}")

        def wrap(inner):
            inner.guardrail_kind = kind
            inner.guardrail_kwargs = kwargs
            inner.guardrail_function = inner
            return inner

        return wrap(fn) if fn is not None else wrap

    return decorator


def fake_function_tool(fn=None, **kwargs):
    allowed = {
        "name_override",
        "description_override",
        "docstring_style",
        "use_docstring_info",
        "failure_error_function",
        "strict_mode",
        "is_enabled",
        "needs_approval",
        "tool_input_guardrails",
        "tool_output_guardrails",
        "timeout",
        "timeout_behavior",
        "timeout_error_function",
        "defer_loading",
        "custom_data_extractor",
    }
    unknown = set(kwargs) - allowed
    if unknown:
        raise TypeError(f"unexpected function_tool kwargs: {unknown}")
    if (
        "needs_approval" in kwargs
        and not isinstance(kwargs["needs_approval"], bool)
        and not callable(kwargs["needs_approval"])
    ):
        raise TypeError("needs_approval must be bool or callable")

    def wrap(inner):
        return FakeFunctionTool(inner, kwargs)

    return wrap(fn) if fn is not None else wrap


def install_fake_agents():
    fake = types.ModuleType("agents")
    fake.Agent = FakeAgent
    fake.Runner = FakeRunner
    fake.RunState = FakeRunState
    fake.RunConfig = FakeRunConfig
    fake.ToolExecutionConfig = FakeToolExecutionConfig
    fake.GuardrailFunctionOutput = FakeGuardrailFunctionOutput
    fake.ToolGuardrailFunctionOutput = FakeToolGuardrailFunctionOutput
    fake.input_guardrail = _mark("input")
    fake.output_guardrail = _mark("output")
    fake.tool_input_guardrail = _mark("tool_input")
    fake.tool_output_guardrail = _mark("tool_output")
    fake.function_tool = fake_function_tool
    fake.RunContextWrapper = object
    sys.modules["agents"] = fake
    return fake


def request():
    context = MobileProjectContext(
        project_root=PurePath("app"),
        technologies=frozenset({MobileTechnology.ANDROID}),
        detected_commands=("python3 -m unittest",),
    )
    return WorkflowRequest(
        workflow="implement-mobile-feature",
        objective="add a safe feature",
        technologies=frozenset({MobileTechnology.ANDROID}),
        project_context=context,
        human_approvals=frozenset({"project-edit"}),
    )


class CountingHost:
    def __init__(self):
        self.read_count = 0
        self.edit_count = 0
        self.validation_count = 0

    def read_project_file(self, path):
        self.read_count += 1
        return ToolResult(True, f"read:{path}", "host")

    def edit_project_file(self, path, content):
        self.edit_count += 1
        return ToolResult(True, f"edited:{path}:{content}", "host")

    def run_validation_command(self, command):
        self.validation_count += 1
        return ToolResult(True, f"ran:{command}", "host")


class SDKWiringTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        install_fake_agents()
        FakeRunner.calls = []
        FakeRunState.from_string_calls = []
        FakeRunState.from_json_calls = []

    def test_coordinator_has_guardrails_function_tools_and_agent_tool_approvals(self):
        from mobile_development_agents.agents.coordinator import build_coordinator_agent

        agent = build_coordinator_agent()
        self.assertTrue(agent.input_guardrails)
        self.assertEqual(agent.input_guardrails[0].guardrail_kind, "input")
        self.assertFalse(agent.input_guardrails[0].guardrail_kwargs["run_in_parallel"])
        self.assertTrue(agent.output_guardrails)
        self.assertEqual(agent.output_guardrails[0].guardrail_kind, "output")

        tools = {tool.tool_name: tool for tool in agent.tools}
        self.assertIn("read_project_file", tools)
        self.assertIn("edit_project_file", tools)
        self.assertIn("run_validation_command", tools)
        self.assertTrue(tools["mobile_release_engineer"].needs_approval)
        self.assertTrue(tools["mobile_code_reviewer"].needs_approval)
        self.assertFalse(tools["android_engineer"].needs_approval)

    def test_function_tools_have_guardrails_and_sdk_approval_gates(self):
        from mobile_development_agents.tools.sdk_tools import build_project_function_tools

        tools = {tool.tool_name: tool for tool in build_project_function_tools()}
        self.assertTrue(tools["read_project_file"].tool_input_guardrails)
        self.assertTrue(tools["read_project_file"].tool_output_guardrails)
        self.assertFalse(tools["read_project_file"].needs_approval)
        self.assertTrue(tools["edit_project_file"].needs_approval)
        self.assertTrue(tools["run_validation_command"].needs_approval)

    async def test_run_workflow_passes_typed_context_run_config_and_bounded_turns(self):
        from mobile_development_agents.app import run_workflow

        await run_workflow(request(), host=CountingHost())
        call = FakeRunner.calls[-1]
        self.assertEqual(call["max_turns"], 12)
        self.assertEqual(call["context"].request.workflow, "implement-mobile-feature")
        self.assertTrue(call["run_config"].tool_execution.pre_approval_tool_input_guardrails)

    def test_runtime_approval_helpers_use_real_items_and_exact_signatures(self):
        from mobile_development_agents.runtime import approve_pending_item, reject_pending_item

        approved_item = FakeToolApprovalItem(call_id="approve_1")
        rejected_item = FakeToolApprovalItem(call_id="reject_1")
        context = SDKWorkflowContext(request=request())
        state = FakeRunState((approved_item, rejected_item), context=context)

        approve_pending_item(
            state,
            "approve_1",
            always_approve=False,
            workflow_context=context,
        )
        reject_pending_item(
            state,
            "reject_1",
            "not safe",
            always_reject=False,
            workflow_context=context,
        )

        self.assertEqual(state.approved, [(approved_item, False)])
        self.assertEqual(state.rejected, [(rejected_item, False, "not safe")])
        self.assertEqual(
            context.approval_audit[0],
            "approved:mobile-development-coordinator.edit_project_file",
        )
        self.assertIn(
            "rejected:mobile-development-coordinator.edit_project_file:not safe",
            context.approval_audit,
        )

        with self.assertRaises(TypeError):
            state.approve("approve_1", always_approve=False)
        with self.assertRaises(TypeError):
            state.reject("reject_1", always_reject=False, rejection_message="reason")

    def test_runtime_rejects_unknown_missing_duplicate_or_resolved_ids(self):
        from mobile_development_agents.runtime import approve_pending_item

        with self.assertRaises(ValueError):
            approve_pending_item(FakeRunState(()), "missing")
        with self.assertRaises(ValueError):
            approve_pending_item(FakeRunState((FakeToolApprovalItem(call_id="known"),)), "unknown")
        with self.assertRaises(ValueError):
            approve_pending_item(
                FakeRunState(
                    (
                        FakeToolApprovalItem(call_id="dup"),
                        FakeToolApprovalItem(call_id="dup"),
                    )
                ),
                "dup",
            )
        state = FakeRunState((FakeToolApprovalItem(call_id="once"),))
        approve_pending_item(state, "once")
        with self.assertRaises(ValueError):
            approve_pending_item(state, "once")

    def test_repeated_pause_cycles_resolve_only_current_pending_items(self):
        from mobile_development_agents.runtime import approve_pending_item, reject_pending_item

        first_item = FakeToolApprovalItem(call_id="first")
        first_state = FakeRunState((first_item,))
        approve_pending_item(first_state, "first")

        second_item = FakeToolApprovalItem(call_id="second")
        second_state = FakeRunState((second_item,))
        with self.assertRaises(ValueError):
            approve_pending_item(second_state, "first")
        reject_pending_item(second_state, "second", "denied on repeated pause")

        self.assertEqual(first_state.approved, [(first_item, False)])
        self.assertEqual(second_state.rejected, [(second_item, False, "denied on repeated pause")])

    async def test_serialization_deserialization_and_resume_use_official_shapes(self):
        from mobile_development_agents.runtime import (
            load_run_state_from_json,
            load_run_state_from_string,
            resume_approved_run,
            serialize_run_state,
        )

        coordinator = FakeAgent(name="coordinator", instructions="test")
        context = SDKWorkflowContext(request=request())
        state = FakeRunState((FakeToolApprovalItem(),), context=context)
        serialized = serialize_run_state(state)
        self.assertIsInstance(json.loads(serialized), dict)
        self.assertNotIn("CountingHost", serialized)

        loaded = await load_run_state_from_string(coordinator, serialized, tool_host=CountingHost())
        self.assertIsInstance(loaded._context.context.tool_host, CountingHost)
        self.assertTrue(FakeRunState.from_string_calls[-1]["strict_context"])

        loaded_json = await load_run_state_from_json(
            coordinator,
            json.loads(serialized),
            tool_host=CountingHost(),
        )
        self.assertIsInstance(loaded_json._context.context.tool_host, CountingHost)
        self.assertTrue(FakeRunState.from_json_calls[-1]["strict_context"])

        await resume_approved_run(coordinator, state, max_turns=12)
        self.assertIs(FakeRunner.calls[-1]["agent"], coordinator)
        self.assertIs(FakeRunner.calls[-1]["input"], state)
        self.assertEqual(FakeRunner.calls[-1]["max_turns"], 12)

    def test_approved_edit_reaches_host_once_without_second_denial(self):
        from mobile_development_agents.tools.sdk_tools import build_project_function_tools

        host = CountingHost()
        context = SDKWorkflowContext(request=request(), tool_host=GuardedToolHost(host))
        ctx = types.SimpleNamespace(context=context)
        tools = {tool.tool_name: tool for tool in build_project_function_tools()}

        result = tools["edit_project_file"].invoke(ctx, path="app/File.kt", content="safe content")

        self.assertTrue(result.ok)
        self.assertEqual(host.edit_count, 1)

    def test_rejected_edit_never_reaches_host(self):
        from mobile_development_agents.runtime import reject_pending_item

        host = CountingHost()
        state = FakeRunState(
            (FakeToolApprovalItem(call_id="edit_1"),),
            SDKWorkflowContext(request=request()),
        )
        reject_pending_item(state, "edit_1", "denied")
        self.assertEqual(host.edit_count, 0)

    def test_tool_guardrails_parse_structured_arguments(self):
        from mobile_development_agents.guardrails.tools import validate_tool_arguments

        self.assertEqual(validate_tool_arguments("read_project_file", {"path": "app/File.kt"}), ())
        self.assertTrue(validate_tool_arguments("read_project_file", {"path": "../secret.txt"}))
        self.assertTrue(
            validate_tool_arguments(
                "edit_project_file",
                {"path": "app/File.kt", "content": "password='example-redacted-value'"},
            )
        )
        self.assertTrue(
            validate_tool_arguments(
                "run_validation_command",
                {"command": "pytest && rm -rf build"},
            )
        )
        self.assertEqual(
            validate_tool_arguments("run_validation_command", {"command": "pytest tests"}),
            (),
        )

    def test_review_specialists_receive_no_edit_capable_project_tools(self):
        from mobile_development_agents.agents.definitions import READ_ONLY_REVIEWERS
        from mobile_development_agents.agents import build_all_specialists

        specialists = build_all_specialists()
        for name in READ_ONLY_REVIEWERS:
            with self.subTest(name=name):
                self.assertEqual(specialists[name].tools, [])


if __name__ == "__main__":
    unittest.main()
