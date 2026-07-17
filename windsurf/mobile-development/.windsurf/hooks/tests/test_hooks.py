from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


HOOK_DIR = Path(__file__).resolve().parents[1]


def run_hook(
    name: str,
    payload: object,
    cwd: Path | None = None,
    *,
    raw: bool = False,
) -> subprocess.CompletedProcess[str]:
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


def missing_command_payload() -> dict[str, object]:
    return {"agent_action_name": "pre_run_command", "tool_info": {}}


def write_payload(path: str, text: str = "") -> dict[str, object]:
    return {
        "agent_action_name": "pre_write_code",
        "tool_info": {"file_path": path, "edits": [{"new_string": text}]},
    }


class WindsurfHookTests(unittest.TestCase):
    def assert_allows(self, script: str, payload: object, cwd: Path | None = None) -> None:
        result = run_hook(script, payload, cwd)
        self.assertEqual(result.returncode, 0, result.stderr)

    def assert_blocks(
        self,
        script: str,
        payload: object,
        cwd: Path | None = None,
        *,
        raw: bool = False,
    ) -> str:
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
            "xcodebuild archive -scheme App",
            "xcodebuild -exportArchive -archivePath App.xcarchive",
            "notarytool submit App.zip",
            "altool --upload-app -f App.ipa",
            "codesign --sign Developer App.app",
            "security import certificate.p12",
            "./gradlew publishReleaseBundle",
            "./gradlew appDistributionUploadRelease",
            "flutter build ipa --release",
            "eas build --platform ios",
            "eas submit --platform android",
            "eas update --branch production",
            "firebase appdistribution:distribute app.apk",
            "appcenter distribute release",
            "sentry-cli releases files 1 upload-sourcemaps build",
            "npm publish",
            "gh release upload v1 app.apk",
            "npm install left-pad",
            "echo ok > file",
            "printf x | sh",
            "echo $(cat .env)",
            "echo %3B rm -rf src",
            "powershell -enc ZQBjAGgAbwA=",
        ]
        for command in commands:
            with self.subTest(command=command):
                self.assert_blocks("command_guard.py", command_payload(command))
        self.assert_blocks("command_guard.py", "{bad", raw=True)
        self.assert_blocks("command_guard.py", missing_command_payload())

    def test_command_guard_blocks_fastlane_release_and_store_actions(self) -> None:
        commands = [
            "fastlane deliver",
            "fastlane pilot",
            "fastlane supply",
            "fastlane precheck",
            "fastlane match",
            "fastlane sigh",
            "fastlane cert",
            "fastlane pem",
            "fastlane produce",
            "fastlane upload_to_app_store",
            "fastlane upload_to_play_store",
            "fastlane upload_symbols_to_crashlytics",
            "fastlane run deliver",
            "fastlane run pilot",
            "fastlane run supply",
            "fastlane run upload_to_app_store",
            "fastlane run upload_to_play_store",
            "bundle exec fastlane deliver",
            "./bin/fastlane deliver",
            "/usr/local/bin/fastlane deliver",
            "'./bin/fastlane' deliver",
            '"./bin/fastlane" upload_to_app_store',
            "fastlane production_release",
            "fastlane submit_to_app_store",
            "fastlane publish_to_play_store",
            "fastlane distribute_beta",
        ]
        for command in commands:
            with self.subTest(command=command):
                self.assert_blocks("command_guard.py", command_payload(command))

    def test_command_guard_allows_safe_validation_examples(self) -> None:
        for command in (
            "python3 -m unittest discover",
            "./gradlew test",
            "./gradlew lint",
            "flutter test",
            "flutter analyze",
            "fastlane --version",
            "fastlane lanes",
            "fastlane scan",
            "bundle exec fastlane scan",
        ):
            self.assert_allows("command_guard.py", command_payload(command))

    def test_scope_guard_blocks_traversal_outside_and_protected_paths(self) -> None:
        with tempfile.TemporaryDirectory(dir=HOOK_DIR.parents[1]) as tmp:
            root = Path(tmp)
            for path in ("../outside.txt", "/tmp/outside.txt", ".git/config", ".ssh/id_rsa"):
                with self.subTest(path=path):
                    self.assert_blocks("scope_guard.py", write_payload(path), root)
            self.assert_allows("scope_guard.py", write_payload("src/main.kt"), root)
            self.assert_blocks("scope_guard.py", "{bad", root, raw=True)

    def test_secret_guard_blocks_secrets_and_allows_public_clients(self) -> None:
        self.assert_blocks(
            "secret_guard.py",
            write_payload(".env", "OPENAI_API_KEY=realistic-secret-value"),
        )
        self.assert_blocks(
            "secret_guard.py",
            write_payload("src/Config.kt", 'api_key="realistic-secret-value"'),
        )
        self.assert_blocks(
            "secret_guard.py",
            write_payload("src/key.pem", "-----BEGIN PRIVATE KEY-----"),
        )
        self.assert_allows(
            "secret_guard.py",
            write_payload("README.md", "API_KEY=${OPENAI_API_KEY}\nTOKEN=YOUR_ACCESS_TOKEN"),
        )
        self.assert_allows(
            "secret_guard.py",
            write_payload(
                "google-services.json",
                '{"current_key":"AIzaSyDUMMYEXAMPLEPLACEHOLDER123456789"}',
            ),
        )
        self.assert_allows(
            "secret_guard.py",
            write_payload(
                "GoogleService-Info.plist",
                "<key>API_KEY</key><string>YOUR_API_KEY</string>",
            ),
        )

    def test_mcp_guard_fails_closed_for_mcp_and_malformed_json(self) -> None:
        self.assert_blocks(
            "mcp_guard.py",
            {
                "agent_action_name": "pre_mcp_tool_use",
                "tool_info": {
                    "mcp_server_name": "github",
                    "mcp_tool_name": "read_issue",
                },
            },
        )
        self.assert_blocks("mcp_guard.py", "{bad", raw=True)


if __name__ == "__main__":
    unittest.main()
