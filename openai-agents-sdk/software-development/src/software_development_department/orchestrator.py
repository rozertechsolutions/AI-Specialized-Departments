from __future__ import annotations

<<<<<<< HEAD
from dataclasses import dataclass
from pathlib import Path
from typing import Any
=======
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping
>>>>>>> feature/software-development

from agents import RunConfig, Runner
from agents.run_config import ToolExecutionConfig

<<<<<<< HEAD
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
=======
from .agents import build_department_agents
from .models import (
    ApprovalDecision,
    ApprovalDecisionRecord,
    DepartmentTask,
    FinalState,
    LeadFinalRecord,
    ProposedToolAction,
    ToolActionType,
    ToolApprovalResult,
)
from .policies import action_requires_human_approval, final_record_is_supported, normalize_relative_path, validate_scope
from .tools import HumanApproval, RepositoryReader, RepositoryWriter, approval_result, approval_result_allows_action


@dataclass(frozen=True)
class RunLimits:
>>>>>>> feature/software-development
    max_turns: int = 16
    max_specialist_calls: int = 12
    max_approval_cycles: int = 4

    def __post_init__(self) -> None:
        if not 1 <= self.max_turns <= 32:
            raise ValueError("max_turns must be between 1 and 32")
        if not 1 <= self.max_specialist_calls <= 24:
            raise ValueError("max_specialist_calls must be between 1 and 24")
<<<<<<< HEAD
        if not 1 <= self.max_total_tool_calls <= 64:
            raise ValueError("max_total_tool_calls must be between 1 and 64")
        if not 1 <= self.max_approval_cycles <= 12:
            raise ValueError("max_approval_cycles must be between 1 and 12")
>>>>>>> feature/software-development
=======
        if not 0 <= self.max_approval_cycles <= 12:
            raise ValueError("max_approval_cycles must be between 0 and 12")


@dataclass
class DepartmentContext:
    workspace_root: Path
    authorized_paths: tuple[str, ...]
    repository_reader: RepositoryReader
    repository_writer: RepositoryWriter
    approval_provider: HumanApproval
    approval_records: list[ApprovalDecisionRecord] = field(default_factory=list)

    def normalize_authorized_path(self, path: str) -> Path:
        if not validate_scope((path,), self.authorized_paths, self.workspace_root):
            raise ValueError("path is outside the active authorized scope")
        return normalize_relative_path(self.workspace_root, path)

    async def read_text(self, path: str) -> str:
        self.normalize_authorized_path(path)
        return await self.repository_reader.read_text(path)

    async def write_text(self, path: str, content: str, reason: str) -> ToolApprovalResult:
        self.normalize_authorized_path(path)
        action = ProposedToolAction(ToolActionType.WRITE, path, reason)
        if not action_requires_human_approval(action):
            await self.repository_writer.write_text(path, content)
            return approval_result(action, ApprovalDecision.APPROVED, "read-only action allowed")
        decision = await self.approval_provider.request_approval(action)
        self.approval_records.append(
            ApprovalDecisionRecord(
                subject=path,
                action=action.action_type.value,
                decision=decision,
                evidence=reason,
            )
        )
        if not approval_result_allows_action(decision):
            return approval_result(action, ApprovalDecision.REJECTED, "sensitive action rejected; no write executed")
        await self.repository_writer.write_text(path, content)
        return approval_result(action, ApprovalDecision.APPROVED, "sensitive action approved by host")


@dataclass(frozen=True)
class DepartmentRunResult:
    state: FinalState
    sdk_result: Any
    resume_state: Any | None = None
    interruptions: tuple[Any, ...] = ()
    final_record: LeadFinalRecord | None = None
    approval_records: tuple[ApprovalDecisionRecord, ...] = ()
    reason: str = ""

    @property
    def paused(self) -> bool:
        return self.state is FinalState.PAUSED

    @property
    def completed(self) -> bool:
        return self.state is FinalState.COMPLETED
>>>>>>> feature/software-development


@dataclass
class DepartmentRuntime:
<<<<<<< HEAD
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
=======
    lead: Agent
    specialists: Mapping[str, Agent]
    context: DepartmentContext
    limits: RunLimits = field(default_factory=RunLimits)
    approval_cycles: int = 0

    @classmethod
    def build(
        cls,
        context: DepartmentContext,
        limits: RunLimits | None = None,
        models: Mapping[str, Any] | None = None,
    ) -> "DepartmentRuntime":
        agents = build_department_agents(models=models)
        lead = agents["software-development-lead"]
        specialists = {slug: agent for slug, agent in agents.items() if slug != "software-development-lead"}
        return cls(lead=lead, specialists=specialists, context=context, limits=limits or RunLimits())
