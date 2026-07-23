---
name: genai-rag-agent-evaluation
description: Review GenAI, RAG, retrieval, prompt, agent, tool, groundedness, safety, and AI inference contract evidence.
user-invocable: true
allowed-tools:
  - grep
  - read_file
  - task
---

# GenAI RAG Agent Evaluation

## Use When
A prompt system, RAG pipeline, retrieval corpus, embedding/reranking design, agent workflow, tool-use design, structured output contract, or GenAI application needs evaluation.

## Procedure
1. Confirm knowledge sources, prompts, embeddings, retrieval/reranking, grounding, memory, tools, output contract, users, fallback, abstention, and human controls.
2. For RAG, verify provenance, retrieval relevance, coverage, groundedness, citation correctness, conflict handling, stale-source behavior, and deletion propagation.
3. For agents, verify tool allowlists, input/output contracts, bounded delegation, loop/stop limits, idempotency, approval boundaries, partial-failure handling, and recoverability.
4. Review prompt-injection, tool-poisoning, data/model poisoning, exfiltration, unsafe tool use, excessive agency, red-team evidence, and acceptance thresholds.
5. Return status as exactly `PASS`, `FAIL`, or `BLOCKED`.

## Output
Groundedness findings, tool-risk findings, safety gaps, inference-contract concerns, release blockers, and status.
