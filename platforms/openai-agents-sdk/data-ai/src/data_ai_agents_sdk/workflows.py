from __future__ import annotations

from .models import WorkflowContract


WORKFLOWS: tuple[WorkflowContract, ...] = (
    WorkflowContract(
        name="use-case-intake-risk-triage",
        owner="data-ai-orchestrator",
        steps=("classify outcome and alternatives", "route specialist reviews", "collect evidence"),
        gates=("value hypothesis present", "risk classified", "human gates identified"),
    ),
    WorkflowContract(
        name="source-dataset-component-onboarding",
        owner="data-architecture-dataset-reviewer",
        steps=("verify provenance", "review contracts and semantics", "assess acceptance"),
        gates=("permitted use proven", "lineage present", "acceptance thresholds defined"),
    ),
    WorkflowContract(
        name="pipeline-data-product-quality",
        owner="data-platform-analytics-reviewer",
        steps=("review pipeline design", "verify lineage and quality", "assess observability"),
        gates=("owners defined", "SLOs present", "incident path documented"),
    ),
    WorkflowContract(
        name="analytics-metric-experiment-lifecycle",
        owner="data-platform-analytics-reviewer",
        steps=("review metric definitions", "assess statistical design", "check interpretation limits"),
        gates=("queries reproducible", "uncertainty stated", "causal claims supported"),
    ),
    WorkflowContract(
        name="ml-candidate-evaluation",
        owner="ml-genai-evaluation-reviewer",
        steps=("review features and splits", "compare baselines", "validate documentation"),
        gates=("leakage checked", "thresholds defined", "model card present"),
    ),
    WorkflowContract(
        name="genai-rag-agent-release-review",
        owner="ml-genai-evaluation-reviewer",
        steps=("review grounding", "assess tool risk", "verify fallback and human controls"),
        gates=("citations checked", "tool allowlist present", "stop limits defined"),
    ),
    WorkflowContract(
        name="ai-operations-risk-readiness",
        owner="ai-ops-risk-reviewer",
        steps=("review monitoring", "assess provider change response", "verify rollback and retirement"),
        gates=("drift monitored", "incident path present", "risk owner identified"),
    ),
    WorkflowContract(
        name="final-independent-assurance",
        owner="data-ai-assurance-reviewer",
        steps=("trace requirements", "verify separation of duties", "issue final status"),
        gates=("evidence complete", "critical findings closed", "human decisions explicit"),
    ),
)


def workflow_names() -> tuple[str, ...]:
    return tuple(workflow.name for workflow in WORKFLOWS)
