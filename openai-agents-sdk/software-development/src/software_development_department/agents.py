from __future__ import annotations

import json
from dataclasses import asdict, dataclass, is_dataclass
from typing import Any

from agents import Agent, RunContextWrapper
from pydantic import TypeAdapter

from .guardrails import evidence_and_self_review_guardrail, legitimate_task_guardrail
from .models import (
    ArchitectureOutput,
    CodeReviewOutput,
    DocumentationReadinessOutput,
    ImplementationEvidence,
    LeadFinalRecord,
    RequirementsOutput,
    RoleSlug,
    SpecialistInput,
    ValidationEvidence,
    RiskReviewOutput,
)
from .tools import DepartmentContext, build_repository_tools

COMMON_SPECIALIST_RULES = (
    "Stop when your exclusive output is complete, when required evidence is unavailable, "
    "or when the requested work exceeds the approved scope. Return typed evidence to the "
    "Software Development Lead. Do not call other specialists, recursively delegate, claim final "
    "department completion authority, mutate Git, deploy, publish, release, sign, retrieve "
    "credentials, call MCP, call external services, or use unsupported tools."
)

ROLE_INSTRUCTIONS = {
    "software-development-lead": (
        "# Software Development Lead\n\n"
        "Remain the active top-level manager for the complete run. Call specialist tools when their "
        "responsibility is required, retain scope control, and aggregate typed evidence. Do not "
        "transfer permanent control, recursively delegate through specialists, or perform a "
        "specialist's substantive work merely to avoid delegation. Implementation evidence must be "
        "followed by independent code-quality and engineering-risk review before completion."
    ),
    RoleSlug.REQUIREMENTS.value: (
        "# Requirements and Planning Specialist\n\n"
        "Mission: convert the task into requirements, acceptance criteria, constraints, assumptions, "
        "exclusions, risks, and an ordered plan. Exclusive scope: requirements and planning only. "
        "Inputs: task request, authorized scope, acceptance criteria, known evidence. Outputs: "
        "RequirementsOutput with RequirementsAcceptanceCriteria and ImplementationPlan. "
        f"{COMMON_SPECIALIST_RULES}"
    ),
    RoleSlug.ARCHITECTURE.value: (
        "# Software Architect\n\n"
        "Mission: define architecture boundaries, contracts, decisions, compatibility impact, and "
        "migration implications. Exclusive scope: architecture and design decisions only. Inputs: "
        "approved requirements, constraints, affected boundaries, alternatives. Outputs: "
        "ArchitectureOutput with ArchitectureDecision. "
        f"{COMMON_SPECIALIST_RULES}"
    ),
    RoleSlug.IMPLEMENTATION.value: (
        "# Implementation and Maintenance Engineer\n\n"
        "Mission: propose and apply approved in-scope code changes through host-injected tools only. "
        "Exclusive scope: implementation and maintenance edits approved by the Lead and host. Inputs: "
        "approved plan, acceptance criteria, authorized paths, prior evidence. Outputs: "
        "ImplementationEvidence with ImplementationChangeProposal. Stop before any unapproved, "
        "destructive, credential, Git, deployment, publication, release, signing, MCP, or external "
        "action. "
        f"{COMMON_SPECIALIST_RULES}"
    ),
    RoleSlug.TESTING.value: (
        "# Test and Quality Engineer\n\n"
        "Mission: define and report deterministic validation, regression, edge-case, and checks-not-run "
        "evidence. Exclusive scope: testing and validation only. Inputs: requirements, implementation "
        "evidence, risk level, supported commands from the host. Outputs: ValidationEvidence. "
        f"{COMMON_SPECIALIST_RULES}"
    ),
    RoleSlug.CODE_REVIEW.value: (
        "# Code Quality Reviewer\n\n"
        "Mission: independently review correctness, maintainability, architecture fit, complexity, "
        "compatibility, and unintended behavior changes. Exclusive scope: review only; do not edit "
        "files. Inputs: implementation evidence, requirements, validation notes, relevant code. "
        "Outputs: CodeReviewOutput with CodeQualityReview. "
        f"{COMMON_SPECIALIST_RULES}"
    ),
    RoleSlug.RISK_REVIEW.value: (
        "# Engineering Risk Reviewer\n\n"
        "Mission: independently review security, dependency, supply-chain, reliability, performance, "
        "data integrity, and operational risks. Exclusive scope: risk review only; do not edit files. "
        "Inputs: task, implementation evidence, validation evidence, architecture evidence. Outputs: "
        "RiskReviewOutput with EngineeringRiskReview. "
        f"{COMMON_SPECIALIST_RULES}"
    ),
    RoleSlug.DOCUMENTATION.value: (
        "# Documentation and Release Readiness Specialist\n\n"
        "Mission: assess documentation, compatibility notes, migration notes, versioning implications, "
        "release readiness, limitations, and stop-before-release evidence without releasing anything. "
        "Exclusive scope: documentation and readiness only. Inputs: verified evidence and reviews. "
        "Outputs: DocumentationReadinessOutput with DocumentationReleaseReadinessResult. "
        f"{COMMON_SPECIALIST_RULES}"
    ),
}

