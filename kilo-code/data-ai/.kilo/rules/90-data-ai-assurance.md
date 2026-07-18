## Data and AI Assurance Rules

Independent evaluation and assurance must remain separate from build ownership. Builders may provide tests and evidence, but final readiness must be reviewed by a role that did not build the artifact.

Evaluation and safety requirements:
- Require benchmarks, regression checks, robustness tests, retrieval evaluations, hallucination checks, agent tool-risk checks, safety behavior tests, and red-team scenarios where applicable.
- For RAG, verify source provenance, retrieval relevance, coverage, groundedness, citation correctness, conflicting-source behavior, and stale-source handling.
- For agents, verify tool allowlists, contracts, idempotency, loop and delegation bounds, approval boundaries, partial-failure handling, and recoverability.
- Include prompt-injection, tool-poisoning, data/model poisoning, exfiltration, unsafe tool use, excessive agency, supply-chain risk, privacy leakage, misuse, and provider-change assumptions where relevant.

Operational readiness must include monitoring for data quality, drift, model/provider changes, safety, bias, user feedback, cost, capacity, latency, and incidents. Release readiness must include rollback criteria, retirement path, evidence retention, deletion/rectification propagation, and corrective-action ownership.

Use only `PASS`, `FAIL`, or `BLOCKED`.
