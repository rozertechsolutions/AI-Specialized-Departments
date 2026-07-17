from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


HOOK_DIR = Path(__file__).resolve().parents[1]
AGENTS_DIR = HOOK_DIR.parent / "agents"
SPECIALIZATION_ROOT = AGENTS_DIR.parents[1]
SUPPORTED_HOOK_FIELDS = {"matcher", "command"}
SHELL_HOOK = {
    "matcher": "execute_bash",
    "command": "python3 .kiro/hooks/guard-shell.py",
}
PATH_HOOK = {
    "matcher": "fs_write",
    "command": "python3 .kiro/hooks/guard-path.py",
}


def shell_payload(command: str, *, tool_name: str = "execute_bash") -> dict[str, object]:
    return {
        "hook_event_name": "preToolUse",
        "cwd": str(SPECIALIZATION_ROOT),
        "session_id": "test-session",
        "tool_name": tool_name,
        "tool_input": {"command": command},
    }


def path_payload(path: str, *, tool_name: str = "fs_write") -> dict[str, object]:
    return {
        "hook_event_name": "preToolUse",
        "cwd": str(SPECIALIZATION_ROOT),
        "session_id": "test-session",
        "tool_name": tool_name,
        "tool_input": {
            "operations": [
                {
                    "mode": "Write",
                    "path": path,
                }
            ]
        },
    }


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

    def test_agents_use_documented_hooks_object(self) -> None:
        agent_paths = sorted(AGENTS_DIR.glob("*.json"))
        self.assertEqual(len(agent_paths), 12)
        for path in agent_paths:
            with self.subTest(agent=path.name):
                data = json.loads(path.read_text())
                tools = set(data.get("tools", []))

                self.assertNotIn("preToolUse", data)
                self.assertIn("hooks", data)
                self.assertIn("preToolUse", data["hooks"])

                hooks = data["hooks"]["preToolUse"]
                self.assertIsInstance(hooks, list)
                self.assertNotEqual(hooks, [])
                for hook in hooks:
                    self.assertEqual(set(hook), SUPPORTED_HOOK_FIELDS)

                expected = []
                if "shell" in tools:
                    expected.append(SHELL_HOOK)
                if "write" in tools:
                    expected.append(PATH_HOOK)
                self.assertEqual(hooks, expected)

                self.assertEqual(data.get("mcpServers"), {})
                self.assertIs(data.get("includeMcpJson"), False)
                self.assertEqual(data.get("allowedTools"), ["read"])
                if "write" not in tools:
                    self.assertNotIn(PATH_HOOK, hooks)

    def test_obsolete_standalone_hook_files_are_absent(self) -> None:
        self.assertFalse((HOOK_DIR / "mobile-safety-guards.json").exists())
        self.assertFalse((HOOK_DIR / "guard-mcp.py").exists())

    def test_shell_guard_requires_official_pretooluse_payload(self) -> None:
        malformed_payloads = [
            "{bad",
            {"hook_event_name": "postToolUse", "cwd": str(SPECIALIZATION_ROOT), "session_id": "s", "tool_name": "execute_bash", "tool_input": {"command": "git status"}},
            {"hook_event_name": "preToolUse", "cwd": str(SPECIALIZATION_ROOT), "session_id": "s", "tool_name": "fs_write", "tool_input": {"command": "git status"}},
            {"hook_event_name": "preToolUse", "cwd": str(SPECIALIZATION_ROOT), "session_id": "s", "tool_name": "execute_bash", "tool_input": {}},
        ]
        self.assert_blocks("guard-shell.py", malformed_payloads[0], raw=True)
        for payload in malformed_payloads[1:]:
            with self.subTest(payload=payload):
                self.assert_blocks("guard-shell.py", payload)

    def test_shell_guard_blocks_risky_commands(self) -> None:
        blocked_commands = [
            "git reset --hard HEAD",
            "git push origin main",
            "rm -rf src",
            "sudo xcodebuild test",
            "npm install left-pad",
            "pip3 install package",
            "dart pub add http",
            "firebase deploy",
            "eas build",
            "fastlane deliver",
            "codesign --sign identity app",
            "security import certificate.p12",
            "echo ok > file",
            "printf x | sh",
            "test -f app && echo ok",
            "echo $(cat .env)",
            "python3 -c 'import os'",
            "../gradlew test",
            r"C:\Users\name\.ssh\id_rsa",
            "/etc/passwd",
            "base64 ZWNobyBzaA==",
        ]
        for command in blocked_commands:
            with self.subTest(command=command):
                self.assert_blocks("guard-shell.py", shell_payload(command))

    def test_shell_guard_allows_safe_read_or_validation_commands(self) -> None:
        for command in ("./gradlew test", "python3 -m unittest discover", "git status --short", "ls .kiro/agents"):
            with self.subTest(command=command):
                self.assert_allows("guard-shell.py", shell_payload(command))

    def test_path_guard_requires_official_pretooluse_payload(self) -> None:
        malformed_payloads = [
            "{bad",
            {"hook_event_name": "postToolUse", "cwd": str(SPECIALIZATION_ROOT), "session_id": "s", "tool_name": "fs_write", "tool_input": {"operations": [{"path": "src/File.kt"}]}},
            {"hook_event_name": "preToolUse", "cwd": str(SPECIALIZATION_ROOT), "session_id": "s", "tool_name": "execute_bash", "tool_input": {"operations": [{"path": "src/File.kt"}]}},
            {"hook_event_name": "preToolUse", "cwd": str(SPECIALIZATION_ROOT), "session_id": "s", "tool_name": "fs_write", "tool_input": {"path": "src/File.kt"}},
            {"hook_event_name": "preToolUse", "cwd": str(SPECIALIZATION_ROOT), "session_id": "s", "tool_name": "fs_write", "tool_input": {"operations": []}},
        ]
        self.assert_blocks("guard-path.py", malformed_payloads[0], raw=True)
        for payload in malformed_payloads[1:]:
            with self.subTest(payload=payload):
                self.assert_blocks("guard-path.py", payload)

    def test_path_guard_blocks_scope_escape_and_secret_material(self) -> None:
        blocked_paths = [
            "../outside.txt",
            "./../outside.txt",
            "/etc/passwd",
            "/tmp/outside.txt",
            r"C:\Users\name\project\file.txt",
            r"\\server\share\file.txt",
            "dir/with space/file.txt",
            '"src/File.kt"',
            "local.properties",
            ".env",
            ".env.local",
            "keys/release.jks",
            "keys/release.keystore",
            "certs/distribution.p12",
            "certs/profile.mobileprovision",
            "config/service-account.json",
            "secrets/private-key.pem",
            "ios/certificate.txt",
            "bad\x00path.txt",
        ]
        for path in blocked_paths:
            with self.subTest(path=path):
                self.assert_blocks("guard-path.py", path_payload(path))

    def test_path_guard_allows_scoped_public_and_regular_mobile_files(self) -> None:
        allowed_paths = [
            "google-services.json",
            "app/google-services.json",
            "GoogleService-Info.plist",
            "ios/App/GoogleService-Info.plist",
            ".env.example",
            ".env.sample",
            ".env.template",
            ".kiro/agents/android-engineer.json",
            "src/main/java/example/Feature.kt",
            "./src/main/kotlin/example/Feature.kt",
            str(SPECIALIZATION_ROOT / ".kiro/agents/android-engineer.json"),
        ]
        for path in allowed_paths:
            with self.subTest(path=path):
                self.assert_allows("guard-path.py", path_payload(path))


if __name__ == "__main__":
    unittest.main()
