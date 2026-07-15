---
name: independent-assurance-review
description: Use to independently review high-impact cybersecurity GRC artifacts before human decisions, especially policy, risk acceptance, exception, supplier, compliance, maturity, reporting, and closure packages.
allowed-tools: Read Grep Glob
---

# Independent Assurance Review

Confirm reviewer independence, artifact purpose, creator, scope, evidence, assumptions, limitations, decision requested, and acceptance criteria. Use `independent-assurance-reviewer` to test traceability, evidence sufficiency, consistency, scope boundaries, assumptions, sensitive-data minimization, hidden residual risk, and completion claims.

Return one status: `ready_for_human_decision`, `returned_for_changes`, or `blocked`. Include defects with severity, affected claim, evidence gap, required correction, and decision impact.

Stop if reviewer independence is false, evidence is insufficient, the artifact exceeds its authority, or the user asks the AI to make a human-only decision.

