from __future__ import annotations

from agents import Agent

from .guardrails import INDEPENDENCE_GUARDRAIL, SAFETY_GUARDRAIL


BASE_INSTRUCTIONS = (
    "You are a static Cybersecurity Area 06 agent. Use supplied evidence only. "
    "Separate evidence, fact, inference, hypothesis, recommendation, confidence, limitation, owner, "
    "approver, and independent reviewer. " + SAFETY_GUARDRAIL + " " + INDEPENDENCE_GUARDRAIL
)

incident_command_evidence_agent = Agent(
    name="incident-command-evidence",
    instructions=BASE_INSTRUCTIONS
    + " Own readiness, classification support, command support, logs, evidence preservation, manifests, and custody planning.",
    tools=[],
)

forensics_containment_recovery_agent = Agent(
    name="forensics-containment-recovery",
    instructions=BASE_INSTRUCTIONS
    + " Own forensic acquisition planning, containment and eradication options, secure recovery planning, validation, and stop conditions.",
    tools=[],
)

scenario_crisis_review_agent = Agent(
    name="scenario-crisis-review",
    instructions=BASE_INSTRUCTIONS
    + " Own scenario playbooks, crisis handoff, tabletop, post-incident review, corrective actions, and independent assurance.",
    tools=[],
)
