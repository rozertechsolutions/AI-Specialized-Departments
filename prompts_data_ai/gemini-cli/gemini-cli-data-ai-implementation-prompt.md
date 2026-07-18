# Gemini CLI — Data and AI specialization implementation prompt

## Objective

Implement the complete, professional **Data and AI** specialization for **Gemini CLI** in `gemini-cli/data-ai/`, using only current native capabilities and the repository's established conventions.

This prompt is self-contained. Complete only this platform. Do not begin or modify another platform.

## Official verification starting points

Use these only as starting points and confirm the latest official documentation, current schemas, feature status, and limitations before implementation:

- https://geminicli.com/docs/
- https://geminicli.com/docs/core/subagents/
- https://geminicli.com/docs/cli/skills/
- https://geminicli.com/docs/hooks/
- https://geminicli.com/docs/tools/mcp-server/


## Mandatory execution method

1. Locate the repository root and inspect existing conventions for this platform and other completed specializations. Read only what is necessary to preserve repository consistency. Do not copy another platform's native structure.
2. Work only inside `gemini-cli/data-ai`. Preserve every other platform, specialization, untracked file, and user change.
3. Before changing files, verify the current product surface and native formats using current official documentation. Detect the installed version when possible without installing or upgrading the platform. If official verification is unavailable or contradictory, stop with `BLOCKED` rather than guessing.
4. Internally classify every candidate component as `native` or `unsupported`. Create only native components. Do not write the classification matrix or an audit report into the repository.
5. Map the complete responsibility architecture to the minimum non-overlapping native components. Keep independent evaluation/assurance separate from builders.
6. Implement the complete package. No placeholders, TODO-only content, empty directories, sample-only components, fake integrations, or unsupported compatibility files.
7. Perform three verification passes:
   - Pass A: professional coverage and lifecycle completeness.
   - Pass B: native-format correctness, paths, schemas, permissions, and platform limitations.
   - Pass C: security, separation of duties, duplication/conflict detection, and evidence-based completion.
   Compare the passes, correct every defect, then repeat the affected checks.
8. Validate all structured files and any deterministic scripts. Do not execute the target AI platform, authenticate services, contact external APIs, use production data, or run model inference.
9. If real compatibility validation genuinely requires an isolated environment, create it only after implementation, preferably in an operating-system temporary directory. Install dependencies only inside that environment, never globally. Do not reuse an existing user environment. Remove the environment, downloaded caches created for it, temporary files, bytecode, logs, coverage output, and test artifacts before finishing. Verify deletion. If cleanup fails, final status is `BLOCKED`.
10. Do not perform any Git mutation: no checkout, branch, add, commit, merge, rebase, tag, push, pull, reset, stash, or worktree operation.
11. Report the result on screen only. Do not create audit, validation, architecture, design, report, summary, evidence, inventory, matrix, or changelog documents.



## Final validated Data and AI responsibility architecture

The implementation must cover all responsibilities below. Do not assume one file, Skill, or agent per responsibility. Consolidate only when ownership remains precise and there is no builder/reviewer conflict.

