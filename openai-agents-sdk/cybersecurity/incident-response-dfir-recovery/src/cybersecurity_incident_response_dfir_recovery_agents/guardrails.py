from __future__ import annotations

SAFETY_GUARDRAIL = (
    "Static planning only. Refuse live-system access, evidence collection, forensic tooling, "
    "malware handling, containment, restoration, credential or key rotation, external notification, "
    "ransom negotiation, incident declaration, residual-risk acceptance, and incident closure."
)

INDEPENDENCE_GUARDRAIL = (
    "Critical conclusions, recovery claims, residual-risk notes, corrective-action closure, and "
    "incident closure require independent review by an agent or human who did not create the artifact."
)
