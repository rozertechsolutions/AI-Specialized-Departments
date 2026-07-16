from __future__ import annotations

from dataclasses import dataclass

from agents import Agent, Runner

from .agents import build_department_agents
from .models import DepartmentTask


@dataclass(frozen=True)
class DepartmentRuntime:
    lead: Agent
    max_turns: int = 16

    @classmethod
    def build(cls, max_turns: int = 16) -> "DepartmentRuntime":
        if not 1 <= max_turns <= 32:
            raise ValueError("max_turns must be between 1 and 32")
        agents = build_department_agents()
        return cls(lead=agents["software-development-lead"], max_turns=max_turns)

    async def run(self, task: DepartmentTask):
        """Run only when the host explicitly invokes the department.

        This method is never called at import time and receives no operational
        tools, credentials, endpoints, sessions, or deployment capabilities.
        """
        prompt = (
            f"Objective: {task.objective}\n"
            f"Authorized scope: {task.authorized_scope}\n"
            f"Acceptance criteria: {task.acceptance_criteria}\n"
            f"Exclusions: {task.exclusions}\n"
            f"Risk level: {task.risk_level}\n"
            "Produce an evidence-based plan and use handoffs without circular delegation."
        )
        return await Runner.run(self.lead, prompt, max_turns=self.max_turns)
