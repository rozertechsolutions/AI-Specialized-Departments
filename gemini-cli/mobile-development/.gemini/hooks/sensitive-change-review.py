#!/usr/bin/env python3
"""Gemini CLI AfterTool hook that requires review for sensitive mobile changes."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any

MAX_INPUT_BYTES = 1_048_576

RULES: tuple[tuple[str, re.Pattern[str], tuple[str, ...]], ...] = (
    (
        "authentication-or-sensitive-data",
        re.compile(
            r"(?i)\b(?:authorization|bearer|oauth|oidc|access[_-]?token|refresh[_-]?token|"
            r"biometric|keychain|keystore|encryptedsharedpreferences|secure[_-]?storage|"
            r"credential|session[_-]?(?:id|token)|password)\b"
        ),
        ("mobile-security-reviewer",),
    ),
    (
        "permissions-or-entitlements",
        re.compile(
            r"(?i)(?:<uses-permission\b|requestPermissions?\b|permission_handler|"
            r"NS(?:Camera|Microphone|Location|PhotoLibrary|Bluetooth|Contacts|Calendars|"
            r"Motion|FaceID|Health|LocalNetwork).*UsageDescription|com\.apple\.developer\.|"
            r"android:(?:permission|exported|allowBackup|debuggable)\b|fullBackupContent|"
            r"dataExtractionRules|<queries\b|UIBackgroundModes)"
        ),
        ("mobile-security-reviewer", "mobile-ui-accessibility-reviewer"),
    ),
    (
        "network-security",
        re.compile(
            r"(?i)(?:usesCleartextTraffic|cleartextTrafficPermitted|networkSecurityConfig|"
            r"NSAppTransportSecurity|NSAllowsArbitraryLoads|CertificatePinner|TrustManager|"
            r"URLSessionDelegate|http://|setHostnameVerifier|allowsInsecureHttpLoads)"
        ),
        ("mobile-security-reviewer",),
    ),
    (
        "deep-links-or-app-links",
        re.compile(
            r"(?i)(?:<intent-filter\b|android:autoVerify|CFBundleURLTypes|"
            r"com\.apple\.developer\.associated-domains|applinks:|universal\s*link|"
            r"deep\s*link|LinkingOptions|linking\s*:)"
        ),
        ("mobile-security-reviewer", "mobile-ui-accessibility-reviewer"),
    ),
    (
        "webview",
        re.compile(
            r"(?i)(?:\bWebView\b|\bWKWebView\b|javaScriptEnabled|addJavascriptInterface|"
            r"setAllowFileAccess|originWhitelist|injectedJavaScript)"
        ),
        ("mobile-security-reviewer",),
    ),
    (
        "privacy-or-tracking",
        re.compile(
            r"(?i)(?:NSPrivacy|PrivacyInfo\.xcprivacy|NSUserTrackingUsageDescription|"
            r"AdSupport|AdvertisingId|trackingAuthorization|analytics|telemetry|crashlytics)"
        ),
        ("mobile-security-reviewer", "mobile-release-engineer"),
    ),
    (
        "signing-or-release-build",
        re.compile(
            r"(?i)(?:signingConfigs?|storeFile|storePassword|keyAlias|keyPassword|"
            r"CODE_SIGN|DEVELOPMENT_TEAM|PROVISIONING_PROFILE|PRODUCT_BUNDLE_IDENTIFIER|"
            r"applicationId\b|bundleIdentifier|ExportOptions|release\s*\{)"
        ),
        ("mobile-security-reviewer", "mobile-release-engineer"),
    ),
    (
        "build-configuration",
        re.compile(
            r"(?i)(?:\b(?:minSdk|targetSdk|compileSdk|versionCode|versionName|buildTypes|"
            r"productFlavors|flavorDimensions|deploymentTarget)\b|"
            r"IPHONEOS_DEPLOYMENT_TARGET|SWIFT_VERSION|ENABLE_BITCODE|EXCLUDED_ARCHS|OTHER_LDFLAGS)"
        ),
        ("mobile-release-engineer",),
    ),
    (
        "dependency-configuration",
        re.compile(
            r"(?i)(?:\b(?:dependencies|devDependencies|peerDependencies|optionalDependencies)\b|"
            r"\b(?:implementation|api|ksp|kapt|classpath)\s*\(|"
            r"\bpod\s+[\"']|\bpackage\s*:\s*[A-Za-z0-9_.-]+|"
            r"\b(?:git|path)\s*:\s*[^\s])"
        ),
        ("mobile-security-reviewer", "mobile-architect"),
    ),
)

LOCKFILE_NAMES = {
    "cartfile.resolved",
    "gradle.lockfile",
    "package-lock.json",
    "packages.resolved",
    "pnpm-lock.yaml",
    "podfile.lock",
    "pubspec.lock",
    "yarn.lock",
}

DEPENDENCY_MANIFEST_NAMES = {
    "build.gradle",
    "build.gradle.kts",
    "cartfile",
    "gemfile",
    "gradle-wrapper.properties",
    "libs.versions.toml",
    "package.json",
    "package.swift",
    "podfile",
    "pubspec.yaml",
    "settings.gradle",
    "settings.gradle.kts",
}

BUILD_CONFIGURATION_NAMES = {
    "build.gradle",
    "build.gradle.kts",
    "gradle.properties",
    "project.pbxproj",
}

PRIVACY_MANIFEST_NAMES = {"privacyinfo.xcprivacy"}


class PayloadError(ValueError):
    """Raised when hook input is invalid."""


def stop(reason: str) -> dict[str, Any]:
    return {"continue": False, "stopReason": reason}


def validate_payload(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise PayloadError("payload must be an object")
    for key in (
        "session_id",
        "transcript_path",
        "cwd",
        "hook_event_name",
        "timestamp",
        "tool_name",
    ):
        if not isinstance(payload.get(key), str) or not payload[key]:
            raise PayloadError(f"{key} must be a non-empty string")
    if payload["hook_event_name"] != "AfterTool":
        raise PayloadError("unexpected hook event")
    if not isinstance(payload.get("tool_input"), dict):
        raise PayloadError("tool_input must be an object")
    if not Path(payload["cwd"]).is_absolute():
        raise PayloadError("cwd must be absolute")
    return payload


def resolve_in_workspace(raw_path: str, cwd: Path) -> Path:
    if not raw_path or "\x00" in raw_path:
        raise PayloadError("invalid path")
    candidate = Path(raw_path).expanduser()
    if not candidate.is_absolute():
        candidate = cwd / candidate
    resolved_cwd = cwd.resolve(strict=False)
    resolved = candidate.resolve(strict=False)
    try:
        resolved.relative_to(resolved_cwd)
    except ValueError as exc:
        raise PayloadError("path escapes the workspace") from exc
    return resolved


def platform_reviewers(path: Path) -> set[str]:
    normalized = "/" + path.as_posix().lower().lstrip("/")
    name = path.name.lower()
    suffix = path.suffix.lower()
    reviewers: set[str] = set()
    if re.search(r"/(?:common|android|ios|apple|native|jvm|js|wasm)(?:main|test)/", normalized) or "/composeapp/" in normalized:
        reviewers.add("kmp-engineer")
        if "/androidmain/" in normalized or "/androidtest/" in normalized:
            reviewers.add("android-engineer")
        if any(segment in normalized for segment in ("/iosmain/", "/iostest/", "/applemain/", "/appletest/")):
            reviewers.add("ios-engineer")
        return reviewers
    if "/android/" in normalized or name == "androidmanifest.xml" or suffix in {".kt", ".kts", ".java"}:
        reviewers.add("android-engineer")
    if "/ios/" in normalized or suffix in {".swift", ".m", ".mm", ".entitlements"} or name in {"info.plist", "project.pbxproj"}:
        reviewers.add("ios-engineer")
    if suffix == ".dart" or name in {"pubspec.yaml", "pubspec.lock"}:
        reviewers.add("flutter-engineer")
    if suffix in {".js", ".jsx", ".ts", ".tsx"} or name in {"metro.config.js", "package.json"}:
        reviewers.add("react-native-engineer")
    return reviewers


def path_review_requirements(path: Path) -> list[tuple[str, tuple[str, ...]]]:
    """Return reviews required by an exact sensitive configuration path."""
    name = path.name.lower()
    suffix = path.suffix.lower()
    requirements: list[tuple[str, tuple[str, ...]]] = []
    if name in LOCKFILE_NAMES:
        requirements.append(
            ("dependency-lockfile", ("mobile-security-reviewer", "mobile-architect"))
        )
    if name in DEPENDENCY_MANIFEST_NAMES:
        requirements.append(
            ("dependency-configuration", ("mobile-security-reviewer", "mobile-architect"))
        )
    if name in BUILD_CONFIGURATION_NAMES or suffix == ".xcconfig":
        requirements.append(("build-configuration", ("mobile-release-engineer",)))
    if suffix == ".entitlements":
        requirements.append(
            (
                "entitlements-file",
                (
                    "mobile-security-reviewer",
                    "mobile-ui-accessibility-reviewer",
                    "mobile-release-engineer",
                ),
            )
        )
    if name in PRIVACY_MANIFEST_NAMES:
        requirements.append(
            ("privacy-manifest", ("mobile-security-reviewer", "mobile-release-engineer"))
        )
    return requirements


def changed_text(tool_name: str, tool_input: dict[str, Any]) -> tuple[str, bool]:
    if tool_name == "write_file":
        content = tool_input.get("content")
        if not isinstance(content, str):
            raise PayloadError("content must be a string")
        return content, bool(content.strip())
    if tool_name == "replace":
        old = tool_input.get("old_string")
        new = tool_input.get("new_string")
        if not isinstance(old, str) or not isinstance(new, str):
            raise PayloadError("old_string and new_string must be strings")
        return old + "\n" + new, old != new
    return "", False


def evaluate(payload: Any) -> dict[str, Any]:
    try:
        data = validate_payload(payload)
        tool_name = data["tool_name"]
        if tool_name not in {"write_file", "replace"}:
            return {}
        raw_path = data["tool_input"].get("file_path")
        if not isinstance(raw_path, str):
            raise PayloadError("file_path must be a string")
        path = resolve_in_workspace(raw_path, Path(data["cwd"]))
        text, has_delta = changed_text(tool_name, data["tool_input"])
        if not has_delta:
            return {}

        categories: list[str] = []
        reviewers: set[str] = set()
        for category, pattern, required_reviewers in RULES:
            if pattern.search(text):
                categories.append(category)
                reviewers.update(required_reviewers)
        for category, required_reviewers in path_review_requirements(path):
            categories.append(category)
            reviewers.update(required_reviewers)

        if not categories:
            return {}
        reviewers.update(platform_reviewers(path))
        ordered_reviewers = sorted(reviewers)
        category_text = ", ".join(sorted(set(categories)))
        reviewer_text = ", ".join(f"`{reviewer}`" for reviewer in ordered_reviewers)
        context = (
            f"Sensitive mobile change detected in {raw_path}: {category_text}. "
            f"Before completion, obtain independent review from {reviewer_text}; "
            "record findings, resolutions, and rerun affected validation. The implementer cannot self-approve."
        )
        return {
            "systemMessage": context,
            "hookSpecificOutput": {"additionalContext": context},
        }
    except (PayloadError, OSError, RuntimeError) as exc:
        return stop(f"Sensitive-change review hook failed safely: {exc}. Stop and inspect the last change.")


def read_stdin_payload() -> Any:
    raw = sys.stdin.buffer.read(MAX_INPUT_BYTES + 1)
    if len(raw) > MAX_INPUT_BYTES:
        raise PayloadError("payload exceeds size limit")
    try:
        return json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PayloadError("payload is not valid UTF-8 JSON") from exc


def base_payload(tool_name: str, tool_input: dict[str, Any]) -> dict[str, Any]:
    return {
        "session_id": "test-session",
        "transcript_path": "/tmp/transcript.json",
        "cwd": "/tmp/mobile-project",
        "hook_event_name": "AfterTool",
        "timestamp": "2026-01-01T00:00:00Z",
        "tool_name": tool_name,
        "tool_input": tool_input,
        "tool_response": {"llmContent": "ok", "returnDisplay": "ok"},
    }


class SensitiveChangeReviewTests(unittest.TestCase):
    def test_harmless_filename_only_change_is_ignored(self) -> None:
        payload = base_payload(
            "replace",
            {
                "file_path": "android/app/src/main/AndroidManifest.xml",
                "old_string": "<!-- old wording -->",
                "new_string": "<!-- new wording -->",
            },
        )
        self.assertEqual(evaluate(payload), {})

    def test_permission_change_requires_reviews(self) -> None:
        payload = base_payload(
            "replace",
            {
                "file_path": "android/app/src/main/AndroidManifest.xml",
                "old_string": "",
                "new_string": '<uses-permission android:name="android.permission.CAMERA" />',
            },
        )
        result = evaluate(payload)
        context = result["hookSpecificOutput"]["additionalContext"]
        self.assertIn("mobile-security-reviewer", context)
        self.assertIn("android-engineer", context)

    def test_lockfile_delta_requires_review(self) -> None:
        payload = base_payload(
            "replace",
            {"file_path": "package-lock.json", "old_string": '"version": "1"', "new_string": '"version": "2"'},
        )
        self.assertIn("dependency-lockfile", evaluate(payload)["systemMessage"])

    def test_auth_change_requires_security_review(self) -> None:
        payload = base_payload(
            "write_file",
            {"file_path": "src/session.ts", "content": "export function refreshToken() { return undefined; }"},
        )
        self.assertIn("mobile-security-reviewer", evaluate(payload)["systemMessage"])

    def test_kmp_sensitive_change_selects_shared_and_native_reviewers(self) -> None:
        payload = base_payload(
            "write_file",
            {
                "file_path": "shared/src/androidMain/kotlin/SecureStorage.kt",
                "content": "class SecureStorage { val accessToken = value }",
            },
        )
        message = evaluate(payload)["systemMessage"]
        self.assertIn("kmp-engineer", message)
        self.assertIn("android-engineer", message)

    def test_build_configuration_change_requires_release_review(self) -> None:
        payload = base_payload(
            "replace",
            {"file_path": "android/app/build.gradle.kts", "old_string": "minSdk = 24", "new_string": "minSdk = 26"},
        )
        self.assertIn("mobile-release-engineer", evaluate(payload)["systemMessage"])

    def test_entitlement_value_only_change_requires_review(self) -> None:
        payload = base_payload(
            "replace",
            {
                "file_path": "ios/App/App.entitlements",
                "old_string": "<string>development</string>",
                "new_string": "<string>production</string>",
            },
        )
        message = evaluate(payload)["systemMessage"]
        self.assertIn("entitlements-file", message)
        self.assertIn("mobile-security-reviewer", message)
        self.assertIn("mobile-release-engineer", message)

    def test_dependency_version_only_change_requires_review(self) -> None:
        payload = base_payload(
            "replace",
            {
                "file_path": "Package.swift",
                "old_string": 'from: "1.2.3"',
                "new_string": 'from: "1.2.4"',
            },
        )
        message = evaluate(payload)["systemMessage"]
        self.assertIn("dependency-configuration", message)
        self.assertIn("mobile-architect", message)

    def test_build_file_value_only_change_requires_review(self) -> None:
        payload = base_payload(
            "replace",
            {
                "file_path": "android/app/build.gradle.kts",
                "old_string": 'versionName = "1.2.3"',
                "new_string": 'versionName = "1.2.4"',
            },
        )
        message = evaluate(payload)["systemMessage"]
        self.assertIn("build-configuration", message)
        self.assertIn("mobile-release-engineer", message)

    def test_workspace_escape_stops_loop(self) -> None:
        payload = base_payload(
            "write_file",
            {"file_path": "../outside.ts", "content": "const token = value;"},
        )
        self.assertFalse(evaluate(payload)["continue"])

    def test_invalid_payload_fails_closed(self) -> None:
        self.assertFalse(evaluate({})["continue"])


def main() -> int:
    if sys.argv[1:] == ["--self-test"]:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(SensitiveChangeReviewTests)
        result = unittest.TextTestRunner(stream=sys.stderr, verbosity=2).run(suite)
        return 0 if result.wasSuccessful() else 1
    try:
        payload = read_stdin_payload()
        result = evaluate(payload)
    except PayloadError as exc:
        result = stop(f"Sensitive-change review hook failed safely: {exc}. Stop and inspect the last change.")
    sys.stdout.write(json.dumps(result, separators=(",", ":")))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
