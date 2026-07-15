import unittest

from mobile_development_agents.context import ActionRisk
from mobile_development_agents.guardrails.input import validate_requested_path, validate_user_input
from mobile_development_agents.guardrails.output import safe_output, validate_agent_output
from mobile_development_agents.policies.permissions import PermissionDecision, decision_for_risk
from mobile_development_agents.policies.security import (
    classify_env_key,
    contains_secret,
    validate_shell_command,
)
from mobile_development_agents.tools.approvals import (
    ApprovalRequest,
    DenyByDefaultApprovalProvider,
    require_approval,
)


class SecurityAndToolTests(unittest.TestCase):
    def test_secret_detection_and_redaction(self) -> None:
        text = "password='example-redacted-value'"
        self.assertTrue(contains_secret(text))
        self.assertIn("[REDACTED]", safe_output(text))
        self.assertTrue(validate_user_input(text))
        self.assertTrue(validate_agent_output(text))

    def test_public_mobile_config_is_not_classified_as_secret(self) -> None:
        self.assertEqual(classify_env_key("GOOGLE_APP_ID"), "public-mobile-client-config")
        self.assertEqual(classify_env_key("ACCESS_TOKEN"), "secret")

    def test_path_guard_blocks_traversal_and_shell_syntax(self) -> None:
        self.assertTrue(validate_requested_path("../secrets.txt"))
        self.assertTrue(validate_requested_path("app/file.txt; rm -rf ."))
        self.assertTrue(validate_requested_path("/tmp/file"))

    def test_command_guard_blocks_chaining_git_and_redirection(self) -> None:
        self.assertTrue(validate_shell_command("pytest && rm -rf build"))
        self.assertTrue(validate_shell_command("git status"))
        self.assertTrue(validate_shell_command("pytest > output.txt"))
        self.assertFalse(validate_shell_command("pytest tests"))

    def test_deny_by_default_approval_provider(self) -> None:
        provider = DenyByDefaultApprovalProvider()
        self.assertTrue(
            provider.request_approval(ApprovalRequest("read", ActionRisk.ROUTINE_READ, "inspect")).approved
        )
        with self.assertRaises(PermissionError):
            require_approval(provider, ApprovalRequest("edit", ActionRisk.PROJECT_EDIT, "modify file"))

    def test_permission_policy_denies_external_and_destructive_actions(self) -> None:
        self.assertIs(decision_for_risk(ActionRisk.EXTERNAL_WRITE).decision, PermissionDecision.DENY)
        self.assertIs(decision_for_risk(ActionRisk.DESTRUCTIVE).decision, PermissionDecision.DENY)
