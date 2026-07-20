from __future__ import annotations

import asyncio
import json
import os
import socket
import unittest
from importlib.metadata import version
from pathlib import Path
from typing import AsyncIterator, get_type_hints

from agents import Agent, Model, ModelSettings, ModelTracing, RunConfig, Runner
from agents.run_config import ToolExecutionConfig
from agents.items import ModelResponse
from agents.models.interface import TResponseInputItem, TResponseStreamEvent
from agents.usage import Usage
from openai.types.responses import ResponseFunctionToolCall, ResponseOutputMessage, ResponseOutputText

from software_development_department import DepartmentRuntime, FinalState, RunLimits
from software_development_department.agents import SPECIALIST_OUTPUTS, build_department_agents
from software_development_department.models import (
    ApprovalDecision,
    ArchitectureDecision,
    ArchitectureOutput,
    CodeQualityReview,
    CodeReviewOutput,
    DocumentationReadinessOutput,
    DocumentationReleaseReadinessResult,
    EngineeringRiskReview,
    EvidenceItem,
    ImplementationChangeProposal,
    ImplementationEvidence,
    ImplementationPlan,
    LeadFinalRecord,
    RequirementsAcceptanceCriteria,
    RequirementsOutput,
    RiskLevel,
    RiskReviewOutput,
    RoleSlug,
    SpecialistInput,
    TaskRequest,
    TaskScope,
    ValidationEvidence,
)
from software_development_department.policies import derive_final_state, final_record_is_supported, normalize_relative_path
from software_development_department.tools import (
    DepartmentContext,
    DeterministicApprovalProvider,
    MemoryRepositoryReader,
    MemoryRepositoryWriter,
    RunLimits,
    build_repository_tools,
)


PRE_APPROVAL_CONFIG = RunConfig(
    tracing_disabled=True,
    tool_execution=ToolExecutionConfig(pre_approval_tool_input_guardrails=True),
)


def enum_value(value: object) -> object:
    return value.value if hasattr(value, "value") else value


def evidence(claim: str = "observed") -> dict[str, object]:
    return {"claim": claim, "source": "context", "observed": True, "limitation": None}


def specialist_json(role: RoleSlug) -> str:
    base = {"role": role.value, "summary": role.value, "evidence": [evidence(role.value)], "assumptions": [], "limitations": [], "checks_not_run": []}
    if role is RoleSlug.REQUIREMENTS:
        base["requirements_result"] = {"requirements": ["req"], "acceptance_criteria": ["ok"], "unresolved_questions": []}
        base["plan"] = {
            "steps": ["plan"],
            "validation_steps": ["validate"],
            "required_specialists": [RoleSlug.REQUIREMENTS.value],
            "approval_checkpoints": [],
        }
    elif role is RoleSlug.ARCHITECTURE:
        base["architecture"] = {"decisions": ["decision"], "contracts": [], "migration_implications": [], "compatibility_notes": []}
    elif role is RoleSlug.IMPLEMENTATION:
        base["proposal"] = {"changed_paths": ["src/example.py"], "change_summary": "change", "approved_scope_reference": "task", "validation_notes": []}
    elif role is RoleSlug.TESTING:
        base["passed_checks"] = ["unit"]
        base["failed_checks"] = []
        base["untested_areas"] = []
    elif role is RoleSlug.CODE_REVIEW:
        base["review"] = {"approved": True, "findings": [], "blocking_findings": []}
    elif role is RoleSlug.RISK_REVIEW:
        base["review"] = {"approved": True, "risks": [], "required_mitigations": []}
    elif role is RoleSlug.DOCUMENTATION:
        base["readiness"] = {"documentation_updates": [], "release_readiness": "ready_for_human", "stop_before_release": True}
    return json.dumps(base)


def final_record_json(required: list[RoleSlug], final_state: FinalState = FinalState.BLOCKED) -> str:
    req_output = json.loads(specialist_json(RoleSlug.REQUIREMENTS)) if RoleSlug.REQUIREMENTS in required else None
    return json.dumps(
        {
            "objective": "task",
            "requirements_result": req_output,
            "implementation_plan": req_output["plan"] if req_output else None,
            "architecture_result": None,
            "required_specialist_roles": [role.value for role in required],
            "specialist_completion_order": [role.value for role in required],
            "completed_requirements": ["req"] if final_state is FinalState.COMPLETED else [],
            "unmet_requirements": [] if final_state is FinalState.COMPLETED else ["blocked"],
            "implementation_evidence": None,
            "validation_evidence": None,
            "code_quality_review_result": None,
            "engineering_risk_review_result": None,
            "documentation_release_readiness_result": None,
            "approvals_and_rejections": [],
            "remaining_risks": [],
            "limitations": [],
            "checks_not_executed": ["not needed"],
            "final_state": final_state.value,
        }
    )


