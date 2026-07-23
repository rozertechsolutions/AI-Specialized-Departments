---
name: ml-genai-evaluation
description: Evaluate ML, GenAI, RAG, agent, and AI application behavior against quality, safety, groundedness, and readiness criteria.
---

# ML and GenAI Evaluation

Use this Skill for model selection, ML validation, RAG evaluation, prompt changes, agent-tool workflows, inference contracts, and AI application readiness.

## Procedure
1. Define task, users, model/application contract, inputs, outputs, abstention/fallback behavior, latency/cost limits, and human controls.
2. Review features, training data, evaluation data, leakage controls, representative slices, baselines, thresholds, uncertainty, calibration, and model documentation.
3. For RAG, check source provenance, retrieval relevance, coverage, groundedness, citation correctness, conflict handling, and stale-source behavior.
4. For agents, check tool allowlists, input/output contracts, bounded delegation, loop/stop limits, idempotency, approval boundaries, partial failure, and recoverability.
5. Include robustness, safety, hallucination, prompt-injection, tool-poisoning, privacy, bias, misuse, supplier, and provider-change tests where applicable.
6. Return `PASS`, `FAIL`, or `BLOCKED` with release blockers, residual risks, and required independent review.

Never replace missing evaluation evidence with intuition or unverified examples.
