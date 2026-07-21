from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from agents import RunConfig, Runner
from agents.run_config import ToolExecutionConfig

from .agents import DepartmentAgents, build_department_agents
from .models import (
    ApprovalDecisionRecord,
    ApprovalDecisionValue,
    DepartmentTask,
    FinalState,
    HumanApprovalProvider,
    InterruptionState,
    LeadFinalRecord,
    RepositoryReader,
    RepositoryWriter,
    TaskRequest,
)
from .policies import derive_final_state, final_record_is_supported
from .tools import DepartmentContext, RunLimits


@dataclass(frozen=True)
<<<<<<< HEAD
class DepartmentRunResult:
    final_state: FinalState
    sdk_result: Any
    interruption_state: InterruptionState | None = None
    approvals_and_rejections: tuple[ApprovalDecisionRecord, ...] = ()
    stopped_reason: str | None = None
=======
class OrchestrationLimits:
    max_turns: int = 16
    max_specialist_calls: int = 12
    max_total_tool_calls: int = 20
    max_approval_cycles: int = 4

    def __post_init__(self) -> None:
        if not 1 <= self.max_turns <= 32:
            raise ValueError("max_turns must be between 1 and 32")
        if not 1 <= self.max_specialist_calls <= 24:
            raise ValueError("max_specialist_calls must be between 1 and 24")
        if not 1 <= self.max_total_tool_calls <= 64:
            raise ValueError("max_total_tool_calls must be between 1 and 64")
        if not 1 <= self.max_approval_cycles <= 12:
            raise ValueError("max_approval_cycles must be between 1 and 12")
>>>>>>> feature/software-development


@dataclass
class DepartmentRuntime:
    context: DepartmentContext
    agents: DepartmentAgents
    state: Any | None = None
    last_result: Any | None = None

    @classmethod
