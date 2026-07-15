"""Inspect file paths for traversal and protected mobile material."""

from __future__ import annotations

import os

from hook_common import Finding, normalize_relative_path


PROTECTED_PATTERNS = (
    ".env",
    "keystore",
    ".jks",
    ".p12",
    ".p8",
    ".mobileprovision",
    "provisioning",
    "certificate",
    "service-account",
    "google-services.json",
    "googleservice-info.plist",
)

PUBLIC_CLIENT_CONFIG = {"google-services.json", "googleservice-info.plist"}


def inspect_path(root: str, path: str, operation: str = "read") -> list[Finding]:
    findings: list[Finding] = []
    try:
        absolute = normalize_relative_path(root, path)
    except ValueError as exc:
        return [Finding("invalid-path", str(exc))]

    lowered = path.lower()
    basename = os.path.basename(lowered)
    if any(pattern in lowered for pattern in PROTECTED_PATTERNS):
        if basename in PUBLIC_CLIENT_CONFIG and operation == "read":
            findings.append(Finding("public-client-config-review", "Public mobile client configuration may be read, but changes require human review.", "warn"))
        else:
            findings.append(Finding("protected-material", f"Path references protected material: {absolute}"))
    return findings


def main() -> int:
    import json
    import sys

    payload = json.load(sys.stdin)
    findings = inspect_path(payload.get("root", "."), payload.get("path", ""), payload.get("operation", "read"))
    blocking = [finding for finding in findings if finding.severity == "block"]
    json.dump({"allow": not blocking, "findings": [finding.__dict__ for finding in findings]}, sys.stdout)
    return 0 if not blocking else 2


if __name__ == "__main__":
    raise SystemExit(main())
