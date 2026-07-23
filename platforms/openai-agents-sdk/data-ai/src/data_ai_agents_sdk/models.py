from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


Status = Literal["PASS", "FAIL", "BLOCKED"]


class DataAIContext(BaseModel):
    model_config = ConfigDict(frozen=True)

    request_id: str
    authorized_scope: tuple[str, ...]
    human_approved_actions: tuple[str, ...] = ()
    max_delegation_depth: int = 1
    tracing_disabled: bool = True


class HandoffRequest(BaseModel):
    model_config = ConfigDict(frozen=True)

    reason: str
    priority: Literal["low", "medium", "high", "critical"] = "medium"
    evidence_needed: tuple[str, ...] = ()
    originating_owner: str = "data-ai-orchestrator"


class EvidenceItem(BaseModel):
    model_config = ConfigDict(frozen=True)

    claim: str
    source: str
    observed: bool
    limitation: str | None = None


class ReviewFinding(BaseModel):
    model_config = ConfigDict(frozen=True)

    finding: str
    severity: Literal["info", "low", "medium", "high", "critical"]
    owner: str
    evidence: str
    closure_criteria: str


class ApprovalRequest(BaseModel):
    model_config = ConfigDict(frozen=True)

    action: str
    reason: str
    risk_owner: str
    evidence_reference: str
    status: Literal["requires_human_approval"] = "requires_human_approval"


class ReviewOutput(BaseModel):
    model_config = ConfigDict(frozen=True)

    owner: str
    status: Status
    summary: str
    evidence: tuple[EvidenceItem, ...] = ()
    findings: tuple[ReviewFinding, ...] = ()
    human_review_required: bool = False
    monitoring_required: bool = False
    rollback_required: bool = False
    unresolved_risks: tuple[str, ...] = ()
    next_owner: str | None = None

    @field_validator("status")
    @classmethod
    def status_must_be_canonical(cls, value: Status) -> Status:
        if value not in {"PASS", "FAIL", "BLOCKED"}:
            raise ValueError("status must be PASS, FAIL, or BLOCKED")
        return value


class WorkflowContract(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    owner: str
    steps: tuple[str, ...] = Field(min_length=1)
    gates: tuple[str, ...] = Field(min_length=1)
    final_status_values: tuple[Status, Status, Status] = ("PASS", "FAIL", "BLOCKED")
