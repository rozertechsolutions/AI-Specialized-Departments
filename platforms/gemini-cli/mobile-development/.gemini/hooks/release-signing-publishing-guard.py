#!/usr/bin/env python3
"""Gemini CLI BeforeTool hook that blocks release, signing, and publication."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any

MAX_INPUT_BYTES = 1_048_576
MAX_COMMAND_CHARS = 20_000

SENSITIVE_PATTERNS = (
    re.compile(r"(?i)(?:^|\s)(?:bundle\s+exec\s+)?fastlane(?:\s|$)"),
    re.compile(r"(?i)(?:^|\s)(?:pilot|deliver|supply|match|gym|snapshot|precheck)\b"),
    re.compile(r"(?i)(?:^|\s)(?:codesign|apksigner|jarsigner|productbuild|pkgbuild)\b"),
    re.compile(r"(?i)(?:^|\s)(?:security\s+import|profiles\s+install|gpg\s+--import|certutil\b.*-import)\b"),
    re.compile(r"(?i)(?:^|\s)keytool\b.*\b(?:-import|-importcert|-genkeypair)\b"),
    re.compile(r"(?i)(?:^|\s)xcodebuild\b.*(?:\sarchive\b|-exportarchive\b)"),
    re.compile(r"(?i)(?:^|\s)xcrun\s+(?:altool|notarytool|iTMSTransporter)\b"),
    re.compile(r"(?i)(?:^|\s)(?:notarytool|altool|iTMSTransporter|transporter)\b"),
    re.compile(r"(?i)(?:^|\s)(?:npm|pnpm)\s+publish\b"),
    re.compile(r"(?i)(?:^|\s)yarn\s+(?:npm\s+)?publish\b"),
    re.compile(r"(?i)(?:^|\s)(?:dart|flutter)\s+pub\s+publish\b"),
    re.compile(r"(?i)(?:^|\s)pod\s+trunk\s+(?:push|register)\b"),
    re.compile(r"(?i)(?:^|\s)(?:firebase|gcloud)\b.*\bdeploy\b"),
    re.compile(r"(?i)(?:^|\s)(?:eas\s+(?:build|submit|update)|expo\s+(?:publish|upload))\b"),
    re.compile(r"(?i)(?:^|\s)(?:appcenter\s+distribute|sentry-cli\s+upload|upload-symbols)\b"),
    re.compile(r"(?i)(?:^|\s)gh\s+release\s+(?:create|upload|edit|delete)\b"),
    re.compile(r"(?i)(?:^|\s)(?:aws\s+s3\s+(?:cp|sync)|gsutil\s+(?:cp|rsync))\b"),
    re.compile(r"(?i)(?:^|\s)(?:scp|sftp|rsync)\b"),
    re.compile(r"(?i)(?:^|\s)curl\b.*(?:--upload-file|-T\s)"),
    re.compile(r"(?i)(?:^|\s)adb\s+install(?:-multiple)?\b"),
    re.compile(r"(?i)\b(?:CODE_SIGNING_ALLOWED\s*=\s*YES|CODE_SIGN_STYLE\s*=|DEVELOPMENT_TEAM\s*=|PROVISIONING_PROFILE(?:_SPECIFIER)?\s*=)"),
    re.compile(r"(?i)(?:--keystore|--ks\b|--store-password|--key-password|--password\b|--private-key)"),
)

GRADLE_RELEASE_TASK = re.compile(
    r"(?i)^\s*(?:\.\\gradlew\.bat|gradlew\.bat|\./gradlew|gradle)\b.*"
    r"(?:^|[\s:])(?:assemble\w*release|bundle\w*release|package\w*release|"
    r"publish\w*|upload\w*|closeandrelease\w*|promote\w*|sign\w*|"
    r"publishToMavenLocal|play\w*|release)(?:\s|$)"
)


class PayloadError(ValueError):
    """Raised when hook input is invalid."""


def deny(reason: str) -> dict[str, Any]:
    return {"decision": "deny", "reason": reason, "continue": True}


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
    if payload["hook_event_name"] != "BeforeTool":
        raise PayloadError("unexpected hook event")
    if not isinstance(payload.get("tool_input"), dict):
        raise PayloadError("tool_input must be an object")
    if not Path(payload["cwd"]).is_absolute():
        raise PayloadError("cwd must be absolute")
    return payload


def unsafe_flutter_release(command: str) -> bool:
    match = re.search(r"(?i)^\s*flutter\s+build\s+(apk|appbundle|ipa|ios)\b", command)
    if not match:
        return False
    artifact = match.group(1).lower()
    lowered = command.lower()
    if artifact in {"appbundle", "ipa"}:
        return True
    if artifact == "ios":
        return not ("--debug" in lowered and "--no-codesign" in lowered)
    return "--debug" not in lowered


def evaluate(payload: Any) -> dict[str, Any]:
    try:
        data = validate_payload(payload)
        if data["tool_name"] != "run_shell_command":
            return {"decision": "allow"}
        command = data["tool_input"].get("command")
        if not isinstance(command, str) or not command.strip():
            raise PayloadError("command must be a non-empty string")
        if len(command) > MAX_COMMAND_CHARS or "\x00" in command:
            raise PayloadError("command exceeds safety limits")
        if unsafe_flutter_release(command):
            return deny("Flutter release or distributable build actions are blocked; use non-signing debug validation only.")
        if GRADLE_RELEASE_TASK.search(command):
            return deny("Gradle release, signing, publishing, upload, promotion, or store tasks are blocked.")
        if any(pattern.search(command) for pattern in SENSITIVE_PATTERNS):
            return deny("Signing, credential import, publication, upload, deployment, distribution, or submission is human-only and blocked.")
        return {"decision": "allow"}
    except (PayloadError, OSError, RuntimeError) as exc:
        return deny(f"Release guard rejected invalid input: {exc}")


def read_stdin_payload() -> Any:
    raw = sys.stdin.buffer.read(MAX_INPUT_BYTES + 1)
    if len(raw) > MAX_INPUT_BYTES:
        raise PayloadError("payload exceeds size limit")
    try:
        return json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PayloadError("payload is not valid UTF-8 JSON") from exc


def base_payload(command: str) -> dict[str, Any]:
    return {
        "session_id": "test-session",
        "transcript_path": "/tmp/transcript.json",
        "cwd": "/tmp/mobile-project",
        "hook_event_name": "BeforeTool",
        "timestamp": "2026-01-01T00:00:00Z",
        "tool_name": "run_shell_command",
        "tool_input": {"command": command},
    }


class ReleaseGuardTests(unittest.TestCase):
    def test_allows_non_signing_validation(self) -> None:
        commands = (
            "./gradlew testDebugUnitTest",
            "flutter build apk --debug",
            "flutter build ios --debug --no-codesign",
            "xcodebuild test -scheme Demo CODE_SIGNING_ALLOWED=NO",
            "npm test",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assertEqual(evaluate(base_payload(command))["decision"], "allow")

    def test_blocks_release_builds(self) -> None:
        commands = (
            "./gradlew bundleRelease",
            "flutter build appbundle",
            "flutter build apk --release",
            "xcodebuild archive -scheme Demo",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assertEqual(evaluate(base_payload(command))["decision"], "deny")

    def test_blocks_publication_and_signing(self) -> None:
        commands = (
            "bundle exec fastlane beta",
            "npm publish",
            "codesign --sign Example App.app",
            "firebase deploy",
            "security import signing.p12",
        )
        for command in commands:
            with self.subTest(command=command):
                self.assertEqual(evaluate(base_payload(command))["decision"], "deny")

    def test_invalid_payload_fails_closed(self) -> None:
        self.assertEqual(evaluate({})["decision"], "deny")


def main() -> int:
    if sys.argv[1:] == ["--self-test"]:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ReleaseGuardTests)
        result = unittest.TextTestRunner(stream=sys.stderr, verbosity=2).run(suite)
        return 0 if result.wasSuccessful() else 1
    try:
        payload = read_stdin_payload()
        result = evaluate(payload)
    except PayloadError as exc:
        result = deny(f"Release guard rejected invalid input: {exc}")
    sys.stdout.write(json.dumps(result, separators=(",", ":")))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

