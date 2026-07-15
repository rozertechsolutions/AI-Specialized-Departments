from __future__ import annotations

from mobile_development_agents.policies.security import contains_secret, redact_secrets


def validate_agent_output(text: str) -> tuple[str, ...]:
    issues: list[str] = []
    if contains_secret(text):
        issues.append("Output appears to contain a secret.")
    if "successfully published" in text.lower() or "uploaded to app store" in text.lower():
        issues.append("Output claims a prohibited release action.")
    return tuple(issues)


def safe_output(text: str) -> str:
    return redact_secrets(text)