1. **Data and AI strategy, portfolio, and product ownership** — business outcomes, use-case selection, value hypotheses, prioritization, adoption objectives, lifecycle ownership, and success metrics.
2. **Coordination and delivery orchestration** — intake, decomposition, routing, dependency control, evidence collection, status, and stop conditions. It cannot approve its own work.
3. **Data and AI solution architecture** — system boundaries, alternatives to AI, integration patterns, non-functional requirements, component contracts, and technology-neutral architecture decisions.
4. **Data governance, stewardship, privacy, and metadata** — ownership, glossary, catalog, classification, lawful/allowed use, retention, consent, access policy, records, and policy exceptions.
5. **Data architecture, modeling, and semantic systems** — conceptual/logical/physical models, master/reference data, schemas, ontologies, taxonomies, knowledge graphs, and semantic interoperability.
6. **Data sourcing, contracts, and dataset engineering** — source assessment, provenance, contracts, collection, labeling, annotation quality, deduplication, synthetic data, representativeness, splits, and dataset versioning.
7. **Data platform and data engineering** — ingestion, batch/stream processing, transformation, orchestration, storage design, data products, performance, and recoverability. Infrastructure provisioning remains outside this specialization.
8. **Data quality, reliability, lineage, and observability** — profiling, validation rules, reconciliation, freshness, completeness, lineage verification, anomaly detection, SLOs, and incident diagnosis.
9. **Analytics engineering, BI, and decision intelligence** — marts, semantic layers, governed metrics, dashboards, analytical queries, decision support, and reproducible reporting.
10. **Data science, causal inference, and experimentation** — exploratory analysis, statistical design, hypothesis testing, causal methods, uncertainty, calibration, segmentation, and experiment interpretation.
11. **Machine learning engineering** — features, training pipelines, algorithm selection, tuning, validation implementation, packaging, model interfaces, and technical performance.
12. **Generative AI, RAG, knowledge, and agent engineering** — prompts, embeddings, retrieval, vector search, reranking, grounding, memory, tool use, agent orchestration, and knowledge-source design.
13. **AI application and inference engineering** — model/application integration, structured outputs, inference contracts, latency, caching, fallback, abstention, user-facing controls, and graceful degradation.
14. **MLOps, LLMOps, and AI operations** — reproducibility, registries, release candidates, configuration/version control, monitoring, drift, rollback readiness, change control, incidents, and retirement.
15. **AI evaluation, validation, safety testing, and red teaming** — independent test design, benchmarks, regression, robustness, security/safety behavior, hallucination, retrieval and agent evaluation, and acceptance evidence.
16. **Responsible AI, model risk, and third-party/supply-chain risk** — impact, fairness, explainability, privacy risk, licensing, misuse, external models/data/providers, legal escalation, and risk acceptance.
17. **Human factors, AI UX, oversight, and adoption** — human roles, review interfaces, contestability, appeals, override, feedback, accessibility, operator training, adoption, and automation-bias controls.
18. **Independent Data and AI assurance** — final cross-domain verification of traceability, evidence, separation of duties, unresolved risk, and completion claims. It must not build the artifact it approves.

### Mandatory separation of duties

- Builders may test their work but cannot provide independent final approval.
- Data/ML/GenAI engineers cannot certify their own quality, risk, or release readiness.
- The coordinator cannot silently override a specialist, risk owner, human reviewer, or assurance gate.
- Responsible AI/model risk defines and reviews risk controls; independent assurance verifies that those controls and their evidence are complete.
- Cybersecurity owns general security operations and penetration testing; this specialization owns Data/AI-specific threat assumptions, controls, evaluation, and escalation.
- DevOps and Cloud owns infrastructure provisioning and production deployment; this specialization owns deployment readiness, model/data operational requirements, monitoring specifications, and rollback criteria.



## Required capability coverage

Create only the native components needed to cover these reusable capability families:

- Use-case intake, feasibility, impact, and risk classification.
- Data contracts, schemas, modeling, semantics, and lineage.
- Dataset sourcing, annotation, synthetic-data controls, acceptance, and versioning.
- Pipeline/data-product design, quality, reliability, and observability.
- Governed metrics, analytics products, statistical analysis, and experiments.
- ML system design, feature/data leakage review, evaluation, and model documentation.
- RAG/retrieval, prompt, agent, tool, and groundedness engineering/evaluation.
- AI application/inference contracts, fallback, abstention, and human controls.
- MLOps/LLMOps readiness, monitoring, change, incident, rollback, and retirement.
- Responsible AI, privacy, bias, licensing, supplier/model risk, and impact assessment.
- Independent evidence review, data/model/system cards, and final assurance.

Do not create a Skill when a short durable instruction or explicit workflow is sufficient. Do not duplicate the same procedure across an agent, Skill, command, and workflow.

## Required professional workflows

The resulting platform package must support, natively or through precise instructions, these lifecycle workflows:

1. Use-case intake, feasibility, value, alternatives-to-AI, impact, and risk triage.
2. Data source, dataset, third-party model, provider, and component onboarding.
3. Data contract, semantic/model design, collection, annotation, and dataset acceptance.
4. Governed pipeline, data product, lineage, quality, and observability delivery.
5. Analytics product and metric definition, validation, certification, and change control.
6. Data-science study and controlled experiment lifecycle.
7. ML model development, comparison, validation, documentation, and candidate selection.
8. RAG, GenAI, and agent-system design, implementation, evaluation, and tool-risk review.
9. AI application/inference integration, human-control design, fallback, and operational readiness.
10. Independent evaluation, red-team review, risk review, and release-readiness decision.
11. Monitoring, drift, foundation-model/provider change, incident, near-miss, corrective action, and rollback.
12. Data rectification/deletion propagation, system retirement, evidence retention, and final assurance.



