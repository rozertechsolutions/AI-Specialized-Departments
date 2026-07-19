from __future__ import annotations

from typing import Any

from agents import Agent, GuardrailFunctionOutput, handoff, input_guardrail, output_guardrail

from .assurance_review import ROLE_INSTRUCTIONS as ASSURANCE_ROLE_INSTRUCTIONS
from .ci_cd_release_engineering import ROLE_INSTRUCTIONS as CI_CD_ROLE_INSTRUCTIONS
from .cloud_foundation import ROLE_INSTRUCTIONS as CLOUD_FOUNDATION_ROLE_INSTRUCTIONS
from .containers_platform_engineering import ROLE_INSTRUCTIONS as CONTAINERS_ROLE_INSTRUCTIONS
from .devsecops import ROLE_INSTRUCTIONS as DEVSECOPS_ROLE_INSTRUCTIONS
from .finops_sustainability import ROLE_INSTRUCTIONS as FINOPS_ROLE_INSTRUCTIONS
from .models import ROLE_BY_SLUG, ROLE_REGISTRY, RoleDefinition
from .performance_capacity_efficiency import ROLE_INSTRUCTIONS as PERFORMANCE_ROLE_INSTRUCTIONS
from .resilience_disaster_recovery import ROLE_INSTRUCTIONS as RESILIENCE_ROLE_INSTRUCTIONS
from .sre_observability_operations import ROLE_INSTRUCTIONS as SRE_ROLE_INSTRUCTIONS


LEADERSHIP_ROLE_INSTRUCTIONS = {
    "devops-cloud-orchestrator": "# DevOps and Cloud Orchestrator\n\nOwn intake, routing, dependency control, escalation, and evidence aggregation for the DevOps and Cloud department. Do not implement specialist work, approve your own output, run tools, deploy, authenticate, mutate infrastructure, spend money, publish, sign, or claim runtime validation. Route to exactly one primary owner and require independent Assurance for material cross-section work.",
    "cloud-and-platform-architect": "# Cloud and Platform Architect\n\nOwn provider-neutral cloud and platform architecture, ADRs, standards, target-state models, technology selection, and cross-section technical boundaries. Cover AWS, Azure, Google Cloud, hybrid, and multicloud only when requirements justify them. Do not implement IaC, pipelines, containers, observability, failover, scanners, or cloud changes.",
}


ROLE_INSTRUCTIONS = {
    **LEADERSHIP_ROLE_INSTRUCTIONS,
    **CLOUD_FOUNDATION_ROLE_INSTRUCTIONS,
    **CI_CD_ROLE_INSTRUCTIONS,
    **CONTAINERS_ROLE_INSTRUCTIONS,
    **SRE_ROLE_INSTRUCTIONS,
    **RESILIENCE_ROLE_INSTRUCTIONS,
    **PERFORMANCE_ROLE_INSTRUCTIONS,
    **DEVSECOPS_ROLE_INSTRUCTIONS,
    **FINOPS_ROLE_INSTRUCTIONS,
    **ASSURANCE_ROLE_INSTRUCTIONS,
}

SECRET_PATTERNS = (
    "-----BEGIN",
    "AKIA",
    "ASIA",
    "sk-",
    "ghp_",
    "github_pat_",
    "xoxb-",
    "password=",
    "secret=",
    "token=",
    "private_key",
)

MUTATION_PATTERNS = (
    "terraform apply",
    "tofu apply",
    "pulumi up",
    "cloudformation deploy",
    "az deployment",
    "gcloud deploy",
    "aws cloudformation deploy",
    "kubectl apply",
    "helm install",
    "docker push",
    "delete production",
    "drop database",
    "destroy",
    "force delete",
)

PRIVILEGED_PATTERNS = (
    "deploy to production",
    "publish the package",
    "push to main",
    "sign the artifact",
    "purchase commitment",
    "buy reserved",
    "increase spend",
    "disable approval",
    "bypass review",
)

RUNTIME_CLAIM_PATTERNS = (
    "deployment succeeded",
    "pipeline passed",
    "tests passed",
    "scan passed",
    "terraform plan succeeded",
    "validated in production",
    "runtime validation completed",
)


def _flatten(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n".join(str(item) for item in value)
    return str(value)


def _matches(text: str, patterns: tuple[str, ...]) -> tuple[str, ...]:
    lowered = text.lower()
    return tuple(pattern for pattern in patterns if pattern.lower() in lowered)


def _guardrail_result(text: str, *, include_runtime_claims: bool) -> GuardrailFunctionOutput:
    patterns = SECRET_PATTERNS + MUTATION_PATTERNS + PRIVILEGED_PATTERNS
    if include_runtime_claims:
        patterns += RUNTIME_CLAIM_PATTERNS
    matches = _matches(text, patterns)
    return GuardrailFunctionOutput(
        output_info={"matched_patterns": matches, "policy": "static-devops-cloud-safety"},
        tripwire_triggered=bool(matches),
    )


@input_guardrail(name="reject-secrets-and-unsafe-actions", run_in_parallel=False)
def reject_secrets_and_unsafe_actions(context: Any, agent: Agent[Any], input_data: str | list[Any]) -> GuardrailFunctionOutput:
    return _guardrail_result(_flatten(input_data), include_runtime_claims=False)


@output_guardrail(name="reject-unsafe-or-unsupported-runtime-claims")
def reject_unsafe_or_unsupported_runtime_claims(context: Any, agent: Agent[Any], output_data: Any) -> GuardrailFunctionOutput:
    return _guardrail_result(_flatten(output_data), include_runtime_claims=True)


INPUT_GUARDRAILS = [reject_secrets_and_unsafe_actions]
OUTPUT_GUARDRAILS = [reject_unsafe_or_unsupported_runtime_claims]
ENTRY_AGENT_SLUG = "devops-cloud-orchestrator"
ASSURANCE_AGENT_SLUG = "devops-and-cloud-assurance-reviewer"


def _agent(role: RoleDefinition) -> Agent[Any]:
    return Agent(
        name=role.name,
        instructions=ROLE_INSTRUCTIONS[role.slug],
        handoff_description=f"{role.section}: {role.mission}",
        tools=[],
        mcp_servers=[],
        input_guardrails=INPUT_GUARDRAILS,
        output_guardrails=OUTPUT_GUARDRAILS,
    )


def build_department_agents() -> dict[str, Agent[Any]]:
    agents = {role.slug: _agent(role) for role in ROLE_REGISTRY}
    entry_agent = agents[ENTRY_AGENT_SLUG]
    entry_agent.handoffs = [
        handoff(agents[slug])
        for slug in ROLE_BY_SLUG[ENTRY_AGENT_SLUG].delegates_to
        if slug != ENTRY_AGENT_SLUG
    ]
    return agents


DEPARTMENT_AGENTS = build_department_agents()

