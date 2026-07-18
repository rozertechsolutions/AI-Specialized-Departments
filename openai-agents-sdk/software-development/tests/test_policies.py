import asyncio
from pathlib import Path

from software_development_department.models import ApprovalDecision, ProposedToolAction, RoleSlug, ToolActionType
from software_development_department.policies import (
    action_requires_human_approval,
    keyword_mentions_are_allowed,
    normalize_relative_path,
    validate_scope,
)
from software_development_department.tools import DeterministicApprovalFake, InertWorkspaceTools


def test_sensitive_concrete_actions_require_approval() -> None:
    action = ProposedToolAction(ToolActionType.PUBLISH, "dist/package", "publish package", RoleSlug.DOCUMENTATION)
    assert action_requires_human_approval(action)
    assert not action_requires_human_approval(ProposedToolAction(ToolActionType.READ, "src/a.py", "inspect"))


def test_keyword_mentions_alone_do_not_block_legitimate_analysis() -> None:
    assert keyword_mentions_are_allowed("Analyze credential handling and deployment risk without taking action")


def test_scope_validation_normalizes_and_blocks_escape(tmp_path: Path) -> None:
    assert validate_scope(("src/a.py",), ("src",), tmp_path)
    assert not validate_scope(("../outside",), ("src",), tmp_path)
    try:
        normalize_relative_path(tmp_path, "/absolute/path")
    except ValueError as exc:
        assert "absolute" in str(exc)
    else:
        raise AssertionError("absolute path escaped")


def test_denied_approval_stops_safely(tmp_path: Path) -> None:
    approval = DeterministicApprovalFake(ApprovalDecision.DENIED)
    tools = InertWorkspaceTools(tmp_path, approval)
    action = ProposedToolAction(ToolActionType.WRITE, "src/a.py", "edit file", RoleSlug.IMPLEMENTATION)
    result = asyncio.run(tools.authorize(action))
    assert result.decision is ApprovalDecision.DENIED
    assert "no action executed" in result.message
    assert approval.requested == [action]


def test_approved_read_only_action_does_not_pause(tmp_path: Path) -> None:
    approval = DeterministicApprovalFake(ApprovalDecision.PENDING)
    tools = InertWorkspaceTools(tmp_path, approval)
    action = ProposedToolAction(ToolActionType.READ, "src/a.py", "read file")
    result = asyncio.run(tools.authorize(action))
    assert result.decision is ApprovalDecision.APPROVED
    assert approval.requested == []
