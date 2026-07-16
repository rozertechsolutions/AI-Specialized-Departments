from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RoleContract:
    slug: str
    name: str
    mission: str
    owns: tuple[str, ...]
    excludes: tuple[str, ...]
    human_review: tuple[str, ...]
