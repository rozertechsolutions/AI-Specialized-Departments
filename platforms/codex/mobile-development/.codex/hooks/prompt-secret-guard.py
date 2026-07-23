#!/usr/bin/env python3
"""Block prompts or apply_patch payloads containing high-confidence secrets."""

from __future__ import annotations

import json
import re
import sys
from pathlib import PurePosixPath
from typing import Any, Optional


DIRECT_PATTERNS = (
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"(?:github_pat_[A-Za-z0-9_]{40,}|gh[pousr]_[A-Za-z0-9]{36,})")),
    ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
)

GOOGLE_API_KEY_PATTERN = re.compile(r"AIza[0-9A-Za-z_-]{35}")
FILE_HEADER = re.compile(r"^\*\*\* (?:Add|Update|Delete) File: (.+)$")

ASSIGNMENT_PATTERN = re.compile(
    r"(?i)(?:api[_-]?key|client[_-]?secret|access[_-]?token|refresh[_-]?token|"
    r"keystore[_-]?password|storepassword|keypassword)\s*[:=]\s*[\"']?"
    r"([A-Za-z0-9_./+=-]{16,})"
)

PLACEHOLDER_MARKERS = (
    "example",
    "placeholder",
    "change_me",
    "changeme",
    "dummy",
    "sample",
    "test_only",
    "your_",
)


def read_payload() -> dict[str, Any]:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, TypeError):
        deny("Secret guard received invalid hook input.")
    if not isinstance(payload, dict):
        deny("Secret guard received invalid hook input.")
    return payload


def added_patch_sections(patch: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, list[str]]] = []
    current: Optional[tuple[str, list[str]]] = None
    for line in patch.splitlines():
        header = FILE_HEADER.match(line)
        if header:
            current = (PurePosixPath(header.group(1).strip()).as_posix(), [])
            sections.append(current)
            continue
        if current is not None and line.startswith("+") and not line.startswith("+++"):
            current[1].append(line[1:])
    if not sections:
        return [("", patch)]
    return [(path, "\n".join(lines)) for path, lines in sections]


def content_for(payload: dict[str, Any]) -> tuple[str, list[tuple[str, str]]]:
    event = payload.get("hook_event_name")
    if event == "UserPromptSubmit":
        prompt = payload.get("prompt")
        if not isinstance(prompt, str):
            deny("Secret guard could not inspect the submitted prompt.")
        return event, [("", prompt)]
    if event == "PreToolUse" and payload.get("tool_name") == "apply_patch":
        tool_input = payload.get("tool_input")
        if not isinstance(tool_input, dict) or not isinstance(tool_input.get("command"), str):
            deny("Secret guard could not inspect the pending patch.")
        return event, added_patch_sections(tool_input["command"])
    return str(event or ""), []


def is_public_google_client_config(path: str, content: str) -> bool:
    name = PurePosixPath(path).name.lower()
    markers = {
        "google-services.json": ("current_key",),
        "googleService-info.plist".lower(): ("API_KEY",),
        "firebase_options.dart": ("apiKey",),
        "google_maps_api.xml": ("google_maps_key",),
        "androidmanifest.xml": ("com.google.android.geo.API_KEY",),
        "info.plist": ("GMSApiKey",),
    }
    return name in markers and any(marker in content for marker in markers[name])


def detect_secret(sections: list[tuple[str, str]], event: str) -> Optional[str]:
    for path, content in sections:
        for label, pattern in DIRECT_PATTERNS:
            if pattern.search(content):
                return label

        public_google_config = event == "PreToolUse" and is_public_google_client_config(path, content)
        if GOOGLE_API_KEY_PATTERN.search(content) and not public_google_config:
            return "Google API key"

        for match in ASSIGNMENT_PATTERN.finditer(content):
            candidate = match.group(1)
            lowered = candidate.lower()
            if lowered.startswith(("${", "env.", "process.env")):
                continue
            if any(marker in lowered for marker in PLACEHOLDER_MARKERS):
                continue
            if public_google_config and GOOGLE_API_KEY_PATTERN.fullmatch(candidate):
                continue
            return "credential-like assignment"
    return None


def deny(reason: str, event: Optional[str] = None) -> None:
    if event == "PreToolUse":
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        }
    else:
        output = {"decision": "block", "reason": reason}
    json.dump(output, sys.stdout)
    sys.stdout.write("\n")
    raise SystemExit(0)


def main() -> None:
    payload = read_payload()
    event, sections = content_for(payload)
    if not sections:
        return
    label = detect_secret(sections, event)
    if label:
        deny(
            f"Potential {label} blocked. Remove the value and use an approved local secret store or environment variable.",
            event,
        )


if __name__ == "__main__":
    main()
