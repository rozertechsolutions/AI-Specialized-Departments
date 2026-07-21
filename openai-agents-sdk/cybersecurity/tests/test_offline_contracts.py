from __future__ import annotations

import asyncio
import importlib
import inspect
from dataclasses import dataclass, field
from typing import Any

import pytest
from agents import Agent, RunContextWrapper, Runner, RunState


AREA_PACKAGES = (
    "cybersecurity_governance_risk_compliance_assurance_agents",
    "cybersecurity_security_architecture_engineering_agents",
    "cybersecurity_application_product_devsecops_security_agents",
    "cybersecurity_exposure_vulnerability_hardening_agents",
    "cybersecurity_defensive_security_operations_detection_intelligence_agents",
    "cybersecurity_incident_response_dfir_recovery_agents",
    "cybersecurity_offensive_security_authorized_validation_agents",
    "cybersecurity_cyber_resilience_specialized_technologies_agents",
)


FORBIDDEN_TOOL_CLASS_NAMES = {
    "WebSearchTool",
    "FileSearchTool",
    "ComputerTool",
    "ShellTool",
    "LocalShellTool",
    "HostedMCPTool",
    "CodeInterpreterTool",
}


def _registry(package_name: str) -> Any:
    return importlib.import_module(f"{package_name}.registry")


def _block_runner(monkeypatch: pytest.MonkeyPatch) -> None:
    def fail(*_args: Any, **_kwargs: Any) -> None:
        raise AssertionError("Runner execution is forbidden in offline validation.")

    monkeypatch.setattr(Runner, "run", fail)
    monkeypatch.setattr(Runner, "run_sync", fail)
    monkeypatch.setattr(Runner, "run_streamed", fail)


def _assert_no_forbidden_tools(agent: Agent[Any]) -> None:
    assert agent.mcp_servers == []
    for tool in agent.tools:
        assert type(tool).__name__ not in FORBIDDEN_TOOL_CLASS_NAMES
        wrapped_agent = getattr(tool, "agent", None)
        if wrapped_agent is not None:
            _assert_no_forbidden_tools(wrapped_agent)


@pytest.mark.parametrize("package_name", AREA_PACKAGES)
def test_import_public_package_registry_and_models(package_name: str) -> None:
    package = importlib.import_module(package_name)
    registry = _registry(package_name)
    for public_name in (
        "AssessmentOutput",
        "EvidenceRecord",
        "FindingRecord",
        "GuardrailDecision",
        "HumanApprovalGate",
        "build_coordinator",
        "build_default_run_config",
        "restore_state",
        "serialize_state",
    ):
        assert hasattr(package, public_name)
        assert hasattr(registry, public_name)


