from __future__ import annotations

from agents import Runner

from .agents import department_lead
from .context import MarketingContext
from .models import WorkOutput


WORKFLOWS: dict[str, list[str]] = {'marketing-engineering-discovery-architecture': ['Validate handoff', 'Inventory systems, data, environments, and owners', 'Model data flows and trust boundaries', 'Define architecture, acceptance tests, rollback, and access', 'Privacy/security review', 'Human scope approval'], 'tracking-event-implementation': ['Map metrics to events', 'Define schemas and identity boundaries', 'Implement or specify instrumentation', 'Validate triggers, payloads, duplication, and consent', 'Add monitoring and rollback', 'Independent QA', 'Prepare release approval'], 'consent-aware-analytics-deployment': ['Validate approved policy inputs', 'Define consent states and regions', 'Map tags and data flows to states', 'Implement or specify fail-safe gating', 'Test grant, deny, revoke, expiry, and failures', 'Privacy/security QA', 'Prepare deployment approval'], 'martech-integration-delivery': ['Validate purpose and owners', 'Define contracts, identities, preferences, deletion, and scopes', 'Implement or specify idempotency, retries, and observability', 'Test mapping, failures, replay, opt-out, and deletion', 'Security/privacy review', 'Runbook and rollback', 'Prepare activation approval'], 'landing-page-form-delivery': ['Validate content, design, and data purpose', 'Implement or specify accessible responsive experience', 'Implement secure form validation and minimization', 'Integrate consent-aware analytics', 'Test functionality, accessibility, performance, privacy, and security', 'Prepare deployment and rollback', 'Independent QA', 'Human release approval'], 'technical-seo-remediation': ['Validate site scope and indexation intent', 'Audit crawl, index, render, and performance', 'Prioritize findings', 'Implement or specify changes', 'Validate and define post-release checks', 'Prepare rollback', 'Independent QA', 'Human release approval'], 'experiment-implementation-validation': ['Freeze experiment contract', 'Implement assignment, flags, and exposure', 'Validate balance, persistence, contamination, metrics, and failure behavior', 'Configure monitoring and kill switch', 'Independent QA', 'Prepare launch/stop approval'], 'marketing-data-pipeline-dashboard-delivery': ['Validate contracts, metrics, and access', 'Implement or specify ingestion and transformation', 'Add lineage and quality tests', 'Build semantic metrics and dashboard', 'Validate reconciliation, freshness, and privacy', 'Add monitoring and recovery', 'Independent QA', 'Human access/release approval'], 'data-quality-observability-review': ['Identify critical data products', 'Define tests and SLOs', 'Implement or specify alerts and ownership', 'Test failure and recovery paths', 'Document incident and runbook process', 'Independent review'], 'final-technical-release-approval-preparation': ['Trace requirements to implementation and tests', 'Verify security, privacy, accessibility, and performance', 'Confirm observability and rollback', 'Reconcile findings and scope changes', 'Verify no secrets or production actions occurred', 'Set readiness state and requested human decision']}


async def run_marketing_request(
    request: str,
    *,
    context: MarketingContext,
    workflow: str | None = None,
) -> WorkOutput:
    """Run a request without preauthorizing external actions."""
    if workflow is not None and workflow not in WORKFLOWS:
        raise ValueError(f"Unknown workflow: {workflow}")
    workflow_context = ""
    if workflow is not None:
        stages = " -> ".join(WORKFLOWS[workflow])
        workflow_context = f"\nRequired workflow: {workflow}. Stages: {stages}"
    result = await Runner.run(
        department_lead,
        input=request + workflow_context,
        context=context,
    )
    return result.final_output
