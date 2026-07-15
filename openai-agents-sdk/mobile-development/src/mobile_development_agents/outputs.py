from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class CriterionStatus(str, Enum):
    REQUIRED = "required"
    CONDITIONALLY_REQUIRED = "conditionally-required"
    NOT_APPLICABLE = "not-applicable"


class WorkflowState(str, Enum):
    PLANNED = "planned"
    BLOCKED = "blocked"
    NEEDS_APPROVAL = "needs-approval"
    VALIDATING = "validating"
    COMPLETE = "complete"
    FAILED = "failed"


@dataclass(frozen=True, slots=True)
class CompletionCriterion:
    name: str
    status: CriterionStatus
    reason: str

    def __post_init__(self) -> None:
        if self.status is CriterionStatus.NOT_APPLICABLE and not self.reason.strip():
            raise ValueError("not-applicable criteria require a concrete reason")


@dataclass(frozen=True, slots=True)
class ValidationEvidence:
    command: str
    result: str
    source: str


@dataclass(frozen=True, slots=True)
class WorkflowResult:
    workflow: str
    state: WorkflowState
    primary_owner: str
    reviewers: tuple[str, ...]
    evidence: tuple[ValidationEvidence, ...] = ()
    criteria: tuple[CompletionCriterion, ...] = ()
    limitations: tuple[str, ...] = ()
    files_changed: tuple[str, ...] = ()

    def independent_reviewers(self) -> tuple[str, ...]:
        return tuple(reviewer for reviewer in self.reviewers if reviewer != self.primary_owner)
