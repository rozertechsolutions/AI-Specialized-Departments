# Use-Case Intake and Risk Triage

1. Invoke `use-case-risk-triage` to capture outcome, users, decision impact, data classes, alternatives to AI, feasibility, value hypothesis, adoption objective, and success metrics.
2. Route governance/privacy/responsible-AI questions to the Strategy and Solution Governance Reviewer.
3. Route data readiness to `data-contract-dataset-readiness`; analytics to `analytics-experiment-review`; ML/GenAI/inference to `ml-genai-system-evaluation`; operations and final evidence review to `ops-risk-assurance`.
4. Stop with `BLOCKED` if authority, provenance, permitted use, owner, human-review gate, or evidence requirements are missing.
5. Return status exactly as `PASS`, `FAIL`, or `BLOCKED`.
