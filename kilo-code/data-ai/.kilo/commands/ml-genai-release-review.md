---
description: ML, GenAI, RAG, agent, and AI application evaluation and release-readiness workflow
agent: ml-genai-evaluation-reviewer
subtask: false
---

# ML GenAI Release Review

Run the `ml-genai-evaluation` Skill and return evidence-backed release findings.

## Gates
1. Verify model/application contract, inputs, outputs, fallback, abstention, latency/cost limits, and human controls.
2. Review leakage, representative slices, baselines, thresholds, calibration, uncertainty, RAG groundedness, citation correctness, agent tool controls, safety tests, and red-team evidence.
3. Identify release blockers, residual risks, required human approvals, monitoring needs, rollback criteria, and documentation gaps.
4. Stop with `BLOCKED` when evaluation evidence or approval authority is missing.

## Safety
Do not call external models, access production data, publish, deploy, configure providers, or replace missing metrics with estimates.
