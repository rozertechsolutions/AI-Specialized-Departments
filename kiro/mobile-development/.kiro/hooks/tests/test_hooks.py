from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


HOOK_DIR = Path(__file__).resolve().parents[1]
AGENTS_DIR = HOOK_DIR.parent / "agents"


def run_hook(name: str, payload: object, *, raw: bool = False) -> subprocess.CompletedProcess[str]:
    data = payload if raw else json.dumps(payload)
    return subprocess.run(
        [sys.executable, "-B", str(HOOK_DIR / name)],
        input=data,
        text=True,
        capture_output=True,
        timeout=5,
        check=False,
    )


class KiroHookTests(unittest.TestCase):
    def assert_allows(self, script: str, payload: object) -> None:
        result = run_hook(script, payload)
        self.assertEqual(result.returncode, 0, result.stderr)

    def assert_blocks(self, script: str, payload: object, *, raw: bool = False) -> str:
        result = run_hook(script, payload, raw=raw)
        self.assertEqual(result.returncode, 2)
        self.assertTrue(result.stderr)
        return result.stderr

    def test_stable_agents_embed_expected_hooks(self) -> None:
        for path in AGENTS_DIR.glob("*.json"):
            data = json.loads(path.read_text())
            hooks = data.get("preToolUse", [])
            names = {hook["name"] for hook in hooks}
            if "shell" in data.get("tools", []):
                self.assertIn("mobile-shell-safety-guard", names, path.name)
            if "write" in data.get("tools", []):
                self.assertIn("mobile-path-scope-guard", names, path.name)
            else:
                self.assertNotIn("mobile-path-scope-guard", names, path.name)
            self.assertEqual(data.get("mcpServers"), {})
            self.assertIs(data.get("includeMcpJson"), False)

    def test_obsolete_standalone_hook_files_are_absent(self) -> None:
        self.assertFalse((HOOK_DIR / "mobile-safety-guards.json").exists())
        self.assertFalse((HOOK_DIR / "guard-mcp.py").exists())

    def test_shell_guard_blocks_risky_commands_and_malformed_tokens(self) -> None:
        blocked = [
            {"command": "git reset --hard HEAD"},
            {"command": "rm -rf src"},
            {"command": "firebase deploy"},
            {"command": "fastlane deliver"},
            {"command": "echo ok > file"},
            {"command": "printf x | sh"},
            {"command": "echo $(cat .env)"},
            {"command": "python3 -c 'import os'"},
            {"command": "../gradlew test"},
            {"command": r"C:\Users\name\.ssh\id_rsa"},
        ]
        for payload in blocked:
            with self.subTest(payload=payload):
                self.assert_blocks("guard-shell.py", payload)
        self.assert_blocks("guard-shell.py", "{bad", raw=True)

    def test_shell_guard_allows_safe_read_or_validation_commands(self) -> None:
        for command in ("./gradlew test", "python3 -m unittest discover", "git status --short"):
            with self.subTest(command=command):
                self.assert_allows("guard-shell.py", {"command": command})

    def test_path_guard_blocks_scope_escape_and_secrets_but_allows_public_clients(self) -> None:
        blocked = [
            {"path": "../outside.txt"},
            {"path": "/etc/passwd"},
            {"path": ".env"},
            {"path": "keys/release.jks"},
            {"path": "config/service-account.json"},
        ]
        for payload in blocked:
            with self.subTest(payload=payload):
                self.assert_blocks("guard-path.py", payload)
        self.assert_allows("guard-path.py", {"path": "google-services.json"})
        self.assert_allows("guard-path.py", {"path": "GoogleService-Info.plist"})
        self.assert_allows("guard-path.py", {"path": ".kiro/agents/android-engineer.json"})


if __name__ == "__main__":
    unittest.main()
