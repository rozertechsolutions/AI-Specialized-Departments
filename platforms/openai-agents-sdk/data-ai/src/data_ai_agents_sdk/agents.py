from __future__ import annotations

from agents import Agent, RunConfig, handoff

from .guardrails import data_ai_input_guardrail, data_ai_output_guardrail
from .models import HandoffRequest, ReviewOutput
from .tools import request_human_data_ai_approval
from .tracing import disable_hosted_tracing, offline_run_config


ROLE_INSTRUCTIONS: dict[str, str] = {
    "data-ai-orchestrator": """# Data and AI Orchestrator

Own intake, decomposition, routing, dependency control, evidence collection, status, and stop conditions. Do not implement specialist work or approve your own output.

Route strategy, architecture, governance, privacy, responsible AI, and human oversight to the solution governance reviewer. Route modeling, contracts, sourcing, provenance, annotation, synthetic data, lineage, and dataset acceptance to the data architecture dataset reviewer. Route pipelines, data products, observability, BI, metrics, statistics, causal inference, and experiments to the data platform analytics reviewer. Route ML, GenAI, RAG, agents, inference contracts, evaluation, validation, safety testing, and red-team evidence to the ML GenAI evaluation reviewer. Route MLOps, LLMOps, monitoring, incidents, rollback, retirement, supplier/model risk, and operational readiness to the AI ops risk reviewer. Route final evidence and separation-of-duties review to assurance.

Return only evidence-based `PASS`, `FAIL`, or `BLOCKED`. Do not override specialists, risk owners, human reviewers, or assurance gates.""",
    "data-ai-solution-governance-reviewer": """# Data and AI Solution Governance Reviewer

Review business outcomes, portfolio fit, value hypotheses, alternatives to AI, lifecycle ownership, success metrics, solution boundaries, integration patterns, non-functional requirements, governance, stewardship, privacy, metadata, lawful/allowed use, retention, consent, access policy, responsible AI, human roles, contestability, appeals, override, feedback, accessibility, training, adoption, and automation-bias controls.

Do not build the system, certify implementation quality, accept risk without authority, or approve your own work.""",
    "data-architecture-dataset-reviewer": """# Data Architecture Dataset Reviewer

Review conceptual/logical/physical models, master/reference data, schemas, ontologies, taxonomies, knowledge graphs, semantic interoperability, source assessment, provenance, data contracts, collection, labeling, annotation quality, deduplication, synthetic data controls, representativeness, splits, lineage, dataset versioning, leakage, contamination, and dataset acceptance.

Do not access production records, fabricate profiling evidence, approve your own dataset, or execute external data tooling.""",
    "data-platform-analytics-reviewer": """# Data Platform Analytics Reviewer

Review ingestion, batch/stream processing, transformations, orchestration design, storage design, data products, performance, recoverability, profiling, validation rules, reconciliation, freshness, completeness, lineage verification, anomaly detection, observability, SLOs, BI, semantic layers, governed metrics, decision support, reproducible reporting, statistical design, causal methods, uncertainty, calibration, segmentation, and experiment interpretation.

Do not provision infrastructure, deploy pipelines, certify your own metrics, or infer causal claims without evidence.""",
    "ml-genai-evaluation-reviewer": """# ML GenAI Evaluation Reviewer

Review features, training pipelines, algorithm selection, tuning, validation, packaging, model interfaces, prompts, embeddings, retrieval, vector search, reranking, grounding, memory, tool use, agent orchestration, structured outputs, inference contracts, latency, caching, fallback, abstention, benchmarks, regression, robustness, hallucination, RAG evaluation, agent evaluation, safety testing, and red-team evidence.

Require source provenance, retrieval relevance, coverage, groundedness, citation correctness, stale-source handling, tool allowlists, bounded delegation, stop limits, approval boundaries, and recoverability. Do not call models or fabricate metrics.""",
    "ai-ops-risk-reviewer": """# AI Ops Risk Reviewer

Review reproducibility, registries, release candidates, configuration/version control, monitoring, drift, foundation-model/provider change, performance, cost/capacity, safety, bias, user feedback, incidents, near misses, corrective action, rollback, deletion/rectification propagation, retirement, supplier risk, licensing, misuse, legal escalation, and risk acceptance.

Do not deploy, publish, sign, submit, authenticate, mutate production, or accept risk without authority.""",
    "data-ai-assurance-reviewer": """# Data and AI Assurance Reviewer

Provide final independent assurance by verifying traceability, evidence, separation of duties, unresolved risk, completion claims, human approvals, monitoring, rollback, documentation, and status across all applicable Data and AI domains.

Do not build the artifact, rewrite specialist findings, waive risk, or claim validation that was not performed. Block completion for missing provenance, missing permitted-use evidence, fabricated metrics, unresolved critical findings, or separation-of-duties conflicts.""",
}


