from __future__ import annotations

from typing import Protocol


class RepositoryReader(Protocol):
    async def read_text(self, path: str) -> str: ...
    async def search(self, query: str, paths: tuple[str, ...]) -> tuple[str, ...]: ...


class RepositoryWriter(Protocol):
    async def write_text(self, path: str, content: str) -> None: ...


class HumanApproval(Protocol):
    async def approve(self, action: str, evidence: str) -> bool: ...


# The reference package intentionally provides no concrete filesystem, shell,
# network, Git, deployment, publication, signing, or credential tools.
