"""Shared helpers for local mobile-development guard hooks."""

from __future__ import annotations

import base64
import os
import re
import shlex
from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    severity: str = "block"


SHELL_META_PATTERN = re.compile(r"(\|\||&&|[|;<>`]|\$\(|\${)")
WINDOWS_ABSOLUTE_PATTERN = re.compile(r"^[a-zA-Z]:[\\/]")
POSIX_ABSOLUTE_PATTERN = re.compile(r"^/")


def split_command(command: str) -> list[str]:
    if not isinstance(command, str) or not command.strip():
        raise ValueError("command must be a non-empty string")
    return shlex.split(command, posix=True)


def has_shell_metacharacters(command: str) -> bool:
    return bool(SHELL_META_PATTERN.search(command))


def contains_encoded_payload(value: str) -> bool:
    compact = re.sub(r"\s+", "", value or "")
    if len(compact) < 16 or len(compact) % 4:
        return False
    if not re.fullmatch(r"[A-Za-z0-9+/]+={0,2}", compact):
        return False
    try:
        decoded = base64.b64decode(compact, validate=True)
    except Exception:
        return False
    if not decoded:
        return False
    text = decoded.decode("utf-8", errors="ignore").lower()
    return any(marker in text for marker in ("rm ", "curl ", "token", "apikey", "api_key", "password", "secret"))


def normalize_relative_path(root: str, path: str) -> str:
    if not isinstance(root, str) or not root:
        raise ValueError("root must be a non-empty string")
    if not isinstance(path, str) or not path:
        raise ValueError("path must be a non-empty string")
    if "\x00" in path:
        raise ValueError("path contains NUL byte")
    if WINDOWS_ABSOLUTE_PATTERN.match(path) or POSIX_ABSOLUTE_PATTERN.match(path):
        raise ValueError("absolute paths are not allowed")
    normalized_root = os.path.abspath(root)
    candidate = os.path.abspath(os.path.join(normalized_root, path))
    if os.path.commonpath([normalized_root, candidate]) != normalized_root:
        raise ValueError("path escapes root")
    return candidate


def any_contains(values: Iterable[str], needles: Sequence[str]) -> bool:
    lowered = " ".join(values).lower()
    return any(needle in lowered for needle in needles)
