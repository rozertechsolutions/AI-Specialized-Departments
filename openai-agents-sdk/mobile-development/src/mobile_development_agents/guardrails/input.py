from __future__ import annotations

from mobile_development_agents.policies.security import contains_secret, validate_relative_project_path


def validate_user_input(text: str) -> tuple[str, ...]:
    issues: list[str] = []
    if contains_secret(text):
        issues.append("Input appears to contain a secret.")
    if "publish" in text.lower() or "submit to app store" in text.lower():
        issues.append("Publishing or store submission is prohibited.")
    return tuple(issues)


def validate_requested_path(path: str) -> tuple[str, ...]:
    return tuple(finding.message for finding in validate_relative_project_path(path) if finding.blocked)
