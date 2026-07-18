"""Policy predicates used by SDK tools and guardrails."""

from __future__ import annotations

import re

from .models import FinalVerdict, FindingSeverity, Verdict


SENSITIVE_ACTIONS = frozenset(
    {
        "authentication",
        "authorization",
        "secret_access",
        "sensitive_data",
        "database_migration",
        "dependency_change",
        "third_party_script",
        "tracking",
        "production_change",
        "deployment",
        "publication",
        "billing",
        "signing",
        "submission",
        "git_mutation",
        "destructive_action",
    }
)

PROHIBITED_AUTOMATIC_ACTIONS = frozenset(
    {
        "execute_command",
        "install_dependency",
        "git_mutation",
        "deploy",
        "publish",
        "authenticate",
        "expose_secret",
        "spend",
        "sign",
        "submit",
        "destructive_action",
    }
)

SECRET_PATTERNS = (
    re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"\b(?:api[_-]?key|token|secret|password)\s*[:=]\s*['\"]?[^'\"\s,;]{8,}", re.I),
    re.compile(r"https?://[^/\s]+:[^@\s]+@"),
)

PROHIBITED_TERMS = (
    "rm -rf",
    "delete everything",
    "drop database",
    "deploy",
    "publish",
    "push commit",
    "git push",
    "merge pull request",
    "install dependency",
    "npm install",
    "pip install",
    "run shell",
    "execute command",
)

OUT_OF_SCOPE_TERMS = (
    "mobile app",
    "ios app",
    "android app",
    "kubernetes cluster",
    "cloud infrastructure",
    "marketing campaign",
)


def normalize_action(action: str) -> str:
    return action.strip().lower().replace("-", "_").replace(" ", "_")


def requires_human_approval(action: str) -> bool:
    normalized = normalize_action(action)
    return normalized in SENSITIVE_ACTIONS or normalized in PROHIBITED_AUTOMATIC_ACTIONS


def contains_secret(text: str) -> bool:
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def describes_prohibited_action(text: str) -> bool:
    lowered = text.lower()
    return any(term in lowered for term in PROHIBITED_TERMS)


def describes_out_of_scope_request(text: str) -> bool:
    lowered = text.lower()
    return any(term in lowered for term in OUT_OF_SCOPE_TERMS)


def final_verdict_is_valid(verdict: FinalVerdict) -> list[str]:
    errors: list[str] = []
    blocking_findings = [
        finding
        for finding in verdict.findings
        if finding.blocking and finding.severity in {FindingSeverity.CRITICAL, FindingSeverity.HIGH}
    ]
    blocking_risks = [risk for risk in verdict.unresolved_risks if risk.blocking]
    if verdict.verdict is Verdict.PASS and blocking_findings:
        errors.append("PASS is invalid with unresolved critical or high blocking findings")
    if verdict.verdict is Verdict.PASS and blocking_risks:
        errors.append("PASS is invalid with unresolved blocking risks")
    if verdict.verdict is Verdict.PASS and not verdict.evidence:
        errors.append("PASS is invalid without evidence")
    if verdict.verdict is Verdict.PASS and any(item.status is Verdict.NOT_EXECUTED for item in verdict.evidence):
        errors.append("PASS is invalid when required evidence is NOT_EXECUTED")
    return errors
