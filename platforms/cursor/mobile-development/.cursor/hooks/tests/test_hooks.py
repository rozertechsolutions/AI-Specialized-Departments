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


class CursorHookTests(unittest.TestCase):
    def decision(self, script: str, payload: object, expected: str, *, cwd: Path | None = None, raw: bool = False) -> str:
        result = run_hook(script, payload, cwd, raw=raw)
        self.assertEqual(result.returncode, 0, result.stderr)
        body = json.loads(result.stdout)
        self.assertEqual(body["permission"], expected)
        return body["user_message"]

    def test_hooks_config_has_native_events_and_fail_closed(self) -> None:
        config = json.loads((HOOK_DIR.parent / "hooks.json").read_text())
        self.assertEqual(config["version"], 1)
        for hooks in config["hooks"].values():
            for hook in hooks:
                self.assertTrue(hook["failClosed"])

    def test_shell_guard_blocks_ambiguity_and_release_actions(self) -> None:
        denied = [
            "git reset --hard HEAD",
            "rm -rf src",
            "firebase deploy",
            "fastlane deliver",
            "npm publish",
        ]
        asked = [
            "echo ok > file",
            "printf x | sh",
            "echo $(cat .env)",
            "powershell -EncodedCommand ZQBjAGgAbwA=",
        ]
        for command in denied:
            with self.subTest(command=command):
                self.decision("guard-shell.py", {"command": command}, "deny")
        for command in asked:
            with self.subTest(command=command):
                self.decision("guard-shell.py", {"command": command}, "ask")

    def test_shell_guard_allows_safe_and_asks_for_dependency_or_network(self) -> None:
        self.decision("guard-shell.py", {"command": "./gradlew test"}, "ask")
        self.decision("guard-shell.py", {"command": "python3 -m unittest discover"}, "allow")
        self.decision("guard-shell.py", "{bad", "deny", raw=True)
        self.decision("guard-shell.py", {}, "deny")

    def test_file_edit_guard_blocks_paths_and_secret_content(self) -> None:
        with tempfile.TemporaryDirectory(dir=HOOK_DIR.parents[1]) as tmp:
            root = Path(tmp)
            safe = root / "google-services.json"
            safe.write_text('{"current_key":"AIzaSyDUMMYEXAMPLEPLACEHOLDER123456789"}')
            self.decision("guard-file-edit.py", {"file_path": str(safe)}, "allow", cwd=root)
            secret = root / "config.txt"
            secret.write_text('api_key="realistic-secret-value-12345"')
            self.decision("guard-file-edit.py", {"file_path": str(secret)}, "deny", cwd=root)
            self.decision("guard-file-edit.py", {"file_path": "../outside.txt"}, "deny", cwd=root)
            self.decision("guard-file-edit.py", {"file_path": "/tmp/outside.txt"}, "deny", cwd=root)
            self.decision("guard-file-edit.py", "{bad", "deny", cwd=root, raw=True)

    def test_mcp_and_subagent_guards(self) -> None:
        self.decision("guard-mcp.py", {"command": "github read issue"}, "ask")
        self.decision("guard-mcp.py", {"command": "github delete release"}, "deny")
        self.decision("guard-subagent.py", {"agent_name": "mobile-security-reviewer", "prompt": "edit the file"}, "deny")
        self.decision("guard-subagent.py", {"agent_name": "android-engineer", "prompt": "inspect Android files"}, "allow")


if __name__ == "__main__":
    unittest.main()
