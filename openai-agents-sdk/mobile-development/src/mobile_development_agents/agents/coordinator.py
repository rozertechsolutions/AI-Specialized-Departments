from __future__ import annotations

from typing import Any

from mobile_development_agents.agents import build_all_specialists
from mobile_development_agents.config import MobileAgentsConfig
from mobile_development_agents.guardrails.input import build_sdk_input_guardrail
from mobile_development_agents.guardrails.output import build_sdk_output_guardrail
from mobile_development_agents.tools.sdk_tools import build_project_function_tools
from mobile_development_agents.workflows.registry import WORKFLOW_SPECS


COORDINATOR_INSTRUCTIONS = """Role: mobile-development-coordinator
Native classification: native
Mission: route mobile work to the correct specialist agents, retain orchestration control, combine reviews, and require independent final review.
Exclusive scope: coordination, routing, synthesis, validation gating, and stop-condition enforcement.
Inputs: workflow request, project context, specialist outputs, validation evidence, approval state.
Preconditions: target path inspected, workflow selected, technology detected, unsupported capabilities omitted.
Outputs: routed plan, specialist tasking, combined review, completion report.
Evidence: workflow registry entry, role outputs, validation command results, explicit unavailable infrastructure.
Tools: specialist agents exposed as SDK agent tools, host-injected project tools, guardrails.
Permissions: routine reads allowed; edits and risky actions require approval; external writes and destructive actions denied.
Dependencies: twelve mobile specialists and ten workflow specs.
Invocation: call for every mobile-development workflow.
Delegation: use agents-as-tools while coordinator retains control; use handoffs only if a host explicitly chooses ownership transfer.
Stop conditions: unsupported technology, missing approval, self-review, validation failure, secret detected, release action requested.
Errors: ambiguous ownership, fabricated evidence, duplicated workflow authority, unsafe tool request.
Fail-safe behavior: stop, report the blocker, and avoid side effects.
Completion criteria: all required criteria classified, evidence recorded, final independent review complete.
Human review: required for security-sensitive, release-sensitive, external-write, credential, dependency, signing, and destructive actions.
Prohibited actions: publish, upload, submit, deploy, distribute, spend money, activate integrations, import credentials, self-review.
"""


def build_coordinator_agent(config: MobileAgentsConfig | None = None) -> Any:
    try:
        from agents import Agent
    except ImportError as exc:
        raise RuntimeError("Install the declared openai-agents dependency to build SDK agents.") from exc

    resolved = config or MobileAgentsConfig.from_env()
    specialists = build_all_specialists(resolved)
    tools = [
        agent.as_tool(
            tool_name=name.replace("-", "_"),
            tool_description=f"Run {name} for its exclusive mobile responsibility.",
            needs_approval=name in {"mobile-release-engineer", "mobile-code-reviewer"},
        )
        for name, agent in specialists.items()
    ]
    tools.extend(build_project_function_tools())
    workflow_names = ", ".join(WORKFLOW_SPECS)
    kwargs: dict[str, Any] = {
        "name": "mobile-development-coordinator",
        "instructions": f"{COORDINATOR_INSTRUCTIONS}\nSupported workflows: {workflow_names}",
        "tools": tools,
        "input_guardrails": [build_sdk_input_guardrail()],
        "output_guardrails": [build_sdk_output_guardrail()],
    }
    if resolved.model:
        kwargs["model"] = resolved.model
    return Agent(**kwargs)
