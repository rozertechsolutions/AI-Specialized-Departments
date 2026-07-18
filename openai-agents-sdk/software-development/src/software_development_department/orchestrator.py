from __future__ import annotations

from dataclasses import dataclass, field

from agents import Agent, Runner

from .agents import SPECIALIST_OUTPUTS, build_department_agents
from .models import DepartmentTask, OrchestrationState


@dataclass(frozen=True)
class OrchestrationLimits:
    max_turns: int = 16
    max_specialist_calls: int = 12

    def __post_init__(self) -> None:
        if not 1 <= self.max_turns <= 32:
            raise ValueError("max_turns must be between 1 and 32")
        if not 1 <= self.max_specialist_calls <= 24:
            raise ValueError("max_specialist_calls must be between 1 and 24")


@dataclass
class DepartmentRuntime:
    lead: Agent
    limits: OrchestrationLimits = field(default_factory=OrchestrationLimits)
    state: OrchestrationState = OrchestrationState.READY

    @classmethod
    def build(cls, limits: OrchestrationLimits | None = None) -> "DepartmentRuntime":
        agents = build_department_agents()
        return cls(lead=agents["software-development-lead"], limits=limits or OrchestrationLimits())

    def validate_specialist_call_sequence(self, calls: tuple[str, ...]) -> OrchestrationState:
        if len(calls) > self.limits.max_specialist_calls:
            return OrchestrationState.STOPPED
        if any(call not in SPECIALIST_OUTPUTS for call in calls):
            return OrchestrationState.STOPPED
        if len(calls) != len(tuple(dict.fromkeys(calls))):
            return OrchestrationState.STOPPED
        return OrchestrationState.RUNNING

    async def run(self, task: DepartmentTask):
        """Run only when the host explicitly invokes the department.

        The Lead remains the active top-level agent. Specialists are available
        only as Agent.as_tool() tools, so their typed results return to the
        Lead without transferring the conversation.
        """
        prompt = (
            f"Objective: {task.objective}\n"
            f"Authorized scope: {task.authorized_scope}\n"
            f"Acceptance criteria: {task.acceptance_criteria}\n"
            f"Exclusions: {task.exclusions}\n"
            f"Risk level: {task.risk_level}\n"
            "Use specialist tools only as bounded calls. Produce a LeadFinalRecord with evidence, "
            "checks not run, limitations, human decisions, and an explicit stop state."
        )
        self.state = OrchestrationState.RUNNING
        result = await Runner.run(self.lead, prompt, max_turns=self.limits.max_turns)
        if getattr(result, "interruptions", None):
            self.state = OrchestrationState.PAUSED_FOR_HUMAN_APPROVAL
        else:
            self.state = OrchestrationState.COMPLETED
        return result
