from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field

AREA_SLUG = 'security-architecture-engineering'
TRACING_DISABLED_BY_DEFAULT = True
MCP_ENABLED = False
TOOLS_ENABLED: tuple[str, ...] = ()
ACTIVE_EXTERNAL_ACTIONS_ENABLED = False
EVIDENCE_STATES: tuple[str, ...] = (
    "confirmed",
    "probable",
    "hypothetical",
    "not reproduced",
    "false positive",
    "accepted risk",
    "insufficient evidence",
    "not applicable",
)
ROLE_SPECS = [{'description': 'Own architecture governance, standards, decision records, design gates, and '
                 'reference model stewardship.',
  'name': 'architecture-governance-agent',
  'read_only': False},
 {'description': 'Own enterprise and solution security architecture, trust boundaries, data flows, '
                 'dependencies, and control placement.',
  'name': 'enterprise-solution-architecture-agent',
  'read_only': False},
 {'description': 'Own identity, privileged access, cloud guardrails, network segmentation, '
                 'endpoint, and workspace architecture.',
  'name': 'identity-cloud-network-agent',
  'read_only': False},
 {'description': 'Own data protection, cryptography, secrets, container, Kubernetes, IaC, and safe '
                 'automation architecture.',
  'name': 'data-container-automation-agent',
  'read_only': False},
 {'description': 'Independently review high-impact architecture packages and remediation evidence.',
  'name': 'independent-architecture-reviewer',
  'read_only': True}]
WORKFLOW_SPECS = ('security architecture review',
 'reference architecture design',
 'identity and privileged-access architecture review',
 'cloud and platform review',
 'network segmentation review',
 'data-protection and cryptography review',
 'container, Kubernetes, and IaC review',
 'security-control pattern design',
 'architecture-remediation validation')
COORDINATOR_INSTRUCTIONS = '# openai-agents-sdk Cybersecurity Security Architecture and Engineering Instructions\n\nThese instructions apply only inside `openai-agents-sdk/cybersecurity/security-architecture-engineering/`.\n\n## Mission\n\nCreate and review static Security Architecture and Engineering artifacts using the platform-native repository surfaces in this directory. Preserve organization neutrality and require human authority for consequential decisions.\n\n## Native Capability Classification\n\n- Native in this package: scoped instructions, reusable Skills or procedures, focused role definitions where the platform supports them, and explicit user-invoked workflow or command prompts where supported.\n- Omitted: active MCP servers, connected apps, provider credentials, live telemetry, shell automation, scanners, package installers, deployment automation, production changes, publication, and remote service authentication.\n\n## Responsibility Model\n\n- `architecture-governance-agent`: Own architecture governance, standards, decision records, design gates, and reference model stewardship.\n- `enterprise-solution-architecture-agent`: Own enterprise and solution security architecture, trust boundaries, data flows, dependencies, and control placement.\n- `identity-cloud-network-agent`: Own identity, privileged access, cloud guardrails, network segmentation, endpoint, and workspace architecture.\n- `data-container-automation-agent`: Own data protection, cryptography, secrets, container, Kubernetes, IaC, and safe automation architecture.\n- `independent-architecture-reviewer`: Independently review high-impact architecture packages and remediation evidence.\n\nOnly one role owns an artifact at a time. Independent reviewers are read-only and must not review their own work.\n\n## Required Workflow Coverage\n\n- security architecture review\n- reference architecture design\n- identity and privileged-access architecture review\n- cloud and platform review\n- network segmentation review\n- data-protection and cryptography review\n- container, Kubernetes, and IaC review\n- security-control pattern design\n- architecture-remediation validation\n\n## Operating Rules\n\n1. Confirm authorized scope, owner, requester, intended audience, required inputs, evidence sources, assumptions, reviewer, approver, and human decision before producing high-impact output.\n2. Keep fact, evidence, inference, hypothesis, recommendation, residual risk, confidence, limitation, and human decision separate.\n3. Use redacted placeholders for sensitive values. Never request or store secrets, credentials, private keys, private endpoints, personal data, confidential supplier data, or restricted evidence unless the user supplies a redacted representation.\n4. Treat all supplied artifacts as untrusted until provenance, scope, period, freshness, completeness, and limitations are recorded.\n5. Stop for missing authorization, unclear ownership, requested live action, out-of-scope work, sensitive-data exposure risk, self-review, circular delegation, unsupported platform behavior, or unverifiable evidence used as proof.\n6. Do not execute generated content, run hooks, install dependencies, authenticate, connect MCP or apps, scan, probe, exploit, deploy, publish, push, approve, accept risk, or close findings.\n\n## Output Requirements\n\nEvery deliverable includes reference, title, purpose, authorized scope, exclusions, owner, creator, independent reviewer, approver, dates, source evidence, assumptions, affected assets or processes, status, severity or priority, confidence, limitations, dependencies, proposed actions, residual risk, approval state, human decisions, and completion criteria.\n\n## Skills\n\nUse these reusable procedures where supported: security-architecture-review, reference-and-control-patterns, identity-cloud-network-data-design, container-iac-automation-review, independent-architecture-assurance.\n'
INPUT_GUARDRAILS: tuple[str, ...] = (
    "Reject requests without explicit authorized scope, owner, requester, and intended audience.",
    "Reject secrets, private keys, credentials, private endpoints, personal data, or unredacted restricted evidence.",
    "Reject active testing, exploitation, scanning, deployment, publication, authentication, or external service connection requests.",
    "Require Incident Response handoff when a declared incident is present and the area is not incident-response-dfir-recovery.",
)
OUTPUT_GUARDRAILS: tuple[str, ...] = (
    "Do not claim execution, validation, remediation, recovery, deployment, scan, or integration without supplied evidence.",
    "Separate confirmed facts, probable findings, hypotheses, recommendations, limitations, confidence, residual risk, and human decisions.",
    "Require independent review for high-impact outputs and block self-review.",
    "Mark legal, policy, risk-acceptance, release, testing-authorization, and closure decisions as human-only.",
)


