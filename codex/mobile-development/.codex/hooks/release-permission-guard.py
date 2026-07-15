#!/usr/bin/env python3
"""Block signing, publishing, deployment, and distribution commands."""

from __future__ import annotations

import json
import re
import sys
from typing import Any


BLOCKED_COMMANDS = (
    ("Android signing", re.compile(r"\b(?:apksigner\s+sign|jarsigner\b)", re.I)),
    ("Android release artifact task", re.compile(r"(?:^|[\s;&|])(?:[^\s;&|]*/)?gradlew?(?:\.bat)?\b[^\n]*(?:assemble|bundle|package)[A-Za-z0-9_-]*Release\b", re.I)),
    ("Gradle publication", re.compile(r"(?:^|[\s;&|])(?:[^\s;&|]*/)?gradlew?(?:\.bat)?\b[^\n]*(?:publish|upload|promote|closeAndRelease)", re.I)),
    ("Apple signing", re.compile(r"\b(?:codesign|productsign)\b|\bsecurity\s+import\b", re.I)),
    ("Apple archive or export", re.compile(r"\bxcodebuild\b[^\n]*(?:\barchive\b|-exportArchive\b)", re.I)),
    ("Apple upload or notarization", re.compile(r"\bxcrun\b[^\n]*(?:\baltool\b|\bnotarytool\b|\btransporter\b)", re.I)),
    ("Fastlane signing or distribution", re.compile(r"\bfastlane\b[^\n]*(?:\bdeliver\b|\bpilot\b|\bsupply\b|\bmatch\b|\bgym\b|\bbuild_app\b|upload_to_(?:app|play)_store)", re.I)),
    ("Flutter release build", re.compile(r"\bflutter\s+build\s+(?:ipa|appbundle|apk|ios|aar)\b(?![^;&|\n]*(?:--debug\b|--simulator\b))", re.I)),
    ("Dart package publication", re.compile(r"\bflutter\s+pub\s+publish\b|\bdart\s+pub\s+publish\b", re.I)),
    ("JavaScript package publication", re.compile(r"\b(?:npm\s+publish|pnpm\s+publish|yarn\s+(?:npm\s+)?publish)\b", re.I)),
    ("Expo or EAS distribution", re.compile(r"\b(?:eas\s+(?:submit|build)|expo\s+upload)\b", re.I)),
    ("Firebase deployment or distribution", re.compile(r"\bfirebase\s+(?:deploy|appdistribution:distribute)\b", re.I)),
    ("GitHub release publication", re.compile(r"\bgh\s+release\s+(?:create|upload)\b", re.I)),
    ("Sentry release mutation", re.compile(r"\bsentry-cli\s+releases\s+(?:new|finalize|deploys|files)\b|\bsentry-cli\s+upload-dif\b", re.I)),
)


def deny(reason: str) -> None:
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )
    sys.stdout.write("\n")
    raise SystemExit(0)


def command_from_stdin() -> str:
    try:
        payload: Any = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, TypeError):
        deny("Release guard received invalid hook input.")
    if not isinstance(payload, dict):
        deny("Release guard received invalid hook input.")
    if payload.get("hook_event_name") != "PreToolUse" or payload.get("tool_name") != "Bash":
        return ""
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict) or not isinstance(tool_input.get("command"), str):
        deny("Release guard could not inspect the pending shell command.")
    return tool_input["command"]


def normalize_command(command: str) -> str:
    """Join shell line continuations so split command tokens remain inspectable."""
    return re.sub(r"\\\r?\n", " ", command)


def main() -> None:
    command = normalize_command(command_from_stdin())
    for label, pattern in BLOCKED_COMMANDS:
        if pattern.search(command):
            deny(f"Blocked {label}. This specialization may prepare a release but may not sign, publish, deploy, or distribute it.")


if __name__ == "__main__":
    main()
