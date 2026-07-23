from __future__ import annotations

from agents import RunConfig, set_tracing_disabled


def disable_hosted_tracing() -> None:
    set_tracing_disabled(True)


def offline_run_config() -> RunConfig:
    return RunConfig(
        tracing_disabled=True,
        trace_include_sensitive_data=False,
        workflow_name="data-ai-offline-construction",
    )
