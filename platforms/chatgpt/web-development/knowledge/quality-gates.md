# Web Development Quality Gates

This file is factual reference material for Project sources or GPT Knowledge. It defines the quality gates used by this specialization. Gate status values are PASS, FAIL, BLOCKED, and NOT APPLICABLE.

## Gate Catalog

1. Scope and acceptance criteria are explicit and traceable.
2. The actual stack and existing conventions are verified from evidence.
3. Architecture and API contracts remain coherent and are documented when materially changed.
4. Frontend behavior covers semantic structure, responsive states, errors, loading, empty states, keyboard behavior, and focus behavior where applicable.
5. Backend behavior covers validation, authorization, errors, idempotency, data integrity, and observability where applicable.
6. Security and privacy review has no unresolved critical or high-risk finding.
7. CSP, CORS, cookies, CSRF, secrets, logging, and third-party code are assessed where applicable.
8. Accessibility evidence covers applicable semantics, keyboard operation, focus order, accessible names, errors, contrast, zoom, and motion.
9. Performance evidence covers applicable rendering, loading, caching, assets, server latency, and budgets.
10. SEO evidence covers applicable metadata, indexability, canonical behavior, structured data, and crawlability.
11. Tests and browser-compatibility checks map to actual risk and supported targets.
12. Dependency and supply-chain changes are justified and human-reviewed.
13. Migrations, rollback, observability, and operational documentation are adequate where applicable.
14. No automatic deployment, publication, Git mutation, installation, secret use, or destructive action occurred.
15. Independent review verifies the final completion claim where the risk level requires it.

## Evidence Format

Useful evidence includes file paths, code excerpts, screenshots, logs, test output, browser observations, configuration values, official documentation, or explicit user decisions. Missing evidence is BLOCKED, not PASS.
