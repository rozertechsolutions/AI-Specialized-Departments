"""Context-aware read-only function tools for the Web Development department."""

from __future__ import annotations

from typing import Any

from agents import RunContextWrapper, function_tool

from .guardrails import (
    no_prohibited_tool_arguments,
    no_secret_tool_arguments,
    no_unsupported_success_claims,
)
from .models import EvidenceType, Verdict, WebDevelopmentRunContext
from .policy import MAX_TOOL_READ_BYTES, add_evidence, normalize_path


def _ctx(wrapper: RunContextWrapper[WebDevelopmentRunContext]) -> WebDevelopmentRunContext:
    context = wrapper.context
    if not isinstance(context, WebDevelopmentRunContext):
        raise ValueError("trusted WebDevelopmentRunContext is required")
    return context


@function_tool(
    tool_output_guardrails=[no_unsupported_success_claims],
)
def list_snapshot_files(ctx: RunContextWrapper[WebDevelopmentRunContext]) -> dict[str, Any]:
    """List trusted in-memory snapshot paths without reading the real filesystem."""
    context = _ctx(ctx)
    paths = [file.path for file in context.snapshot.files]
    evidence = add_evidence(
        context,
        "application-tool",
        EvidenceType.SNAPSHOT_LIST,
        None,
        "list_snapshot_files",
        paths,
        Verdict.PASS,
        False,
    )
    return {"paths": paths, "evidence_id": evidence.evidence_id}


@function_tool(
    tool_input_guardrails=[no_secret_tool_arguments],
    tool_output_guardrails=[no_unsupported_success_claims],
)
def read_snapshot_file(ctx: RunContextWrapper[WebDevelopmentRunContext], path: str) -> dict[str, Any]:
    """Read a trusted in-memory snapshot file by canonical logical path."""
    context = _ctx(ctx)
    normalized = normalize_path(path)
    matches = [file for file in context.snapshot.files if file.path == normalized]
    if not matches:
        raise ValueError("snapshot path is not available")
    file = matches[0]
    content = file.content[:MAX_TOOL_READ_BYTES]
    evidence = add_evidence(
        context,
        "application-tool",
        EvidenceType.SNAPSHOT_READ,
        None,
        "read_snapshot_file",
        [normalized],
        Verdict.PASS,
        False,
    )
    return {
        "path": normalized,
        "content": content,
        "truncated": len(file.content) > MAX_TOOL_READ_BYTES,
        "evidence_id": evidence.evidence_id,
    }


@function_tool(tool_output_guardrails=[no_unsupported_success_claims])
def inspect_snapshot_metadata(ctx: RunContextWrapper[WebDevelopmentRunContext]) -> dict[str, Any]:
    """Return trusted snapshot metadata without exposing full file content."""
    context = _ctx(ctx)
    extensions: dict[str, int] = {}
    total_bytes = 0
    for file in context.snapshot.files:
        suffix = file.path.rsplit(".", 1)[-1] if "." in file.path else ""
        extensions[suffix] = extensions.get(suffix, 0) + 1
        total_bytes += len(file.content.encode("utf-8", "surrogatepass"))
    evidence = add_evidence(
        context,
        "application-tool",
        EvidenceType.SNAPSHOT_LIST,
        None,
        "inspect_snapshot_metadata",
        [file.path for file in context.snapshot.files],
        Verdict.PASS,
        False,
    )
    return {
        "file_count": len(context.snapshot.files),
        "total_bytes": total_bytes,
        "extensions": extensions,
        "evidence_id": evidence.evidence_id,
    }


@function_tool(
    tool_input_guardrails=[no_secret_tool_arguments, no_prohibited_tool_arguments],
    tool_output_guardrails=[no_unsupported_success_claims],
)
def draft_scoped_proposal(ctx: RunContextWrapper[WebDevelopmentRunContext], summary: str, affected_paths: list[str]) -> dict[str, Any]:
    """Draft a non-mutating proposal bound to trusted task scope and snapshot paths."""
    context = _ctx(ctx)
    snapshot_paths = {file.path for file in context.snapshot.files}
    normalized = [normalize_path(path) for path in affected_paths]
    unknown = [path for path in normalized if path not in snapshot_paths and path not in context.scope.affected_paths]
    if unknown:
        raise ValueError("proposal references paths outside trusted scope or snapshot")
    evidence = add_evidence(
        context,
        "application-tool",
        EvidenceType.STATIC_VALIDATION,
        None,
        "draft_scoped_proposal",
        normalized,
        Verdict.PASS,
        False,
    )
    return {
        "summary": summary,
        "affected_paths": normalized,
        "execution": "not performed",
        "evidence_id": evidence.evidence_id,
    }


@function_tool(
    needs_approval=True,
    tool_input_guardrails=[no_secret_tool_arguments, no_prohibited_tool_arguments],
    tool_output_guardrails=[no_unsupported_success_claims],
)
def request_sensitive_transition(ctx: RunContextWrapper[WebDevelopmentRunContext], action_id: str) -> dict[str, Any]:
    """Request approval for a non-executing sensitive transition already created by preflight."""
    context = _ctx(ctx)
    matches = [action for action in context.sensitive_action_ledger if action.action_id == action_id]
    if not matches:
        raise ValueError("unknown sensitive action ID")
    action = matches[0]
    return {
        "approval_required": True,
        "action_id": action.action_id,
        "requested_transition": action.requested_transition,
        "execution": "not performed",
    }


READ_CONTEXT_TOOLS = [list_snapshot_files, read_snapshot_file, inspect_snapshot_metadata]
PROPOSAL_TOOLS = [draft_scoped_proposal]
SENSITIVE_ACTION_TOOLS = [request_sensitive_transition]
