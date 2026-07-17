#!/usr/bin/env python3
"""Deterministic policy tests plus bounded contract tests for Claude Code hooks."""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from typing import Any, Dict, Optional, Tuple


HOOK_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HOOK_DIR))

from hook_common import HookInputError, normalize_target, protected_path_reason  # noqa: E402


POSIX_ROOT = "/tmp/mobile project"
WINDOWS_ROOT = r"C:\repo\mobile project"
CONTRACT_TIMEOUT_SECONDS = 2


def load_hook_module(filename: str, module_name: str) -> Any:
    spec = importlib.util.spec_from_file_location(module_name, HOOK_DIR / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load hook module: {filename}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


dangerous_hook = load_hook_module(
    "dangerous-mobile-command-guard.py", "dangerous_mobile_command_guard"
)
release_hook = load_hook_module(
    "release-signing-publishing-guard.py", "release_signing_publishing_guard"
)
secret_hook = load_hook_module(
    "secret-and-protected-file-guard.py", "secret_and_protected_file_guard"
)
sensitive_hook = load_hook_module("sensitive-change-review.py", "sensitive_change_review")


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
        timeout=CONTRACT_TIMEOUT_SECONDS,
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


class HookContractTestCase(unittest.TestCase):
    def assert_contract_safe(
        self, script: str, payload: Dict[str, Any], *, root: str = POSIX_ROOT
    ) -> None:
        result, parsed = run_hook(script, payload, root=root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIsNone(parsed, result.stdout)

    def assert_contract_decision(
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

    def assert_contract_context(self, payload: Any, *, raw: bool = False) -> str:
        result, parsed = run_hook("sensitive-change-review.py", payload, raw=raw)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIsNotNone(parsed, result.stdout)
        output = parsed["hookSpecificOutput"]
        self.assertEqual(output["hookEventName"], "PostToolUse")
        self.assertTrue(output["additionalContext"])
        return output["additionalContext"]


class ProtectedPathPolicyTests(unittest.TestCase):
    def assert_file_safe(
        self,
        tool_name: str,
        path: str,
        *,
        root: str = POSIX_ROOT,
        cwd: str = POSIX_ROOT,
    ) -> None:
        self.assertIsNone(
            secret_hook.file_access_reason(tool_name, {"file_path": path}, root, cwd)
        )

    def assert_file_blocked(
        self,
        tool_name: str,
        path: str,
        *,
        root: str = POSIX_ROOT,
        cwd: str = POSIX_ROOT,
    ) -> str:
        reason = secret_hook.file_access_reason(tool_name, {"file_path": path}, root, cwd)
        self.assertIsNotNone(reason)
        return reason

    def test_allows_public_mobile_clients_and_environment_templates(self) -> None:
        for filename in (
            "google-services.json",
            "GoogleService-Info.plist",
            ".env.example",
            ".env.production.template",
            ".env.sample",
        ):
            with self.subTest(filename=filename):
                self.assertIsNone(protected_path_reason(filename))
                self.assert_file_safe("Read", f"{POSIX_ROOT}/{filename}")

    def test_blocks_private_signing_and_service_account_material(self) -> None:
        cases = (
            ".env",
            ".env.production",
            ".envrc",
            "config/credentials.yaml",
            "config/secrets.properties",
            "keys/Release Key.p12",
            "keys/AuthKey_TEST.p8",
            "config/service-account-prod.json",
            "firebase-adminsdk-prod.json",
            ".ssh/id_ed25519",
            ".docker/config.json",
            ".config/gcloud/application_default_credentials.json",
        )
        for relative in cases:
            with self.subTest(relative=relative):
                self.assert_file_blocked("Read", f"{POSIX_ROOT}/{relative}")

    def test_blocks_command_references_without_mocking_shell_policy(self) -> None:
        cases = (
            ('cat "keys/Release Key.p12"', True),
            ("cat .env*", True),
            ("echo '-----BEGIN PRIVATE KEY-----'", True),
            (r'Get-Content "C:\repo\mobile project\config\secrets.yaml"', False),
            ("cat \x00.env", True),
        )
        for command, posix in cases:
            with self.subTest(command=command):
                self.assertIsNotNone(
                    secret_hook.command_protected_reason(command, posix=posix)
                )

    def test_handles_posix_windows_unc_traversal_outside_and_nul_paths(self) -> None:
        self.assert_file_blocked("Edit", "src/../../outside.txt")
        self.assert_file_blocked("Write", "/tmp/outside.txt")
        self.assert_file_safe(
            "Read",
            WINDOWS_ROOT + r"\src\main.kt",
            root=WINDOWS_ROOT,
            cwd=WINDOWS_ROOT,
        )
        self.assert_file_blocked(
            "Read",
            r"C:\Users\name\.ssh\id_rsa",
            root=WINDOWS_ROOT,
            cwd=WINDOWS_ROOT,
        )
        unc_target = normalize_target(r"\\server\share\.ssh\id_rsa", WINDOWS_ROOT, cwd=WINDOWS_ROOT)
        self.assertFalse(unc_target.within_root)
        with self.assertRaises(HookInputError):
            normalize_target("src/main.kt\x00", POSIX_ROOT, cwd=POSIX_ROOT)

    def test_missing_fields_and_unsupported_tools_fail_closed_in_policy(self) -> None:
        with self.assertRaises(HookInputError):
            secret_hook.file_access_reason("Read", {}, POSIX_ROOT, POSIX_ROOT)
        with self.assertRaises(HookInputError):
            secret_hook.file_access_reason("Task", {"file_path": "src/main.kt"}, POSIX_ROOT, POSIX_ROOT)


class DangerousCommandPolicyTests(unittest.TestCase):
    def assert_command_safe(
        self,
        command: str,
        *,
        shell_tool: str = "Bash",
        root: str = POSIX_ROOT,
        cwd: str = POSIX_ROOT,
    ) -> None:
        self.assertIsNone(
            dangerous_hook.shell_command_reason(shell_tool, {"command": command}, root, cwd)
        )

    def assert_command_blocked(
        self,
        command: str,
        *,
        shell_tool: str = "Bash",
        root: str = POSIX_ROOT,
        cwd: str = POSIX_ROOT,
    ) -> str:
        reason = dangerous_hook.shell_command_reason(shell_tool, {"command": command}, root, cwd)
        self.assertIsNotNone(reason)
        return reason

    def test_allows_safe_read_build_test_lint_and_generated_cleanup(self) -> None:
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
            "rm -rf build android/build",
            "git status --short",
            "git --no-pager log -1",
            "grep -R 'rm -rf' docs",
            "defaults read com.apple.dt.Xcode",
            "adb shell getprop ro.build.version.sdk",
            "xcrun simctl list devices",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assert_command_safe(command)

    def test_validates_chaining_pipes_redirection_substitution_and_encoded_execution(self) -> None:
        blocked = (
            "./gradlew test && rm -rf src",
            "printf ZWNobyBoaQ== | base64 --decode | sh",
            "echo data > /tmp/outside.txt",
            "cat < ../secret.txt",
            "cat <<EOF",
            "echo $(rm -rf src)",
            "echo `git reset --hard`",
            "cat $'.env'",
            "python3 -c 'import os; os.remove(\"src/main.kt\")'",
            "node -p 'process.version'",
            "powershell -EncodedCommand ZQBjAGgAbwA=",
            "env -S 'rm -rf src'",
            "stdbuf -o L rm -rf src",
            "cd - && rm -rf src",
            "PATH=tools ./gradlew test",
        )
        for command in blocked:
            with self.subTest(command=command):
                self.assert_command_blocked(command)
        self.assert_command_safe('echo ok > "build/Test Results.txt"')
        self.assert_command_safe("./gradlew test 2>/dev/null")

    def test_blocks_scope_escape_destructive_git_filesystem_and_privilege_escalation(self) -> None:
        commands = (
            "cd .. && ./gradlew test",
            "rm -rf src",
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
            "sudo ./gradlew test",
            "chmod 777 gradlew",
            "chown user src/main.kt",
            "killall Simulator",
            "truncate -s 0 src/main.kt",
            "unlink src/main.kt",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assert_command_blocked(command)

    def test_blocks_package_install_device_system_and_external_mutation(self) -> None:
        commands = (
            "npm install",
            "pnpm add @scope/pkg",
            "yarn add react-native",
            "bun install",
            "pod install",
            "python3 -m pip install requests",
            "defaults write com.example Flag true",
            "plutil -replace NSCameraUsageDescription -string Camera ios/Info.plist",
            "adb shell pm clear com.example.app",
            "xcrun simctl erase all",
            "avdmanager delete avd --name Test",
            "sdkmanager --uninstall 'platforms;android-35'",
            "ssh example.com rm -rf app",
            "docker prune -f",
            "kubectl delete pod app",
            "terraform apply",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assert_command_blocked(command)

    def test_handles_powershell_cleanup_scope_and_provider_blocks(self) -> None:
        self.assert_command_safe(
            r".\gradlew test", shell_tool="PowerShell", root=WINDOWS_ROOT, cwd=WINDOWS_ROOT
        )
        self.assert_command_safe(
            "Remove-Item -Recurse build",
            shell_tool="PowerShell",
            root=WINDOWS_ROOT,
            cwd=WINDOWS_ROOT,
        )
        for command in (
            "Remove-Item -Recurse src",
            "git reset --hard HEAD",
            "Invoke-Expression 'git status'",
            "Get-ChildItem Env:",
        ):
            with self.subTest(command=command):
                self.assert_command_blocked(
                    command, shell_tool="PowerShell", root=WINDOWS_ROOT, cwd=WINDOWS_ROOT
                )

    def test_malformed_missing_unsupported_and_out_of_workspace_payloads_fail_closed(self) -> None:
        with self.assertRaises(HookInputError):
            dangerous_hook.shell_command_reason("Bash", {}, POSIX_ROOT, POSIX_ROOT)
        with self.assertRaises(HookInputError):
            dangerous_hook.shell_command_reason("Read", {"command": "cat README.md"}, POSIX_ROOT, POSIX_ROOT)
        self.assert_command_blocked("echo 'unterminated")
        self.assert_command_blocked("echo hi", cwd="/tmp/outside")
        self.assert_command_blocked("echo \x00hi")


class ReleasePolicyTests(unittest.TestCase):
    def assert_release_safe(self, command: str) -> None:
        self.assertIsNone(release_hook.release_decision(command))

    def assert_release_decision(self, command: str, expected: str) -> str:
        decision = release_hook.release_decision(command)
        self.assertIsNotNone(decision)
        mode, reason = decision
        self.assertEqual(mode, expected)
        self.assertTrue(reason)
        return reason

    def test_allows_non_release_commands(self) -> None:
        for command in (
            "./gradlew assembleDebug",
            "xcodebuild test -scheme App",
            "flutter build apk --debug",
            "xcodebuild test -scheme App -destination 'platform=iOS Simulator,name=iPhone 15'",
        ):
            with self.subTest(command=command):
                self.assert_release_safe(command)

    def test_asks_for_non_publishing_release_preparation(self) -> None:
        commands = (
            "./gradlew bundleRelease",
            "./gradlew :app:assembleProdRelease",
            "xcodebuild archive -scheme App CODE_SIGNING_ALLOWED=NO",
            "xcodebuild build -configuration Release CODE_SIGNING_ALLOWED=NO",
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
                self.assert_release_decision(command, "ask")

    def test_blocks_signing_credentials_publication_upload_distribution_and_deployment(self) -> None:
        commands = (
            "codesign --sign Developer_ID App.app",
            "jarsigner app.jar release-key",
            "xcodebuild archive -scheme App",
            "xcodebuild build -configuration Release",
            "xcodebuild build -sdk iphoneos",
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
            "fastlane firebase_app_distribution",
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
            "Import-PfxCertificate -FilePath cert.pfx",
            "rsync app.apk user@example.com:/releases/",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assert_release_decision(command, "deny")

    def test_release_guard_blocks_malformed_substitution_multiline_and_nul(self) -> None:
        for command in (
            "echo $(fastlane deliver)",
            "npm publish\nnpm test",
            "npm publish\x00",
        ):
            with self.subTest(command=command):
                self.assert_release_decision(command, "deny")


class SensitiveChangePolicyTests(unittest.TestCase):
    def assert_reviews(self, relative: str, text: str, *expected: str) -> None:
        reviews = sensitive_hook.review_requirements(relative, text)
        for reviewer in expected:
            self.assertIn(reviewer, reviews)

    def test_requests_android_ios_dependency_webview_and_signing_reviews(self) -> None:
        self.assert_reviews(
            "android/app/src/main/AndroidManifest.xml",
            '<uses-permission android:name="android.permission.CAMERA" />',
            "android-engineer",
            "mobile-security-reviewer",
            "mobile-release-engineer",
        )
        self.assert_reviews(
            "pubspec.lock", "packages: {}", "mobile-security-reviewer", "mobile-code-reviewer"
        )
        self.assert_reviews(
            "src/Browser.tsx",
            "<WebView javaScriptEnabled originWhitelist={['*']} />",
            "mobile-security-reviewer",
            "mobile-ui-accessibility-reviewer",
        )
        self.assert_reviews(
            "android/app/build.gradle.kts",
            'implementation("com.example:library:1.0")',
            "mobile-security-reviewer",
            "mobile-release-engineer",
        )
        self.assert_reviews(
            "ios/Release.xcconfig",
            "CODE_SIGN_IDENTITY = Apple Distribution",
            "mobile-security-reviewer",
            "mobile-release-engineer",
        )

    def test_ignores_harmless_filename_only_change(self) -> None:
        self.assertFalse(
            sensitive_hook.review_requirements(
                "ios/App/Info.plist",
                "<string>Old Name</string>\n<string>New Name</string>",
            )
        )

    def test_changed_text_is_bounded_and_uses_supported_payload_fields(self) -> None:
        payload = {
            "file_path": "src/Main.kt",
            "old_string": "old",
            "new_string": "new",
            "ignored": "x" * 300_000,
        }
        self.assertEqual(sensitive_hook.changed_text(payload), "old\nnew")


class HookExecutableContractTests(HookContractTestCase):
    def test_protected_file_guard_contract_for_safe_deny_and_malformed_json(self) -> None:
        self.assert_contract_safe(
            "secret-and-protected-file-guard.py",
            pretool("Read", {"file_path": f"{POSIX_ROOT}/google-services.json"}),
        )
        self.assert_contract_decision(
            "secret-and-protected-file-guard.py",
            pretool("Read", {"file_path": f"{POSIX_ROOT}/.env.production"}),
            "deny",
        )
        self.assert_contract_decision(
            "secret-and-protected-file-guard.py", "{not json", "deny", raw=True
        )

    def test_dangerous_command_guard_contract_for_safe_deny_and_missing_command(self) -> None:
        self.assert_contract_safe(
            "dangerous-mobile-command-guard.py",
            pretool("Bash", {"command": "./gradlew test"}),
        )
        self.assert_contract_decision(
            "dangerous-mobile-command-guard.py",
            pretool("Bash", {"command": "rm -rf src"}),
            "deny",
        )
        self.assert_contract_decision(
            "dangerous-mobile-command-guard.py", pretool("Bash", {}), "deny"
        )

    def test_release_guard_contract_for_safe_ask_deny_and_malformed_input(self) -> None:
        self.assert_contract_safe(
            "release-signing-publishing-guard.py",
            pretool("Bash", {"command": "./gradlew assembleDebug"}),
        )
        self.assert_contract_decision(
            "release-signing-publishing-guard.py",
            pretool("Bash", {"command": "./gradlew bundleRelease"}),
            "ask",
        )
        self.assert_contract_decision(
            "release-signing-publishing-guard.py",
            pretool("Bash", {"command": "fastlane deliver"}),
            "deny",
        )
        self.assert_contract_decision(
            "release-signing-publishing-guard.py", "null", "deny", raw=True
        )

    def test_sensitive_change_contract_for_context_safe_and_malformed_json(self) -> None:
        context = self.assert_contract_context(
            posttool(
                "Edit",
                {
                    "file_path": f"{POSIX_ROOT}/android/app/src/main/AndroidManifest.xml",
                    "old_string": "",
                    "new_string": '<uses-permission android:name="android.permission.CAMERA" />',
                },
            )
        )
        self.assertIn("mobile-security-reviewer", context)
        self.assert_contract_safe(
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
        malformed = self.assert_contract_context("{not-json", raw=True)
        self.assertIn("failed safely", malformed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
