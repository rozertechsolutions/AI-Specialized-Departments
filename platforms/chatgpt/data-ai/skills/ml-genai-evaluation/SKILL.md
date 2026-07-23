---
name: ml-genai-evaluation
description: Use for data science, experimentation, ML engineering, RAG, GenAI, agent systems, inference contracts, validation, safety tests, red-team review, and candidate selection evidence.
---

# ML GenAI Evaluation

Use this skill when designing, comparing, validating, or reviewing statistical studies, experiments, ML models, RAG systems, prompts, agent workflows, tools, or AI application inference contracts. Keep independent evaluation separate from builders.

## Procedure

1. For studies or experiments, define hypothesis, unit, population, allocation, confounders, sample size or precision, assumptions, guardrails, uncertainty, segmentation, and interpretation limits.
2. For ML, define feature provenance, leakage controls, training/validation/test split, algorithm choices, tuning method, baselines, evaluation slices, calibration, robustness, packaging, interface, and model documentation.
3. For RAG/GenAI, define prompt contracts, knowledge sources, embedding/retrieval design, reranking, grounding, citation requirements, conflict handling, stale-source behavior, hallucination tests, and fallback/abstention criteria.
4. For agents, define tool allowlist, input/output contracts, bounded delegation, loop/stop limits, idempotency, approval boundaries, tool-poisoning and prompt-injection controls, partial-failure handling, and recoverability.
5. For inference applications, define structured outputs, latency/cost targets, caching, user controls, human review, accessibility, feedback, graceful degradation, monitoring signals, and rollback readiness.
6. Return evaluation design or results with evidence, thresholds, unresolved findings, risk review needs, release recommendation, and independent reviewer assignment.

## Quality Gates

- Baselines, thresholds, representative slices, uncertainty, calibration, and failure modes are explicit.
- RAG evaluation covers retrieval relevance, coverage, groundedness, citation correctness, conflicts, and stale sources.
- Agent evaluation covers unsafe tool use, excessive agency, injection, poisoning, exfiltration, loop limits, and approval boundaries.
- Builders cannot certify their own release readiness.
- Status is exactly `PASS`, `FAIL`, or `BLOCKED`.
