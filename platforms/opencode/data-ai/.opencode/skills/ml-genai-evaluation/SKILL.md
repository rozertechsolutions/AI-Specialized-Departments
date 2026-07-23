---
name: ml-genai-evaluation
description: Review ML, GenAI, RAG, agent, inference contract, safety, groundedness, and release-candidate evidence.
---

# ML GenAI Evaluation

## Procedure
1. Confirm purpose, inputs, outputs, users, baselines, features, splits, evaluation data, thresholds, lifecycle owner, risk owner, fallback, abstention, and human controls.
2. Review leakage, contamination, representative slices, fairness-relevant slices, uncertainty/calibration, robustness, failure modes, documentation, reproducibility, packaging, and monitoring needs.
3. For RAG, verify provenance, retrieval relevance, coverage, groundedness, citation correctness, conflict handling, stale-source behavior, and deletion propagation.
4. For agents, verify tool allowlists, contracts, bounded delegation, loop/stop limits, idempotency, approval boundaries, partial failure, and recoverability.
5. Return evaluation findings, safety gaps, release blockers, approvals, and exactly `PASS`, `FAIL`, or `BLOCKED`.