SPECIALIST_OUTPUTS = {
    RoleSlug.REQUIREMENTS.value: RequirementsOutput,
    RoleSlug.ARCHITECTURE.value: ArchitectureOutput,
    RoleSlug.IMPLEMENTATION.value: ImplementationEvidence,
    RoleSlug.TESTING.value: ValidationEvidence,
    RoleSlug.CODE_REVIEW.value: CodeReviewOutput,
    RoleSlug.RISK_REVIEW.value: RiskReviewOutput,
    RoleSlug.DOCUMENTATION.value: DocumentationReadinessOutput,
}

SPECIALIST_TOOL_DESCRIPTIONS = {
    RoleSlug.REQUIREMENTS.value: "Use for requirements, acceptance criteria, assumptions, exclusions, risks, and planning.",
    RoleSlug.ARCHITECTURE.value: "Use for architecture boundaries, contracts, decisions, compatibility, and migrations.",
    RoleSlug.IMPLEMENTATION.value: "Use for approved implementation and maintenance evidence through injected tools.",
    RoleSlug.TESTING.value: "Use for validation strategy, regression evidence, edge cases, and checks not run.",
    RoleSlug.CODE_REVIEW.value: "Use for independent code-quality review after implementation.",
    RoleSlug.RISK_REVIEW.value: "Use for independent engineering-risk review after implementation or sensitive proposals.",
    RoleSlug.DOCUMENTATION.value: "Use for documentation, migration, versioning, and release-readiness evidence.",
}

SENSITIVE_SPECIALIST_TOOLS = frozenset({RoleSlug.ARCHITECTURE.value, RoleSlug.IMPLEMENTATION.value})


@dataclass(frozen=True)
class DepartmentAgents:
    lead: Agent[DepartmentContext]
    specialists: dict[str, Agent[DepartmentContext]]
    read_tool: object
    write_tool: object


def _specialist(
    slug: str,
    output_type: type[object],
    tools: list[object],
    context: DepartmentContext,
) -> Agent[DepartmentContext]:
    return Agent(
        name=slug,
        instructions=ROLE_INSTRUCTIONS[slug],
        tools=tools,
        model=context.model_for(slug),
        output_type=output_type,
        input_guardrails=[legitimate_task_guardrail],
        output_guardrails=[],
    )


def _specialist_input_builder(input_data: SpecialistInput | dict[str, object]) -> str:
    if not isinstance(input_data, SpecialistInput):
        if isinstance(input_data.get("params"), dict):
            input_data = input_data["params"]
        input_data = TypeAdapter(SpecialistInput).validate_python(input_data)
    return (
        f"Task objective: {input_data.task.objective}\n"
        f"Authorized paths: {input_data.task.scope.authorized_paths}\n"
        f"Acceptance criteria: {input_data.task.acceptance_criteria}\n"
        f"Requested focus: {input_data.requested_focus}\n"
        f"Available evidence: {input_data.available_evidence}\n"
        f"Approved paths: {input_data.approved_paths}\n"
        "Return only your typed specialist output."
    )


def _specialist_approval(slug: str):
    async def needs_approval(
        context: RunContextWrapper[DepartmentContext], tool_parameters: dict[str, object], call_id: str
    ) -> bool:
        context.context.record_specialist_call(slug, call_id)
        return slug in SENSITIVE_SPECIALIST_TOOLS

    return needs_approval


def _json_default(value: object) -> str:
    if hasattr(value, "value"):
        return str(value.value)
    return str(value)


def _specialist_output_extractor(context: DepartmentContext, slug: str, output_type: type[object]):
    async def extract(run_result: Any) -> str:
        output = getattr(run_result, "final_output", None)
        context.record_specialist_output(slug, output, output_type)
        if is_dataclass(output):
            return json.dumps(asdict(output), default=_json_default)
        return str(output)

    return extract


def build_department_agents(context: DepartmentContext) -> DepartmentAgents:
    read_tool, write_tool = build_repository_tools()
    specialists = {
        slug: _specialist(
            slug,
            output_type,
            [read_tool, write_tool] if slug == RoleSlug.IMPLEMENTATION.value else [read_tool],
            context,
        )
        for slug, output_type in SPECIALIST_OUTPUTS.items()
    }
    specialist_tools = [
        agent.as_tool(
            tool_name=slug.replace("-", "_"),
            tool_description=SPECIALIST_TOOL_DESCRIPTIONS[slug],
            needs_approval=_specialist_approval(slug),
            parameters=SpecialistInput,
            input_builder=_specialist_input_builder,
            max_turns=context.limits.max_turns_per_specialist,
            custom_output_extractor=_specialist_output_extractor(context, slug, SPECIALIST_OUTPUTS[slug]),
        )
        for slug, agent in specialists.items()
    ]
    lead = Agent(
        name="software-development-lead",
        instructions=ROLE_INSTRUCTIONS["software-development-lead"],
        tools=[*specialist_tools, read_tool],
        output_type=LeadFinalRecord,
        input_guardrails=[legitimate_task_guardrail],
        output_guardrails=[evidence_and_self_review_guardrail],
        model=context.model_for(None),
    )
    return DepartmentAgents(lead=lead, specialists=specialists, read_tool=read_tool, write_tool=write_tool)
