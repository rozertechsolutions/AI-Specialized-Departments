from __future__ import annotations

from typing import Any


def build_optional_session(session_id: str, enabled: bool) -> Any | None:
    if not enabled:
        return None
    try:
        from agents import SQLiteSession
    except ImportError as exc:
        raise RuntimeError("Install openai-agents to enable SDK sessions.") from exc
    return SQLiteSession(session_id)
