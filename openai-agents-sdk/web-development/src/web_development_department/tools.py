"""Safe in-memory function tools for the web department."""

from __future__ import annotations

import json
from dataclasses import asdict
from typing import Any

from agents import function_tool

from .guardrails import (
    no_prohibited_tool_arguments,
    no_secret_tool_arguments,
    no_unsupported_success_claims,
)
from .models import ApprovalRequest, FindingSeverity, RepositoryFile
from .policy import requires_human_approval


def _load_files(snapshot_json: str) -> list[RepositoryFile]:
    data = json.loads(snapshot_json or "{}")
    files = data.get("files", [])
    return [
        RepositoryFile(
            path=str(item.get("path", "")),
            content=str(item.get("content", "")),
            language=item.get("language"),
        )
        for item in files
        if isinstance(item, dict) and item.get("path")
    ]


@function_tool(
    tool_input_guardrails=[no_secret_tool_arguments],
    tool_output_guardrails=[no_unsupported_success_claims],
)
def inspect_repository_context(snapshot_json: str) -> dict[str, Any]:
    """Summarize caller-supplied in-memory repository content."""
    files = _load_files(snapshot_json)
    extensions: dict[str, int] = {}
    for file in files:
        suffix = file.path.rsplit(".", 1)[-1] if "." in file.path else ""
        extensions[suffix] = extensions.get(suffix, 0) + 1
    return {
        "file_count": len(files),
        "paths": [file.path for file in files],
        "extensions": extensions,
        "evidence": "caller-supplied in-memory snapshot only",
    }


@function_tool(
    tool_input_guardrails=[no_secret_tool_arguments, no_prohibited_tool_arguments],
    tool_output_guardrails=[no_unsupported_success_claims],
)
def draft_implementation_proposal(scope_json: str, snapshot_json: str) -> dict[str, Any]:
    """Draft a non-mutating implementation proposal from in-memory inputs."""
    scope = json.loads(scope_json or "{}")
    files = _load_files(snapshot_json)
    affected = scope.get("affected_paths") or [file.path for file in files[:10]]
    return {
        "summary": "Non-mutating implementation proposal only.",
        "affected_files": affected,
        "behavior": scope.get("goal", ""),
        "validation_plan": [
            "Run repository-native tests only after explicit caller authorization.",
            "Mark unavailable runtime, browser, deployment, and integration checks as NOT_EXECUTED.",
        ],
        "requires_approval": scope.get("requires_human_review", []),
    }


@function_tool(
    needs_approval=True,
    tool_input_guardrails=[no_secret_tool_arguments, no_prohibited_tool_arguments],
    tool_output_guardrails=[no_unsupported_success_claims],
)
def request_sensitive_action(action: str, rationale: str, affected_paths_json: str = "[]") -> dict[str, Any]:
    """Create an approval-gated request for a sensitive action without executing it."""
    affected_paths = json.loads(affected_paths_json or "[]")
    request = ApprovalRequest(
        action=action,
        rationale=rationale,
        affected_paths=[str(path) for path in affected_paths],
        risk_level=FindingSeverity.HIGH if requires_human_approval(action) else FindingSeverity.MEDIUM,
    )
    return {
        "approval_required": True,
        "request": asdict(request),
        "execution": "not performed",
    }


READ_CONTEXT_TOOLS = [inspect_repository_context]
PROPOSAL_TOOLS = [draft_implementation_proposal]
SENSITIVE_ACTION_TOOLS = [request_sensitive_action]
