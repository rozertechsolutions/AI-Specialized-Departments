from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True, slots=True)
class MobileAgentsConfig:
    """Runtime configuration that does not require API access during import."""

    model: str | None
    tracing_disabled: bool
    session_enabled: bool

    @classmethod
    def from_env(cls) -> "MobileAgentsConfig":
        disabled = os.getenv("OPENAI_AGENTS_DISABLE_TRACING", "1").strip().lower()
        return cls(
            model=os.getenv("OPENAI_AGENTS_MODEL") or None,
            tracing_disabled=disabled in {"1", "true", "yes", "on"},
            session_enabled=os.getenv("MOBILE_AGENTS_ENABLE_SESSION", "0").strip().lower()
            in {"1", "true", "yes", "on"},
        )
