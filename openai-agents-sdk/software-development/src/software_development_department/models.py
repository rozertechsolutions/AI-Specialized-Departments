from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class RiskLevel(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class DepartmentTask:
    objective: str
    authorized_scope: tuple[str, ...]
    acceptance_criteria: tuple[str, ...]
    exclusions: tuple[str, ...] = ()
    risk_level: RiskLevel = RiskLevel.MEDIUM


@dataclass(frozen=True)
class EvidenceItem:
    claim: str
    source: str
    observed: bool
    limitation: str | None = None


@dataclass(frozen=True)
class ReviewResult:
    reviewer: str
    approved: bool
    findings: tuple[str, ...] = ()
    blocking_findings: tuple[str, ...] = ()


@dataclass(frozen=True)
class CompletionReport:
    objective: str
    acceptance_status: dict[str, bool]
    evidence: tuple[EvidenceItem, ...]
    reviews: tuple[ReviewResult, ...]
    checks_not_run: tuple[str, ...] = ()
    remaining_risks: tuple[str, ...] = ()
    ready_for_human_release_decision: bool = False
