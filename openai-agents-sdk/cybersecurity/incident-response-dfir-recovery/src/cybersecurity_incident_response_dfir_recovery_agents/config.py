from __future__ import annotations

SPECIALIZATION_ID = "cybersecurity.incident-response-dfir-recovery"
STATIC_ONLY = True
EXTERNAL_INTEGRATIONS_ENABLED = False
TOOLS_ENABLED = False
HUMAN_DECISIONS: tuple[str, ...] = (
    "incident declaration",
    "command assignment",
    "evidence acquisition",
    "destructive action",
    "recovery acceptance",
    "legal position",
    "privacy position",
    "public communication",
    "residual risk acceptance",
    "corrective action closure",
    "incident closure",
)
