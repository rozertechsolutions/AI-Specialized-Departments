import sys
import types
import unittest
from pathlib import PurePath

from mobile_development_agents.context import MobileProjectContext, MobileTechnology, WorkflowRequest
from mobile_development_agents.tools.contracts import ToolResult


class FakeAgent:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def as_tool(self, **kwargs):
        tool = types.SimpleNamespace(kind="agent_tool", **kwargs)
        return tool


class FakeRunner:
    last_call = None

    @staticmethod
    async def run(agent, input, **kwargs):
        FakeRunner.last_call = {"agent": agent, "input": input, **kwargs}
        return types.SimpleNamespace(interruptions=(), final_output="ok")


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
    def allow():
        return types.SimpleNamespace(decision="allow")

    @staticmethod
    def reject_content(message):
        return types.SimpleNamespace(decision="reject", message=message)


def _mark(kind):
    def decorator(fn=None, **kwargs):
        def wrap(inner):
            inner.guardrail_kind = kind
            inner.guardrail_kwargs = kwargs
            return inner
        return wrap(fn) if fn is not None else wrap
    return decorator


def fake_function_tool(fn=None, **kwargs):
    def wrap(inner):
        inner.tool_kwargs = kwargs
        inner.tool_name = inner.__name__
        return inner
    return wrap(fn) if fn is not None else wrap


def install_fake_agents():
    fake = types.ModuleType("agents")
    fake.Agent = FakeAgent
    fake.Runner = FakeRunner
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


class Host:
    def read_project_file(self, path):
        return ToolResult(True, f"read:{path}", "host")

    def edit_project_file(self, path, content):
        return ToolResult(True, f"edited:{path}:{content}", "host")

    def run_validation_command(self, command):
        return ToolResult(True, f"ran:{command}", "host")


class SDKWiringTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        install_fake_agents()

    def test_coordinator_has_input_output_guardrails_and_host_function_tools(self):
        from mobile_development_agents.agents.coordinator import build_coordinator_agent

        agent = build_coordinator_agent()
        self.assertTrue(agent.input_guardrails)
        self.assertEqual(agent.input_guardrails[0].guardrail_kind, "input")
        self.assertFalse(agent.input_guardrails[0].guardrail_kwargs["run_in_parallel"])
        self.assertTrue(agent.output_guardrails)
        self.assertEqual(agent.output_guardrails[0].guardrail_kind, "output")
        names = {getattr(tool, "tool_name", getattr(tool, "tool_name", "")) for tool in agent.tools}
        self.assertIn("read_project_file", names)
        self.assertIn("edit_project_file", names)
        self.assertIn("run_validation_command", names)

    def test_function_tools_have_tool_guardrails_and_approval_gates(self):
        from mobile_development_agents.tools.sdk_tools import build_project_function_tools

        tools = {tool.tool_name: tool for tool in build_project_function_tools()}
        self.assertIn("tool_input_guardrails", tools["read_project_file"].tool_kwargs)
        self.assertIn("tool_output_guardrails", tools["read_project_file"].tool_kwargs)
        self.assertTrue(tools["edit_project_file"].tool_kwargs["needs_approval"])
        self.assertTrue(tools["run_validation_command"].tool_kwargs["needs_approval"])

    async def test_run_workflow_passes_typed_context_run_config_and_bounded_turns(self):
        from mobile_development_agents.app import run_workflow

        await run_workflow(request(), host=Host())
        call = FakeRunner.last_call
        self.assertIsNotNone(call)
        self.assertEqual(call["max_turns"], 12)
        self.assertEqual(call["context"].request.workflow, "implement-mobile-feature")
        self.assertTrue(call["run_config"].tool_execution.pre_approval_tool_input_guardrails)

    def test_runtime_exposes_pending_approval_and_serialization_helpers(self):
        from mobile_development_agents.runtime import pending_approval_interruptions, serialize_run_state

        interruption = types.SimpleNamespace(id="call_1", name="edit_project_file", reason="approval")
        state = types.SimpleNamespace(to_string=lambda: "serialized")
        result = types.SimpleNamespace(interruptions=(interruption,), to_state=lambda: state)
        pending = pending_approval_interruptions(result)
        self.assertEqual(pending[0].id, "call_1")
        self.assertEqual(serialize_run_state(result), "serialized")


if __name__ == "__main__":
    unittest.main()
