#!/usr/bin/env python3
"""Focused tests for deterministic mobile-development Claude Code hooks."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from typing import Any, Dict, Optional, Tuple


HOOK_DIR = Path(__file__).resolve().parents[1]
POSIX_ROOT = "/tmp/mobile project"
WINDOWS_ROOT = r"C:\repo\mobile project"


def run_hook(
    script: str,
    payload: Any,
    *,
    root: str = POSIX_ROOT,
    raw: bool = False,
) -> Tuple[subprocess.CompletedProcess[str], Optional[Dict[str, Any]]]:
    input_text = payload if raw else json.dumps(payload)
    environment = os.environ.copy()
    environment["CLAUDE_PROJECT_DIR"] = root
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        [sys.executable, "-B", str(HOOK_DIR / script)],
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
        env=environment,
        timeout=5,
    )
    parsed = json.loads(result.stdout) if result.stdout else None
    return result, parsed


def pretool(tool: str, tool_payload: Dict[str, Any], *, cwd: str = POSIX_ROOT) -> Dict[str, Any]:
    return {
        "session_id": "test",
        "cwd": cwd,
        "hook_event_name": "PreToolUse",
        "tool_name": tool,
        "tool_input": tool_payload,
    }


def posttool(tool: str, tool_payload: Dict[str, Any], *, cwd: str = POSIX_ROOT) -> Dict[str, Any]:
    return {
        "session_id": "test",
        "cwd": cwd,
        "hook_event_name": "PostToolUse",
        "tool_name": tool,
        "tool_input": tool_payload,
        "tool_response": {"success": True},
    }


class HookTestCase(unittest.TestCase):
    def assert_safe(self, script: str, payload: Dict[str, Any], *, root: str = POSIX_ROOT) -> None:
        result, parsed = run_hook(script, payload, root=root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIsNone(parsed, result.stdout)

    def assert_decision(
        self,
        script: str,
        payload: Any,
        expected: str,
        *,
        root: str = POSIX_ROOT,
        raw: bool = False,
    ) -> str:
        result, parsed = run_hook(script, payload, root=root, raw=raw)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIsNotNone(parsed, result.stdout)
        output = parsed["hookSpecificOutput"]
        self.assertEqual(output["hookEventName"], "PreToolUse")
        self.assertEqual(output["permissionDecision"], expected)
        self.assertTrue(output["permissionDecisionReason"])
        return output["permissionDecisionReason"]

    def assert_context(self, payload: Any, *, raw: bool = False) -> str:
        result, parsed = run_hook("sensitive-change-review.py", payload, raw=raw)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIsNotNone(parsed, result.stdout)
        output = parsed["hookSpecificOutput"]
        self.assertEqual(output["hookEventName"], "PostToolUse")
        self.assertTrue(output["additionalContext"])
        return output["additionalContext"]


class ProtectedFileGuardTests(HookTestCase):
    SCRIPT = "secret-and-protected-file-guard.py"

    def test_allows_public_mobile_client_configuration(self) -> None:
        for filename in ("google-services.json", "GoogleService-Info.plist"):
            with self.subTest(filename=filename):
                self.assert_safe(self.SCRIPT, pretool("Read", {"file_path": f"{POSIX_ROOT}/{filename}"}))

    def test_allows_public_environment_templates(self) -> None:
        for filename in (".env.example", ".env.production.template", ".env.sample"):
            with self.subTest(filename=filename):
                self.assert_safe(self.SCRIPT, pretool("Read", {"file_path": f"{POSIX_ROOT}/{filename}"}))

    def test_blocks_private_and_signing_material(self) -> None:
        cases = (
            ".env",
            ".env.production",
            ".envrc",
            "config/credentials.yaml",
            "config/secrets.properties",
            "keys/Release Key.p12",
            "keys/AuthKey_TEST.p8",
            "config/service-account-prod.json",
            ".ssh/id_ed25519",
            ".docker/config.json",
            ".config/gcloud/application_default_credentials.json",
        )
        for relative in cases:
            with self.subTest(relative=relative):
                self.assert_decision(
                    self.SCRIPT,
                    pretool("Read", {"file_path": f"{POSIX_ROOT}/{relative}"}),
                    "deny",
                )

    def test_blocks_quoted_protected_path_with_spaces_in_bash(self) -> None:
        self.assert_decision(
            self.SCRIPT,
            pretool("Bash", {"command": 'cat "keys/Release Key.p12"'}),
            "deny",
        )
        self.assert_decision(
            self.SCRIPT,
            pretool("Bash", {"command": "cat .env*"}),
            "deny",
        )

    def test_blocks_protected_path_in_powershell(self) -> None:
        self.assert_decision(
            self.SCRIPT,
            pretool("PowerShell", {"command": r'Get-Content "C:\repo\mobile project\config\secrets.yaml"'}, cwd=WINDOWS_ROOT),
            "deny",
            root=WINDOWS_ROOT,
        )

    def test_blocks_posix_path_traversal_and_outside_path(self) -> None:
        self.assert_decision(
            self.SCRIPT,
            pretool("Edit", {"file_path": "src/../../outside.txt"}),
            "deny",
        )
        self.assert_decision(
            self.SCRIPT,
            pretool("Write", {"file_path": "/tmp/outside.txt"}),
            "deny",
        )

    def test_handles_windows_paths(self) -> None:
        self.assert_safe(
            self.SCRIPT,
            pretool("Read", {"file_path": WINDOWS_ROOT + r"\src\main.kt"}, cwd=WINDOWS_ROOT),
            root=WINDOWS_ROOT,
        )
        self.assert_decision(
            self.SCRIPT,
            pretool("Read", {"file_path": r"C:\Users\name\.ssh\id_rsa"}, cwd=WINDOWS_ROOT),
            "deny",
            root=WINDOWS_ROOT,
        )

    def test_fails_closed_for_malformed_or_missing_input(self) -> None:
        self.assert_decision(self.SCRIPT, "{not json", "deny", raw=True)
        self.assert_decision(
            self.SCRIPT,
            {"hook_event_name": "PreToolUse", "tool_name": "Read", "tool_input": {}},
            "deny",
        )


class DangerousCommandGuardTests(HookTestCase):
    SCRIPT = "dangerous-mobile-command-guard.py"

    def test_allows_scoped_build_test_lint_and_clean_commands(self) -> None:
        commands = (
            "./gradlew test lint",
            "FOO=1 ./gradlew test",
            "./gradlew test -Pendpoint=https://example.com",
            "./gradlew clean",
            "xcodebuild clean -scheme App",
            "flutter analyze",
            "npm run test",
            "python3 -m pytest -c pyproject.toml",
            "./gradlew test && ./gradlew lint",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assert_safe(self.SCRIPT, pretool("Bash", {"command": command}))

    def test_allows_generated_output_cleanup_only(self) -> None:
        self.assert_safe(self.SCRIPT, pretool("Bash", {"command": "rm -rf build android/build"}))
        self.assert_decision(
            self.SCRIPT,
            pretool("Bash", {"command": "rm -rf src"}),
            "deny",
        )

    def test_blocks_destructive_command_inside_chain(self) -> None:
        self.assert_decision(
            self.SCRIPT,
            pretool("Bash", {"command": "./gradlew test && rm -rf src"}),
            "deny",
        )

    def test_validates_redirection_targets(self) -> None:
        self.assert_safe(
            self.SCRIPT,
            pretool("Bash", {"command": 'echo ok > "build/Test Results.txt"'}),
        )
        self.assert_safe(
            self.SCRIPT,
            pretool("Bash", {"command": "./gradlew test 2>/dev/null"}),
        )
        self.assert_decision(
            self.SCRIPT,
            pretool("Bash", {"command": "echo data > /tmp/outside.txt"}),
            "deny",
        )

    def test_blocks_substitution_encoded_and_inline_execution(self) -> None:
        commands = (
            "echo $(rm -rf src)",
            "echo `git reset --hard`",
            "cat $'.env'",
            "printf ZWNobyBoaQ== | base64 --decode | sh",
            "python3 -c 'import os; os.remove(\"src/main.kt\")'",
            "node -p 'process.version'",
            "powershell -EncodedCommand ZQBjAGgAbwA=",
            "env -S 'rm -rf src'",
            "stdbuf -o L rm -rf src",
            "cd - && rm -rf src",
            "FOO=1 rm -rf src",
            "PATH=tools ./gradlew test",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assert_decision(self.SCRIPT, pretool("Bash", {"command": command}), "deny")

    def test_blocks_scope_escape_and_destructive_git(self) -> None:
        commands = (
            "cd .. && ./gradlew test",
            "git reset --hard HEAD",
            "git clean -fdx",
            "git rm src/main.kt",
            "git checkout README.md",
            "git -c alias.wipe='!rm -rf src' wipe",
            "git push origin :main",
            "git remote set-url origin https://example.com/repository.git",
            "git merge --abort",
            "git push --force origin main",
            "find . -delete",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assert_decision(self.SCRIPT, pretool("Bash", {"command": command}), "deny")

    def test_allows_read_only_git_and_false_positive_text(self) -> None:
        self.assert_safe(self.SCRIPT, pretool("Bash", {"command": "git status --short"}))
        self.assert_safe(self.SCRIPT, pretool("Bash", {"command": "git --no-pager log -1"}))
        self.assert_safe(self.SCRIPT, pretool("Bash", {"command": "grep -R 'rm -rf' docs"}))

    def test_allows_read_only_platform_inspection(self) -> None:
        commands = (
            "defaults read com.apple.dt.Xcode",
            "adb shell getprop ro.build.version.sdk",
            "xcrun simctl list devices",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assert_safe(self.SCRIPT, pretool("Bash", {"command": command}))

    def test_blocks_system_and_device_destructive_operations(self) -> None:
        commands = (
            "truncate -s 0 src/main.kt",
            "unlink src/main.kt",
            "defaults write com.example Flag true",
            "plutil -replace NSCameraUsageDescription -string Camera ios/Info.plist",
            "adb shell pm clear com.example.app",
            "xcrun simctl erase all",
            "avdmanager delete avd --name Test",
            "sdkmanager --uninstall 'platforms;android-35'",
            "ssh example.com rm -rf app",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assert_decision(self.SCRIPT, pretool("Bash", {"command": command}), "deny")

    def test_handles_powershell_commands_without_weakening_cleanup_scope(self) -> None:
        self.assert_safe(
            self.SCRIPT,
            pretool("PowerShell", {"command": r".\gradlew test"}, cwd=WINDOWS_ROOT),
            root=WINDOWS_ROOT,
        )
        self.assert_safe(
            self.SCRIPT,
            pretool("PowerShell", {"command": "Remove-Item -Recurse build"}, cwd=WINDOWS_ROOT),
            root=WINDOWS_ROOT,
        )
        for command in (
            "Remove-Item -Recurse src",
            "git reset --hard HEAD",
            "Invoke-Expression 'git status'",
            "Get-ChildItem Env:",
        ):
            with self.subTest(command=command):
                self.assert_decision(
                    self.SCRIPT,
                    pretool("PowerShell", {"command": command}, cwd=WINDOWS_ROOT),
                    "deny",
                    root=WINDOWS_ROOT,
                )

    def test_fails_closed_for_malformed_or_missing_command(self) -> None:
        self.assert_decision(self.SCRIPT, "[]", "deny", raw=True)
        self.assert_decision(self.SCRIPT, pretool("Bash", {}), "deny")
        self.assert_decision(
            self.SCRIPT,
            pretool("Bash", {"command": "echo 'unterminated"}),
            "deny",
        )


class ReleaseGuardTests(HookTestCase):
    SCRIPT = "release-signing-publishing-guard.py"

    def test_allows_non_release_commands(self) -> None:
        self.assert_safe(self.SCRIPT, pretool("Bash", {"command": "./gradlew assembleDebug"}))
        self.assert_safe(self.SCRIPT, pretool("Bash", {"command": "xcodebuild test -scheme App"}))
        self.assert_safe(self.SCRIPT, pretool("Bash", {"command": "flutter build apk --debug"}))
        self.assert_safe(
            self.SCRIPT,
            pretool(
                "Bash",
                {"command": "xcodebuild test -scheme App -destination 'platform=iOS Simulator,name=iPhone 15'"},
            ),
        )

    def test_asks_for_non_publishing_release_preparation(self) -> None:
        commands = (
            "./gradlew bundleRelease",
            "./gradlew :app:assembleProdRelease",
            "xcodebuild archive -scheme App CODE_SIGNING_ALLOWED=NO",
            "xcodebuild build -configuration Release CODE_SIGNING_ALLOWED=NO",
            "xcodebuild build -configuration='Release' CODE_SIGNING_ALLOWED='NO'",
            "xcodebuild test -destination 'platform=iOS,id=DEVICE' CODE_SIGNING_ALLOWED=NO",
            "flutter build ipa --release --no-codesign",
            "flutter build appbundle",
            "flutter build web",
            "flutter build aar",
            "flutter build bundle",
            "npx react-native bundle --dev false",
            "npx --no-install react-native bundle --dev false",
            "npx expo export",
            "fastlane run build_app skip_codesigning:true",
            "bundletool build-apks --bundle app.aab --output app.apks",
            "xcrun simctl uninstall booted com.example.app",
            "git tag v1.2.3",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assert_decision(self.SCRIPT, pretool("Bash", {"command": command}), "ask")

    def test_blocks_signing_publication_upload_and_deployment(self) -> None:
        commands = (
            "codesign --sign Developer_ID App.app",
            "jarsigner app.jar release-key",
            "xcodebuild archive -scheme App",
            "xcodebuild build -configuration Release",
            "xcodebuild build -sdk iphoneos",
            "xcodebuild build -sdk=iphoneos17.4",
            "xcodebuild build CODE_SIGNING_ALLOWED=YES",
            "xcodebuild test -destination 'platform=iOS,id=DEVICE'",
            "xcodebuild build -allowProvisioningUpdates",
            "xcodebuild -exportArchive -archivePath App.xcarchive",
            "flutter build ipa --release",
            "flutter build ipa --no-codesign=false",
            "flutter build ios --debug",
            "npm publish",
            "npm run release",
            "./gradlew publishReleaseBundle",
            "./gradlew signReleaseBundle",
            "fastlane deliver",
            "fastlane build_app",
            "fastlane upload_to_testflight",
            "bundletool build-apks --bundle app.aab --output app.apks --ks release.jks",
            "productbuild --sign 'Developer ID Installer' App.pkg",
            "eas build --platform ios",
            "npx eas-cli submit --platform android",
            "npx expo publish",
            "firebase appdistribution:distribute app.apk",
            "npx firebase-tools deploy --only hosting",
            "firebase crashlytics:symbols:upload symbols.zip",
            "sentry-cli releases files 1.2.3 upload-sourcemaps build",
            "appcenter codepush release-react -a org/app",
            "shorebird patch android",
            "gh release upload v1 app.apk",
            "curl --upload-file app.apk https://uploads.example.com",
            "curl -F file=@app.apk https://uploads.example.com",
            "Invoke-WebRequest -Method Put -InFile app.apk https://uploads.example.com",
            "security add-generic-password -a user -s service -w value",
            "rsync app.apk user@example.com:/releases/",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assert_decision(self.SCRIPT, pretool("Bash", {"command": command}), "deny")

    def test_enforces_release_boundaries_for_powershell(self) -> None:
        self.assert_decision(
            self.SCRIPT,
            pretool("PowerShell", {"command": "eas build --platform android"}, cwd=WINDOWS_ROOT),
            "deny",
            root=WINDOWS_ROOT,
        )

    def test_fails_closed_for_malformed_input(self) -> None:
        self.assert_decision(self.SCRIPT, "null", "deny", raw=True)
        self.assert_decision(self.SCRIPT, pretool("Bash", {}), "deny")


class SensitiveChangeReviewTests(HookTestCase):
    def test_requests_android_security_and_release_review(self) -> None:
        context = self.assert_context(
            posttool(
                "Edit",
                {
                    "file_path": f"{POSIX_ROOT}/android/app/src/main/AndroidManifest.xml",
                    "old_string": "",
                    "new_string": '<uses-permission android:name="android.permission.CAMERA" />',
                },
            )
        )
        self.assertIn("android-engineer", context)
        self.assertIn("mobile-security-reviewer", context)
        self.assertIn("mobile-release-engineer", context)

    def test_does_not_flag_harmless_filename_only_change(self) -> None:
        self.assert_safe(
            "sensitive-change-review.py",
            posttool(
                "Edit",
                {
                    "file_path": f"{POSIX_ROOT}/ios/App/Info.plist",
                    "old_string": "<string>Old Name</string>",
                    "new_string": "<string>New Name</string>",
                },
            ),
        )

    def test_requests_dependency_and_webview_review(self) -> None:
        dependency_context = self.assert_context(
            posttool(
                "Write",
                {"file_path": f"{POSIX_ROOT}/pubspec.lock", "content": "packages: {}"},
            )
        )
        self.assertIn("mobile-security-reviewer", dependency_context)
        webview_context = self.assert_context(
            posttool(
                "Edit",
                {
                    "file_path": f"{POSIX_ROOT}/src/Browser.tsx",
                    "old_string": "",
                    "new_string": "<WebView javaScriptEnabled originWhitelist={['*']} />",
                },
            )
        )
        self.assertIn("mobile-ui-accessibility-reviewer", webview_context)

    def test_requests_review_for_real_build_and_signing_syntax(self) -> None:
        gradle_context = self.assert_context(
            posttool(
                "Edit",
                {
                    "file_path": f"{POSIX_ROOT}/android/app/build.gradle.kts",
                    "old_string": "",
                    "new_string": 'implementation("com.example:library:1.0")',
                },
            )
        )
        self.assertIn("mobile-security-reviewer", gradle_context)
        self.assertIn("mobile-release-engineer", gradle_context)

        xcode_context = self.assert_context(
            posttool(
                "Edit",
                {
                    "file_path": f"{POSIX_ROOT}/ios/Release.xcconfig",
                    "old_string": "",
                    "new_string": "CODE_SIGN_IDENTITY = Apple Distribution",
                },
            )
        )
        self.assertIn("mobile-security-reviewer", xcode_context)
        self.assertIn("mobile-release-engineer", xcode_context)

    def test_handles_path_traversal_and_malformed_json_safely(self) -> None:
        context = self.assert_context(
            posttool("Edit", {"file_path": "../outside/Info.plist", "new_string": "NSCameraUsageDescription"})
        )
        self.assertIn("unresolved", context)
        malformed = self.assert_context("{not-json", raw=True)
        self.assertIn("failed safely", malformed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
