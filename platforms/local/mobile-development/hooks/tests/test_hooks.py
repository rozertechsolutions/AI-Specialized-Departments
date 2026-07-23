import os
import sys
import unittest


HOOK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, HOOK_DIR)

from mobile_command_guard import inspect_command
from protected_file_guard import inspect_path
from release_action_guard import inspect_release_action
from sensitive_change_guard import inspect_change


class HookTests(unittest.TestCase):
    def test_blocks_shell_chaining(self):
        findings = inspect_command("gradle test && rm -rf build")
        self.assertTrue(any(f.code == "shell-metacharacter" for f in findings))
        self.assertTrue(any(f.code == "destructive-command" for f in findings))

    def test_blocks_path_traversal(self):
        findings = inspect_path("/tmp/project", "../secret.env", "read")
        self.assertTrue(any(f.code == "invalid-path" for f in findings))

    def test_warns_public_client_config_read(self):
        findings = inspect_path("/tmp/project", "app/google-services.json", "read")
        self.assertTrue(any(f.code == "public-client-config-review" for f in findings))

    def test_blocks_release_action(self):
        findings = inspect_release_action("xcrun notarytool submit app.zip")
        self.assertTrue(any(f.code == "release-action" for f in findings))

    def test_sensitive_change_warns(self):
        findings = inspect_change("ios/App/App.entitlements", "com.apple.developer.associated-domains")
        self.assertTrue(any(f.code == "sensitive-path" for f in findings))
        self.assertTrue(any(f.code == "sensitive-content" for f in findings))


if __name__ == "__main__":
    unittest.main()