## Mandatory safety, governance, and quality rules

- Never expose or copy sensitive datasets, secrets, credentials, private endpoints, proprietary prompts, personal data, or production records.
- Never fabricate data quality results, statistical significance, causal claims, model metrics, benchmarks, costs, latency, robustness, fairness, or compliance status.
- Require provenance and permitted-use evidence for data, models, prompts, embeddings, libraries, and third-party components.
- Require human review for high-impact decisions and any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, or production action.
- Include prompt-injection, tool-poisoning, data/model poisoning, exfiltration, unsafe tool use, excessive agency, and supply-chain risk controls where relevant.
- Require dataset leakage/contamination checks, representative evaluation slices, uncertainty/calibration, abstention/fallback criteria, and failure-mode analysis.
- For RAG: require source provenance, retrieval relevance, coverage, groundedness, citation correctness, conflict handling, and stale-source behavior.
- For agents: require tool allowlists, input/output contracts, bounded delegation, loop/stop limits, idempotency, approval boundaries, partial-failure handling, and recoverability.
- Require monitoring and response plans for data quality, drift, model/provider changes, performance, cost/capacity, safety, bias, and user feedback.
- Require deletion/rectification propagation and retirement/rollback readiness where applicable.
- Completion status must be exactly `PASS`, `FAIL`, or `BLOCKED`, based on evidence.

A deliverable is complete only when applicable requirements, owners, inputs, outputs, assumptions, dependencies, versions, tests, baselines, thresholds, risks, human-review gates, monitoring, rollback, documentation, and evidence are present and internally consistent.


## Platform-native implementation requirements

Use the current Gemini CLI project-scoped context, subagent, Agent Skill, hook, settings, sandbox, and extension mechanisms.

Expected implementation direction:
- Use `GEMINI.md` or the current official workspace context mechanism.
- Use project-local subagents for specialist responsibilities only where the schema is stable and documented.
- Use Agent Skills for focused reusable workflows.
- Use hooks only for deterministic local safety and validation controls.
- Preserve safe planning/sandbox behavior and do not weaken approval or isolation controls.
- Do not build an extension merely to bundle files unless the extension format adds real native value.
- Omit active remote agents and MCP servers by default. Never add credentials or authentication setup.


## Repository documentation rule

`gemini-cli/data-ai/README.md` must be the single general explanatory document for this platform implementation. It must contain:

- Purpose and supported native product surface.
- Exact installation/import/discovery and usage instructions.
- Component map and invocation/delegation behavior.
- Permissions, approval, human-review, and safety behavior.
- Optional integrations and how to enable them manually; all remain disabled by default.
- Platform/version/plan/IDE/CLI/account limitations.
- Verification commands or checks that a maintainer may run.

Do not create additional explanatory Markdown files such as `ARCHITECTURE.md`, `DESIGN.md`, `AUDIT.md`, `REPORT.md`, `VALIDATION.md`, `IMPLEMENTATION_SUMMARY.md`, `COMPONENT_MATRIX.md`, or `CHANGELOG.md`.

Markdown files required by the platform itself—such as `AGENTS.md`, `CLAUDE.md`, `SKILL.md`, rules, agent profiles, commands, prompts, or workflow definitions—are native configuration artifacts and are allowed. Keep explanatory prose out of separate files when it belongs in the README.


## Additional hard prohibitions

- No `common/` directory, shared cross-platform runtime, universal adapter, converter, installer, or migration framework.
- No copying structures from another platform merely for consistency.
- No unsupported or deprecated component retained as a fallback unless current official documentation explicitly requires backward compatibility.
- No real secrets, example secrets that resemble real values, live endpoints, private URLs, or environment-specific absolute paths.
- No active external integration, MCP server, connector, plugin, provider, model download, account trust, authentication, or network access by default.
- No automatic deployment, publication, submission, spending, signing, destructive operation, or production mutation.
- No dependency installation except inside a disposable verification environment when strictly necessary.
- No audit artifacts inside the project. Validation results belong only in the final on-screen response.


## Required final on-screen response

Return only a concise result with:

- Status: `PASS`, `FAIL`, or `BLOCKED`.
- Target platform and path.
- Native components created or modified.
- Validation actually executed and its result.
- Temporary environment created: `yes/no`; if yes, confirm its exact deletion.
- Remaining limitations or blockers.

Do not claim success unless all mandatory checks pass and no temporary environment or generated test residue remains.