class ScriptedModel(Model):
    def __init__(self, steps: list[dict[str, object]], name: str) -> None:
        self.steps = steps
        self.name = name
        self.calls = 0

    async def get_response(
        self,
        system_instructions: str | None,
        input: str | list[TResponseInputItem],
        model_settings: ModelSettings,
        tools: list[object],
        output_schema: object | None,
        handoffs: list[object],
        tracing: ModelTracing,
        *,
        previous_response_id: str | None,
        conversation_id: str | None,
        prompt: object | None,
    ) -> ModelResponse:
        if self.calls >= len(self.steps):
            raise AssertionError(f"unexpected extra model call: {self.name}")
        step = self.steps[self.calls]
        self.calls += 1
        if step["kind"] == "tool":
            output = [
                ResponseFunctionToolCall(
                    id=f"fc_{self.name}_{self.calls}",
                    call_id=str(step.get("call_id", f"call_{self.name}_{self.calls}")),
                    name=str(step["name"]),
                    arguments=json.dumps(step["arguments"]),
                    status="completed",
                    type="function_call",
                )
            ]
        else:
            text = str(step["text"])
            if output_schema is not None:
                text = json.dumps({"response": json.loads(text)})
            output = [
                ResponseOutputMessage(
                    id=f"msg_{self.name}_{self.calls}",
                    content=[ResponseOutputText(annotations=[], text=text, type="output_text")],
                    role="assistant",
                    status="completed",
                    type="message",
                )
            ]
        return ModelResponse(output=output, usage=Usage(), response_id=f"response_{self.name}_{self.calls}")

    async def stream_response(
        self,
        system_instructions: str | None,
        input: str | list[TResponseInputItem],
        model_settings: ModelSettings,
        tools: list[object],
        output_schema: object | None,
        handoffs: list[object],
        tracing: ModelTracing,
        *,
        previous_response_id: str | None,
        conversation_id: str | None,
        prompt: object | None,
    ) -> AsyncIterator[TResponseStreamEvent]:
        raise AssertionError("streaming is not used in deterministic tests")


class NetworkBlocker:
    def __enter__(self) -> "NetworkBlocker":
        self.original_create_connection = socket.create_connection
        self.original_connect = socket.socket.connect

        def fail(*args: object, **kwargs: object) -> None:
            raise AssertionError("network call attempted")

        socket.create_connection = fail
        socket.socket.connect = fail
        return self

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        socket.create_connection = self.original_create_connection
        socket.socket.connect = self.original_connect


