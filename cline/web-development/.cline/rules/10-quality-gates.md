# Web Development Quality Gates

For completion or review tasks, record **PASS**, **FAIL**, **BLOCKED**, or **NOT APPLICABLE** and the supporting evidence. These project rules define review expectations; they do not technically enforce checks.

1. Scope and acceptance criteria are explicit and traceable.
2. The actual stack and existing conventions were verified.
3. Architecture and API contracts remain coherent and documented when materially changed.
4. Frontend behavior covers semantic structure, responsive states, errors, loading, empty states, keyboard and focus behavior where applicable.
5. Backend behavior covers validation, authorization, errors, idempotency, data integrity and observability where applicable.
6. Security and privacy review has no unresolved critical or high-risk finding.
7. CSP, CORS, cookies, CSRF, secrets, logging and third-party code were assessed where applicable.
8. Accessibility evidence covers applicable semantics, keyboard, focus, names, errors, contrast, zoom and motion.
9. Performance evidence covers applicable rendering, loading, caching, assets, server latency and budgets.
10. SEO evidence covers applicable metadata, indexability, canonical behavior, structured data and crawlability.
11. Tests and browser compatibility map to actual risk and supported targets.
12. Dependency and supply-chain changes are justified and human-reviewed.
13. Migrations, rollback, observability and operational documentation are adequate where applicable.
14. No automatic deployment, publication, Git mutation, installation, secret use or destructive action occurred.
15. An independent reviewer verified the final completion claim.
