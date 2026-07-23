"""Block signing, publishing, upload, deployment, and spending actions."""

from __future__ import annotations

from hook_common import Finding, split_command


BLOCKED_TERMS = (
    "sign",
    "codesign",
    "notarytool",
    "altool",
    "pilot",
    "deliver",
    "supply",
    "publish",
    "upload",
    "submit",
    "deploy",
    "distribute",
    "release",
    "firebase",
    "sentry-cli",
    "app-store-connect",
    "play-console",
)


def inspect_release_action(command: str) -> list[Finding]:
    try:
        parts = split_command(command)
    except ValueError as exc:
        return [Finding("malformed-command", str(exc))]
    lowered = " ".join(parts).lower()
    findings = [
        Finding("release-action", f"Command appears to perform prohibited release action: {term}")
        for term in BLOCKED_TERMS
        if term in lowered
    ]
    return findings


def main() -> int:
    import json
    import sys

    payload = json.load(sys.stdin)
    findings = inspect_release_action(payload.get("command", ""))
    json.dump({"allow": not findings, "findings": [finding.__dict__ for finding in findings]}, sys.stdout)
    return 0 if not findings else 2


if __name__ == "__main__":
    raise SystemExit(main())
