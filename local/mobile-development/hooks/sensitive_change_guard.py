"""Identify sensitive mobile configuration changes requiring human review."""

from __future__ import annotations

from hook_common import Finding


SENSITIVE_PATH_TERMS = (
    "androidmanifest.xml",
    "network_security_config",
    "entitlements",
    "privacyinfo.xcprivacy",
    "info.plist",
    "build.gradle",
    "gradle.lockfile",
    "pubspec.yaml",
    "package.json",
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "metro.config",
)

SENSITIVE_CONTENT_TERMS = (
    "uses-permission",
    "associated-domains",
    "keychain",
    "biometric",
    "webview",
    "deeplink",
    "deep_link",
    "analytics",
    "telemetry",
    "authorization",
    "authentication",
    "crypto",
    "encrypt",
)


def inspect_change(path: str, content: str) -> list[Finding]:
    lowered_path = (path or "").lower()
    lowered_content = (content or "").lower()
    findings: list[Finding] = []
    if any(term in lowered_path for term in SENSITIVE_PATH_TERMS):
        findings.append(Finding("sensitive-path", "Change touches mobile configuration that requires human review.", "warn"))
    if any(term in lowered_content for term in SENSITIVE_CONTENT_TERMS):
        findings.append(Finding("sensitive-content", "Change appears to affect security, privacy, telemetry, WebView, or deep-link behavior.", "warn"))
    return findings


def main() -> int:
    import json
    import sys

    payload = json.load(sys.stdin)
    findings = inspect_change(payload.get("path", ""), payload.get("content", ""))
    json.dump({"allow": True, "findings": [finding.__dict__ for finding in findings]}, sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
