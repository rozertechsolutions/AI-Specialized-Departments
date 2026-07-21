from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
<<<<<<< HEAD
from pathlib import Path
from typing import Any, Mapping

from agents import RunContextWrapper, function_tool, tool_input_guardrail
from agents.tool_guardrails import ToolGuardrailFunctionOutput

from .models import (
    ApprovalDecision,
    ApprovalDecisionValue,
    HumanApprovalProvider,
    ProposedToolAction,
    ReadToolResult,
    RepositoryReader,
    RepositoryWriter,
    RoleSlug,
    SpecialistResult,
    TaskRequest,
    ToolActionType,
    ToolApprovalResult,
    WriteToolResult,
)
from .policies import (
    action_requires_human_approval,
    approval_result_allows_action,
    concrete_action_is_prohibited,
    normalize_relative_path,
    validate_scope,
)
=======
from typing import Protocol

from .models import ApprovalDecision, ProposedToolAction, ToolApprovalResult
>>>>>>> feature/software-development


@dataclass(frozen=True)
class RunLimits:
    max_top_level_turns: int = 16
    max_turns_per_specialist: int = 6
    max_calls_per_specialist: int = 3
    max_total_specialist_calls: int = 12
    max_approval_resume_cycles: int = 4

    def __post_init__(self) -> None:
        if self.max_top_level_turns < 1:
            raise ValueError("max_top_level_turns must be at least 1")
        if self.max_turns_per_specialist < 1:
            raise ValueError("max_turns_per_specialist must be at least 1")
        if self.max_calls_per_specialist < 1:
            raise ValueError("max_calls_per_specialist must be at least 1")
        if self.max_total_specialist_calls < 1:
            raise ValueError("max_total_specialist_calls must be at least 1")
        if self.max_approval_resume_cycles < 0:
            raise ValueError("max_approval_resume_cycles must not be negative")


@dataclass
<<<<<<< HEAD
class DepartmentContext:
    repository_reader: RepositoryReader
    repository_writer: RepositoryWriter
    approval_provider: HumanApprovalProvider
    workspace_root: Path
    limits: RunLimits = field(default_factory=RunLimits)
    lead_model: Any | None = None
    specialist_models: Mapping[RoleSlug, Any] = field(default_factory=dict)
    specialist_call_counts: dict[str, int] = field(default_factory=dict)
    specialist_call_ids: set[str] = field(default_factory=set)
    total_specialist_calls: int = 0
    approval_resume_cycles: int = 0
    rejected_required_action: str | None = None
    stopped_limit: str | None = None
    completed_tool_calls: list[str] = field(default_factory=list)
    write_events: list[tuple[str, str]] = field(default_factory=list)
    active_task: TaskRequest | None = None
    active_authorized_paths: tuple[Path, ...] = ()
    specialist_outputs: dict[RoleSlug, list[object]] = field(default_factory=dict)
    specialist_completion_order: list[RoleSlug] = field(default_factory=list)
=======
class DeterministicApprovalProvider:
    decision: ApprovalDecision = ApprovalDecision.PENDING
    requested: list[ProposedToolAction] = field(default_factory=list)
