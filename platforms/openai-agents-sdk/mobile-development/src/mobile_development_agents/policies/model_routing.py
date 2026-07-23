from __future__ import annotations

from dataclasses import dataclass

from mobile_development_agents.config import MobileAgentsConfig


@dataclass(frozen=True, slots=True)
class ModelRoute:
    role: str
    model: str | None
    reason: str


def route_model(role: str, config: MobileAgentsConfig | None = None) -> ModelRoute:
    resolved = config or MobileAgentsConfig.from_env()
    if resolved.model:
        return ModelRoute(role=role, model=resolved.model, reason="Model supplied by OPENAI_AGENTS_MODEL.")
    return ModelRoute(role=role, model=None, reason="No hardcoded model; SDK/provider default is used.")
