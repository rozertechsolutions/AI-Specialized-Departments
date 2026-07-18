---
name: ml-genai-system-evaluation
description: Review ML, GenAI, RAG, agent, prompt, retrieval, inference, evaluation, red-team, safety, and release-candidate evidence.
---

# ML, GenAI, and System Evaluation

## When to use

Use for ML model design, feature review, training validation, RAG/retrieval design, prompt and agent systems, inference contracts, evaluation, red teaming, safety testing, and release-candidate selection.

## Instructions

1. Confirm task, model role, training or prompt data, feature set, candidate versions, provider/model dependencies, inference contract, user controls, fallback, abstention, and latency/cost constraints.
2. Review leakage, contamination, splits, baselines, evaluation slices, calibration, uncertainty, robustness, fairness, privacy, security/safety behavior, and documentation.
3. For RAG and agents, require source provenance, retrieval relevance, coverage, groundedness, citation correctness, stale-source behavior, tool allowlists, input/output contracts, bounded delegation, loop limits, approval boundaries, and recoverability.
4. Separate builders from evaluation, red-team, risk, and release-readiness reviewers.
5. Return `PASS`, `FAIL`, or `BLOCKED` with thresholds, failed cases, residual risks, and required human review.