@pytest.mark.parametrize("package_name", AREA_PACKAGES)
def test_constructs_agents_and_run_config_without_runtime_tools(
    package_name: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    _block_runner(monkeypatch)
    registry = _registry(package_name)

    specialists = registry.build_specialists(model="offline-static-model")
    assert specialists
    assert {agent.name for agent in specialists} == {role["name"] for role in registry.role_specs()}
    for agent in specialists:
        assert agent.output_type is registry.AssessmentOutput
        assert agent.input_guardrails == []
        assert agent.output_guardrails
        _assert_no_forbidden_tools(agent)

    coordinator = registry.build_coordinator(model="offline-static-model")
    assert coordinator.name == f"{registry.AREA_SLUG}-coordinator"
    assert coordinator.output_type is registry.AssessmentOutput
    assert coordinator.input_guardrails
    assert coordinator.output_guardrails
    assert len(coordinator.tools) == len(specialists)
    _assert_no_forbidden_tools(coordinator)

    run_config = registry.build_default_run_config()
    assert run_config.tracing_disabled is True
    assert run_config.input_guardrails
    assert run_config.output_guardrails
    assert getattr(run_config, "sandbox", None) is None
    assert registry.TRACING_DISABLED_BY_DEFAULT is True
    assert registry.MCP_ENABLED is False
    assert registry.TOOLS_ENABLED == ()
    assert registry.ACTIVE_EXTERNAL_ACTIONS_ENABLED is False


@pytest.mark.parametrize("package_name", AREA_PACKAGES)
def test_guardrail_policy_helpers_cover_required_blockers(package_name: str) -> None:
    registry = _registry(package_name)

    allowed = registry.evaluate_static_request(
        "Authorized scope: review repository architecture evidence for static control gaps.",
        authorized_scope="repository architecture review",
    )
    assert allowed.allowed is True

    cases = (
        ("review this without an authorization record", None, "authorized-scope"),
        ("authorized scope: scan this live host", "approved static scope", "scan"),
        ("authorized scope: exploit the target", "approved static scope", "exploit"),
        ("authorized scope: here is an api key", "approved static scope", "api key"),
        ("authorized scope: private key exposure", "approved static scope", "private key"),
        ("authorized scope: deploy the fix", "approved static scope", "deploy"),
        ("authorized scope: connect mcp to the SIEM", "approved static scope", "connect mcp"),
    )
    for summary, authorized_scope, expected_rule in cases:
        decision = registry.evaluate_static_request(summary, authorized_scope)
        assert decision.allowed is False
        assert expected_rule in decision.triggered_rules

    output = registry.AssessmentOutput(
        reference="OUT-1",
        scope="authorized static repository review",
        owner="product security owner",
        creator="area specialist",
        independent_reviewer="independent reviewer",
        evidence=(),
        classification="internal",
        confidence="low",
        approval_state="approved by supplied evidence",
    )
    blocked_terms = {"output-without-evidence", "insufficient-confidence", "unsupported-approval-claim"}

    async def evaluate_output_guardrail() -> Any:
        guardrail = registry.output_guardrails()[0]
        return await guardrail.run(None, None, output)

    result = asyncio.run(evaluate_output_guardrail())
    guardrail_output = result.output
    assert guardrail_output.tripwire_triggered is True
    assert blocked_terms.issubset(set(guardrail_output.output_info.triggered_rules))


@dataclass
class FakeState:
    approved: list[Any] = field(default_factory=list)
    rejected: list[tuple[Any, str]] = field(default_factory=list)

    def approve(self, interruption: Any, *, always_approve: bool) -> None:
        assert always_approve is False
        self.approved.append(interruption)

    def reject(self, interruption: Any, *, rejection_message: str, always_reject: bool) -> None:
        assert always_reject is False
        self.rejected.append((interruption, rejection_message))


@pytest.mark.parametrize("package_name", AREA_PACKAGES)
def test_hitl_helpers_require_explicit_interruptions(package_name: str) -> None:
    registry = _registry(package_name)
    interruptions = ("approval-1", "approval-2")
    assert registry.list_pending_interruptions(type("Result", (), {"interruptions": interruptions})()) == interruptions
    assert registry.select_interruption(interruptions, 1) == "approval-2"
    with pytest.raises(IndexError):
        registry.select_interruption(interruptions, 2)

    state = FakeState()
    assert registry.record_explicit_approval(state, "approval-1") is state
    assert state.approved == ["approval-1"]
    assert registry.record_explicit_rejection(state, "approval-2", "scope is not authorized") is state
    assert state.rejected == [("approval-2", "scope is not authorized")]
    with pytest.raises(ValueError):
        registry.record_explicit_rejection(state, "approval-3", " ")


@pytest.mark.parametrize("package_name", AREA_PACKAGES)
def test_state_string_persistence_restores_runstate(package_name: str) -> None:
    registry = _registry(package_name)
    agent = Agent(name=f"{registry.AREA_SLUG}-offline-state", instructions="No model call.", tools=[])
    state = RunState(RunContextWrapper(context=None), "static input", agent, max_turns=1)
    serialized = registry.serialize_state(state)

    assert isinstance(serialized, str)
    assert not isinstance(serialized, dict)
    assert inspect.iscoroutinefunction(registry.restore_state)

    restored = asyncio.run(registry.restore_state(agent, serialized))
    assert isinstance(restored, RunState)
    assert not inspect.iscoroutine(restored)


def test_sdk_api_contract_protects_async_restore_signature() -> None:
    signature = inspect.signature(RunState.from_string)
    assert inspect.iscoroutinefunction(RunState.from_string)
    assert "initial_agent" in signature.parameters
    assert "state_string" in signature.parameters


def test_forbidden_runtime_and_hosted_tool_classes_are_not_used() -> None:
    for package_name in AREA_PACKAGES:
        registry = _registry(package_name)
        source = inspect.getsource(registry)
        forbidden_runtime_calls = ("Runner.run(", "Runner.run_sync(", "Runner.run_streamed(")
        assert not any(call in source for call in forbidden_runtime_calls)
        assert not any(tool_class in source for tool_class in FORBIDDEN_TOOL_CLASS_NAMES)
