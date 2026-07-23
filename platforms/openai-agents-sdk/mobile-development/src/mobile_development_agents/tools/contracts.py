from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from mobile_development_agents.context import ActionRisk
from mobile_development_agents.policies.security import (
    contains_secret,
    redact_secrets,
    validate_relative_project_path,
    validate_shell_command,
)
from mobile_development_agents.tools.approvals import (
    ApprovalProvider,
    ApprovalRequest,
    require_approval,
)


@dataclass(frozen=True, slots=True)
class ToolResult:
    ok: bool
    output: str
    evidence: str


class ToolHost(Protocol):
    def read_project_file(self, path: str) -> ToolResult:
        """Read a project-relative file."""

    def edit_project_file(self, path: str, content: str) -> ToolResult:
        """Apply a scoped project edit."""

    def run_validation_command(self, command: str) -> ToolResult:
        """Run a discovered, non-destructive validation command."""


@dataclass(slots=True)
class GuardedToolHost:
    host: ToolHost
    approvals: ApprovalProvider | None = None

    def read_project_file(self, path: str) -> ToolResult:
        findings = validate_relative_project_path(path)
        if any(f.blocked for f in findings):
            return ToolResult(False, "; ".join(f.message for f in findings), "path guard")
        result = self.host.read_project_file(path)
        return ToolResult(result.ok, redact_secrets(result.output), result.evidence)

    def edit_project_file(self, path: str, content: str) -> ToolResult:
        findings = validate_relative_project_path(path)
        if any(f.blocked for f in findings):
            return ToolResult(False, "; ".join(f.message for f in findings), "path guard")
        if contains_secret(content):
            return ToolResult(False, "Edit content appears to contain a secret.", "secret guard")
        if self.approvals is not None:
            require_approval(
                self.approvals,
                ApprovalRequest("edit project file", ActionRisk.PROJECT_EDIT, f"edit {path}"),
            )
        result = self.host.edit_project_file(path, content)
        return ToolResult(result.ok, redact_secrets(result.output), result.evidence)

    def run_validation_command(self, command: str) -> ToolResult:
        findings = validate_shell_command(command)
        if any(f.blocked for f in findings):
            return ToolResult(False, "; ".join(f.message for f in findings), "command guard")
        result = self.host.run_validation_command(command)
        return ToolResult(result.ok, redact_secrets(result.output), result.evidence)
