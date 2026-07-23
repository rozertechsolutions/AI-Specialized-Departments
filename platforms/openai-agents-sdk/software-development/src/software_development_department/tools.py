from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

from .models import ApprovalDecision, ProposedToolAction, ToolApprovalResult


class RepositoryReader(Protocol):
    async def read_text(self, path: str) -> str: ...
    async def search(self, query: str, paths: tuple[str, ...]) -> tuple[str, ...]: ...


class RepositoryWriter(Protocol):
    async def write_text(self, path: str, content: str) -> None: ...
    async def replace_text(self, path: str, old: str, new: str) -> None: ...


class HumanApproval(Protocol):
    async def request_approval(self, action: ProposedToolAction) -> ApprovalDecision: ...


@dataclass
class DeterministicApprovalProvider:
    decision: ApprovalDecision = ApprovalDecision.PENDING
    requested: list[ProposedToolAction] = field(default_factory=list)

    async def request_approval(self, action: ProposedToolAction) -> ApprovalDecision:
        self.requested.append(action)
        return self.decision


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
