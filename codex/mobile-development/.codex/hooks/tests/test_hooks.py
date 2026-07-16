from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


HOOK_DIR = Path(__file__).resolve().parents[1]


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


def pre(tool: str, tool_input: dict[str, object]) -> dict[str, object]:
    return {"hook_event_name": "PreToolUse", "tool_name": tool, "tool_input": tool_input}


def post(tool: str, tool_input: dict[str, object]) -> dict[str, object]:
    return {"hook_event_name": "PostToolUse", "tool_name": tool, "tool_input": tool_input}


class CodexHookTests(unittest.TestCase):
    def assert_allows(self, script: str, payload: object) -> None:
        result = run_hook(script, payload)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")

    def assert_denies(self, script: str, payload: object, *, raw: bool = False) -> str:
        result = run_hook(script, payload, raw=raw)
        self.assertEqual(result.returncode, 0, result.stderr)
        body = json.loads(result.stdout)
        output = body.get("hookSpecificOutput", body)
        reason = output.get("permissionDecisionReason") or output.get("reason") or output.get("stopReason")
        self.assertTrue(reason)
        return str(reason)

    def test_hook_config_uses_native_events_and_bounded_timeouts(self) -> None:
        config = json.loads((HOOK_DIR.parent / "hooks.json").read_text())
        self.assertIn("UserPromptSubmit", config["hooks"])
        self.assertIn("PreToolUse", config["hooks"])
        self.assertIn("PostToolUse", config["hooks"])
        for groups in config["hooks"].values():
            for group in groups:
                for hook in group["hooks"]:
                    self.assertGreater(hook["timeout"], 0)
                    self.assertLessEqual(hook["timeout"], 30)

    def test_mobile_command_guard_blocks_destructive_device_actions(self) -> None:
        blocked = [
            "adb reboot bootloader",
            "adb shell pm clear com.example.app",
            "fastboot flash boot boot.img",
            "emulator -wipe-data",
            "avdmanager delete avd --name Pixel",
            "xcrun simctl erase all",
            "ideviceerase",
        ]
        for command in blocked:
            with self.subTest(command=command):
                self.assert_denies("mobile-command-guard.py", pre("Bash", {"command": command}))

    def test_mobile_command_guard_allows_safe_examples_and_fails_closed(self) -> None:
        for command in ("./gradlew test", "xcrun simctl list devices", "flutter test"):
            self.assert_allows("mobile-command-guard.py", pre("Bash", {"command": command}))
        self.assert_denies("mobile-command-guard.py", "{bad", raw=True)
        self.assert_denies("mobile-command-guard.py", pre("Bash", {}))

    def test_release_guard_blocks_signing_publication_and_upload(self) -> None:
        blocked = [
            "apksigner sign app.apk",
            "./gradlew bundleRelease",
            "xcodebuild archive -scheme App",
            "xcrun notarytool submit App.zip",
            "fastlane deliver",
            "flutter build ipa",
            "npm publish",
            "eas submit --platform ios",
            "firebase deploy",
            "gh release upload v1 app.apk",
            "sentry-cli releases files 1 upload-sourcemaps build",
        ]
        for command in blocked:
            with self.subTest(command=command):
                self.assert_denies("release-permission-guard.py", pre("Bash", {"command": command}))
        self.assert_allows("release-permission-guard.py", pre("Bash", {"command": "./gradlew test"}))

    def test_secret_guard_blocks_real_secrets_but_allows_placeholders_and_public_clients(self) -> None:
        patch = "*** Add File: src/Config.kt\n+val token = \"ghp_abcdefghijklmnopqrstuvwxyz1234567890\"\n"
        self.assert_denies("prompt-secret-guard.py", pre("apply_patch", {"command": patch}))
        placeholder = "*** Add File: README.md\n+API_KEY=${OPENAI_API_KEY}\n+token=YOUR_ACCESS_TOKEN\n"
        self.assert_allows("prompt-secret-guard.py", pre("apply_patch", {"command": placeholder}))
        public_google = "*** Add File: google-services.json\n+{\"current_key\":\"AIzaSyDUMMYEXAMPLEPLACEHOLDER123456789\"}\n"
        self.assert_allows("prompt-secret-guard.py", pre("apply_patch", {"command": public_google}))
        self.assert_denies("prompt-secret-guard.py", {"hook_event_name": "UserPromptSubmit"}, raw=False)

    def test_sensitive_change_guard_stops_for_mobile_security_changes(self) -> None:
        patch = "*** Update File: AndroidManifest.xml\n+<uses-permission android:name=\"android.permission.CAMERA\" />\n"
        result = run_hook("sensitive-change-guard.py", post("apply_patch", {"command": patch}))
        self.assertEqual(result.returncode, 0)
        body = json.loads(result.stdout)
        self.assertIs(body["continue"], False)
        self.assertIn("AndroidManifest.xml", body["stopReason"])


if __name__ == "__main__":
    unittest.main()
