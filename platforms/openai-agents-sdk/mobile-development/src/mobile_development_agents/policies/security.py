from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import PurePosixPath, PureWindowsPath


SECRET_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)?PRIVATE KEY-----"),
    re.compile(r"\b(?:password|passwd|pwd|secret|token|api[_-]?key)\s*=\s*['\"][^'\"]{8,}['\"]", re.I),
    re.compile(r"\b[A-Za-z0-9_]*_SECRET[A-Za-z0-9_]*\s*=", re.I),
)

PUBLIC_MOBILE_CONFIG_KEYS: frozenset[str] = frozenset(
    {
        "google_app_id",
        "gcm_sender_id",
        "firebase_project_id",
        "firebase_storage_bucket",
        "android_package_name",
        "ios_bundle_id",
    }
)


@dataclass(frozen=True, slots=True)
class SecurityFinding:
    code: str
    message: str
    blocked: bool


def contains_secret(text: str) -> bool:
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def redact_secrets(text: str) -> str:
    redacted = text
    for pattern in SECRET_PATTERNS:
        redacted = pattern.sub("[REDACTED]", redacted)
    return redacted


def classify_env_key(key: str) -> str:
    normalized = key.strip().lower()
    if normalized in PUBLIC_MOBILE_CONFIG_KEYS:
        return "public-mobile-client-config"
    if any(part in normalized for part in ("secret", "token", "password", "private", "key")):
        return "secret"
    return "configuration"


def validate_relative_project_path(path: str) -> tuple[SecurityFinding, ...]:
    findings: list[SecurityFinding] = []
    if not path.strip():
        findings.append(SecurityFinding("empty-path", "Path must not be empty.", True))
    if "\x00" in path:
        findings.append(SecurityFinding("nul-byte", "Path contains a NUL byte.", True))
    if any(marker in path for marker in ("&&", "||", ";", "`", "$(", ">", "<", "|")):
        findings.append(SecurityFinding("command-syntax", "Path contains shell control syntax.", True))
    posix = PurePosixPath(path)
    windows = PureWindowsPath(path)
    if posix.is_absolute() or windows.is_absolute() or windows.drive:
        findings.append(SecurityFinding("absolute-path", "Path must be project-relative.", True))
    if ".." in posix.parts or ".." in windows.parts:
        findings.append(SecurityFinding("path-traversal", "Path traversal is not allowed.", True))
    return tuple(findings)


def validate_shell_command(command: str) -> tuple[SecurityFinding, ...]:
    findings: list[SecurityFinding] = []
    stripped = command.strip()
    if not stripped:
        findings.append(SecurityFinding("empty-command", "Command must not be empty.", True))
    blocked_tokens = ("&&", "||", ";", "|", "`", "$(", ">", "<", "\n", "\r")
    if any(token in stripped for token in blocked_tokens):
        findings.append(SecurityFinding("shell-control", "Command chaining, redirection, and substitution are blocked.", True))
    first = stripped.split(maxsplit=1)[0] if stripped else ""
    if first in {"rm", "rmdir", "del", "erase", "git"}:
        findings.append(SecurityFinding("destructive-or-git", "Destructive and Git commands require a separate human-controlled path.", True))
    if contains_secret(stripped):
        findings.append(SecurityFinding("secret-in-command", "Command appears to contain a secret.", True))
    return tuple(findings)
