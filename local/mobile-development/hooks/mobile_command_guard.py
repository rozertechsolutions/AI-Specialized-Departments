"""Inspect proposed shell commands for unsafe mobile-development actions."""

from __future__ import annotations

from hook_common import Finding, any_contains, contains_encoded_payload, has_shell_metacharacters, split_command


DESTRUCTIVE_PREFIXES = (
    ("rm",),
    ("git", "reset"),
    ("git", "clean"),
    ("git", "checkout"),
    ("git", "restore"),
    ("adb", "shell", "pm", "clear"),
    ("xcrun", "simctl", "erase"),
)

SENSITIVE_TERMS = (
    "keystore",
    "provisioning",
    "certificate",
    "privatekey",
    "private_key",
    "service-account",
    ".env",
)


def inspect_command(command: str) -> list[Finding]:
    findings: list[Finding] = []
    try:
        parts = split_command(command)
    except ValueError as exc:
        return [Finding("malformed-command", str(exc))]

    lowered = [part.lower() for part in parts]
    if has_shell_metacharacters(command):
        findings.append(Finding("shell-metacharacter", "Command contains chaining, redirection, substitution, or pipe syntax."))
    if any(contains_encoded_payload(part) for part in parts):
        findings.append(Finding("encoded-payload", "Command contains a suspicious encoded payload."))
    for prefix in DESTRUCTIVE_PREFIXES:
        for index in range(0, len(lowered) - len(prefix) + 1):
            if tuple(lowered[index : index + len(prefix)]) == prefix:
                findings.append(Finding("destructive-command", f"Command prefix {' '.join(prefix)} is prohibited."))
                break
    if any_contains(lowered, SENSITIVE_TERMS):
        findings.append(Finding("sensitive-material-reference", "Command references protected mobile credential or environment material."))
    return findings


def main() -> int:
    import json
    import sys

    payload = json.load(sys.stdin)
    findings = inspect_command(payload.get("command", ""))
    json.dump({"allow": not findings, "findings": [finding.__dict__ for finding in findings]}, sys.stdout)
    return 0 if not findings else 2


if __name__ == "__main__":
    raise SystemExit(main())
