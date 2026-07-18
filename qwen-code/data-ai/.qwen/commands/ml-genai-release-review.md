---
description: Review ML model, RAG, GenAI, agent-system, AI inference, independent evaluation, red-team, and release readiness.
---

# ML GenAI Release Review

1. Run `ml-genai-evaluation`.
2. Review ML data splits, leakage, representative slices, baselines, thresholds, calibration, documentation, RAG provenance, retrieval quality, groundedness, citations, agent tool allowlists, stop limits, approval boundaries, fallback, abstention, and human controls.
3. Route responsible AI and high-impact concerns to `data-ai-solution-governance-reviewer`.
4. Route operations, monitoring, risk acceptance, and rollback to `ops-risk-assurance-reviewer`.
5. Stop on fabricated metrics, missing evaluation evidence, unsafe tool use, unresolved red-team blockers, or model/provider calls.

Return release-readiness decision packet, evaluation gaps, safety risks, human approvals, blockers, and exactly `PASS`, `FAIL`, or `BLOCKED`.