>>>>>>> feature/software-development

    def model_for(self, role: RoleSlug | str | None) -> Any | None:
        if role is None or role == "software-development-lead":
            return self.lead_model
        role_slug = role if isinstance(role, RoleSlug) else RoleSlug(role)
        return self.specialist_models.get(role_slug)

    def start_task(self, task: TaskRequest) -> None:
        if self.active_task is not None:
            if self.active_task == task:
                return
            raise RuntimeError("runtime context already has an active task")
        if not task.scope.authorized_paths:
            raise ValueError("authorized scope must not be empty")
        authorized = tuple(normalize_relative_path(self.workspace_root, path) for path in task.scope.authorized_paths)
        self.active_task = task
        self.active_authorized_paths = authorized

    def reset_task(self) -> None:
        self.active_task = None
        self.active_authorized_paths = ()

    def resolve_safe_path(self, path: str) -> str:
        resolved = normalize_relative_path(self.workspace_root, path)
        if not self.active_authorized_paths:
            raise ValueError("no active task scope is configured")
        if not any(resolved == allowed or allowed in resolved.parents for allowed in self.active_authorized_paths):
            raise ValueError("path is outside the active authorized task scope")
        return resolved.relative_to(self.workspace_root.expanduser().resolve(strict=False)).as_posix()

    def require_in_scope(self, path: str, authorized_paths: tuple[str, ...]) -> None:
        if not validate_scope((path,), authorized_paths, self.workspace_root):
            raise ValueError("path is outside the authorized task scope")

    def record_specialist_call(self, slug: str, call_id: str) -> None:
        if call_id in self.specialist_call_ids:
            return
        current = self.specialist_call_counts.get(slug, 0) + 1
        total = self.total_specialist_calls + 1
        if current > self.limits.max_calls_per_specialist:
            self.stopped_limit = f"max_calls_per_specialist:{slug}"
            raise RuntimeError(self.stopped_limit)
        if total > self.limits.max_total_specialist_calls:
            self.stopped_limit = "max_total_specialist_calls"
            raise RuntimeError(self.stopped_limit)
        self.specialist_call_ids.add(call_id)
        self.specialist_call_counts[slug] = current
        self.total_specialist_calls = total

    def record_approval_resume_cycle(self) -> None:
        self.approval_resume_cycles += 1
        if self.approval_resume_cycles > self.limits.max_approval_resume_cycles:
            self.stopped_limit = "max_approval_resume_cycles"
            raise RuntimeError(self.stopped_limit)

    def record_specialist_output(self, slug: str, output: object, expected_type: type[object]) -> None:
        role = RoleSlug(slug)
        if not isinstance(output, expected_type):
            self.stopped_limit = f"wrong_specialist_output_type:{slug}"
            raise TypeError(self.stopped_limit)
        outputs = self.specialist_outputs.setdefault(role, [])
        if len(outputs) >= self.limits.max_calls_per_specialist:
            self.stopped_limit = f"max_calls_per_specialist:{slug}"
            raise RuntimeError(self.stopped_limit)
        outputs.append(output)
        self.specialist_completion_order.append(role)


@dataclass
class DeterministicApprovalProvider:
    decision: ApprovalDecision = ApprovalDecision(True, "approved by deterministic fake")
    requested: list[object] = field(default_factory=list)

    async def pending_decisions(self, interruptions: tuple[Any, ...]) -> tuple[ApprovalDecision, ...]:
        self.requested.extend(interruptions)
        return tuple(self.decision for _ in interruptions)


@dataclass
class MemoryRepositoryReader:
    files: dict[str, str]
    reads: list[str] = field(default_factory=list)

    async def read_text(self, path: str) -> str:
        self.reads.append(path)
        return self.files[path]


@dataclass
class MemoryRepositoryWriter:
    files: dict[str, str] = field(default_factory=dict)
    writes: list[tuple[str, str]] = field(default_factory=list)

    async def write_text(self, path: str, content: str) -> None:
        self.files[path] = content
        self.writes.append((path, content))


def _validate_read(path: str, context: DepartmentContext) -> None:
    context.resolve_safe_path(path)


def _validate_write(path: str, content: str, reason: str, context: DepartmentContext) -> None:
    context.resolve_safe_path(path)
    action = ProposedToolAction(ToolActionType.WRITE, path, reason)
    if concrete_action_is_prohibited(action):
        raise ValueError("prohibited write action")
    if not action_requires_human_approval(action):
        raise ValueError("write action must require approval")
    secret_patterns = (
        r"OPENAI_API_KEY\s*=",
        r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
        r"(?i)\b(api[_-]?key|token|password|secret)\s*=\s*['\"]?[A-Za-z0-9_./+=-]{12,}",
    )
    safe_example = path.startswith("docs/") and "safe example" in reason.lower()
    if not safe_example and any(re.search(pattern, content) for pattern in secret_patterns):
        raise ValueError("tool output would contain secret-like content")


