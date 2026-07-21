import asyncio
import os
import unittest

from agents import Agent, Model, ModelResponse, Runner, function_tool
from agents.usage import Usage
from openai.types.responses import ResponseFunctionToolCall, ResponseOutputMessage, ResponseOutputText


class DeterministicModel(Model):
    def __init__(self) -> None:
        self.calls = 0

    async def get_response(self, *args, **kwargs) -> ModelResponse:
        self.calls += 1
        if self.calls == 1:
            return ModelResponse(
                output=[
                    ResponseFunctionToolCall(
                        arguments='{"value":"scoped-change"}',
                        call_id="call_approval_1",
                        name="sensitive_write",
                        type="function_call",
                    )
                ],
                usage=Usage(),
                response_id="response_1",
            )
        return ModelResponse(
            output=[
                ResponseOutputMessage(
                    id="message_1",
                    content=[ResponseOutputText(annotations=[], text="evidence-backed final state", type="output_text")],
                    role="assistant",
                    status="completed",
                    type="message",
                )
            ],
            usage=Usage(),
            response_id="response_2",
        )

    async def stream_response(self, *args, **kwargs):
        if False:
            yield None


class SdkRuntimeTests(unittest.TestCase):
    def test_public_sdk_symbols_import(self) -> None:
        self.assertIsNotNone(Agent)
        self.assertIsNotNone(Runner)
        self.assertIsNotNone(function_tool)
        self.assertIsNotNone(ModelResponse)

    def test_real_sdk_hitl_approve_reject_and_resume_with_injected_model(self) -> None:
        executed: list[str] = []

        @function_tool(needs_approval=True)
        def sensitive_write(value: str) -> str:
            executed.append(value)
            return f"wrote {value}"

        async def run_approve() -> str:
            agent = Agent(name="approval-test", instructions="Call the tool, then finish.", model=DeterministicModel(), tools=[sensitive_write])
            result = await Runner.run(agent, "request scoped write", max_turns=4)
            self.assertEqual(len(result.interruptions), 1)
            self.assertEqual(result.interruptions[0].tool_name, "sensitive_write")
            state = result.to_state()
            state.approve(result.interruptions[0])
            resumed = await Runner.run(agent, state, max_turns=4)
            return resumed.final_output

        async def run_reject() -> str:
            agent = Agent(name="rejection-test", instructions="Call the tool, then finish.", model=DeterministicModel(), tools=[sensitive_write])
            result = await Runner.run(agent, "request scoped write", max_turns=4)
            self.assertEqual(len(result.interruptions), 1)
            state = result.to_state()
            state.reject(result.interruptions[0], rejection_message="human rejected")
            resumed = await Runner.run(agent, state, max_turns=4)
            return resumed.final_output

        approved_output = asyncio.run(run_approve())
        self.assertEqual(approved_output, "evidence-backed final state")
        self.assertEqual(executed, ["scoped-change"])

        rejected_output = asyncio.run(run_reject())
        self.assertEqual(rejected_output, "evidence-backed final state")
        self.assertEqual(executed, ["scoped-change"])

    def test_no_api_key_or_external_model_is_required(self) -> None:
        for key in (
            "OPENAI_API_KEY",
            "OPENAI_BASE_URL",
            "OPENAI_ORG_ID",
            "OPENAI_PROJECT_ID",
            "AZURE_OPENAI_API_KEY",
            "AZURE_OPENAI_ENDPOINT",
        ):
            self.assertNotIn(key, os.environ)


if __name__ == "__main__":
    unittest.main()
