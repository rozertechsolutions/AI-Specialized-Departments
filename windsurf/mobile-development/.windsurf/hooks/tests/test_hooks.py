from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


HOOK_DIR = Path(__file__).resolve().parents[1]


def run_hook(name: str, payload: object, cwd: Path | None = None, *, raw: bool = False) -> subprocess.CompletedProcess[str]:
    data = payload if raw else json.dumps(payload)
    return subprocess.run(
        [sys.executable, "-B", str(HOOK_DIR / name)],
        input=data,
        text=True,
        cwd=str(cwd or HOOK_DIR.parents[1]),
        capture_output=True,
        timeout=5,
        check=False,
    )


def command_payload(command: str) -> dict[str, object]:
    return {"agent_action_name": "pre_run_command", "tool_info": {"command_line": command}}


def write_payload(path: str, text: str = "") -> dict[str, object]:
    return {
        "agent_action_name": "pre_write_code",
        "tool_info": {"file_path": path, "edits": [{"new_string": text}]},
    }


class WindsurfHookTests(unittest.TestCase):
    def assert_allows(self, script: str, payload: object, cwd: Path | None = None) -> None:
        result = run_hook(script, payload, cwd)
        self.assertEqual(result.returncode, 0, result.stderr)

    def assert_blocks(self, script: str, payload: object, cwd: Path | None = None, *, raw: bool = False) -> str:
        result = run_hook(script, payload, cwd, raw=raw)
        self.assertEqual(result.returncode, 2)
        self.assertTrue(result.stderr)
        return result.stderr

    def test_hooks_config_references_existing_scripts(self) -> None:
        config = json.loads((HOOK_DIR.parent / "hooks.json").read_text())
        scripts = {path.name for path in HOOK_DIR.glob("*.py")}
        serialized = json.dumps(config)
        for name in ("command_guard.py", "scope_guard.py", "mcp_guard.py", "secret_guard.py"):
            self.assertIn(name, scripts)
            self.assertIn(name, serialized)

    def test_command_guard_blocks_chaining_encoded_release_and_dependency_actions(self) -> None:
        commands = [
            "rm -rf src",
            "git reset --hard HEAD",
            "firebase deploy",
            "fastlane deliver",
            "xcodebuild archive -scheme App",
            "npm install left-pad",
            "echo ok > file",
            "printf x | sh",
            "echo $(cat .env)",
            "powershell -enc ZQBjAGgAbwA=",
        ]
        for command in commands:
            with self.subTest(command=command):
                self.assert_blocks("command_guard.py", command_payload(command))
        self.assert_blocks("command_guard.py", "{bad", raw=True)

    def test_command_guard_allows_safe_validation_examples(self) -> None:
        for command in ("python3 -m unittest discover", "./gradlew test", "flutter test"):
            self.assert_allows("command_guard.py", command_payload(command))

    def test_scope_guard_blocks_traversal_outside_and_protected_paths(self) -> None:
        with tempfile.TemporaryDirectory(dir=HOOK_DIR.parents[1]) as tmp:
            root = Path(tmp)
            for path in ("../outside.txt", "/tmp/outside.txt", ".git/config", ".ssh/id_rsa"):
                with self.subTest(path=path):
                    self.assert_blocks("scope_guard.py", write_payload(path), root)
            self.assert_allows("scope_guard.py", write_payload("src/main.kt"), root)
            self.assert_blocks("scope_guard.py", "{bad", root, raw=True)

    def test_secret_guard_blocks_real_secrets_and_allows_placeholders_and_public_clients(self) -> None:
        self.assert_blocks("secret_guard.py", write_payload(".env", "OPENAI_API_KEY=realistic-secret-value"))
        self.assert_blocks("secret_guard.py", write_payload("src/Config.kt", 'api_key="realistic-secret-value"'))
        self.assert_blocks("secret_guard.py", write_payload("src/key.pem", "-----BEGIN PRIVATE KEY-----"))
        self.assert_allows("secret_guard.py", write_payload("README.md", "API_KEY=${OPENAI_API_KEY}\nTOKEN=YOUR_ACCESS_TOKEN"))
        self.assert_allows("secret_guard.py", write_payload("google-services.json", '{"current_key":"AIzaSyDUMMYEXAMPLEPLACEHOLDER123456789"}'))
        self.assert_allows("secret_guard.py", write_payload("GoogleService-Info.plist", "<key>API_KEY</key><string>YOUR_API_KEY</string>"))

    def test_mcp_guard_fails_closed_for_mcp_and_malformed_json(self) -> None:
        self.assert_blocks(
            "mcp_guard.py",
            {"agent_action_name": "pre_mcp_tool_use", "tool_info": {"mcp_server_name": "github", "mcp_tool_name": "read_issue"}},
        )
        self.assert_blocks("mcp_guard.py", "{bad", raw=True)


if __name__ == "__main__":
    unittest.main()
