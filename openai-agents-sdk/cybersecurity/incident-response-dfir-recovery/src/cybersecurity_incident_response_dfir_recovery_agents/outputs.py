from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class IncidentArtifact:
    reference: str
    title: str
    purpose: str
    scope: str
    owner: str
    independent_reviewer: str
    evidence: tuple[str, ...] = field(default_factory=tuple)
    assumptions: tuple[str, ...] = field(default_factory=tuple)
    confidence: str = "undetermined"
    limitations: tuple[str, ...] = field(default_factory=tuple)
    human_decisions: tuple[str, ...] = field(default_factory=tuple)
    completion_criteria: tuple[str, ...] = field(default_factory=tuple)