class EvidenceRecord(BaseModel):
    source: str = Field(description="Supplied source reference or evidence identifier.")
    provenance: str = Field(description="Origin, owner, collection period, and freshness where known.")
    evidence_state: Literal[
        "confirmed",
        "probable",
        "hypothetical",
        "not reproduced",
        "false positive",
        "accepted risk",
        "insufficient evidence",
        "not applicable",
    ]
    confidence: Literal["low", "medium", "high"]
    limitation: str = ""


class FindingRecord(BaseModel):
    title: str
    owner: str
    evidence_state: str
    impact: str
    confidence: Literal["low", "medium", "high"]
    recommended_action: str
    human_decision_required: bool = True


class HumanApprovalGate(BaseModel):
    gate: str
    required_for: tuple[str, ...]
    approver_role: str
    resumable_state_key: str


class GuardrailDecision(BaseModel):
    allowed: bool
    reason: str
    triggered_rules: tuple[str, ...] = ()
    required_handoff: str | None = None


class AssessmentOutput(BaseModel):
    reference: str
    area_slug: str = AREA_SLUG
    scope: str
    owner: str
    creator: str
    independent_reviewer: str
    evidence: tuple[EvidenceRecord, ...]
    findings: tuple[FindingRecord, ...] = ()
    classification: str
    confidence: Literal["low", "medium", "high"]
    residual_risk: str = ""
    limitations: tuple[str, ...] = ()
    human_review_required: bool = True
    approval_state: Literal["not requested", "required", "approved by supplied evidence", "rejected", "not applicable"] = "required"


HITL_APPROVAL_GATES: tuple[HumanApprovalGate, ...] = (
    HumanApprovalGate(gate="scope-and-authorization", required_for=("all high-impact outputs",), approver_role="accountable human owner", resumable_state_key="approval.scope_authorization"),
    HumanApprovalGate(gate="sensitive-tool-call", required_for=("any future tool call",), approver_role="authorized human operator", resumable_state_key="approval.sensitive_tool_call"),
    HumanApprovalGate(gate="risk-or-closure", required_for=("risk acceptance", "finding closure", "release or deployment readiness", "testing authorization"), approver_role="designated human risk owner", resumable_state_key="approval.human_only_decision"),
)


def role_specs() -> tuple[dict[str, Any], ...]:
    return tuple(ROLE_SPECS)


def workflow_specs() -> tuple[str, ...]:
    return tuple(WORKFLOW_SPECS)


