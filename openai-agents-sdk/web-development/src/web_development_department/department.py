"""OpenAI Agents SDK department wiring for web development."""

from __future__ import annotations

from agents import Agent

from .guardrails import final_verdict_guardrail, safe_web_request_guardrail
from .instructions import BASE_INSTRUCTIONS
from .models import ArchitectureDecision, FinalVerdict, ImplementationProposal, ReviewerFinding
from .tools import PROPOSAL_TOOLS, READ_CONTEXT_TOOLS, SENSITIVE_ACTION_TOOLS


ARCHITECTURE_INSTRUCTIONS = """Own web architecture decisions only.
Use caller-supplied repository snapshots and return structured architecture decisions with evidence,
alternatives, risks, and rollback notes. Do not implement, deploy, mutate files, or approve release readiness."""

FRONTEND_INSTRUCTIONS = """Own frontend implementation proposals only.
Assess semantic HTML, components, state, forms, loading/error/empty states, responsive behavior,
progressive enhancement, and browser compatibility. Return proposals and evidence; do not approve security or release readiness."""

BACKEND_INSTRUCTIONS = """Own backend/API implementation proposals only.
Assess contracts, validation, auth, sessions, cookies, CORS, CSRF, persistence, idempotency,
observability, migrations, rollback, and failure handling. Return proposals and evidence; do not approve security or deployment."""

SECURITY_REVIEW_INSTRUCTIONS = """Remain read-only and independent.
Review trust boundaries, authn/authz, sessions, secrets, input/output handling, injection, XSS, CSRF, SSRF,
CSP, CORS, cookies, logging, caching, trackers, dependencies, and privacy. Return findings only."""

ACCESSIBILITY_REVIEW_INSTRUCTIONS = """Remain read-only and independent.
Review accessibility, responsive states, performance, Core Web Vitals risks, metadata, SEO, crawlability,
and user-visible resilience. Return findings only."""

QUALITY_REVIEW_INSTRUCTIONS = """Remain read-only and independent.
Verify acceptance traceability, evidence, tests, browser compatibility, required reviews, documentation,
observability, migration, rollback, and unresolved risks. Return a final readiness finding only."""

LEAD_INSTRUCTIONS = (
    BASE_INSTRUCTIONS
    + """

## SDK orchestration contract
You are the manager. Keep control after every specialist call by using specialist agents exposed as tools.
Do not use handoffs for this workflow. Validate request scope, inspect caller-supplied snapshots, call
specialists as needed, reconcile their structured results, request human approval for sensitive actions,
and emit exactly one FinalVerdict. PASS is invalid with unresolved critical/high blocking findings,
missing required reviews, missing evidence, or unsupported execution-success claims.
"""
)


web_architecture_specialist = Agent(
    name="Web Architecture Specialist",
    instructions=ARCHITECTURE_INSTRUCTIONS,
    tools=READ_CONTEXT_TOOLS,
    output_type=ArchitectureDecision,
)

frontend_specialist = Agent(
    name="Frontend Specialist",
    instructions=FRONTEND_INSTRUCTIONS,
    tools=[*READ_CONTEXT_TOOLS, *PROPOSAL_TOOLS],
    output_type=ImplementationProposal,
)

backend_api_specialist = Agent(
    name="Backend and API Specialist",
    instructions=BACKEND_INSTRUCTIONS,
    tools=[*READ_CONTEXT_TOOLS, *PROPOSAL_TOOLS],
    output_type=ImplementationProposal,
)

security_privacy_reviewer = Agent(
    name="Security and Privacy Reviewer",
    instructions=SECURITY_REVIEW_INSTRUCTIONS,
    tools=READ_CONTEXT_TOOLS,
    output_type=ReviewerFinding,
)

accessibility_performance_seo_reviewer = Agent(
    name="Accessibility, Performance and SEO Reviewer",
    instructions=ACCESSIBILITY_REVIEW_INSTRUCTIONS,
    tools=READ_CONTEXT_TOOLS,
    output_type=ReviewerFinding,
)

quality_release_reviewer = Agent(
    name="Quality and Release Reviewer",
    instructions=QUALITY_REVIEW_INSTRUCTIONS,
    tools=READ_CONTEXT_TOOLS,
    output_type=ReviewerFinding,
)

web_development_lead = Agent(
    name="Web Development Lead",
    instructions=LEAD_INSTRUCTIONS,
    tools=[
        web_architecture_specialist.as_tool(
            tool_name="analyze_web_architecture",
            tool_description="Return architecture decisions, alternatives, evidence, risks, and rollback notes.",
        ),
        frontend_specialist.as_tool(
            tool_name="analyze_frontend_delivery",
            tool_description="Return frontend implementation proposals and evidence from supplied context.",
        ),
        backend_api_specialist.as_tool(
            tool_name="analyze_backend_api_auth",
            tool_description="Return backend/API/auth implementation proposals and evidence from supplied context.",
        ),
        security_privacy_reviewer.as_tool(
            tool_name="review_security_privacy",
            tool_description="Return independent read-only security and privacy findings.",
        ),
        accessibility_performance_seo_reviewer.as_tool(
            tool_name="review_accessibility_performance_seo",
            tool_description="Return independent read-only accessibility, performance, responsive, and SEO findings.",
        ),
        quality_release_reviewer.as_tool(
            tool_name="review_quality_release",
            tool_description="Return independent read-only quality and release readiness findings.",
        ),
        *READ_CONTEXT_TOOLS,
        *PROPOSAL_TOOLS,
        *SENSITIVE_ACTION_TOOLS,
    ],
    input_guardrails=[safe_web_request_guardrail],
    output_guardrails=[final_verdict_guardrail],
    output_type=FinalVerdict,
)


SPECIALIST_AGENTS = (
    web_architecture_specialist,
    frontend_specialist,
    backend_api_specialist,
    security_privacy_reviewer,
    accessibility_performance_seo_reviewer,
    quality_release_reviewer,
)
