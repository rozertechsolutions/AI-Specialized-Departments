from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import PurePath


class MobileTechnology(str, Enum):
    ANDROID = "android"
    IOS = "ios"
    KMP = "kmp"
    FLUTTER = "flutter"
    REACT_NATIVE = "react-native"


class ActionRisk(str, Enum):
    ROUTINE_READ = "routine-read"
    PROJECT_EDIT = "project-edit"
    SECURITY_SENSITIVE = "security-sensitive"
    RELEASE_SENSITIVE = "release-sensitive"
    EXTERNAL_WRITE = "external-write"
    DESTRUCTIVE = "destructive"


@dataclass(frozen=True, slots=True)
class MobileProjectContext:
    project_root: PurePath
    technologies: frozenset[MobileTechnology]
    package_manager: str | None = None
    build_system: str | None = None
    detected_commands: tuple[str, ...] = ()
    constraints: tuple[str, ...] = ()
    evidence: tuple[str, ...] = ()

    def supports(self, technology: MobileTechnology) -> bool:
        return technology in self.technologies


@dataclass(frozen=True, slots=True)
class WorkflowRequest:
    workflow: str
    objective: str
    technologies: frozenset[MobileTechnology]
    project_context: MobileProjectContext
    human_approvals: frozenset[str] = field(default_factory=frozenset)
    cancellation_requested: bool = False

    def requires_technology(self, technology: MobileTechnology) -> bool:
        return technology in self.technologies


@dataclass(slots=True)
class SDKWorkflowContext:
    request: WorkflowRequest
    tool_host: object | None = None
    approval_audit: list[str] = field(default_factory=list)
