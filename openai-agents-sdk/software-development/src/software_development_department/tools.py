from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol

from .models import ApprovalDecision, ProposedToolAction, ToolApprovalResult
from .policies import action_requires_human_approval, approval_result_allows_action, normalize_relative_path


class RepositoryReader(Protocol):
    async def read_text(self, path: str) -> str: ...
    async def search(self, query: str, paths: tuple[str, ...]) -> tuple[str, ...]: ...


class RepositoryWriter(Protocol):
    async def write_text(self, path: str, content: str) -> None: ...
    async def replace_text(self, path: str, old: str, new: str) -> None: ...


class HumanApproval(Protocol):
    async def request_approval(self, action: ProposedToolAction) -> ApprovalDecision: ...


@dataclass
class DeterministicApprovalFake:
    decision: ApprovalDecision = ApprovalDecision.PENDING
    requested: list[ProposedToolAction] = field(default_factory=list)

    async def request_approval(self, action: ProposedToolAction) -> ApprovalDecision:
        self.requested.append(action)
        return self.decision


@dataclass(frozen=True)
class InertWorkspaceTools:
    workspace_root: Path
    approval: HumanApproval

    async def authorize(self, action: ProposedToolAction) -> ToolApprovalResult:
        normalize_relative_path(self.workspace_root, action.target)
        if not action_requires_human_approval(action):
            return ToolApprovalResult(action, ApprovalDecision.APPROVED, "read-only action allowed")
        decision = await self.approval.request_approval(action)
        if not approval_result_allows_action(decision):
            return ToolApprovalResult(action, ApprovalDecision.DENIED, "sensitive action denied; no action executed")
        return ToolApprovalResult(action, ApprovalDecision.APPROVED, "sensitive action approved by host")


# The reference package intentionally provides no concrete filesystem, shell,
# network, Git, deployment, publication, signing, credential, or unrestricted
# operational tools. Hosts must inject implementations and SDK HITL approval.