<<<<<<< HEAD
    def build(
        cls,
        *,
        repository_reader: RepositoryReader,
        repository_writer: RepositoryWriter,
        approval_provider: HumanApprovalProvider,
        workspace_root: Path,
        run_limits: RunLimits | None = None,
        lead_model: Any | None = None,
        specialist_models: dict[Any, Any] | None = None,
    ) -> "DepartmentRuntime":
        context = DepartmentContext(
            repository_reader=repository_reader,
            repository_writer=repository_writer,
            approval_provider=approval_provider,
            workspace_root=workspace_root,
            limits=run_limits or RunLimits(),
            lead_model=lead_model,
            specialist_models=specialist_models or {},
=======
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

    def validate_total_tool_calls(self, count: int) -> OrchestrationState:
        if count < 0 or count > self.limits.max_total_tool_calls:
            return OrchestrationState.STOPPED
        return OrchestrationState.RUNNING

    def validate_approval_cycles(self, count: int) -> OrchestrationState:
        if count < 0 or count > self.limits.max_approval_cycles:
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
>>>>>>> feature/software-development
        )
        return cls(context=context, agents=build_department_agents(context))

    def _prompt(self, task: TaskRequest) -> str:
        return (
            f"Objective: {task.objective}\n"
            f"Authorized scope: {task.scope.authorized_paths}\n"
            f"Acceptance criteria: {task.acceptance_criteria}\n"
            f"Exclusions: {task.scope.exclusions}\n"
            f"Risk level: {task.risk_level.value}\n"
            "The Lead must call specialists when their responsibility is required, retain manager "
            "control after each specialist tool call, preserve evidence, separate implementation "
            "from independent review, and return LeadFinalRecord."
        )

    def _paused_result(self, result: Any) -> DepartmentRunResult:
        subjects = tuple(getattr(item, "name", repr(item)) for item in result.interruptions)
        self.state = result.to_state()
        return DepartmentRunResult(
            final_state=FinalState.PAUSED,
            sdk_result=result,
            interruption_state=InterruptionState(
                pending_count=len(result.interruptions),
                pending_subjects=subjects,
                resume_available=True,
            ),
        )

    def _completed_or_blocked_result(self, result: Any) -> DepartmentRunResult:
        final_output = getattr(result, "final_output", None)
        if isinstance(final_output, LeadFinalRecord) and final_record_is_supported(final_output, self.context):
            return DepartmentRunResult(final_state=derive_final_state(final_output), sdk_result=result)
        return DepartmentRunResult(
            final_state=FinalState.BLOCKED,
            sdk_result=result,
            stopped_reason="final output was missing, untyped, unsupported, or lacked independent evidence",
        )

    async def run(self, task: DepartmentTask | TaskRequest) -> DepartmentRunResult:
        task_request = task.to_request() if isinstance(task, DepartmentTask) else task
        try:
            self.context.start_task(task_request)
            result = await Runner.run(
                self.agents.lead,
                self._prompt(task_request),
                context=self.context,
                max_turns=self.context.limits.max_top_level_turns,
                run_config=RunConfig(
                    tracing_disabled=True,
                    tool_execution=ToolExecutionConfig(pre_approval_tool_input_guardrails=True),
                ),
            )
        except RuntimeError as exc:
            return DepartmentRunResult(final_state=FinalState.STOPPED, sdk_result=None, stopped_reason=str(exc))
        except Exception as exc:
            return DepartmentRunResult(final_state=FinalState.BLOCKED, sdk_result=None, stopped_reason=f"{type(exc).__name__}: {exc}")
        self.last_result = result
        if getattr(result, "interruptions", None):
            return self._paused_result(result)
        return self._completed_or_blocked_result(result)

    async def apply_host_decisions_and_resume(self) -> DepartmentRunResult:
        if self.last_result is None or self.state is None:
            return DepartmentRunResult(final_state=FinalState.BLOCKED, sdk_result=None, stopped_reason="no paused run exists")
        interruptions = tuple(getattr(self.last_result, "interruptions", ()))
        if not interruptions:
            return DepartmentRunResult(final_state=FinalState.BLOCKED, sdk_result=self.last_result, stopped_reason="no pending interruption exists")
        try:
            self.context.record_approval_resume_cycle()
            decisions = await self.context.approval_provider.pending_decisions(interruptions)
        except RuntimeError as exc:
            return DepartmentRunResult(final_state=FinalState.STOPPED, sdk_result=self.last_result, stopped_reason=str(exc))
        except Exception as exc:
            return DepartmentRunResult(final_state=FinalState.BLOCKED, sdk_result=self.last_result, stopped_reason=f"approval provider failed: {type(exc).__name__}")
        if len(decisions) != len(interruptions):
            return DepartmentRunResult(
                final_state=FinalState.BLOCKED,
                sdk_result=self.last_result,
                stopped_reason="approval decision count did not match interruption count",
            )
        records: list[ApprovalDecisionRecord] = []
        for interruption, decision in zip(interruptions, decisions, strict=True):
            subject = getattr(interruption, "name", repr(interruption))
            value = ApprovalDecisionValue.APPROVED if decision.approved else ApprovalDecisionValue.REJECTED
            records.append(ApprovalDecisionRecord(subject=subject, decision=value, evidence=decision.reason))
            if decision.approved:
                self.state.approve(interruption)
            else:
                self.state.reject(interruption)
                self.context.rejected_required_action = subject
        if self.context.rejected_required_action:
            return DepartmentRunResult(
                final_state=FinalState.STOPPED,
                sdk_result=self.last_result,
                approvals_and_rejections=tuple(records),
                stopped_reason=f"required sensitive action rejected: {self.context.rejected_required_action}",
            )
        try:
            result = await Runner.run(
                self.agents.lead,
                self.state,
                max_turns=self.context.limits.max_top_level_turns,
                run_config=RunConfig(
                    tracing_disabled=True,
                    tool_execution=ToolExecutionConfig(pre_approval_tool_input_guardrails=True),
                ),
            )
        except RuntimeError as exc:
            return DepartmentRunResult(final_state=FinalState.STOPPED, sdk_result=self.last_result, approvals_and_rejections=tuple(records), stopped_reason=str(exc))
        except Exception as exc:
            return DepartmentRunResult(final_state=FinalState.BLOCKED, sdk_result=self.last_result, approvals_and_rejections=tuple(records), stopped_reason=f"{type(exc).__name__}: {exc}")
        self.last_result = result
        if getattr(result, "interruptions", None):
            return self._paused_result(result)
        resumed = self._completed_or_blocked_result(result)
        return DepartmentRunResult(
            final_state=resumed.final_state,
            sdk_result=resumed.sdk_result,
            approvals_and_rejections=tuple(records),
            stopped_reason=resumed.stopped_reason,
        )
