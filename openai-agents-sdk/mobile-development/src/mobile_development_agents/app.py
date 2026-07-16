from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from mobile_development_agents.agents.definitions import ROLE_SPECS
from mobile_development_agents.config import MobileAgentsConfig
from mobile_development_agents.context import MobileTechnology, SDKWorkflowContext, WorkflowRequest
from mobile_development_agents.outputs import (
    CompletionCriterion,
    CriterionStatus,
    WorkflowResult,
    WorkflowState,
)
from mobile_development_agents.tools.approvals import DenyByDefaultApprovalProvider
from mobile_development_agents.tools.contracts import GuardedToolHost, ToolHost
from mobile_development_agents.workflows.registry import WorkflowSpec, get_workflow


TECHNOLOGY_OWNER: dict[MobileTechnology, str] = {
    MobileTechnology.ANDROID: "android-engineer",
    MobileTechnology.IOS: "ios-engineer",
    MobileTechnology.KMP: "kmp-engineer",
    MobileTechnology.FLUTTER: "flutter-engineer",
    MobileTechnology.REACT_NATIVE: "react-native-engineer",
}


@dataclass(frozen=True, slots=True)
class RoutedWorkflow:
    spec: WorkflowSpec
    primary_owner: str
    reviewers: tuple[str, ...]
    validation_issues: tuple[str, ...]


def configure_sdk(config: MobileAgentsConfig | None = None) -> None:
    resolved = config or MobileAgentsConfig.from_env()
    if resolved.tracing_disabled:
        try:
            from agents import set_tracing_disabled
        except ImportError:
            return
        set_tracing_disabled(True)


def select_implementation_owner(request: WorkflowRequest, spec: WorkflowSpec) -> str:
    if spec.primary_owner not in {"mobile-architect", "mobile-test-engineer", "mobile-performance-reviewer"}:
        return spec.primary_owner
    if len(request.technologies) == 1:
        return TECHNOLOGY_OWNER[next(iter(request.technologies))]
    return spec.primary_owner


def route_workflow(request: WorkflowRequest) -> RoutedWorkflow:
    spec = get_workflow(request.workflow)
    issues = list(spec.validate_request(request))
    owner = select_implementation_owner(request, spec)
    reviewers = tuple(reviewer for reviewer in spec.reviewers if reviewer != owner)
    if owner == "mobile-code-reviewer" or "mobile-code-reviewer" not in reviewers:
        issues.append("mobile-code-reviewer must be an independent final reviewer")
    if owner in reviewers:
        issues.append("self-review is not allowed")
    return RoutedWorkflow(spec=spec, primary_owner=owner, reviewers=reviewers, validation_issues=tuple(issues))


def classify_completion_criteria(spec: WorkflowSpec, request: WorkflowRequest) -> tuple[CompletionCriterion, ...]:
    criteria: list[CompletionCriterion] = [
        CompletionCriterion("requirements traceability", CriterionStatus.REQUIRED, "Every workflow starts from explicit inputs."),
        CompletionCriterion("project configuration", CriterionStatus.REQUIRED, "Project inspection and command discovery are mandatory."),
        CompletionCriterion("security", CriterionStatus.REQUIRED, "Secrets and approval-controlled surfaces are always checked."),
        CompletionCriterion("independent review", CriterionStatus.REQUIRED, "mobile-code-reviewer is required for completion."),
    ]
    tech_values = {technology.value for technology in request.technologies}
    technology_criteria = {
        MobileTechnology.ANDROID: "Android Gradle/lint/unit or instrumented validation",
        MobileTechnology.IOS: "iOS scheme discovery and non-publishing build/test validation",
        MobileTechnology.KMP: "KMP target compilation and expect/actual validation",
        MobileTechnology.FLUTTER: "Flutter analyze and test validation",
        MobileTechnology.REACT_NATIVE: "React Native type/lint/test and native host validation",
    }
    for technology, name in technology_criteria.items():
        if technology in request.technologies:
            criteria.append(CompletionCriterion(name, CriterionStatus.CONDITIONALLY_REQUIRED, f"{technology.value} requested."))
        else:
            criteria.append(CompletionCriterion(name, CriterionStatus.NOT_APPLICABLE, f"{technology.value} not in scope; requested: {sorted(tech_values)}."))
    if spec.name == "prepare-mobile-release":
        criteria.append(CompletionCriterion("publication/upload/submission", CriterionStatus.NOT_APPLICABLE, "Release actions are prohibited; readiness only."))
    return tuple(criteria)


def dry_run_workflow(request: WorkflowRequest) -> WorkflowResult:
    routed = route_workflow(request)
    state = WorkflowState.NEEDS_APPROVAL if routed.validation_issues else WorkflowState.PLANNED
    return WorkflowResult(
        workflow=routed.spec.name,
        state=state,
        primary_owner=routed.primary_owner,
        reviewers=routed.reviewers,
        criteria=classify_completion_criteria(routed.spec, request),
        limitations=routed.validation_issues,
    )


async def run_workflow(
    request: WorkflowRequest,
    config: MobileAgentsConfig | None = None,
    host: ToolHost | None = None,
) -> Any:
    routed = route_workflow(request)
    if routed.validation_issues:
        return dry_run_workflow(request)
    configure_sdk(config)
    from agents import RunConfig, Runner, ToolExecutionConfig
    from mobile_development_agents.agents.coordinator import build_coordinator_agent
    from mobile_development_agents.runtime import pending_approval_interruptions

    coordinator = build_coordinator_agent(config)
    guarded_host = GuardedToolHost(host, DenyByDefaultApprovalProvider()) if host is not None else None
    context = SDKWorkflowContext(request=request, tool_host=guarded_host)
    prompt = (
        f"Execute workflow {routed.spec.name}. Primary owner: {routed.primary_owner}. "
        f"Reviewers: {', '.join(routed.reviewers)}. Objective: {request.objective}. "
        "Do not publish, sign, upload, deploy, spend money, activate integrations, or fabricate evidence."
    )
    run_config = RunConfig(
        workflow_name="mobile-development",
        tracing_disabled=(config or MobileAgentsConfig.from_env()).tracing_disabled,
        tool_execution=ToolExecutionConfig(pre_approval_tool_input_guardrails=True),
    )
    result = await Runner.run(coordinator, prompt, context=context, run_config=run_config, max_turns=12)
    interruptions = pending_approval_interruptions(result)
    if interruptions:
        return result
    return result


def responsibility_matrix() -> dict[str, dict[str, str | bool]]:
    return {
        name: {
            "exclusive_scope": spec.exclusive_scope,
            "read_only": spec.read_only,
            "native_classification": spec.native_classification,
        }
        for name, spec in ROLE_SPECS.items()
    }