>>>>>>> feature/software-development

    async def run(self, task: DepartmentTask) -> DepartmentRunResult:
        if not task.objective.strip():
            return DepartmentRunResult(FinalState.BLOCKED, None, reason="task objective is required")
        if not task.authorized_scope:
            return DepartmentRunResult(FinalState.BLOCKED, None, reason="authorized scope is required")
        if not validate_scope(task.authorized_scope, self.context.authorized_paths, self.context.workspace_root):
            return DepartmentRunResult(FinalState.BLOCKED, None, reason="task scope is outside the active authorized scope")

        prompt = self._task_prompt(task)
        result = await Runner.run(self.lead, prompt, max_turns=self.limits.max_turns)
        return self._classify_result(result)

    async def approve_and_resume(self, run_result: DepartmentRunResult, interruption: Any | None = None) -> DepartmentRunResult:
        state = self._require_resume_state(run_result)
        selected = interruption or self._single_interruption(run_result)
        if self.approval_cycles >= self.limits.max_approval_cycles:
            return DepartmentRunResult(FinalState.STOPPED, run_result.sdk_result, reason="approval cycle limit reached")
        state.approve(selected)
        self.approval_cycles += 1
        result = await Runner.run(self.lead, state, max_turns=self.limits.max_turns)
        return self._classify_result(result)

    async def reject_and_resume(self, run_result: DepartmentRunResult, interruption: Any | None = None, message: str = "human rejected") -> DepartmentRunResult:
        state = self._require_resume_state(run_result)
        selected = interruption or self._single_interruption(run_result)
        state.reject(selected, rejection_message=message)
        self.approval_cycles += 1
        result = await Runner.run(self.lead, state, max_turns=self.limits.max_turns)
        return self._classify_result(result)

    def _task_prompt(self, task: DepartmentTask) -> str:
        return (
            f"Objective: {task.objective}\n"
            f"Authorized scope: {task.authorized_scope}\n"
            f"Acceptance criteria: {task.acceptance_criteria}\n"
            f"Exclusions: {task.exclusions}\n"
<<<<<<< HEAD
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
=======
            f"Risk level: {task.risk_level.value}\n"
            "The Software Development Lead remains the active manager. Use the seven specialist tools only as bounded "
            "agents-as-tools calls. Return a LeadFinalRecord with observed evidence, independent code-quality review, "
            "risk review when applicable, checks not run, limitations, approval records, and an explicit final state."
        )

    def _classify_result(self, result: Any) -> DepartmentRunResult:
        interruptions = tuple(getattr(result, "interruptions", ()) or ())
        if interruptions:
            return DepartmentRunResult(
                state=FinalState.PAUSED,
                sdk_result=result,
                resume_state=result.to_state(),
                interruptions=interruptions,
                approval_records=tuple(self.context.approval_records),
                reason="paused for SDK HITL approval",
            )
        final_output = getattr(result, "final_output", None)
        if isinstance(final_output, LeadFinalRecord):
            state = FinalState.COMPLETED if final_record_is_supported(final_output) else FinalState.BLOCKED
            return DepartmentRunResult(
                state=state,
                sdk_result=result,
                final_record=final_output,
                approval_records=tuple(self.context.approval_records),
                reason="evidence-backed completion" if state is FinalState.COMPLETED else "final record lacks required evidence",
            )
        return DepartmentRunResult(
            state=FinalState.STOPPED,
            sdk_result=result,
            approval_records=tuple(self.context.approval_records),
            reason="runner stopped without typed final record",
        )

    def _require_resume_state(self, run_result: DepartmentRunResult) -> Any:
        if run_result.resume_state is None:
            raise ValueError("run result does not contain resumable SDK state")
        return run_result.resume_state

    def _single_interruption(self, run_result: DepartmentRunResult) -> Any:
        if len(run_result.interruptions) != 1:
            raise ValueError("exactly one interruption must be selected explicitly")
        return run_result.interruptions[0]
>>>>>>> feature/software-development