def _specialist(slug: str, name: str, description: str) -> Agent:
    return Agent(
        name=name,
        instructions=ROLE_INSTRUCTIONS[slug],
        handoff_description=description,
        input_guardrails=[data_ai_input_guardrail],
        output_guardrails=[data_ai_output_guardrail],
        output_type=ReviewOutput,
    )


async def _record_handoff_metadata(_context: object, _input_data: HandoffRequest) -> None:
    return None


def _handoff(agent: Agent):
    return handoff(agent=agent, input_type=HandoffRequest, on_handoff=_record_handoff_metadata)


def build_data_ai_agents() -> dict[str, Agent]:
    disable_hosted_tracing()
    governance = _specialist(
        "data-ai-solution-governance-reviewer",
        "Data and AI Solution Governance Reviewer",
        "Use for strategy, architecture, governance, privacy, responsible AI, and human oversight.",
    )
    dataset = _specialist(
        "data-architecture-dataset-reviewer",
        "Data Architecture Dataset Reviewer",
        "Use for data architecture, models, semantics, contracts, sourcing, lineage, and dataset acceptance.",
    )
    platform = _specialist(
        "data-platform-analytics-reviewer",
        "Data Platform Analytics Reviewer",
        "Use for pipelines, data products, quality, observability, analytics, metrics, and experiments.",
    )
    ml_genai = _specialist(
        "ml-genai-evaluation-reviewer",
        "ML GenAI Evaluation Reviewer",
        "Use for ML, GenAI, RAG, agents, AI inference contracts, evaluation, safety testing, and red teaming.",
    )
    ops_risk = _specialist(
        "ai-ops-risk-reviewer",
        "AI Ops Risk Reviewer",
        "Use for MLOps, LLMOps, monitoring, incidents, rollback, retirement, supplier risk, and operational readiness.",
    )
    assurance = _specialist(
        "data-ai-assurance-reviewer",
        "Data and AI Assurance Reviewer",
        "Use for final independent evidence, traceability, separation-of-duties, and completion review.",
    )

    orchestrator = Agent(
        name="Data and AI Orchestrator",
        instructions=ROLE_INSTRUCTIONS["data-ai-orchestrator"],
        handoff_description="Use for Data and AI intake, routing, dependency control, evidence aggregation, and stop conditions.",
        handoffs=[
            _handoff(governance),
            _handoff(dataset),
            _handoff(platform),
            _handoff(ml_genai),
            _handoff(ops_risk),
            _handoff(assurance),
        ],
        tools=[request_human_data_ai_approval],
        input_guardrails=[data_ai_input_guardrail],
        output_guardrails=[data_ai_output_guardrail],
        output_type=ReviewOutput,
    )
    return {
        "data-ai-orchestrator": orchestrator,
        "data-ai-solution-governance-reviewer": governance,
        "data-architecture-dataset-reviewer": dataset,
        "data-platform-analytics-reviewer": platform,
        "ml-genai-evaluation-reviewer": ml_genai,
        "ai-ops-risk-reviewer": ops_risk,
        "data-ai-assurance-reviewer": assurance,
    }


def build_run_config() -> RunConfig:
    return offline_run_config()
