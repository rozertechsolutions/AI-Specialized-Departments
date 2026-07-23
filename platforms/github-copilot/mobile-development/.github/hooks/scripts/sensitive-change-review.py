#!/usr/bin/env python3
"""Require explicit review before Copilot changes sensitive mobile configuration."""

from __future__ import annotations

import json
import re
import sys
from collections.abc import Iterator
from typing import Any


PATH_KEYS = {
    "path",
    "file",
    "filepath",
    "file_path",
    "filename",
    "file_name",
    "target",
    "destination",
}
SENSITIVE_NAMES = {
    "androidmanifest.xml",
    "appfile",
    "babel.config.js",
    "babel.config.mjs",
    "build.gradle",
    "build.gradle.kts",
    "exportoptions.plist",
    "fastfile",
    "gemfile",
    "gemfile.lock",
    "gradle.properties",
    "info.plist",
    "libs.versions.toml",
    "matchfile",
    "metro.config.js",
    "metro.config.mjs",
    "network_security_config.xml",
    "package-lock.json",
    "package.json",
    "package.resolved",
    "package.swift",
    "pnpm-lock.yaml",
    "podfile",
    "podfile.lock",
    "privacyinfo.xcprivacy",
    "project.pbxproj",
    "pubspec.lock",
    "pubspec.yaml",
    "settings.gradle",
    "settings.gradle.kts",
    "yarn.lock",
}
SENSITIVE_SUFFIXES = (".entitlements", ".xcprivacy")
DOCUMENTATION_SUFFIXES = (".md", ".mdx", ".rst")
SENSITIVE_CONTENT_PATTERNS = (
    re.compile(r"(?i)<uses-permission\b"),
    re.compile(r"(?i)\bandroid\.permission\.[A-Z0-9_]+"),
    re.compile(r"(?i)\bandroid:(?:exported|permission|grantUriPermissions)\b"),
    re.compile(r"(?i)\busesCleartextTraffic\b|\bnetworkSecurityConfig\b"),
    re.compile(r"\bNS[A-Za-z]+UsageDescription\b"),
    re.compile(r"\bNSAppTransportSecurity\b|\bNSAllowsArbitraryLoads\b"),
    re.compile(r"(?i)\bcom\.apple\.developer\.[A-Za-z0-9.-]+"),
    re.compile(r"(?i)\bCODE_SIGN(?:ING)?_[A-Z_]+\b|\bPROVISIONING_PROFILE"),
    re.compile(r"(?i)\bsigningConfigs?\b|\bstoreFile\b|\bkeyAlias\b"),
    re.compile(r"(?i)\b(?:oauth|openid|client_secret|authorization|bearer)\b"),
    re.compile(r"(?i)\b(?:keychain|keystore|cryptograph|certificate pinning|public key pinning)\b"),
    re.compile(r"(?i)\b(?:WebView|WKWebView|javascriptInterface|setJavaScriptEnabled)\b"),
    re.compile(r"(?i)\b(?:deep link|app link|universal link|url scheme|associated domains)\b"),
    re.compile(r"(?i)\b(?:firebase|crashlytics|sentry|telemetry|analytics|appdistribution)\b"),
    re.compile(r"(?i)\b(?:publish|signing|distribution)\s*\{"),
)


def _deny(reason: str) -> dict[str, str]:
    return {"permissionDecision": "deny", "permissionDecisionReason": reason}


def _ask(reason: str) -> dict[str, str]:
    return {"permissionDecision": "ask", "permissionDecisionReason": reason}


def _strings(value: Any) -> Iterator[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from _strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from _strings(item)


def _paths(value: Any) -> Iterator[str]:
    if isinstance(value, dict):
        for key, item in value.items():
            normalized_key = str(key).casefold()
            if isinstance(item, str) and normalized_key in PATH_KEYS:
                yield item
            else:
                yield from _paths(item)
    elif isinstance(value, list):
        for item in value:
            yield from _paths(item)


def _patch_paths(value: Any) -> Iterator[str]:
    for text in _strings(value):
        for match in re.finditer(r"(?m)^\*\*\* (?:Add|Delete|Update) File:\s*(.+?)\s*$", text):
            yield match.group(1)


def _normalize_path(value: str) -> str:
    return value.strip().strip("\"'").replace("\\", "/")


def _has_traversal(value: str) -> bool:
    return ".." in [part for part in _normalize_path(value).split("/") if part not in {"", "."}]


def _is_sensitive_path(value: str) -> bool:
    normalized = _normalize_path(value).casefold().rstrip("/")
    name = normalized.rsplit("/", 1)[-1]
    if name in SENSITIVE_NAMES or name.endswith(SENSITIVE_SUFFIXES):
        return True
    if normalized.startswith(".github/workflows/") or "/.github/workflows/" in normalized:
        return True
    if "/fastlane/" in f"/{normalized}/":
        return True
    return normalized.endswith("/res/xml/network_security_config.xml")


def _is_documentation_path(value: str) -> bool:
    normalized = _normalize_path(value).casefold().rstrip("/")
    name = normalized.rsplit("/", 1)[-1]
    return name.startswith("readme") or name.endswith(DOCUMENTATION_SUFFIXES) or normalized.startswith("docs/")


def _contains_sensitive_change(value: str) -> bool:
    return any(pattern.search(value) for pattern in SENSITIVE_CONTENT_PATTERNS)


def evaluate(payload: Any) -> dict[str, str]:
    if not isinstance(payload, dict):
        return _deny("Malformed hook input: expected a JSON object.")
    tool_name = payload.get("toolName", payload.get("tool_name"))
    tool_args = payload.get("toolArgs", payload.get("tool_input"))
    write_tools = {"apply_patch", "create", "edit", "str_replace_editor", "write"}
    if not isinstance(tool_name, str) or tool_name.casefold() not in write_tools:
        return _deny("Malformed hook input: expected a file modification tool call.")
    if not isinstance(tool_args, (dict, list, str)):
        return _deny("Malformed hook input: missing or invalid tool arguments.")

    paths = list(_paths(tool_args)) + list(_patch_paths(tool_args))
    if any(_has_traversal(path) for path in paths):
        return _deny("File modifications containing parent traversal are blocked.")
    if any(_is_sensitive_path(path) for path in paths):
        return _ask(
            "This change affects mobile security, permissions, dependencies, build, privacy, or release configuration and requires explicit human review."
        )
    if paths and all(_is_documentation_path(path) for path in paths):
        return {}
    if any(_contains_sensitive_change(value) for value in _strings(tool_args)):
        return _ask(
            "This change contains security-, privacy-, external-service-, signing-, or publication-sensitive behavior and requires explicit human review."
        )
    return {}


def main() -> int:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        result = _deny("Malformed hook input: invalid JSON.")
    else:
        result = evaluate(payload)
    sys.stdout.write(json.dumps(result, separators=(",", ":"), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
