from __future__ import annotations

from agents import Runner

from .agents import department_lead
from .context import MarketingContext
from .models import WorkOutput


WORKFLOWS: dict[str, list[str]] = {'marketing-strategy-development': ['Validate brief', 'Research market, audience, and competitors', 'Define objectives and positioning', 'Select channel roles and initiatives', 'Define measurement, risk, and dependencies', 'Compliance review', 'Independent quality review', 'Prepare human approval'], 'market-audience-competitor-research': ['Define questions', 'Create source plan', 'Collect current evidence', 'Triangulate and normalize', 'Analyze segments and competitors', 'Document contradictions and limits', 'Independent quality review'], 'positioning-messaging': ['Validate product truth and audience evidence', 'Define category and differentiation', 'Draft value proposition', 'Build message hierarchy and proof points', 'Test objections and channel adaptability', 'Compliance review', 'Human brand/product approval'], 'product-launch-go-to-market': ['Confirm product and market readiness', 'Define objective and audience sequence', 'Align positioning and channels', 'Plan assets, timeline, owners, and dependencies', 'Define measurement and hold criteria', 'Localization and compliance review', 'Independent review', 'Prepare launch approval'], 'integrated-campaign-planning': ['Validate campaign brief', 'Confirm evidence and audience', 'Define message and channel roles', 'Build asset, timing, owner, and budget-scenario matrix', 'Define measurement and contingency', 'Localization when needed', 'Compliance review', 'Independent review', 'Prepare campaign approval'], 'content-program-planning': ['Define content jobs and questions', 'Prioritize themes and formats', 'Create briefs and calendar', 'Plan distribution, reuse, maintenance, and retirement', 'Define measurement', 'Rights/accessibility/localization checks', 'Human editorial approval'], 'marketing-copy-production-review': ['Validate brief and evidence', 'Draft copy', 'Adapt to channel and locale', 'Annotate claims and disclosures', 'SEO review when relevant', 'Compliance review', 'Independent review', 'Prepare content approval'], 'seo-strategy-planning': ['Validate market, site, and search evidence', 'Model search intent', 'Create topic and content-gap map', 'Define information architecture and briefs', 'Identify technical dependencies', 'Set measurement', 'Human content/site review'], 'social-media-planning': ['Validate objective, audience, and messages', 'Select channels and roles', 'Define pillars and formats', 'Build calendar and production plan', 'Define engagement, moderation, and escalation', 'Policy/accessibility/rights review', 'Prepare social approval'], 'email-lifecycle-campaign-planning': ['Validate consent, sender, and suppression', 'Define eligible segments', 'Map triggers, sequence, caps, exits, and fallbacks', 'Prepare copy requirements', 'Define tests and measurement', 'Compliance review', 'Prepare CRM approval'], 'paid-media-planning-review': ['Validate objective, budget owner, category, claims, and destination', 'Select platforms and placements', 'Define targeting, exclusions, and creative matrix', 'Create budget scenarios', 'Define measurement and brand safety', 'Policy/compliance review', 'Prepare budget/campaign approval'], 'cro-experimentation': ['Validate funnel and data', 'Diagnose friction', 'Create and prioritize hypotheses', 'Define experiment, eligibility, metrics, guardrails, sample assumptions, and stop rules', 'Technical feasibility review', 'Compliance/quality review', 'Prepare implementation approval'], 'campaign-performance-analysis': ['Validate data and metric definitions', 'Reproduce KPIs', 'Compare against plan and baseline', 'Assess plausible drivers and attribution limits', 'Document uncertainty', 'Recommend actions or tests', 'Independent quality review'], 'localization-international-release': ['Confirm source intent and market availability', 'Adapt language, culture, terminology, formats, and disclosures', 'Check product, channel, and policy context', 'Qualified local review', 'Compliance review', 'Independent review', 'Prepare local release approval'], 'marketing-compliance-review': ['Confirm independence and scope', 'Review privacy, consent, tracking, and targeting', 'Verify claims, disclosures, comparisons, and testimonials', 'Check rights, accessibility, policy, localization, and reputation', 'Classify findings and remediation', 'Escalate high-risk domains', 'Set review status'], 'final-campaign-approval-preparation': ['Collect validated brief and deliverables', 'Reconcile ownership and dependencies', 'Verify evidence and measurement', 'Confirm localization and compliance resolutions', 'Run independent quality gate', 'Record residual risk and requested human decision']}


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
