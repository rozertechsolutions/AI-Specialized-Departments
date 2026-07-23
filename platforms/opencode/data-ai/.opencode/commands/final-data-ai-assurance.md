---
description: Perform final independent Data and AI evidence, separation-of-duties, risk, and completion assurance.
---

# Final Data and AI Assurance

## Workflow
1. `ops-risk-assurance-reviewer` confirms independence from the artifact being approved.
2. Trace requirements to owners, evidence, validation results, thresholds, unresolved risk, monitoring, rollback, documentation, and closure decision.
3. Verify that builders did not provide independent final approval and reviewers did not approve their own artifacts.
4. Verify unsupported capabilities were omitted rather than simulated and no active MCP/provider/plugin/credential configuration was added.
5. Stop on missing provenance, missing permitted-use evidence, fabricated metrics, unresolved critical findings, absent human approvals, or separation-of-duties conflicts.

## Output
Final assurance status, blockers, residual risk, human-only decisions, evidence gaps, and exactly `PASS`, `FAIL`, or `BLOCKED`.
