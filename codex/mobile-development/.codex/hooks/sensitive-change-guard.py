#!/usr/bin/env python3
"""Stop after apply_patch changes that require explicit human review."""

from __future__ import annotations

import json
import re
import sys
from pathlib import PurePosixPath
from typing import Any


FILE_HEADER = re.compile(r"^\*\*\* (?:Add|Update|Delete) File: (.+)$")
MOVE_HEADER = re.compile(r"^\*\*\* Move to: (.+)$")
ALWAYS_SENSITIVE = re.compile(
    r"(?:\.entitlements$|PrivacyInfo\.xcprivacy$|network_security_config\.xml$|"
    r"(?:^|/)(?:ExportOptions\.plist|Matchfile|Appfile)$|\.(?:jks|keystore|p12|p8|mobileprovision)$)",
    re.I,
)

CONDITIONAL_RULES = (
    (
        re.compile(r"AndroidManifest\.xml$", re.I),
        re.compile(r"uses-permission|uses-feature|android:exported\s*=\s*[\"']true|android:debuggable|usesCleartextTraffic|networkSecurityConfig|requestLegacyExternalStorage", re.I),
    ),
    (
        re.compile(r"(?:Info|ExportOptions)\.plist$|project\.pbxproj$", re.I),
        re.compile(r"UsageDescription|NSAppTransportSecurity|NSAllowsArbitraryLoads|UIBackgroundModes|aps-environment|CODE_SIGN|PROVISIONING_PROFILE|DEVELOPMENT_TEAM", re.I),
    ),
    (
        re.compile(r"(?:build\.gradle(?:\.kts)?|gradle\.properties)$", re.I),
        re.compile(r"signingConfig|storeFile|storePassword|keyAlias|keyPassword|debuggable\s*[=( ]\s*true", re.I),
    ),
    (
        re.compile(r"(?:^|/)fastlane/Fastfile$", re.I),
        re.compile(r"match\b|gym\b|build_app\b|deliver\b|pilot\b|supply\b|upload_to_(?:app|play)_store", re.I),
    ),
)


def stop(reason: str) -> None:
    json.dump(
        {
            "continue": False,
            "stopReason": reason,
            "systemMessage": reason,
        },
        sys.stdout,
    )
    sys.stdout.write("\n")
    raise SystemExit(0)


def patch_from_stdin() -> str:
    try:
        payload: Any = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, TypeError):
        stop("Sensitive-change guard received invalid hook input; review the completed edit before continuing.")
    if not isinstance(payload, dict):
        stop("Sensitive-change guard received invalid hook input; review the completed edit before continuing.")
    if payload.get("hook_event_name") != "PostToolUse" or payload.get("tool_name") != "apply_patch":
        return ""
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict) or not isinstance(tool_input.get("command"), str):
        stop("Sensitive-change guard could not inspect the completed edit; review it before continuing.")
    return tool_input["command"]


def changed_sections(patch: str) -> list[tuple[list[str], str]]:
    sections: list[tuple[list[str], list[str]]] = []
    current: tuple[list[str], list[str]] | None = None
    for line in patch.splitlines():
        header = FILE_HEADER.match(line)
        if header:
            current = ([PurePosixPath(header.group(1).strip()).as_posix()], [])
            sections.append(current)
            continue
        moved = MOVE_HEADER.match(line)
        if moved and current is not None:
            current[0].append(PurePosixPath(moved.group(1).strip()).as_posix())
            continue
        if current is not None and line.startswith(("+", "-")) and not line.startswith(("+++", "---")):
            current[1].append(line[1:])
    return [(paths, "\n".join(lines)) for paths, lines in sections]


def sensitive_paths(patch: str) -> list[str]:
    flagged: list[str] = []
    for paths, changed_text in changed_sections(patch):
        for path in paths:
            if ALWAYS_SENSITIVE.search(path):
                flagged.append(path)
                continue
            for path_pattern, content_pattern in CONDITIONAL_RULES:
                if path_pattern.search(path) and content_pattern.search(changed_text):
                    flagged.append(path)
                    break
    return sorted(set(flagged))


def main() -> None:
    patch = patch_from_stdin()
    if not patch:
        return
    paths = sensitive_paths(patch)
    if paths:
        display = ", ".join(paths[:5])
        if len(paths) > 5:
            display += f", and {len(paths) - 5} more"
        stop(
            "Sensitive mobile configuration changed. Stop for human review before further edits or commands. "
            f"Review: {display}."
        )


if __name__ == "__main__":
    main()
