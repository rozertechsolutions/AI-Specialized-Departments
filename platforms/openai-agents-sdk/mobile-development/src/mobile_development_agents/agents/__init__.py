from __future__ import annotations

from typing import Any

from mobile_development_agents.agents import (
    android_engineer,
    flutter_engineer,
    ios_engineer,
    kmp_engineer,
    mobile_architect,
    mobile_code_reviewer,
    mobile_performance_reviewer,
    mobile_release_engineer,
    mobile_security_reviewer,
    mobile_test_engineer,
    mobile_ui_accessibility_reviewer,
    react_native_engineer,
)
from mobile_development_agents.agents.definitions import ROLE_SPECS, SPECIALIST_NAMES, RoleSpec
from mobile_development_agents.config import MobileAgentsConfig


AGENT_BUILDERS = {
    "mobile-architect": mobile_architect.build_agent,
    "android-engineer": android_engineer.build_agent,
    "ios-engineer": ios_engineer.build_agent,
    "kmp-engineer": kmp_engineer.build_agent,
    "flutter-engineer": flutter_engineer.build_agent,
    "react-native-engineer": react_native_engineer.build_agent,
    "mobile-test-engineer": mobile_test_engineer.build_agent,
    "mobile-security-reviewer": mobile_security_reviewer.build_agent,
    "mobile-ui-accessibility-reviewer": mobile_ui_accessibility_reviewer.build_agent,
    "mobile-performance-reviewer": mobile_performance_reviewer.build_agent,
    "mobile-release-engineer": mobile_release_engineer.build_agent,
    "mobile-code-reviewer": mobile_code_reviewer.build_agent,
}


def build_all_specialists(config: MobileAgentsConfig | None = None) -> dict[str, Any]:
    return {name: builder(config) for name, builder in AGENT_BUILDERS.items()}


__all__ = ["AGENT_BUILDERS", "ROLE_SPECS", "SPECIALIST_NAMES", "RoleSpec", "build_all_specialists"]
