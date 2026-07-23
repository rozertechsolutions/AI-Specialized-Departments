from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, Field


class WorkState(str, Enum):
    DRAFT = 'draft'
    BLOCKED = 'blocked'
    REVIEW_REQUIRED = 'review_required'
    READY_FOR_HUMAN_APPROVAL = 'ready_for_human_approval'
    HUMAN_APPROVED = 'human_approved'


class EvidenceItem(BaseModel):
    source: str = Field(min_length=1)
    finding: str = Field(min_length=1)
    confidence: str = Field(min_length=1)
    limitation: str | None = None


class RiskItem(BaseModel):
    description: str = Field(min_length=1)
    severity: str = Field(pattern="^(low|medium|high|critical)$")
    mitigation: str = Field(min_length=1)
    owner: str = Field(min_length=1)


class WorkOutput(BaseModel):
    state: WorkState
    owner: str = Field(min_length=1)
    scope: str = Field(min_length=1)
    summary: str = Field(min_length=1)
    deliverables: list[str] = Field(default_factory=list)
    evidence: list[EvidenceItem] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    risks: list[RiskItem] = Field(default_factory=list)
    reviewers: list[str] = Field(default_factory=list)
    unresolved_questions: list[str] = Field(default_factory=list)
    next_human_decision: str = Field(min_length=1)
    external_action_performed: bool = False
