---
name: ml-genai-evaluation
description: Evaluate data science, experiments, ML systems, RAG, GenAI, agents, inference contracts, validation, red-team findings, and model candidate evidence.
---

# ML GenAI Evaluation

Use this skill for statistical studies, experiments, ML model development, RAG/GenAI systems, agents, tool use, inference contracts, benchmark design, safety testing, and candidate selection. Keep evaluation independent from implementation.

## Steps

1. For studies, define hypothesis, unit, population, design, confounders, causal assumptions, power or precision, uncertainty, calibration, segmentation, guardrails, and interpretation limits.
2. For ML, review feature provenance, leakage controls, splits, algorithms, tuning, baselines, evaluation slices, robustness, calibration, packaging, interface, and model documentation.
3. For RAG and GenAI, review prompts, knowledge sources, embeddings, retrieval, reranking, grounding, citations, conflict handling, stale-source behavior, hallucination tests, and fallback/abstention criteria.
4. For agents, review tool allowlists, input/output contracts, bounded delegation, loop limits, stop conditions, idempotency, approvals, injection/poisoning/exfiltration controls, partial failures, and recoverability.
5. Return evaluation design or results, thresholds, findings, evidence gaps, risk review needs, release recommendation, and independent reviewer.

## Acceptance Gates

- Baselines, thresholds, representative slices, failure modes, uncertainty, and calibration are explicit.
- RAG and agent safety controls are tested or blocked for missing evidence.
- Builder and final evaluator are separate.
- Final status is `PASS`, `FAIL`, or `BLOCKED`.