class DepartmentRuntimeTests(unittest.TestCase):
    def make_context(self, lead_model: Model | None = None, specialist_models: dict[RoleSlug, Model] | None = None) -> DepartmentContext:
        context = DepartmentContext(
            repository_reader=MemoryRepositoryReader({"src/example.py": "old", "src/nested/example.py": "nested"}),
            repository_writer=MemoryRepositoryWriter(),
            approval_provider=DeterministicApprovalProvider(),
            workspace_root=Path("/workspace"),
            limits=RunLimits(max_top_level_turns=8, max_turns_per_specialist=3, max_calls_per_specialist=1, max_total_specialist_calls=3),
            lead_model=lead_model,
            specialist_models=specialist_models or {},
        )
        context.start_task(TaskRequest("task", TaskScope(("src",)), ("ok",), RiskLevel.MEDIUM))
        return context

    def specialist_models(self) -> dict[RoleSlug, Model]:
        return {role: ScriptedModel([{"kind": "message", "text": specialist_json(role)}], role.value) for role in RoleSlug}

    def test_sdk_version_imports_and_function_tool_construction(self) -> None:
        self.assertEqual(version("openai-agents"), "0.18.3")
        read_tool, write_tool = build_repository_tools()
        self.assertEqual(read_tool.name, "read_repository_file")
        self.assertEqual(write_tool.name, "write_repository_file")
        self.assertTrue(callable(Runner.run))

    def test_constructs_lead_specialists_models_tools_and_no_handoffs(self) -> None:
        lead = ScriptedModel([{"kind": "message", "text": final_record_json([])}], "lead")
        context = self.make_context(lead, self.specialist_models())
        agents = build_department_agents(context)
        self.assertEqual(agents.lead.name, "software-development-lead")
        self.assertEqual(set(agents.specialists), set(SPECIALIST_OUTPUTS))
        self.assertEqual(len(agents.specialists), 7)
        specialist_tool_names = {slug.replace("-", "_") for slug in SPECIALIST_OUTPUTS}
        self.assertEqual(specialist_tool_names, {tool.name for tool in agents.lead.tools if tool.name in specialist_tool_names})
        self.assertEqual(agents.lead.handoffs, [])
        self.assertTrue(all(agent.handoffs == [] for agent in agents.specialists.values()))
        self.assertIs(agents.lead.output_type, LeadFinalRecord)
        self.assertIs(agents.lead.model, lead)
        self.assertTrue(all(agent.model is not None for agent in agents.specialists.values()))
        hints = get_type_hints(ArchitectureOutput)
        self.assertIs(hints["architecture"], ArchitectureDecision)

    def test_manager_calls_specialist_and_returns_control_to_lead(self) -> None:
        required = [RoleSlug.REQUIREMENTS]
        lead = ScriptedModel(
            [
                {
                    "kind": "tool",
                    "name": RoleSlug.REQUIREMENTS.value.replace("-", "_"),
                    "arguments": {"task": {"objective": "task", "scope": {"authorized_paths": ["src"], "exclusions": [], "prohibited_actions": []}, "acceptance_criteria": ["ok"], "risk_level": "medium"}, "requested_focus": "requirements", "available_evidence": [], "approved_paths": []},
                },
                {"kind": "message", "text": final_record_json(required)},
            ],
            "lead",
        )
        context = self.make_context(lead, self.specialist_models())
        runtime = DepartmentRuntime(context=context, agents=build_department_agents(context))
        with NetworkBlocker():
            result = asyncio.run(runtime.run(context.active_task))
        self.assertEqual(result.final_state, FinalState.BLOCKED)
        self.assertEqual(context.specialist_completion_order, required)
        self.assertIsInstance(context.specialist_outputs[RoleSlug.REQUIREMENTS][0], RequirementsOutput)
        self.assertEqual(lead.calls, 2)

    def test_sensitive_specialist_pause_resume_and_independent_review(self) -> None:
        required = [RoleSlug.IMPLEMENTATION, RoleSlug.CODE_REVIEW]
        specialist_args = {
            "task": {
                "objective": "task",
                "scope": {"authorized_paths": ["src"], "exclusions": [], "prohibited_actions": []},
                "acceptance_criteria": ["ok"],
                "risk_level": "medium",
            },
            "available_evidence": [],
            "approved_paths": [],
        }
        lead = ScriptedModel(
            [
                {
                    "kind": "tool",
                    "name": RoleSlug.IMPLEMENTATION.value.replace("-", "_"),
                    "call_id": "impl1",
                    "arguments": {**specialist_args, "requested_focus": "implementation"},
                },
                {
                    "kind": "tool",
                    "name": RoleSlug.CODE_REVIEW.value.replace("-", "_"),
                    "call_id": "review1",
                    "arguments": {**specialist_args, "requested_focus": "independent code review"},
                },
                {"kind": "message", "text": final_record_json(required)},
            ],
            "lead-sensitive",
        )
        implementation_model = ScriptedModel([{"kind": "message", "text": specialist_json(RoleSlug.IMPLEMENTATION)}], "impl")
        review_model = ScriptedModel([{"kind": "message", "text": specialist_json(RoleSlug.CODE_REVIEW)}], "code-review")
        context = self.make_context(
            lead,
            {
                RoleSlug.IMPLEMENTATION: implementation_model,
                RoleSlug.CODE_REVIEW: review_model,
            },
        )
        runtime = DepartmentRuntime(context=context, agents=build_department_agents(context))
        with NetworkBlocker():
            paused = asyncio.run(runtime.run(context.active_task))
            self.assertEqual(paused.final_state, FinalState.PAUSED)
            self.assertEqual(paused.interruption_state.pending_count, 1)
            resumed = asyncio.run(runtime.apply_host_decisions_and_resume())
        self.assertEqual(resumed.final_state, FinalState.BLOCKED)
        self.assertEqual(context.specialist_completion_order, required)
        self.assertIsInstance(context.specialist_outputs[RoleSlug.IMPLEMENTATION][0], ImplementationEvidence)
        self.assertIsInstance(context.specialist_outputs[RoleSlug.CODE_REVIEW][0], CodeReviewOutput)
        self.assertEqual(implementation_model.calls, 1)
        self.assertEqual(review_model.calls, 1)
        self.assertEqual(context.approval_provider.requested, list(paused.sdk_result.interruptions))

    def test_in_scope_tools_use_injected_reader_writer_and_scope(self) -> None:
        context = self.make_context()
        self.assertEqual(asyncio.run(context.repository_reader.read_text(context.resolve_safe_path("src/nested/example.py"))), "nested")
        self.assertEqual(context.repository_reader.reads, ["src/nested/example.py"])
        self.assertEqual(context.resolve_safe_path("src/example.py"), "src/example.py")
        with self.assertRaises(ValueError):
            normalize_relative_path(Path("/workspace"), "/absolute")
        with self.assertRaises(ValueError):
            context.resolve_safe_path("../outside.py")
        with self.assertRaises(ValueError):
            context.resolve_safe_path("other/example.py")
        with self.assertRaises(ValueError):
            context.resolve_safe_path("")

    def test_hitl_approval_resume_and_rejection_for_write(self) -> None:
        read_tool, write_tool = build_repository_tools()
        model = ScriptedModel(
            [
                {"kind": "tool", "name": write_tool.name, "call_id": "write_1", "arguments": {"path": "src/example.py", "content": "value = 1\n", "reason": "deterministic test"}},
                {"kind": "message", "text": "done"},
            ],
            "writer",
        )
        agent = Agent(name="writer", tools=[write_tool], model=model)
        context = self.make_context()
        with NetworkBlocker():
            result = asyncio.run(Runner.run(agent, "write", context=context, max_turns=4, run_config=PRE_APPROVAL_CONFIG))
            self.assertEqual(len(result.interruptions), 1)
            state = result.to_state()
            state.approve(result.interruptions[0])
            asyncio.run(Runner.run(agent, state, run_config=PRE_APPROVAL_CONFIG))
        self.assertEqual(context.repository_writer.writes, [("src/example.py", "value = 1\n")])

        reject_model = ScriptedModel(
            [
                {"kind": "tool", "name": write_tool.name, "call_id": "write_2", "arguments": {"path": "src/example.py", "content": "value = 2\n", "reason": "deterministic test"}},
                {"kind": "message", "text": "done"},
            ],
            "reject-writer",
        )
        reject_context = self.make_context()
        reject_result = asyncio.run(Runner.run(Agent(name="writer", tools=[write_tool], model=reject_model), "write", context=reject_context, max_turns=4, run_config=PRE_APPROVAL_CONFIG))
        reject_state = reject_result.to_state()
        reject_state.reject(reject_result.interruptions[0])
        asyncio.run(Runner.run(Agent(name="writer", tools=[write_tool], model=reject_model), reject_state, run_config=PRE_APPROVAL_CONFIG))
        self.assertEqual(reject_context.repository_writer.writes, [])

    def test_invalid_write_rejected_before_approval_and_secret_rejected(self) -> None:
        read_tool, write_tool = build_repository_tools()
        for path, content in [("other/file.py", "ok"), ("src/secret.py", "OPENAI_API_KEY=abc123456789")]:
            model = ScriptedModel(
                [
                    {"kind": "tool", "name": write_tool.name, "arguments": {"path": path, "content": content, "reason": "deterministic test"}},
                    {"kind": "message", "text": "done"},
                ],
                f"invalid-{path}",
            )
            context = self.make_context()
            result = asyncio.run(Runner.run(Agent(name="writer", tools=[write_tool], model=model), "write", context=context, max_turns=4, run_config=PRE_APPROVAL_CONFIG))
            self.assertEqual(result.interruptions, [])
            self.assertEqual(context.repository_writer.writes, [])

    def test_specialist_call_limits_are_enforced_by_real_tool_invocation(self) -> None:
        lead = ScriptedModel(
            [
                {"kind": "tool", "name": RoleSlug.REQUIREMENTS.value.replace("-", "_"), "call_id": "req1", "arguments": {"task": {"objective": "task", "scope": {"authorized_paths": ["src"], "exclusions": [], "prohibited_actions": []}, "acceptance_criteria": ["ok"], "risk_level": "medium"}, "requested_focus": "one", "available_evidence": [], "approved_paths": []}},
                {"kind": "tool", "name": RoleSlug.REQUIREMENTS.value.replace("-", "_"), "call_id": "req2", "arguments": {"task": {"objective": "task", "scope": {"authorized_paths": ["src"], "exclusions": [], "prohibited_actions": []}, "acceptance_criteria": ["ok"], "risk_level": "medium"}, "requested_focus": "two", "available_evidence": [], "approved_paths": []}},
            ],
            "limit-lead",
        )
        context = self.make_context(lead, {RoleSlug.REQUIREMENTS: ScriptedModel([{"kind": "message", "text": specialist_json(RoleSlug.REQUIREMENTS)}], "req")})
        runtime = DepartmentRuntime(context=context, agents=build_department_agents(context))
        result = asyncio.run(runtime.run(context.active_task))
        self.assertIn("max_calls_per_specialist", result.stopped_reason or "")

    def test_approval_edge_cases_return_safe_results(self) -> None:
        context = self.make_context()
        runtime = DepartmentRuntime(context=context, agents=build_department_agents(context))
        self.assertEqual(asyncio.run(runtime.apply_host_decisions_and_resume()).final_state, FinalState.BLOCKED)
        context.approval_resume_cycles = context.limits.max_approval_resume_cycles
        runtime.last_result = type("R", (), {"interruptions": (object(),), "to_state": lambda self: object()})()
        runtime.state = type("S", (), {})()
        self.assertEqual(asyncio.run(runtime.apply_host_decisions_and_resume()).final_state, FinalState.STOPPED)

    def test_evidence_backed_completion(self) -> None:
        context = self.make_context()
        req = RequirementsOutput(RoleSlug.REQUIREMENTS, "req", (EvidenceItem("req", "context", True),), requirements_result=RequirementsAcceptanceCriteria(("req",), ("ok",)), plan=ImplementationPlan(("impl",), ("test",), tuple(RoleSlug)))
        impl = ImplementationEvidence(RoleSlug.IMPLEMENTATION, "impl", (EvidenceItem("impl", "context", True),), proposal=ImplementationChangeProposal(("src/example.py",), "change", "task"))
        validation = ValidationEvidence(RoleSlug.TESTING, "test", (EvidenceItem("test", "context", True),), passed_checks=("unit",))
        code = CodeReviewOutput(RoleSlug.CODE_REVIEW, "code", (EvidenceItem("code", "context", True),), review=CodeQualityReview(True))
        risk = RiskReviewOutput(RoleSlug.RISK_REVIEW, "risk", (EvidenceItem("risk", "context", True),), review=EngineeringRiskReview(True))
        docs = DocumentationReadinessOutput(RoleSlug.DOCUMENTATION, "docs", (EvidenceItem("docs", "context", True),), readiness=DocumentationReleaseReadinessResult((), "ready", True))
        for output in [req, impl, validation, code, risk, docs]:
            context.record_specialist_output(output.role.value, output, type(output))
        context.write_events.append(("src/example.py", "value = 1\n"))
        record = LeadFinalRecord("task", req, req.plan, None, (RoleSlug.REQUIREMENTS, RoleSlug.IMPLEMENTATION, RoleSlug.TESTING, RoleSlug.CODE_REVIEW, RoleSlug.RISK_REVIEW, RoleSlug.DOCUMENTATION), tuple(context.specialist_completion_order), ("req",), (), impl, validation, code, risk, docs, (), (), (), (), FinalState.COMPLETED)
        self.assertEqual(derive_final_state(record), FinalState.COMPLETED)
        self.assertTrue(final_record_is_supported(record, context))
        invented = LeadFinalRecord("task", req, req.plan, None, (RoleSlug.REQUIREMENTS,), (RoleSlug.REQUIREMENTS,), ("req",), (), impl, validation, code, risk, docs, (), (), (), (), FinalState.COMPLETED)
        self.assertFalse(final_record_is_supported(invented, self.make_context()))

    def test_no_credentials_or_external_operations_are_required(self) -> None:
        for name in ("OPENAI_API_KEY", "OPENAI_BASE_URL", "OPENAI_ORG_ID", "OPENAI_PROJECT_ID", "AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT"):
            self.assertIsNone(os.environ.get(name))


if __name__ == "__main__":
    unittest.main()