@tool_input_guardrail
async def repository_tool_input_guardrail(data: object) -> ToolGuardrailFunctionOutput:
    try:
        args = json.loads(data.context.tool_arguments)
        path = args.get("path", "")
        data.context.context.resolve_safe_path(path)
        if data.context.tool_name == "write_repository_file":
            _validate_write(path, args.get("content", ""), args.get("reason", ""), data.context.context)
    except Exception as exc:
        return ToolGuardrailFunctionOutput.reject_content(
            f"Rejected invalid repository tool input: {exc}",
            output_info={"valid": False, "reason": str(exc)},
        )
    return ToolGuardrailFunctionOutput.allow({"valid": True})


def build_repository_tools():
    @function_tool(
        name_override="read_repository_file",
        description_override="Read a normalized relative file path through the injected repository reader.",
        needs_approval=False,
        tool_input_guardrails=[repository_tool_input_guardrail],
    )
    async def read_repository_file(context: RunContextWrapper[DepartmentContext], path: str) -> ReadToolResult:
        normalized_path = context.context.resolve_safe_path(path)
        content = await context.context.repository_reader.read_text(normalized_path)
        return ReadToolResult(path=normalized_path, content=content)

    @function_tool(
        name_override="write_repository_file",
        description_override="Write a normalized relative file path through the injected repository writer after SDK approval.",
        needs_approval=True,
        tool_input_guardrails=[repository_tool_input_guardrail],
    )
    async def write_repository_file(
        context: RunContextWrapper[DepartmentContext],
        path: str,
        content: str,
        reason: str,
    ) -> WriteToolResult:
        normalized_path = context.context.resolve_safe_path(path)
        _validate_write(normalized_path, content, reason, context.context)
        await context.context.repository_writer.write_text(normalized_path, content)
        context.context.completed_tool_calls.append(f"write:{normalized_path}")
        context.context.write_events.append((normalized_path, content))
        return WriteToolResult(path=normalized_path, applied=True, message="approved write applied through injected writer")

    return read_repository_file, write_repository_file


<<<<<<< HEAD
@dataclass(frozen=True)
class InertWorkspaceTools:
    workspace_root: Path

    async def authorize(self, action: ProposedToolAction, decision: ApprovalDecisionValue) -> ToolApprovalResult:
        normalize_relative_path(self.workspace_root, action.target)
        if not action_requires_human_approval(action):
            return ToolApprovalResult(action, ApprovalDecisionValue.APPROVED, "read-only action allowed")
        if not approval_result_allows_action(decision):
            return ToolApprovalResult(action, ApprovalDecisionValue.REJECTED, "sensitive action denied; no action executed")
        return ToolApprovalResult(action, ApprovalDecisionValue.APPROVED, "sensitive action approved by host")


# The package provides protocols, in-memory fakes for tests, and SDK wrappers
# only. It intentionally does not instantiate filesystem, shell, Git, network,
# MCP, deployment, publication, signing, release, or credential clients.
=======
@dataclass
class MemoryRepository:
    files: dict[str, str] = field(default_factory=dict)
    writes: list[tuple[str, str]] = field(default_factory=list)

    async def read_text(self, path: str) -> str:
        return self.files[path]

    async def search(self, query: str, paths: tuple[str, ...]) -> tuple[str, ...]:
        return tuple(path for path in paths if query in self.files.get(path, ""))

    async def write_text(self, path: str, content: str) -> None:
        self.files[path] = content
        self.writes.append((path, content))

    async def replace_text(self, path: str, old: str, new: str) -> None:
        self.files[path] = self.files[path].replace(old, new)
        self.writes.append((path, self.files[path]))


def approval_result_allows_action(decision: ApprovalDecision) -> bool:
    return decision is ApprovalDecision.APPROVED


def approval_result(action: ProposedToolAction, decision: ApprovalDecision, message: str) -> ToolApprovalResult:
    return ToolApprovalResult(action=action, decision=decision, message=message)


# The reference package intentionally provides no concrete filesystem, shell,
# network, Git, deployment, publication, signing, credential, MCP, or
# unrestricted operational tools. Hosts inject repository tools and models.
>>>>>>> feature/software-development