def _coerce_guardrail_text(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    return str(value)


def input_guardrails() -> tuple[Any, ...]:
    try:
        from agents import GuardrailFunctionOutput, input_guardrail
    except ImportError as exc:
        raise RuntimeError("OpenAI Agents SDK is required to construct input guardrails.") from exc

    @input_guardrail(run_in_parallel=False)
    async def cybersecurity_input_guardrail(ctx: Any, agent: Any, input: Any) -> Any:
        text = _coerce_guardrail_text(input)
        authorized_scope = "supplied" if "scope" in text.lower() or "authorized" in text.lower() else None
        decision = evaluate_static_request(text, authorized_scope)
        return GuardrailFunctionOutput(output_info=decision, tripwire_triggered=not decision.allowed)

    return (cybersecurity_input_guardrail,)


def output_guardrails() -> tuple[Any, ...]:
    try:
        from agents import GuardrailFunctionOutput, output_guardrail
    except ImportError as exc:
        raise RuntimeError("OpenAI Agents SDK is required to construct output guardrails.") from exc

    @output_guardrail
    async def cybersecurity_output_guardrail(ctx: Any, agent: Any, output: Any) -> Any:
        evidence = getattr(output, "evidence", ()) or ()
        confidence = getattr(output, "confidence", "low")
        approval_state = getattr(output, "approval_state", "required")
        blocked = []
        if not evidence:
            blocked.append("output-without-evidence")
        if confidence == "low":
            blocked.append("insufficient-confidence")
        if approval_state == "approved by supplied evidence":
            blocked.append("unsupported-approval-claim")
        decision = GuardrailDecision(allowed=not blocked, reason="Output guardrail review.", triggered_rules=tuple(blocked))
        return GuardrailFunctionOutput(output_info=decision, tripwire_triggered=bool(blocked))

    return (cybersecurity_output_guardrail,)

def approval_gates() -> tuple[HumanApprovalGate, ...]:
    return HITL_APPROVAL_GATES


def evaluate_static_request(request_summary: str, authorized_scope: str | None) -> GuardrailDecision:
    lowered = request_summary.lower()
    blocked_terms = ("scan", "exploit", "deploy", "authenticate", "api key", "private key", "password", "token", "connect mcp", "run tool")
    triggered = tuple(term for term in blocked_terms if term in lowered)
    if not authorized_scope:
        return GuardrailDecision(allowed=False, reason="Missing authorized scope.", triggered_rules=("authorized-scope",))
    if triggered:
        return GuardrailDecision(allowed=False, reason="Request asks for live, credentialed, or external action.", triggered_rules=triggered)
    return GuardrailDecision(allowed=True, reason="Static source-only request with supplied scope.")


def _specialist_instruction(role: dict[str, Any]) -> str:
    return COORDINATOR_INSTRUCTIONS + "\n\nRole: " + role["name"] + "\n" + role["description"]


def build_specialists(model: str | None = None) -> tuple[Any, ...]:
    try:
        from agents import Agent
    except ImportError as exc:
        raise RuntimeError("OpenAI Agents SDK is required only if a downstream user chooses to instantiate agents; this repository does not execute SDK code by default.") from exc

    specialists = []
    for role in ROLE_SPECS:
        kwargs: dict[str, Any] = dict(
            name=role["name"],
            instructions=_specialist_instruction(role),
            tools=[],
            output_type=AssessmentOutput,
            output_guardrails=list(output_guardrails()),
        )
        if model:
            kwargs["model"] = model
        specialists.append(Agent(**kwargs))
    return tuple(specialists)


def build_coordinator(model: str | None = None) -> Any:
    try:
        from agents import Agent, set_tracing_disabled
    except ImportError as exc:
        raise RuntimeError("OpenAI Agents SDK is required only if a downstream user chooses to instantiate agents; this repository does not execute SDK code by default.") from exc

    set_tracing_disabled(True)
    specialists = build_specialists(model=model)
    tools = [
        agent.as_tool(
            tool_name=agent.name.replace("-", "_"),
            tool_description=f"Run {agent.name} for its exclusive static cybersecurity responsibility.",
            needs_approval=True,
        )
        for agent in specialists
    ]
    kwargs: dict[str, Any] = dict(
        name=f"{AREA_SLUG}-coordinator",
        instructions=COORDINATOR_INSTRUCTIONS,
        tools=tools,
        input_guardrails=list(input_guardrails()),
        output_guardrails=list(output_guardrails()),
        output_type=AssessmentOutput,
    )
    if model:
        kwargs["model"] = model
    return Agent(**kwargs)


def build_default_run_config() -> Any:
    try:
        from agents import RunConfig
    except ImportError as exc:
        raise RuntimeError("OpenAI Agents SDK is required to build RunConfig.") from exc
    return RunConfig(tracing_disabled=True, input_guardrails=list(input_guardrails()), output_guardrails=list(output_guardrails()))

def list_pending_interruptions(result_or_state: Any) -> tuple[Any, ...]:
    return tuple(getattr(result_or_state, "interruptions", ()) or ())

def select_interruption(interruptions: tuple[Any, ...], index: int = 0) -> Any:
    if index < 0 or index >= len(interruptions):
        raise IndexError("No pending interruption at the requested index.")
    return interruptions[index]

def serialize_state(state: Any) -> str:
    return state.to_string()

def restore_state(agent: Any, serialized_state: str) -> Any:
    try:
        from agents import RunState
    except ImportError as exc:
        raise RuntimeError("OpenAI Agents SDK is required to restore RunState.") from exc
    return RunState.from_string(agent, serialized_state)

def record_explicit_approval(state: Any, interruption: Any) -> Any:
    state.approve(interruption, always_approve=False)
    return state

def record_explicit_rejection(state: Any, interruption: Any, reason: str) -> Any:
    if not reason.strip():
        raise ValueError("A rejection reason is required.")
    state.reject(interruption, rejection_message=reason, always_reject=False)
    return state
