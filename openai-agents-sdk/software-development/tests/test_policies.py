import asyncio
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from software_development_department.models import ApprovalDecision, ProposedToolAction, RoleSlug, ToolActionType
from software_development_department.policies import (
    action_requires_human_approval,
    keyword_mentions_are_allowed,
    normalize_relative_path,
    validate_scope,
)
from software_development_department.tools import DeterministicApprovalFake, InertWorkspaceTools


class PolicyTests(unittest.TestCase):
    def test_sensitive_concrete_actions_require_approval(self) -> None:
        action = ProposedToolAction(ToolActionType.PUBLISH, "dist/package", "publish package", RoleSlug.DOCUMENTATION)
        self.assertTrue(action_requires_human_approval(action))
        self.assertFalse(action_requires_human_approval(ProposedToolAction(ToolActionType.READ, "src/a.py", "inspect")))

    def test_keyword_mentions_alone_do_not_block_legitimate_analysis(self) -> None:
        self.assertTrue(keyword_mentions_are_allowed("Analyze credential handling and deployment risk without taking action"))

    def test_scope_validation_normalizes_and_blocks_escape(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.assertTrue(validate_scope(("src/a.py",), ("src",), root))
            self.assertFalse(validate_scope(("../outside",), ("src",), root))
            with self.assertRaisesRegex(ValueError, "absolute"):
                normalize_relative_path(root, "/absolute/path")

    def test_scope_validation_rejects_symlink_escape(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp) / "workspace"
            outside = Path(tmp) / "outside"
            root.mkdir()
            outside.mkdir()
            (root / "link").symlink_to(outside)
            with self.assertRaisesRegex(ValueError, "escapes"):
                normalize_relative_path(root, "link/secret.txt")

    def test_denied_approval_stops_safely(self) -> None:
        with TemporaryDirectory() as tmp:
            approval = DeterministicApprovalFake(ApprovalDecision.DENIED)
            tools = InertWorkspaceTools(Path(tmp), approval)
            action = ProposedToolAction(ToolActionType.WRITE, "src/a.py", "edit file", RoleSlug.IMPLEMENTATION)
            result = asyncio.run(tools.authorize(action))
            self.assertIs(result.decision, ApprovalDecision.DENIED)
            self.assertIn("no action executed", result.message)
            self.assertEqual(approval.requested, [action])

    def test_approved_read_only_action_does_not_pause(self) -> None:
        with TemporaryDirectory() as tmp:
            approval = DeterministicApprovalFake(ApprovalDecision.PENDING)
            tools = InertWorkspaceTools(Path(tmp), approval)
            action = ProposedToolAction(ToolActionType.READ, "src/a.py", "read file")
            result = asyncio.run(tools.authorize(action))
            self.assertIs(result.decision, ApprovalDecision.APPROVED)
            self.assertEqual(approval.requested, [])


if __name__ == "__main__":
    unittest.main()
