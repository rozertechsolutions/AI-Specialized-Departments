from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import PurePath
from typing import Any, Mapping


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

    def to_json_dict(self) -> dict[str, Any]:
        return {
            "project_root": str(self.project_root),
            "technologies": sorted(technology.value for technology in self.technologies),
            "package_manager": self.package_manager,
            "build_system": self.build_system,
            "detected_commands": list(self.detected_commands),
            "constraints": list(self.constraints),
            "evidence": list(self.evidence),
        }

    @classmethod
    def from_json_dict(cls, data: Mapping[str, Any]) -> "MobileProjectContext":
        technologies = data.get("technologies", ())
        if not isinstance(technologies, list):
            raise ValueError("project context technologies must be a list")
        return cls(
            project_root=PurePath(str(data.get("project_root", ""))),
            technologies=frozenset(MobileTechnology(str(value)) for value in technologies),
            package_manager=_optional_string(data.get("package_manager")),
            build_system=_optional_string(data.get("build_system")),
            detected_commands=_string_tuple(data.get("detected_commands", ())),
            constraints=_string_tuple(data.get("constraints", ())),
            evidence=_string_tuple(data.get("evidence", ())),
        )


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

    def to_json_dict(self) -> dict[str, Any]:
        return {
            "workflow": self.workflow,
            "objective": self.objective,
            "technologies": sorted(technology.value for technology in self.technologies),
            "project_context": self.project_context.to_json_dict(),
            "human_approvals": sorted(self.human_approvals),
            "cancellation_requested": self.cancellation_requested,
        }

    @classmethod
    def from_json_dict(cls, data: Mapping[str, Any]) -> "WorkflowRequest":
        technologies = data.get("technologies", ())
        if not isinstance(technologies, list):
            raise ValueError("workflow technologies must be a list")
        project_context = data.get("project_context", {})
        if not isinstance(project_context, Mapping):
            raise ValueError("project_context must be an object")
        return cls(
            workflow=str(data.get("workflow", "")),
            objective=str(data.get("objective", "")),
            technologies=frozenset(MobileTechnology(str(value)) for value in technologies),
            project_context=MobileProjectContext.from_json_dict(project_context),
            human_approvals=frozenset(_string_tuple(data.get("human_approvals", ()))),
            cancellation_requested=bool(data.get("cancellation_requested", False)),
        )


@dataclass(slots=True)
class SDKWorkflowContext:
    request: WorkflowRequest
    tool_host: object | None = None
    approval_audit: list[str] = field(default_factory=list)

    def to_json_dict(self) -> dict[str, Any]:
        return {
            "schema": "mobile-development-sdk-workflow-context.v1",
            "request": self.request.to_json_dict(),
            "approval_audit": list(self.approval_audit),
        }

    @classmethod
    def from_json_dict(
        cls,
        data: Mapping[str, Any],
        *,
        tool_host: object | None = None,
    ) -> "SDKWorkflowContext":
        if data.get("schema") != "mobile-development-sdk-workflow-context.v1":
            raise ValueError("unsupported SDK workflow context schema")
        request = data.get("request", {})
        if not isinstance(request, Mapping):
            raise ValueError("request must be an object")
        return cls(
            request=WorkflowRequest.from_json_dict(request),
            tool_host=tool_host,
            approval_audit=list(_string_tuple(data.get("approval_audit", ()))),
        )


def _optional_string(value: object) -> str | None:
    return None if value is None else str(value)


def _string_tuple(value: object) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)):
        raise ValueError("expected a list of strings")
    return tuple(str(item) for item in value)


def serialize_sdk_context(context: object) -> dict[str, Any]:
    if not isinstance(context, SDKWorkflowContext):
        raise TypeError("Run state context must be SDKWorkflowContext")
    return context.to_json_dict()


def deserialize_sdk_context(data: object) -> SDKWorkflowContext:
    if not isinstance(data, Mapping):
        raise TypeError("Serialized SDK workflow context must be an object")
    return SDKWorkflowContext.from_json_dict(data)
