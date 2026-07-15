from __future__ import annotations

from typing import Any

from mobile_development_agents.agents.definitions import ROLE_SPECS, build_specialist_agent
from mobile_development_agents.config import MobileAgentsConfig


def build_agent(config: MobileAgentsConfig | None = None) -> Any:
    return build_specialist_agent(ROLE_SPECS["react-native-engineer"], config)
