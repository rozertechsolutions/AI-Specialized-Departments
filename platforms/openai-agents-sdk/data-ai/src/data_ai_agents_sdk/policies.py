from __future__ import annotations

SENSITIVE_ACTION_TERMS = (
    "deploy",
    "publish",
    "release",
    "submit",
    "sign",
    "production",
    "credential",
    "secret",
    "private endpoint",
    "personal data",
    "sensitive dataset",
    "destructive",
    "irreversible",
    "spend",
)

UNSUPPORTED_COMPLETION_CLAIMS = (
    "data quality passed",
    "statistically significant",
    "causal impact proven",
    "model benchmark passed",
    "fairness certified",
    "compliance approved",
    "deployed successfully",
    "released successfully",
)

SECRET_PATTERNS = (
    "sk" + "-",
    "api" + "_key",
    "api" + "-key",
    "pass" + "word",
    "BEGIN " + "PRIVATE",
    "BEGIN " + "RSA",
    "BEGIN " + "OPENSSH",
)


def requires_human_approval(text: str) -> bool:
    normalized = text.casefold()
    return any(term in normalized for term in SENSITIVE_ACTION_TERMS)


def appears_to_contain_secret(text: str) -> bool:
    normalized = text.casefold()
    return any(pattern.casefold() in normalized for pattern in SECRET_PATTERNS)


def has_evidence_marker(text: str) -> bool:
    normalized = text.casefold()
    return "evidence" in normalized or "observed" in normalized or "source:" in normalized


def claims_unsupported_completion(text: str) -> bool:
    normalized = text.casefold()
    return any(claim in normalized for claim in UNSUPPORTED_COMPLETION_CLAIMS) and not has_evidence_marker(text)
