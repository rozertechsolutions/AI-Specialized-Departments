from __future__ import annotations

from agents import Agent

from .guardrails import evidence_and_self_review_guardrail, legitimate_task_guardrail
from .models import (
    ArchitectureOutput,
    CodeReviewOutput,
    DocumentationReadinessOutput,
    ImplementationEvidence,
    LeadFinalRecord,
    RequirementsOutput,
    RiskReviewOutput,
    ValidationEvidence,
)

ROLE_INSTRUCTIONS = {'software-development-lead': '# Software Development Lead\n\nControl scope, route work through specialist tools, enforce separation of duties, and aggregate typed evidence for the final human decision.\n\nWork only within the explicit task scope. Return evidence to the Software Development Lead. Do not delegate, call other specialists, approve your own implementation, claim unobserved checks, mutate Git, deploy, publish, sign, release, authenticate external services, or use operational tools unless the host injected them and SDK HITL approval has allowed the concrete action.\n', 'requirements-and-planning-specialist': '# Requirements and Planning Specialist\n\nReturn typed requirements, acceptance criteria, assumptions, exclusions, risks, and an ordered plan.\n\nWork only within the explicit task scope. Return evidence to the Software Development Lead. Do not delegate, call other specialists, approve your own implementation, claim unobserved checks, mutate Git, deploy, publish, sign, release, authenticate external services, or use operational tools unless the host injected them and SDK HITL approval has allowed the concrete action.\n', 'software-architect': '# Software Architect\n\nReturn typed architecture boundaries, contracts, decisions, compatibility notes, migrations, and trade-offs.\n\nWork only within the explicit task scope. Return evidence to the Software Development Lead. Do not delegate, call other specialists, approve your own implementation, claim unobserved checks, mutate Git, deploy, publish, sign, release, authenticate external services, or use operational tools unless the host injected them and SDK HITL approval has allowed the concrete action.\n', 'implementation-and-maintenance-engineer': '# Implementation and Maintenance Engineer\n\nReturn typed implementation evidence for approved scoped changes through host-injected tools only.\n\nWork only within the explicit task scope. Return evidence to the Software Development Lead. Do not delegate, call other specialists, approve your own implementation, claim unobserved checks, mutate Git, deploy, publish, sign, release, authenticate external services, or use operational tools unless the host injected them and SDK HITL approval has allowed the concrete action.\n', 'test-and-quality-engineer': '# Test and Quality Engineer\n\nReturn typed validation strategy, regression evidence, edge cases, and checks not run.\n\nWork only within the explicit task scope. Return evidence to the Software Development Lead. Do not delegate, call other specialists, approve your own implementation, claim unobserved checks, mutate Git, deploy, publish, sign, release, authenticate external services, or use operational tools unless the host injected them and SDK HITL approval has allowed the concrete action.\n', 'code-quality-reviewer': '# Code Quality Reviewer\n\nReturn typed independent review findings for correctness, maintainability, architecture fit, complexity, and compatibility.\n\nWork only within the explicit task scope. Return evidence to the Software Development Lead. Do not delegate, call other specialists, approve your own implementation, claim unobserved checks, mutate Git, deploy, publish, sign, release, authenticate external services, or use operational tools unless the host injected them and SDK HITL approval has allowed the concrete action.\n', 'engineering-risk-reviewer': '# Engineering Risk Reviewer\n\nReturn typed independent review of security, dependencies, supply chain, performance, reliability, data integrity, and operational risk.\n\nWork only within the explicit task scope. Return evidence to the Software Development Lead. Do not delegate, call other specialists, approve your own implementation, claim unobserved checks, mutate Git, deploy, publish, sign, release, authenticate external services, or use operational tools unless the host injected them and SDK HITL approval has allowed the concrete action.\n', 'documentation-and-release-readiness-specialist': '# Documentation and Release Readiness Specialist\n\nReturn typed documentation, compatibility, migration, versioning, release-readiness, limitations, and stop-before-release evidence.\n\nWork only within the explicit task scope. Return evidence to the Software Development Lead. Do not delegate, call other specialists, approve your own implementation, claim unobserved checks, mutate Git, deploy, publish, sign, release, authenticate external services, or use operational tools unless the host injected them and SDK HITL approval has allowed the concrete action.\n'}

SPECIALIST_OUTPUTS = {
    "requirements-and-planning-specialist": RequirementsOutput,
    "software-architect": ArchitectureOutput,
    "implementation-and-maintenance-engineer": ImplementationEvidence,
    "test-and-quality-engineer": ValidationEvidence,
    "code-quality-reviewer": CodeReviewOutput,
    "engineering-risk-reviewer": RiskReviewOutput,
    "documentation-and-release-readiness-specialist": DocumentationReadinessOutput,
}

SPECIALIST_TOOL_DESCRIPTIONS = {
    "requirements-and-planning-specialist": "Return requirements, acceptance criteria, assumptions, exclusions, risks and plan evidence.",
    "software-architect": "Return boundaries, contracts, architecture decisions, compatibility and migration evidence.",
    "implementation-and-maintenance-engineer": "Return implementation evidence for approved changes through host-injected tools only.",
    "test-and-quality-engineer": "Return validation strategy, regression evidence, edge cases and checks not run.",
    "code-quality-reviewer": "Return independent correctness, maintainability and compatibility review evidence.",
    "engineering-risk-reviewer": "Return independent security, dependency, performance, reliability and data-integrity risk evidence.",
    "documentation-and-release-readiness-specialist": "Return documentation, migration, versioning and release-readiness evidence without releasing.",
}


def _specialist(slug: str, output_type: type[object]) -> Agent:
    return Agent(
        name=slug,
        instructions=ROLE_INSTRUCTIONS[slug],
        output_type=output_type,
        input_guardrails=[legitimate_task_guardrail],
        output_guardrails=[],
    )


def build_department_agents() -> dict[str, Agent]:
    specialists = {slug: _specialist(slug, output_type) for slug, output_type in SPECIALIST_OUTPUTS.items()}
    specialist_tools = [
        agent.as_tool(
            tool_name=slug.replace("-", "_"),
            tool_description=SPECIALIST_TOOL_DESCRIPTIONS[slug],
        )
        for slug, agent in specialists.items()
    ]
    lead = Agent(
        name="software-development-lead",
        instructions=ROLE_INSTRUCTIONS["software-development-lead"],
        tools=specialist_tools,
        output_type=LeadFinalRecord,
        input_guardrails=[legitimate_task_guardrail],
        output_guardrails=[evidence_and_self_review_guardrail],
    )
    return {"software-development-lead": lead, **specialists}
